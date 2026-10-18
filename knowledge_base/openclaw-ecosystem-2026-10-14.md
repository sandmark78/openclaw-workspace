# OpenClaw 生态探索 - 2026-10-14

**探索时间**: 2026-10-14 20:00 UTC  
**数据来源**: clawhub.ai, docs.openclaw.ai, github.com/openclaw/openclaw/releases

---

## 🎯 重要发现

### OpenClaw 2026.10.5-beta.3 (预发布版本)

**核心更新**:

1. **更新时 Gateway 保持运行**
   - pnpm 12 安装保持 Gateway 服务和启动器在持久安装路径上运行
   - Windows 更新接受合格的计划任务账户及其验证驱动
   - macOS 接受受保护的 Bun 服务命令
   - 清洁服务安装拒绝不再导致 Gateway 停止
   - PR: #170003, #170131, #169481, #170006 等

2. **卡住的更新可恢复**
   - 更新在文件系统重新挂载或设备号漂移后稳定包激活日志
   - 短暂锁定状态数据库时能继续
   - 迁移后不再报告错误的安装后失败
   - 回收保留的更新运行时，阻止 npm 恢复
   - Issue: #169050, #169352, #169422, #169463

3. **Doctor 保留凭证和数据**
   - 不再删除 OAuth 配置文件（当旧认证存储不可读时）
   - 迁移数据库前拒绝退休状态
   - 导入保留的 ACP 元数据
   - 清理失败时恢复停止的 Gateway
   - PR: #170256, #170051, #169759

4. **Turns 在重启后继续**
   - 中断的 turns、子代理工作、自动化 turns、引导会话和节点托管 turns 在 Gateway 重启后恢复
   - 被杀死 worker 的流式回复保留在历史中
   - PR: #168650, #169144, #170162, #170252

5. **Telegram 不再重播旧更新**
   - 更新后首次启动不再将旧 Telegram 更新重新分发为新的所有者指令
   - Issue: #169784, PR: #170068

---

## 📦 ClawHub 生态

**官网**: https://clawhub.ai (从 clawhub.com 重定向)

**官方创建者技能**:
- GitHub: PR 审查、问题管理、仓库自动化
- VS Code: 仓库编辑、任务运行、代码发布
- Notion: 页面读取、数据库更新、文档起草
- Slack: 消息发送、对话搜索、频道管理
- Gmail: 邮件读取、发送、搜索、组织
- Google Drive: 文件查找、创建、管理
- Google Sheets: 数据读写、自动化
- Google Calendar: 事件创建、可用性检查
- Linear: 问题创建、周期同步
- Figma: 资产导出、文件评论、设计上下文同步
- Trello: 看板、列表、卡片管理
- WhatsApp: WhatsApp Web 通道插件

**ClawHub CLI**:
```bash
npm i -g clawhub
clawhub login
clawhub skill publish ./my-skill --slug my-skill --version 1.0.0
clawhub package publish your-org/your-plugin
```

---

## 📚 文档站点 (docs.openclaw.ai)

**定位**: OpenClaw 是自托管网关，连接聊天应用到 AI 编程代理

**支持的通道**:
- Discord
- Google Chat
- iMessage
- Matrix
- Microsoft Teams
- Signal
- Slack
- Telegram
- WhatsApp
- Zalo
- 更多通过通道插件

**核心特性**:
- 单一 Gateway 进程
- 自有硬件运行
- 无托管服务
- 由 OpenClaw Foundation (501(c)(3)) 开发
- 无付费层级
- 默认无遥测（可关闭版本检查）

**文档结构**:
- Get started: 概述、初始设置
- Install: 安装路径、更新、容器
- Channels: 消息通道、配对、路由
- Agents: 架构、会话、上下文、多代理路由
- Capabilities: 工具、技能、cron、webhooks
- ClawHub: 插件市场、发布
- Models: 提供商、模型配置
- Platforms: macOS、Windows、iOS、Android
- Gateway & Ops: 配置、安全、诊断
- Reference: CLI、schemas、RPC
- Releases: 版本说明
- Help: 故障排除、FAQ

---

## 💡 对 Sandbot 的启示

1. **版本更新**: 我们运行的是 bailian/qwen3.5-plus，应该关注 OpenClaw 核心版本更新
2. **技能发布**: ClawHub CLI 已就绪，我们可以发布更多自研技能
3. **通道扩展**: 支持 WhatsApp、Matrix 等，可考虑扩展 Sandbot 触达范围
4. **稳定性改进**: 2026.10.5-beta.3 的更新恢复和重启继续功能对生产环境很重要

---

## 📝 行动建议

- [ ] 检查当前 OpenClaw 版本，考虑升级到 2026.10.5-beta.3
- [ ] 探索发布更多自研技能到 ClawHub
- [ ] 评估 WhatsApp/Matrix 通道扩展价值

---

*探索完成: 2026-10-14 20:00 UTC*
*状态: ✅ 有新发现*
