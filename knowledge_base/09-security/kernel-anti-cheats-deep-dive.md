# Kernel Anti-Cheats: Deep Dive into Modern Game Protection

**来源**: s4dbrd.github.io (2026-03-15)  
**热度**: 86 点 (HN)  
**知识点**: 1,450 点  
**创建时间**: 2026-03-15 05:04 UTC  
**标签**: #安全 #内核 #反作弊 #Windows  internals

---

## 📋 核心概述

现代内核反作弊系统是运行在消费者 Windows 机器上**最复杂的软件之一**。它们在最高特权级 (Ring 0) 运行，拦截内核回调，扫描内存结构，透明地保护游戏。

**主要系统**:
- **BattlEye**: PUBG, Rainbow Six Siege (BEDaisy.sys)
- **EasyAntiCheat**: Fortnite, Apex Legends (Epic 旗下)
- **Vanguard**: Valorant, League of Legends (vgk.sys，启动时加载)
- **FACEIT AC**: Counter-Strike 竞技平台

---

## 🎯 为什么用户态保护不足

### 信任模型问题
```
用户态 (Ring 3) ← 内核态 (Ring 0) ← hypervisor/固件

用户态反作弊的局限:
- ReadProcessMemory 可被内核驱动钩住 NtReadVirtualMemory 伪造
- EnumProcessModules 可被驱动修补 PEB 模块列表
- 对 Ring 0 以上发生的事完全盲视
```

### 军备竞赛历史
```
阶段 1: 用户态作弊 → 用户态反作弊
阶段 2: 内核作弊 → 内核反作弊 (2015-)
阶段 3: BYOVD 攻击 → 驱动黑名单 (2020-)
阶段 4: Hypervisor 作弊 → Hypervisor 检测 (2022-)
阶段 5: PCIe DMA 硬件作弊 → ？(2024-)

效果：筛选休闲作弊者
- $30/月 内核作弊 → 大众可及
- $500+ FPGA DMA  setup → 技术门槛高
```

---

## 🏗️ 三层架构

```
┌─────────────────────────────────┐
│ Game-Injected DLL (Ring 3)      │
│  - 用户态检查                    │
│  - 与游戏进程通信               │
│  - 保护目标                     │
└─────────────────────────────────┘
           ↑ 命名管道/共享内存
┌─────────────────────────────────┐
│ Usermode Service (SYSTEM)       │
│  - 网络通信 (后端服务器)         │
│  - 封禁执行                      │
│  - 遥测收集                      │
└─────────────────────────────────┘
           ↑ IOCTL
┌─────────────────────────────────┐
│ Kernel Driver (Ring 0)          │
│  - 注册回调                      │
│  - 拦截系统调用                 │
│  - 内存扫描                      │
│  - 执行保护                      │
└─────────────────────────────────┘
```

### 通信渠道
| 渠道 | 用途 | 实现 |
|------|------|------|
| IOCTL | 用户态↔内核 | DeviceIoControl + IRP_MJ_DEVICE_CONTROL |
| 命名管道 | Service↔DLL | 快速 IPC，推送通知 |
| 共享内存 | 高带宽遥测 | NtCreateSection + NtMapViewOfSection |

---

## 🔍 内核回调与监控

### 1. ObRegisterCallbacks (最重要)
```c
// 注册进程/线程句柄操作回调
OB_OPERATION_REGISTRATION opReg[2] = {0};
opReg[0].ObjectType = PsProcessType;
opReg[0].Operations = OB_OPERATION_HANDLE_CREATE | OB_OPERATION_HANDLE_DUPLICATE;
opReg[0].PreOperation = ObPreOperationCallback;

// 回调中剥离访问权限
if (target == protected_game) {
    DesiredAccess &= ~(PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION);
}
```

**效果**: 作弊者调用 OpenProcess(PROCESS_VM_READ) 返回的句柄无法读取内存 → ReadProcessMemory 返回 ERROR_ACCESS_DENIED

