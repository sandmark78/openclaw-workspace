# OpenClaw 版本追踪

**最后检查**: 2026-09-22 20:00 UTC

## 当前状态
| 项目 | 版本 |
|------|------|
| 本机安装 | 2026.7.1 |
| 最新稳定版 | 2026.9.5 |
| 扩展稳定版(LTS) | 2026.7.35 |

## 版本差距分析
- 本机 2026.7.1 → 最新 2026.9.5，**落后约 2 个月**
- 2026.9.5: 64 direct commits, 4179 PRs, 503 contributors
- 2026.7.35: 扩展稳定版，含安全修复和可靠性改进

## 2026.7.35 关键修复 (LTS)
- Doctor 插件注册表修复（Browser/Canvas/pairing/file-transfer 等默认插件）
- 安全加固：命令解析、浏览器 origin 检查、插件 Git 安装
- 消息完整性：保留排队/导入/流式消息
- 通道修复：Discord/Matrix/Telegram/Slack/WhatsApp/LINE/Feishu/Zalo

## 2026.9.5 亮点
- 503 位贡献者
- 大量 PR 合并 (4179)
- 文档：https://docs.openclaw.ai/releases/2026.9.5

## ClawHub 生态
- clawhub.com → clawhub.ai (已迁移)
- 支持技能：GitHub/VS Code/Notion/Slack/Gmail/Google Drive/Sheets/Calendar/Linear/Figma/Trello/WhatsApp
- CLI 发布工具：`clawhub skill publish` / `clawhub package publish`

## 升级建议
⚠️ 建议升级到 2026.7.35 (LTS) 或 2026.9.5 (最新)
- 安全修复重要
- 需老大确认后执行
