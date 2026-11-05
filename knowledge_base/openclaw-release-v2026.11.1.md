# OpenClaw v2026.11.1 发布记录

**抓取时间**: 2026-11-05 20:00 UTC  
**来源**: https://github.com/openclaw/openclaw/releases  
**文档**: https://docs.openclaw.ai/releases

---

## 主要更新

### 1. Mac 安全性改进
- 配置保存失败时不再覆盖 secrets
- 关闭 Tailscale 暴露时保持 Gateway 认证完整
- PR: #187734, #187664

### 2. 频道回复可靠性提升
- Telegram、Discord、webhook 对话在请求处理完成或早期回合结束后仍能触达 agent
- PR: #179200, #179385, #179704, #189457

### 3. 对话中断恢复
- 超长回合保留有用历史
- 停止第一个 Claude CLI 回合不再导致下一条消息从头开始
- PR: #191146, #181966, #186380

### 4. 更新恢复改进
- 崩溃/取消的 updater 不再卡住
- Windows Gateway 验证失败后恢复
- 大状态检查时避免重复全量数据库复制
- PR: #177932, #186787, #189647, #182632, #187921

### 5. 子 Agent 改进
- 子 Agent 在模型和会话变更后保留后续操作
- 父会话即使使用自定义 session store 也能收到子 Agent 审批
- PR: #186238, #183501, #189827

### 6. Android 通话结束改进
- 兼容 Gateway 的"结束通话"不再取消已接受的 agent 工作
- 答案仍可送达聊天中；显式取消仍可用
- PR: #172276, #188798

### 7. Provider 恢复改进
- 尊重 provider 指定的限速时间
- Gemini Flash 文本模型默认使用 Interactions

---

## 近期版本线 (2026年10-11月)

| 版本 | 亮点 |
|------|------|
| v2026.11.1 | 更新/对话/应用/模型连接补丁修复 |
| v2026.10.10 | Chat Details, 实验性 Advisor, 浏览器 Talk 分体语音模式 |
| v2026.10.9 | 安全修复 |
| v2026.10.8 | 安全补丁 |
| v2026.10.7 | 更新/恢复/回复补丁 |
| v2026.10.6 | 安全修复, Windows 设置, Discord 命令, iPhone Talk 修复 |
| v2026.10.5 | 刷新侧边栏, Skill Workshop 2.0, 公开对话链接 |
| v2026.10.4 | 更新/恢复修复, 聊天刷新, 消息/登录修复 |
| v2026.10.3 | 更新/Doctor 修复, Mac 设置, 对话延续, Muse Wonder/MiniMax 修复 |
| v2026.10.2 | 升级/修复, 缺失/重复回复, 长对话, 凭证掩码 |
| v2026.10.1 | 已安装技能发现, MCP Apps, 完整备份 |

---

## ClawHub 生态现状

- 域名已迁移至 clawhub.ai (从 clawhub.com 重定向)
- 官方创作者专区: /official
- 支持应用集成: GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello, WhatsApp
- CLI 发布流程: `clawhub skill publish` / `clawhub package publish`
