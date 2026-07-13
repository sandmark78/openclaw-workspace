# OpenClaw 生态扫描报告 — 2026-06-22

**扫描时间**: 2026-06-22 20:00 UTC  
**扫描者**: Sandbot 自动生态探索 (Cron)

---

## 📊 版本状态

| 项目 | 当前版本 | 最新稳定版 | 差距 |
|------|----------|------------|------|
| OpenClaw | 2026.3.8 | v2026.6.9 | ~3 个月，12 个稳定版本 |
| GitHub Beta | - | v2026.6.10-beta.2 (2026-06-22) | 最新 beta 已发布 |

---

## 🔥 重要版本更新 (2026.3.8 → v2026.6.9)

### v2026.6.9 (2026-06-21) ⭐ 最新稳定版
- **更丰富的 Telegram 推送**: 发送富 HTML、保留 rich markdown 和 sticker 路径、更忠实地渲染进度草稿和命令输出、安全地标准化 HTML 表格
- **更可靠的 Agent 恢复**: 重试、终端结果、压缩后的使用情况、会话历史修复和回复协调

### v2026.6.8 (2026-06-16)
- **更丰富的频道推送**: Telegram 渲染结构化文本（表格、列表、可扩展引用块、保留换行）、WhatsApp 现已支持配置的 ACP 绑定
- **更可靠的 Agent 运行**: 账户作用域 DM 发送、生成的媒体完成、自动回复消息工具最终回复

### v2026.6.6 (2026-06-12)
- **更紧的安全边界**: transcript、sandbox、MCP、browser、channel、exec-approval 路径现在在不安全访问、超时审批、畸形输入时 fail closed
- **可靠的 Telegram 推送**: 账户作用域主题路由到正确 agent、流式文本在工具调用中存活

### v2026.6.5 (2026-06-09)
- **更安全的频道输出**: QQBot 在推送前剥离模型推理和思考脚手架
- **MCP 结果不再污染会话**: resource_link、音频、畸形图像在 provider 转换前被标准化

### v2026.6.1 (2026-06-03)
- **弹性 Agent 和 Codex 运行**: 中断的工具调用、过期会话绑定、压缩交接、auth-profile failover 都能恢复
- **更可靠的频道和移动端推送**: WhatsApp、iMessage、Discord、QQBot、iOS Talk 在重启和传输失败后保持连接

### v2026.5.x 系列 (2026-05-18 至 2026-05-30)
- 共 6 个稳定版本 (v2026.5.18 → v2026.5.28)
- 持续改进 Agent 运行、频道推送、安全边界

---

## 🏪 ClawHub 动态

- **域名变更**: clawhub.com → clawhub.ai (自动重定向)
- **热门技能/插件**:
  - GitHub (Review PRs, 管理 issues, 自动化工作流)
  - VS Code (编辑 repo, 运行任务, 发布代码)
  - Notion (读取页面, 更新数据库, 起草文档)
  - Slack (发送消息, 搜索对话, 管理频道)
  - Gmail (读取、发送、搜索、整理邮件)
  - Google Drive / Sheets / Calendar (文件、表格、日历)
  - Linear (创建 issues, 同步 cycles)
  - Figma (导出资源, 评论文件)
  - Trello (管理 boards, lists, cards)
  - WhatsApp Web (频道插件)
- **ClawHub CLI**: `npm i -g clawhub` → `clawhub login` → `clawhub skill publish`

---

## 📚 文档 (docs.openclaw.ai)

- 文档首页正常访问
- 核心内容: 安装引导、模型 provider、插件、工具
- 无 changelog 页面 (404)

---

### v2026.6.10-beta.2 (2026-06-22) 🔥 今日发布
- **自动 fast mode**: 短对话自动启用 fast mode，长对话回到正常模式
- **更可靠的模型路由**: Zai 模型合成、GLM 过载 failover、原生 reasoning 级别选择
- **更安全的会话和频道状态**: 频道切换重置过期 origin 字段，cron 交付感知保持绑定到目标会话
- **trusted policies 在 hook 组合中存活**: 组合 hook 注册表保留审批敏感流程所需的 trusted tool policies

---

## 💡 建议

1. **版本升级**: 从 2026.3.8 到 v2026.6.9 有 12 个稳定版本，建议升级（包含大量 Telegram 推送改进和安全加固）
2. **ClawHub 新技能**: 多个新技能和插件可用，可浏览 clawhub.ai 探索
3. **Beta 测试**: v2026.6.10-beta.2 已发布（2026-06-22），包含自动 fast mode、更可靠的模型路由
