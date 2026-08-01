# OpenClaw 生态探索 - 2026-07-18

## 版本状态

| 项目 | 当前 | 最新稳定 | 最新 Beta |
|------|------|----------|-----------|
| OpenClaw | 2026.3.8 | 2026.7.1 | 2026.7.2-beta.2 |

**版本差距**: 约 4 个月的更新未应用

## 2026.7.2 主要更新亮点

### 1. 远程编码会话 (Remote Coding Sessions)
- Control UI 会话可在云端 worker 上运行
- 支持在宿主终端中打开 Codex 和 Claude catalog 会话
- 可直接在终端中恢复 OpenCode 和 Pi 会话
- PR: #107670, #107086, #107200

### 2. 原生自动化与节点 (Native Automation & Nodes)
- 移动端自动化功能对齐
- Android 新增前台 Voice Wake
- 无头 Linux 节点暴露摄像头、位置、通知能力
- PR: #106355, #107081, #107193

### 3. 更安全的通道运行 (Safer Channel Operation)
- 修复 Telegram 重启后 durable-ingress 丢失问题
- Signal 停止和审批控制在活跃 turn 期间保持响应
- 通道 allowlist 不再授予 owner 权限
- PR: #107288, #107422, #107403

### 4. 引导式 Control UI 设置 (Guided Control UI Setup)
- 从 Settings 配置模型提供商
- 通过引导页面接入通道
- 创建会话时可选择图片和模型
- PR: #106490, #106469, #107358

### 5. Gateway 和会话恢复 (Gateway & Session Recovery)
- 防止重启准入阻塞 Gateway
- finalization 卡住后恢复 reply 会话
- 一次性 cron 任务在生命周期竞争期间保持启用
- PR: #107339, #106792, #107236

## ClawHub 状态
- 域名已迁移至 clawhub.ai（从 clawhub.com 重定向）
- 支持技能发布: `clawhub skill publish`
- 支持包发布: `clawhub package publish`
- 官方创作者板块上线
- 已集成: GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello, WhatsApp

## 文档站 (docs.openclaw.ai)
- 结构正常，涵盖: 入门、安装、通道、Agent 架构、能力等
- 支持的通道: Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等

## 建议
- ⚠️ 考虑升级到 2026.7.1 稳定版（差距 4 个月，重要修复较多）
- 特别关注 Telegram durable-ingress 修复（影响我们当前通道）
- Gateway 恢复改进也与我们的心跳机制相关
