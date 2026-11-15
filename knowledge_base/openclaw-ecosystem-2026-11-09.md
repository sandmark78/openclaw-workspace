# OpenClaw 生态探索 - 2026-11-09

## 版本状态
- **当前版本**: 2026.7.1
- **最新正式版**: 2026.11.1 (落后约4个月)
- **最新预发布版**: 2026.11.5-beta.1

## 2026.11.1 正式版重要更新

### 核心改进
1. **更安全的 Mac 设置** - 配置保存失败不再覆盖 secrets
2. **更可靠的频道回复** - Telegram/Discord/Webhook 对话保持连接
3. **对话容错增强** - 超大 turn 保留有用历史，停止 Claude CLI 首轮不再丢失上下文
4. **更新恢复改进** - 崩溃/取消后不再卡住
5. **子 Agent 增强** - 模型和会话变更后保持后续对话
6. **Android 通话改进** - 结束通话不再取消已接受的 agent 工作

### 新功能
- **Claude CLI 集成** - 订阅账户可直接使用配置模型，支持原生 Agent/Workflow 编排
- **Anthropic Workspace ID** - API-key 可记录可选工作区 ID
- **Google Interactions** - 托管代理和 TLS 设置支持
- **Bedrock Mantle** - 自动选择 Responses/Chat Completions 路由
- **Control UI** - 模型选择器显示实际上下文预算

### 安全修复
- ClickClack/ClawHub 拒绝重定向到私有服务
- Discord CDN 下载不再继承浏览器私有网络访问
- 拒绝不受信任的 emSign ECC G3 根证书
- 日志脱敏改进

### 频道修复
- Slack 检测死连接
- Feishu 保留工具调用前后的文本
- iMessage PostgreSQL 兼容性
- Tlon 重连改进

---

## 2026.11.5-beta.1 预发布版

### 重大新功能
1. **Knowledge Scribes** - 一等公民知识捕获和可复用 scribe 工作流
2. **PostgreSQL 数据平面** - PostgreSQL 后端状态存储 + 迁移工具

---

## 建议行动
- [ ] 考虑升级到 2026.11.1（稳定性改进很多）
- [ ] Knowledge Scribes 功能值得关注（与我们的知识库系统相关）
- [ ] PostgreSQL 数据平面如果成熟，可能替代当前文件存储

## ClawHub 状态
- 域名已迁移到 clawhub.ai（原 clawhub.com 自动跳转）
- 官方技能集成：GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello, WhatsApp
- CLI 发布流程：`clawhub skill publish` / `clawhub package publish`

## 文档站状态
- docs.openclaw.ai 正常运行
- 文档结构完整：安装、频道、Agent、工具、ClawHub、模型、平台、网关、参考、发布、帮助