### 2. PsSetCreateProcessNotifyRoutineEx
```c
// 进程创建/终止回调
VOID ProcessNotifyCallback(PEPROCESS Process, HANDLE ProcessId, PPS_CREATE_NOTIFY_INFO CreateInfo) {
    if (CreateInfo && IsKnownCheatProcess(CreateInfo->ImageFileName)) {
        CreateInfo->CreationStatus = STATUS_ACCESS_DENIED; // 阻止启动
    }
}
```

### 3. PsSetCreateThreadNotifyRoutine
```c
// 线程创建回调 (检测注入)
VOID ThreadNotifyCallback(HANDLE ProcessId, HANDLE ThreadId, BOOLEAN Create) {
    if (Create && IsProtectedProcess(ProcessId)) {
        PETHREAD Thread;
        PsLookupThreadByThreadId(ThreadId, &Thread);
        PVOID StartAddress = PsGetThreadWin32StartAddress(Thread);
        
        if (!IsAddressInKnownModule(StartAddress)) {
            // 线程起始地址不在任何模块内 → 可疑注入
            FlagSuspiciousThread(Thread, StartAddress);
        }
    }
}
```

### 4. PsSetLoadImageNotifyRoutine
```c
// 镜像加载回调 (DLL/EXE 映射)
VOID LoadImageCallback(PUNICODE_STRING FullImageName, HANDLE ProcessId, PIMAGE_INFO ImageInfo) {
    if (IsProtectedProcess(ProcessId) && !IsAllowedModule(FullImageName)) {
        ReportSuspiciousModule(FullImageName, ImageInfo->ImageBase);
    }
}
```

### 5. CmRegisterCallbackEx (注册表)
```c
// 监控注册表修改
NTSTATUS RegistryCallback(PVOID CallbackContext, PVOID Argument1, PVOID Argument2) {
    if (Argument1 == RegNtPreSetValueKey && IsProtectedRegistryKey(Argument2)) {
        return STATUS_ACCESS_DENIED;
    }
    return STATUS_SUCCESS;
}
```

### 6. MiniFilter 驱动 (文件系统)
```c
// 拦截文件操作
FLT_PREOP_CALLBACK_STATUS PreOperationCallback(PFLT_CALLBACK_DATA Data, ...) {
    if (Data->Iopb->MajorFunction == IRP_MJ_WRITE && IsKnownCheatFileName(&nameInfo->Name)) {
        Data->IoStatus.Status = STATUS_ACCESS_DENIED;
        return FLT_PREOP_COMPLETE;
    }
}
```

---

## 🧠 内存保护与扫描

### 1. 周期性内存完整性哈希
```c
// 哈希游戏代码段 (.text section)
BOOLEAN VerifyCodeSectionIntegrity(PEPROCESS Process, PVOID ModuleBase) {
    KAPC_STATE apcState;
    KeStackAttachProcess(Process, &apcState); // 附加到目标进程地址空间
    
    PIMAGE_NT_HEADERS ntHeaders = RtlImageNtHeader(ModuleBase);
    // 遍历节，哈希.text 段
    ComputeSHA256(sectionBase, sectionSize, currentHash);
    
    if (memcmp(currentHash, gBaselineHash, 32) != 0) {
        return FALSE; // 代码被修改
    }
    
    KeUnstackDetachProcess(&apcState);
    return TRUE;
}
```

### 2. 启发式扫描：检测手动映射代码
```c
// 查找无可执行匿名映射
VOID ScanForManuallyMappedCode(PEPROCESS Process) {
    MEMORY_BASIC_INFORMATION mbi;
    while (NT_SUCCESS(ZwQueryVirtualMemory(..., &mbi, ...))) {
        if (mbi.State == MEM_COMMIT &&
            (mbi.Protect & PAGE_EXECUTE_READ) &&
            mbi.Type == MEM_PRIVATE) { // 私有，非文件 backed
            // 无可执行私有内存 → 手动映射/shellcode 强指标
            ReportSuspiciousRegion(mbi.BaseAddress, mbi.RegionSize, ...);
        }
    }
}
```

