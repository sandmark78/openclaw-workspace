# OpenClaw v2026.7.1-beta.1 更新记录

**发现时间**: 2026-07-03 20:00 UTC  
**发布时间**: 2026-07-02 07:25 UTC  
**类型**: Beta 预发布  
**标签**: v2026.7.1-beta.1

---

## 🔥 重要更新

### 1. GPT-5.6 支持
- OpenClaw 现已识别 GPT-5.6 模型族
- 跨 catalog、capability、runtime 选择路径全面支持
- PR: #98333

### 2. `openclaw attach` - 外部 Harness 挂载
- 新命令：`openclaw attach`
- 可对已有 Gateway 会话启动外部 harness
- 方便恢复和检查交互式 Codex 风格工作流
- PR: #96454

### 3. Telegram Codex 工作流
- Telegram 可通过 `/login` 启动 Codex 配对
- 可引导活跃 Codex 运行
- 可在临时 API 故障时恢复最终回复
- PR: #98006, #98126, #98786

### 4. 事件驱动 Cron
- 新 `on-exit` schedule 类型：监控命令退出时唤醒 agent
- session-targeted runs 可干净分离
- PR: #92037, #98755

### 5. iOS 原生应用刷新
- 采用 iOS 26 视觉系统
- 更清晰的导航、设置、Chat、Talk 和 onboarding 流程
- Apple/Android 本地化扩展
- PR: #98452, #98736, #98811 等

### 6. iMessage 原生投票
- 支持创建、读取、投票原生 poll
- PR: #98421

### 7. 更安全的会话作用域
- Capability profiles：按会话准备工具和访问边界
- 不削弱现有默认 profile
- PR: #98536

### 8. 其他改进
- Nemotron Super 1M 上下文窗口支持
- OpenRouter 认证头保留
- Node context-path 支持
- 设备审批恢复指引优化
- 插件安装退出诊断优化
- 内置用量 footer（每轮计费更清晰）

---

## 📊 与 Sandbot 相关性

| 功能 | 相关性 | 行动建议 |
|------|--------|---------|
| GPT-5.6 | 中 | 当前用 qwen3.5-plus，暂不需要 |
| `openclaw attach` | 高 | 可用于调试子 Agent 会话 |
| Telegram Codex | 高 | 可直接在 Telegram 启动 Codex 工作流 |
| 事件驱动 Cron | 高 | 可替代部分心跳轮询逻辑 |
| iMessage poll | 低 | 当前未使用 iMessage |

---

*此文件由生态探索 cron 自动创建*
