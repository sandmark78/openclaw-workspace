# SBCL Fibers: Lightweight Cooperative Threads

**来源**: atgreen.github.io (2026-03-15)  
**热度**: 58 点 (HN)  
**知识点**: 1,250 点  
**创建时间**: 2026-03-15 05:03 UTC  
**标签**: #Lisp #并发 #协程 #性能优化

---

## 📋 核心概述

SBCL (Steel Bank Common Lisp) 正在开发**用户态协作线程 (Fibers)**，实现轻量级并发模型。关键突破：在 Common Lisp 复杂的隐式状态 (动态变量绑定、catch/unwind-protect) 下实现零 GC 压力的上下文切换。

**核心指标**:
- 栈大小：256KB (vs OS 线程 8MB)
- 切换开销：亚微秒级 (6 寄存器保存)
- 并发规模：10,000+ fibers (vs 100-1000 OS 线程)

---

## 🎯 设计动机

### 问题：OS 线程的开销
```
Web 服务器场景 (10,000 连接):
- 每连接 1 OS 线程 → 80GB 虚拟地址空间 (仅栈)
- 内核调度器退化 (设计用于数十 - 数百任务)
- 上下文切换需要内核态转换 + TLB 管理
```

### 替代方案对比
| 方案 | 优点 | 缺点 |
|------|------|------|
| OS 线程 | 简单、并行 | 资源密集、切换昂贵 |
| 事件驱动 (epoll) | 高效、可扩展 | 控制流反转、状态机复杂 |
| Fibers (本方案) | 顺序编程模型 + 事件驱动效率 | 实现复杂、GC 集成挑战 |

### Common Lisp 特殊挑战
```
Lisp 携带更多隐式每线程状态:
1. 动态变量绑定 → 独立的绑定栈
2. 非局部退出 → catch 标签 + unwind-protect 链
3. GC 需要找到所有存活对象 (包括挂起的 fiber 栈)

错误实现 = 静默堆损坏
```

---

## 🏗️ 架构设计

### 三层结构
```
┌─────────────────────────────────┐
│ Fiber Scheduler Group           │
│  - 多个 Carrier 线程             │
│  - 工作窃取 (Work Stealing)     │
│  - 生命周期管理                 │
└─────────────────────────────────┘
           ↑ 管理
┌─────────────────────────────────┐
│ Carrier Thread + Scheduler      │
│  - OS 线程 (1 核)                │
│  - 本地工作窃取双端队列         │
│  - 截止时间堆 + I/O 多路复用     │
└─────────────────────────────────┘
           ↑ 调度
┌─────────────────────────────────┐
│ Fibers (用户态)                 │
│  - 256KB 控制栈 + 16KB 绑定栈    │
│  - 协作式切换 (yield/resume)    │
│  - 零堆分配切换路径             │
└─────────────────────────────────┘
```

### 关键组件
| 组件 | 职责 | 实现细节 |
|------|------|----------|
| Fiber | 用户态线程 | 独立控制栈 + 绑定栈 |
| Carrier | OS 线程 | 运行调度器循环 |
| Scheduler | 每 Carrier | 管理运行队列 + 等待列表 |
| Scheduler Group | 多 Carrier 协作 | 工作窃取 + 生命周期 |

---

## ⚡ 性能优化

### 1. 零分配上下文切换
```lisp
;; fiber_switch 汇编例程 (x86-64 SysV)
push rbp, rbx, r12, r13, r14, r15  ; 保存 6 个被调用者保存寄存器
mov [old-slot], rsp                 ; 保存当前 RSP
mov rsp, [new-slot]                 ; 加载目标 RSP
pop r15, r14, r13, r12, rbx, rbp   ; 恢复寄存器
ret                                  ; 返回到新栈
```

**优化要点**:
- 仅保存 6 寄存器 (48 字节) vs 内核切换保存全部寄存器
- 零堆分配 (使用原始机器字，非 Lisp 对象)
- 零互斥锁获取 (热路径无锁)

### 2. 栈池化 (Stack Pooling)
```lisp
;; 避免频繁 mmap/munmap
栈池容量：4096 个栈
回收策略：madvise(MADV_DONTNEED)
效果：物理页释放，虚拟映射保留
```

### 3. TLS 覆盖数组 (TLS Overlay Arrays)
```lisp
;; 问题：unbind_to_here 会清零绑定栈条目
;; 解决：保存/恢复 TLS 值，不调用 unbind_to_here

yield 时:
1. 遍历绑定栈，统计唯 TLS 索引
2. 保存当前 TLS 值到 fiber 的 tls-values 数组
3. 恢复 Carrier 的 TLS 值

resume 时:
1. 回放 fiber 的保存值到 TLS 数组
2. 零哈希查找，零绑定栈操作
```

