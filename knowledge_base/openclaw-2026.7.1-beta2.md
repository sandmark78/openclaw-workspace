# OpenClaw 2026.7.1-beta.2 更新

**发布日期**: 2026-07-05
**版本**: v2026.7.1-beta.2
**commit**: a580a7f

## 重要更新

### 1. OpenAI GPT-5.6 支持
- 识别 GPT-5.6 模型家族
- 支持 catalog、capability、runtime 选择路径
- PR: #98333

### 2. 外部 Harness 附件
- `openclaw attach` 命令：对现有 Gateway 会话启动外部 harness
- 方便恢复和检查 Codex 风格的交互式工作流
- PR: #96454

### 3. Telegram Codex 工作流
- Telegram 可用 `/login` 启动 Codex 配对
- 可引导活跃的 Codex 运行
- 可在临时 API 故障时恢复最终回复
- PR: #98006, #98126, #98786

### 4. 事件驱动 Cron 运行
- 新增 `on-exit` schedule kind：监控命令退出时唤醒 agent
- session-targeted runs 可干净地分离
- PR: #92037, #98755

### 5. 原生 App 刷新
- iOS 采用 iOS 26 视觉系统
- 更清晰的 Chat、Talk、onboarding、reconnect 流程
- 原生 app 本地化扩展（Apple + Android）
- PR: #98452, #98736, #99243, #97110-97113

### 6. 更丰富的消息功能
- iMessage 原生支持 poll 创建、阅读、投票
- 内置 usage footers 提供更清晰的每轮计费
- PR: #98421, #92657, #92877

### 7. 更安全的 scoped conversations
- capability profiles 为每个对话准备工具和访问边界
- 不削弱现有默认 profile
- PR: #98536

### 8. Mac 本地 Gateway 设置
- macOS app 可自动安装和启动本地 Gateway
- 减少首次使用前的手动设置
- PR: #99767

### 9. Control UI 导航改进
- (内容被截断)

## 历史版本
- 2026.7.1-beta.1
- 2026.6.11 (稳定版)
- 2026.6.10
- 2026.6.9

## 与 Sandbot 的关系
- **Telegram Codex 工作流**：可直接在我们的 Telegram 通道使用
- **事件驱动 Cron**：可改进心跳和定时任务机制
- **GPT-5.6 支持**：如果切换模型可直接使用
