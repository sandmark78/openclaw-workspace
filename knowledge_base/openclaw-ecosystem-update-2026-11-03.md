# OpenClaw 生态更新 - 2026-11-03

## 版本状态
- **当前版本**: 2026.7.1
- **最新稳定版**: 2026.10.9
- **最新预发布**: 2026.10.10-beta.5
- **落后**: 3-4 个版本

## 2026.10.9 关键更新 (最新稳定版)

### 安全补丁 (重要)
- fast-uri 4.2.3: 拒绝畸形 URI scheme 和 host
- Zod: A2UI/Discord 超大集合提前拒绝
- nodemailer 10.1.4: IMAP 发送者解析修复，防止伪造
- MSAL Node 7.1.1: Microsoft Teams 补丁

### 安全边界强化
- `tools.fs.workspaceOnly` 扩展到 Gateway 构建的工具
  - delegate 工具现在需要审批
  - media 工具限制在 workspace 内
- MCP CLI 检查不再暴露实时凭证
- Google OAuth client secrets 日志脱敏

### 更新/回滚安全
- npm 回滚失败不再导致包丢失
- Git 回滚保留操作者编辑
- 更新执行器死亡后恢复离线状态

### 数据恢复
- SQLite tokenizer 变更后恢复数据库和全文索引
- 大文件转录迁移不超 Node.js 字符串限制
- 磁盘满后空间恢复时 agent 自动恢复（无需重启）

### Cron 修复
- 错过的 slot 不再被丢弃（stale next run time 修复）
- 重启后 catch-up 运行正常

## 2026.9.36 关键更新

### 安全
- workspaceOnly 限制扩展到 Gateway 构建工具
- Microsoft Teams allowlist 未解析时保持封闭（不再开放给所有团队）
- 不可信输入边界：Matrix 媒体元数据、IMAP 邮件、TOML、URI 解析限制

### 修复
- emoji/astral 字符后的文本不再被截断
- Docker 镜像架构构建更可靠
- xAI: 旧模型无 reasoning effort 配置时不再报错

## 2026.10.10-beta.5 预发布亮点

- Node 兼容性放宽：>=24.16.0 <25 || >=26.1.0
- Gateway streaming 修复：含 tool-call XML 的回复不再卡住
- Cron: 错过的 slot 恢复 + 重启 catch-up
- 大量安全边界修复（exec allowlist、browser proxy、sandbox）
- 终端输出转义修复（防止控制序列注入）
- 会话保留改进（transcript ID、model account 跨重置保留）
- 子 agent 崩溃预防
- Gateway 重启可靠性提升

## ClawHub 状态
- 域名 clawhub.com 已重定向到 clawhub.ai
- 新增官方集成：GitHub、VS Code、Notion、Slack、Gmail、Google Drive/Sheets/Calendar、Linear、Figma、Trello、WhatsApp
- CLI 发布流程：`clawhub skill publish` / `clawhub package publish`

## 建议
1. **考虑升级到 2026.10.9** - 安全补丁重要
2. 关注 workspaceOnly 变更对现有技能的影响
3. Cron 修复对我们的心跳/定时任务有正面影响
4. Node 兼容性放宽意味着未来升级更灵活
