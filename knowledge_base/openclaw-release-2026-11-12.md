# OpenClaw 生态探索记录 - 2026-11-12

## GitHub Releases 新发现

### 版本：2026.11.5-beta.2 (Pre-release)

**发布日期**: 2026年11月5日  
**检查时间**: 2026-11-12 20:00 UTC

#### 重要更新

**1. 大对话历史分页浏览**
- 长对话现在支持双向分页浏览
- 可见的历史边界
- 有界归档读取
- PRs: #188450, #188483, #188557, #188372, #190690
- 作者: @steipete, 感谢 @xydt-tanshanshan

**2. macOS 应用改进**
- 配置保存失败或 Tailscale 暴露关闭时，保留已保存的密钥和 Gateway 认证
- PRs: #187734, #187664
- 相关 issues: #187600, #187597
- 贡献者: @anmol0b

**3. Android Talk 功能修复**
- 结束 Talk 不再取消 Gateway 已接受的工作
- PR: #188798
- 相关 issue: #188134
- 贡献者: @RomneyDa, @jeffjhunter

**4. Google Gemini 集成优化**
- Gemini Flash 模型在官方端点使用 Interactions API
- 保留自定义端点覆盖能力
- PR: #189395
- 贡献者: @obviyus

**5. 安全修复**
- 使用 fast-uri 4.2.3 拒绝格式错误的 URI 标识符，同时保留有效的相对引用 (PR #187284)
- 在 Discord SDK 及其 Zod 3 解析器中提前拒绝过大的有界集合 (PR #187296)

#### 贡献者致谢
- @steipete (核心开发)
- @xydt-tanshanshan
- @anmol0b
- @RomneyDa
- @jeffjhunter
- @obviyus
- @shakkernerd

---

## ClawHub 状态

**网址**: clawhub.com → clawhub.ai (重定向)  
**状态**: 正常运行

### 当前技能分类
- GitHub: PR 审查、issue 管理、仓库工作流自动化
- VS Code: 编辑仓库、运行任务、从编辑器发布代码
- Notion: 读取页面、更新数据库、起草文档
- Slack: 发送消息、搜索对话、管理频道
- Gmail: 读取、发送、搜索、组织邮件
- Google Drive/Sheets/Calendar: 文件管理、电子表格自动化、日历管理
- Linear: issue 创建、周期同步
- Figma: 资产导出、文件评论、设计上下文同步
- Trello: 看板、列表、卡片管理
- WhatsApp: WhatsApp Web 频道插件

### CLI 工具
```bash
npm i -g clawhub
clawhub login
clawhub skill publish ./my-skill --slug my-skill --version 1.0.0
clawhub package publish your-org/your-plugin
```

---

## 文档站点

**网址**: docs.openclaw.ai  
**状态**: 正常运行

### 主要文档区域
- Get started: 概述、第一步、设置指南
- Install: 安装路径、更新、容器、托管、高级设置
- Channels: Discord、Signal、Telegram、WhatsApp 等连接
- Control UI: 浏览器仪表板（聊天、配置、会话）

### 核心特性
- 开源 AI 助手，运行在自己的硬件上
- 支持所有主流聊天应用
- 一个 Gateway，任意模型，任意设备
- 由 OpenClaw Foundation (501(c)(3)) 开发
- 无托管服务，无默认遥测（可关闭版本检查）

---

## 总结

✅ **发现新版本**: 2026.11.5-beta.2 (Pre-release)
- 大对话历史分页功能（对长会话很有用）
- macOS/Android 客户端改进
- Google Gemini 集成优化
- 安全修复

✅ **ClawHub**: 正常运行，技能生态稳定
✅ **文档站**: 正常运行，结构清晰

**建议**: 关注 2026.11.5-beta.2 的大对话分页功能，可能对 Sandbot 的长会话管理有帮助。