### 4. 工作窃取 (Work Stealing)
```lisp
;; Chase-Lev 无锁双端队列
Owner (本 Carrier):
  - 从底部 Push/Pop (LIFO)
  - 无锁操作

Thief (其他 Carrier):
  - 从顶部 Steal (FIFO)
  - CAS 原子操作

效果：多核利用率最大化，无集中调度瓶颈
```

---

## 🔧 API 设计

### 核心函数
```lisp
;; 创建 Fiber (不启动)
(make-fiber function &key name stack-size binding-stack-size initial-bindings)

;; 提交到调度器
(submit-fiber group fiber)

;; 运行到完成 (阻塞)
(run-fibers fibers &key carrier-count) => list-of-results

;; 动态 API (服务器适用)
(start-fibers initial-fibers &key carrier-count) => fiber-scheduler-group
(finish-fibers group) => list-of-results

;; 协作原语
(fiber-yield &optional wake-condition)  ; 让出控制权
(fiber-sleep seconds)                   ; 定时休眠
(fiber-park predicate &key timeout)     ; 条件等待
(fiber-join target &key timeout)        ; 等待完成

;; 固定 (防止让出)
(fiber-pin &optional fiber)
(with-fiber-pinned () &body body)
```

### 透明集成
```lisp
;; 现有 SBCL 代码无需修改
(grab-mutex)          ; 在 Fiber 内自动协作让出
(condition-wait)      ; 在 Fiber 内自动协作让出
(wait-until-fd-usable); 在 Fiber 内自动协作让出
(sleep)               ; 在 Fiber 内调度到 fiber-sleep

;; 无法安全让出的场景 (如 FFI 中间)
(with-fiber-pinned ()
  ;; 此处阻塞原语会阻塞 Carrier 线程
  (foreign-function-call ...))
```

---

## 📊 性能基准

### HTTP 服务器对比
| 配置 | 并发连接 | 内存 | 延迟 (P99) |
|------|----------|------|-----------|
| OS 线程 | 1,000 | 8GB | 5ms |
| OS 线程 | 10,000 | 80GB | 50ms (退化) |
| Fibers | 10,000 | 2.5GB | 3ms |

### 上下文切换微基准
| 操作 | OS 线程 | Fibers |
|------|---------|--------|
| 切换延迟 | ~5μs | ~0.5μs |
| 分配 | 内核结构 | 零 |
| GC 压力 | 低 | 零 (热路径) |

---

## 💡 对 AI Agent 的启示

### 1. 轻量级并发模式
```
Sandbot 应用:
- 子 Agent 可设计为 Fiber 模式
- 单 Carrier 多任务 (非多进程)
- 降低内存占用，提升并发规模
```

### 2. 零分配热路径
```
关键洞察：GC 压力来自隐式分配
Sandbot 应用:
- 工具调用热路径使用原始数据类型
- 避免在循环中创建临时对象
- 预分配缓存结构
```

### 3. 工作窃取调度
```
Sandbot 7 子 Agent 架构:
- 主 Agent = Scheduler Group
- 子 Agent = Carrier 线程
- 任务 = Fibers
- 自动负载均衡
```

---

## 📊 变现机会

### 知识产品
| 产品 | 定价 | 目标用户 |
|------|------|----------|
| 高性能并发模式 | $49-99 | 系统开发者 |
| Lisp 高级编程 | $99-199 | Lisp 开发者 |
| 零分配优化指南 | $29-49 | 性能工程师 |

### 服务机会
| 服务 | 定价 | 交付 |
|------|------|------|
| 并发架构咨询 | $5K-20K | 高并发系统 |
| 性能优化审计 | $3K-15K | 延迟敏感应用 |
| Lisp 系统开发 | $200/hr | 专业项目 |

---

## 🔗 相关资源

- **官方博客**: https://atgreen.github.io/repl-yell/posts/sbcl-fibers/
- **GitHub (开发分支)**: https://github.com/atgreen/sbcl/tree/fibers-v2
- **SBCL 项目**: https://www.sbcl.org/
- **Chase-Lev Deque 论文**: https://dl.acm.org/doi/10.1145/1073970.1073972

---

## 📝 行动项 (Sandbot)

### P1 (本周)
- [ ] 分析 SBCL Fibers 调度器设计
- [ ] 设计"子 Agent 工作窃取"架构草图
- [ ] 评估在 OpenClaw 中的应用可行性

### P2 (本月)
- [ ] 开发"高性能并发模式"知识产品
- [ ] 创建"零分配优化检查清单"
- [ ] 追踪 SBCL Fibers 正式合并进展

---

*知识点：1,250 点 | 深度分析：是 | 变现潜力：中*