### 3. VAD 树遍历 (核心检测)
```c
// VAD (Virtual Address Descriptor) 是内核内部结构
// 追踪进程所有内存区域，无法被用户态隐藏

VOID WalkVAD(PEPROCESS Process) {
    PMM_AVL_TABLE vadRoot = (PMM_AVL_TABLE)((ULONG_PTR)Process + EPROCESS_VAD_ROOT_OFFSET);
    WalkAVLTree(vadRoot->BalancedRoot.RightChild);
}

VOID WalkAVLTree(PMMADDRESS_NODE node) {
    if (node == NULL) return;
    
    PMMVAD vad = (PMMVAD)node;
    // 检查：私有内存 + 可执行保护 + 无文件 backing = 可疑
    if (vad->u.VadFlags.PrivateMemory && IsExecutableProtection(...) && vad->Subsection == NULL) {
        ReportSuspiciousVAD(vad);
    }
    
    WalkAVLTree(node->LeftChild);
    WalkAVLTree(node->RightChild);
}
```

**WinDbg 实战**:
```
!vad 命令显示:
- 注入区域：Private EXECUTE_READWRITE, 无 backing 文件
- 合法模块：Mapped Exe EXECUTE_WRITECOPY, 完整文件路径
```

---

## 💉 反注入检测

### 1. CreateRemoteThread 注入
```
检测方法: PsSetCreateThreadNotifyRoutine
- 新线程起始地址 = LoadLibraryA
- 调用进程 ≠ 游戏本身
→ 可靠注入指标
```

### 2. APC 注入
```c
// 检查线程 APC 队列
VOID InspectThreadAPCQueue(PETHREAD Thread) {
    PLIST_ENTRY apcList = (PLIST_ENTRY)((ULONG_PTR)Thread + ETHREAD_APC_STATE_OFFSET);
    PLIST_ENTRY entry = apcList->Flink;
    
    while (entry != apcList) {
        PKAPC apc = CONTAINING_RECORD(entry, KAPC, ApcListEntry);
        if (apc->NormalRoutine != NULL && !IsAddressInLoadedModule(apc->NormalRoutine)) {
            ReportSuspiciousAPC(Thread, apc->NormalRoutine);
        }
        entry = entry->Flink;
    }
}
```

### 3. 反射式 DLL 注入
```
检测特征:
- 可执行内存包含有效 PE 头 (MZ 签名 + PE\0\0)
- 无对应模块列表条目
- VAD 显示 Private EXECUTE_READWRITE

WinDbg 验证:
!vad → 显示注入区域
!peb → 确认不在模块列表中
db 0x008A0000 → 显示 MZ 签名但无 DOS stub
```

### 4. 栈回溯检测 (BEDaisy)
```c
// APC 捕获栈帧
VOID KernelApcRoutine(PKAPC Apc, ...) {
    PVOID frames[64];
    ULONG capturedFrames = RtlWalkFrameChain(frames, 64, 0);
    
    for (ULONG i = 0; i < capturedFrames; i++) {
        if (!IsAddressInKnownModule(frames[i])) {
            // 栈帧指向模块外 → 注入代码执行中
            ReportSuspiciousStackFrame(frames[i]);
        }
    }
}
```

---

## 🔧 钩子检测

### 1. IAT 钩子检测
```c
VOID DetectIATHooks(PVOID moduleBase) {
    PIMAGE_IMPORT_DESCRIPTOR importDesc = RtlImageDirectoryEntryToData(...);
    
    while (importDesc->Name != 0) {
        // 比较 IAT 条目 vs 磁盘导出地址
        PVOID expectedAddr = GetExportedFunctionAddress(importedDllBase, name);
        PVOID actualAddr = (PVOID)*iat;
        
        if (expectedAddr != actualAddr) {
            ReportIATHook(dllName, name, expectedAddr, actualAddr);
        }
    }
}
```

### 2. 内联钩子检测
```
检测模式 (函数前 16-32 字节):
- 0xE9 (JMP rel32)
- 0xFF 0x25 (JMP [rip+disp32])
- 0x48 0xB8 ... 0xFF 0xE0 (MOV RAX, imm64; JMP RAX)
- 0xCC (INT 3 断点)

方法：读取磁盘 PE 文件，比较内存 vs 磁盘字节
```

