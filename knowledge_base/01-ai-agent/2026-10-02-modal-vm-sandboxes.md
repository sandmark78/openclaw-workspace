# Modal VM Sandboxes: Agent 执行环境的 VM 级隔离

**日期**: 2026-10-02  
**来源**: Modal 官方文档 + Hacker News  
**关键词**: modal, sandbox, vm, agent-infra, isolation

---

## 核心事件

Modal 推出 Sandboxes 产品，为 AI Agent 提供完整 Linux 虚拟机级别的沙箱环境，区别于 E2B/Open Sandbox 的进程级隔离方案。

## 关键数据

- **VM 启动时间**: 1-5 秒（vs 进程级 ~100ms）
- **最长运行时间**: 24 小时（支持 Filesystem Snapshot 保存/恢复）
- **隔离级别**: 完整 VM（独立内核、文件系统、网络栈）
- **生命周期**: Created → Scheduled → Started → Ready → Finished

## 技术对比

| 维度 | 进程级沙箱 (E2B/Open Sandbox) | VM 级沙箱 (Modal) |
|------|------|------|
| 隔离 | namespace + cgroup | 完整 VM |
| 启动 | ~100ms | 1-5s |
| 能力 | 受限（共享内核） | 完整 OS（apt install, systemd） |
| 成本 | 低 | 高 |
| 安全 | 内核漏洞可逃逸 | 更强隔离 |

## Agent 能力影响

VM 级沙箱让 Agent 可以：
- 任意安装软件包
- 启动和管理多进程
- 运行需要特定内核模块的工具
- Docker-in-Docker 场景
- 启动 web 服务器并暴露

## 核心洞察

Agent 基础设施正沿"安全-能力"光谱分化：
- 轻任务 → 进程级沙箱（快、便宜）
- 重任务 → VM 级沙箱（慢、强大）

没有银弹，只有正确的取舍。

## 教训

执行环境不是"刚好够用"就行——Agent 能做什么，取决于它住在什么样的"房子"里。
