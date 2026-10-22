# 生态探索更新 2026-10-21

**检查时间**: 2026-10-21 20:00 UTC

---

## 🟢 发现新变化

### GitHub Releases
| 项目 | 状态 |
|------|------|
| 最新稳定版 | **v2026.10.5** (2026-10-18 发布) |
| 最新 Beta | 2026.10.10-beta.3 |
| 当前安装版本 | 2026.7.1 |
| 版本差距 | **约 3 个月** |

### v2026.10.5 主要更新亮点
- **Windows 可靠性改进**: 恢复 fresh state 初始化、Gateway 启动优化、SQLite helper 窗口隐藏
- **升级恢复机制**: app-owned plugins 自动对齐核心版本、schema 变更后 agent store 恢复
- **Agent 状态修复**: 并发初始化不再允许两个 agent 抢占同一数据库
- **Codex/native apps**: 预览不再阻塞

### ClawHub 变化
- 域名从 clawhub.com 重定向到 **clawhub.ai**
- 定位更新: "Skills and plugins for OpenClaw agents"
- 新增官方集成技能:
  - GitHub (PR review, issue 管理)
  - VS Code (编辑器内操作)
  - Notion (页面读取、数据库更新)
  - Slack (消息、搜索、频道管理)
  - Gmail (邮件读写搜索)
  - Google Drive/Sheets/Calendar
  - Linear、Figma、Trello
  - WhatsApp Web 插件
- CLI 发布流程: `clawhub skill publish` / `clawhub package publish`

### docs.openclaw.ai
- 结构稳定，文档完整
- 新增/完善: Control UI、Channels、Install 指南

---

## ⚠️ 建议

- 当前版本 2026.7.1 落后最新稳定版 v2026.10.5 约 3 个月
- 建议择机执行 `openclaw gateway update` 升级
- ClawHub 新增大量官方集成技能，值得探索安装

---

## 📊 对比上次 (2026-05-16)

| 项目 | 上次 | 本次 | 变化 |
|------|------|------|------|
| 最新稳定版 | 2026.5.12 | 2026.10.5 | +5 个月版本 |
| 当前安装版 | 2026.3.8 | 2026.7.1 | 已升级 |
| ClawHub 域名 | clawhub.com | clawhub.ai | 变更 |
| ClawHub 定位 | 技能市场 | 官方集成+技能 | 重大更新 |
