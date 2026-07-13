# OpenClaw 2026.5.31 Pre-release 更新记录

**抓取时间**: 2026-05-31 20:00 UTC
**版本**: 2026.5.31 (Pre-release)
**当前运行**: 2026.3.8 (落后约 2 个月)
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🆕 重大变更摘要

### 1. Agent 运行时恢复增强
- Agent 和 CLI 运行时从中断的工具调用、过期会话绑定、压缩交接、媒体交付重试中恢复更平滑
- PR: #88129, #88136, #88141, #88162, #88182

### 2. 通道稳定性提升
- Telegram、WhatsApp、iMessage、Slack、Discord、Microsoft Teams、Google Chat、Google Meet、iOS realtime Talk 更稳定
- PR: #88096, #88105, #88183, #88231

### 3. Gateway 和通道设置
- Tailscale Serve 服务名绑定
- Communication 通知设置
- 更安全的 agent add
- Discord、Telegram、Slack、Matrix、Teams 进度草稿更可靠
- PR: #74715, #83115, #88314, #88749

### 4. 请求超时管理
- Provider 和 plugin 请求现在对计时器、重试、OAuth/设备码生命周期、媒体下载、本地服务探测、生成内容轮询路径做了更多边界限制，避免挂起

### 5. Skills 系统重大升级 ⭐
- **Skill Workshop** 新增（由 @shakkernerd 贡献）
  - 技能提案的审查流程（apply/reject/quarantine）
  - 提案携带支持文件，带扫描器、hash、回滚保护
  - 待定提案可就地修订，带版本化前置信息
  - skill_workshop agent tool 新增
- Skills 核心索引和集中化运行时加载、状态、过滤、提示格式化

### 6. 插件系统扩展 ⭐
- **@openclaw/tokenjuice** 官方插件外部化（npm + ClawHub 发布元数据）
- **@openclaw/copilot** GitHub Copilot agent 运行时官方插件（npm + ClawHub 发布元数据）
- SecretRef provider 集成 manifest 合约
- 提取共享 LLM 核心包供 provider/plugin 复用

### 7. iOS 增强
- 托管推送中继默认值
- realtime Talk 回放
- 受保护的 WebSocket ping 路径

### 8. Workboard（新！）
- 多 Agent 编排原语和协调工具
- 多 Agent 规划和运行追踪
- PR: #87469

### 9. Control UI
- Dreaming tab 新增 agent 选择器
- Communication Notifications 设置 tab 暴露
- 折叠工具卡片保留工具名和 action 标签

### 10. 代码模式
- 内部命名空间用于 scoped agent/global 会话
- 精确命名空间工具分发

### 11. 修复项
- 异步图像/音乐/视频生成不结束 Codex turn
- 公开 OpenAI API-key profile 不被当作原生 Codex 认证
- Codex app-server 最终答案流式预览
- 认证 profile 原子写入、强制重新登录恢复
- 更多...

---

## 📊 ClawHub 状态
- 52.7k tools
- 180k users
- 12M downloads
- 4.8 avg rating

## 📊 docs.openclaw.ai
- 文档无重大结构变化
- 新增 Node 24 推荐（Node 22 LTS 22.19+ 仍兼容）
- 通道覆盖：Discord、Google Chat、iMessage、Matrix、Microsoft Teams、Signal、Slack、Telegram、WhatsApp、Zalo 等
