# OpenClaw 版本更新记录 (2026-07)

**探索时间**: 2026-07-30 20:00 UTC  
**当前版本**: 2026.3.8 (我们运行的)  
**最新稳定版**: 2026.7.1  
**最新测试版**: 2026.7.2-beta.5 (2026-07-28)

---

## ⚠️ 版本差距

我们从 2026.3.8 → 最新 2026.7.1，差了约 4 个月的更新。  
建议老大考虑升级。

---

## 📦 v2026.7.1 主要更新 (3,063 贡献, 532 贡献者)

### Control UI 大改
- 对话管理更方便，支持并排工作
- 实时 Tasks、更清晰的聊天控制
- 更好的用量和成本视图
- 文件、下载、配对、审批、Gateway 健康检查

### 安装与引导
- 引导式设置，更清晰的第一步
- 保存连接前自动检查
- 中断后保留之前的选择

### 官方 App 更新
- iOS/iPadOS、Android、macOS 大量改进
- 设置、导航、聊天、语音、权限、本地化
- 文件、定时任务、离线阅读、排队发送
- 连接恢复、原生会话控制

### 模型和提供商
- **GPT-5.6** 兼容性
- **腾讯混元 Hy3** 完整支持
- **Meta Muse Spark 1.1** 支持
- Claude、Ollama、ClawRouter、LongCat 等扩展

### Codex 和编程 Agent
- `openclaw attach` 给 Claude Code 临时会话访问
- Codex 委托和原生子 Agent 更可靠
- Copilot 更多提供商选择
- 长时间运行会话和目标更容易恢复

### 各通道更新
- **Telegram**: 实时进度、照片文档、话题、命令、重试、账户路由
- **Slack**: 线程、卡片、进度、身份、反应、重复预防
- **Discord**: 回复、附件、语音会话、进度、重连、多账户
- **Apple Messages**: 回复、打字、媒体、路由、设置引导

### Gateway 稳定性
- 反复崩溃的 Gateway 不再无限重启，提供修复路径
- 定时任务仅在变化时唤醒
- 远程浏览器控制和终端改进

### 安全加固
- 密码和 token 不再出现在更多日志中
- 设备配对更清晰
- 不安全的下载、文件和网络请求更早被阻止

---

## 📦 v2026.7.2-beta.5 (2026-07-28 测试版)

亮点：状态安全和恢复 - 隔离存储保护持久化数据，崩溃可恢复的 SQLite 快照，崩溃持久的文件系统发布，schema 升级数据损失修复。

---

## 🏪 ClawHub 状态

- 域名从 clawhub.com 重定向到 clawhub.ai
- 新增官方技能分类：GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello, WhatsApp
- WhatsApp 作为 OpenClaw 插件可用
- ClawHub CLI 发布方式：`clawhub skill publish` / `clawhub package publish`

---

## 🤔 对我们的意义

1. **升级建议**: 我们落后 4 个月，GPT-5.6 和新模型支持可能有用
2. **Telegram 改进**: 实时进度、话题支持等对我们直接有用
3. **ClawHub**: 可以发布更多技能，WhatsApp 插件值得关注
4. **安全加固**: 凭证保护改进值得升级