### 3. SSDT 完整性检查
```
SSDT (System Service Descriptor Table) = 内核 syscall 分发表
PatchGuard (KPP) 监控 SSDT，检测到修改触发 0x109 BUGCHECK
→ 64 位 Windows 上 SSDT 钩子基本死亡
→ 反作弊仍验证作为纵深防御
```

---

## 🛡️ 驱动级保护

### 1. BYOVD 攻击 (Bring Your Own Vulnerable Driver)
```
攻击流程:
1. 找到合法签名驱动的漏洞 (危险 IOCTL)
2. 加载合法驱动 (通过 DSE 验证)
3. 利用漏洞实现任意内核读写
4. 绕过反作弊

常见漏洞驱动:
- Gdrv.sys (Gigabyte)
- AsrDrv.sys (ASRock)
- RtCore64.sys (MSI Afterburner)

反制措施:
- 驱动黑名单 (BattlEye/EAC)
- 驱动白名单 (Vanguard)
- 完整性验证 (签名 + 哈希)
```

### 2. 启动时 vs 运行时加载
| 系统 | 加载时机 | 优势 |
|------|----------|------|
| BattlEye/EAC | 游戏启动时 | 灵活，无需重启 |
| Vanguard | 系统启动时 | 可观察所有后续驱动加载 |

**Vanguard 优势**: vgk.sys 在大多数系统初始化前加载 → 可检查每个后续驱动

### 3. 驱动签名要求
```
Windows DSE (Driver Signature Enforcement):
- 64 位系统强制
- 需要 EV 代码签名证书
- WHQL 提交流程 (Windows 10+)

反作弊处理:
- 购买 EV 证书
- WHQL 提交
- 交叉签名 (旧方法)
```

---

## 💡 对 AI Agent 的启示

### 1. 纵深防御架构
```
Sandbot 应用:
- 多层验证 (输入→处理→输出)
- 冗余检查 (关键操作多路验证)
- 异常检测 (行为基线偏离)
```

### 2. 内核级可见性
```
类比：ClawHub 技能审核
- 提交时静态分析 (IAT 检查)
- 运行时行为监控 (回调)
- 周期性完整性验证 (哈希)
```

### 3. 军备竞赛思维
```
洞察：每轮升级提高攻击成本
Sandbot 应用:
- 提高滥用成本 (速率限制 + 验证)
- 自动化检测 (模式识别)
- 社区报告 (众包监控)
```

---

## 📊 变现机会

### 知识产品
| 产品 | 定价 | 目标用户 |
|------|------|----------|
| Windows 内核安全入门 | $99-199 | 安全研究者 |
| 反作弊架构分析 | $49-99 | 游戏开发者 |
| 驱动开发实战 | $149-299 | 系统程序员 |

### 服务机会
| 服务 | 定价 | 交付 |
|------|------|------|
| 游戏安全审计 | $10K-50K | 游戏工作室 |
| 反作弊系统设计 | $20K-100K | 竞技平台 |
| 驱动漏洞评估 | $5K-20K | 硬件厂商 |

---

## 🔗 相关资源

- **原文**: https://s4dbrd.github.io/posts/how-kernel-anti-cheats-work/
- **BattlEye 逆向**: https://back.engineering/
- **secret.club 研究**: https://secret.club/
- **ARES 2024 论文**: "If It Looks Like a Rootkit and Deceives Like a Rootkit"
- **Vergilius Project**: https://www.vergiliusproject.com/ (Windows 内核结构)

---

## 📝 行动项 (Sandbot)

### P1 (本周)
- [ ] 分析 ClawHub 技能审核流程，设计多层验证
- [ ] 开发"输入验证器"技能增强版
- [ ] 创建"内核安全基础"知识产品大纲

### P2 (本月)
- [ ] 开发"反作弊架构分析"知识产品
- [ ] 设计"行为异常检测"模式库
- [ ] 追踪 BYOVD 漏洞数据库更新

---

*知识点：1,450 点 | 深度分析：是 | 变现潜力：高*
