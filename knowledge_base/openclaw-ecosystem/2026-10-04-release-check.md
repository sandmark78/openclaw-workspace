# OpenClaw 生态探索 - 2026-10-04

## 版本状态
| 项目 | 版本 | 日期 |
|------|------|------|
| **当前运行版本** | 2026.7.1 | - |
| **最新稳定版** | v2026.9.7 | 2026-09-30 |
| **LTS 扩展稳定版** | v2026.8.35 | - |

**状态**: ⚠️ 落后约 2 个月（3157 commits）

---

## v2026.9.7 亮点 (2026-09-30 发布)
- 规模：518 直接提交 · 2,818 PR · 334 贡献者
- 详细变更：https://docs.openclaw.ai/releases/2026.9.7

## v2026.8.35 亮点 (LTS)
### 新增模型支持
- **GPT-6.1 Sol** 支持（OpenAI 路由、发现、推理等）

### 安全与稳定性
- 更安全的更新和恢复：保留插件设置、防止重复 Gateway
- 安全强化：secret-store 轮换稳定、cron 工具白名单
- Agent 完成可靠性：保留完整的委派答案、释放挂起的子进程

### 通道与集成
- Gmail/IMAP 监听修复
- Matrix 直接映射修复
- Telegram 进度修复
- 远程 MCP 启动修复

### 性能
- 模型目录等待边界
- Codex fleet 堆压力降低
- WebChat 历史刷新竞态修复

---

## ClawHub 状态
- 网址：clawhub.ai（已从 .com 重定向）
- 官方技能：GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello
- WhatsApp 插件可用
- CLI 发布流程正常

---

## 建议
1. 考虑升级到 v2026.9.7 或至少 v2026.8.35 (LTS)
2. 关注 GPT-6.1 Sol 模型支持（如需要）
3. 安全更新建议尽快应用

---

*探索时间：2026-10-04 20:00 UTC*
