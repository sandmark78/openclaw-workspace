# OpenClaw 生态更新 - 2026-10-03

**探索时间**: 2026-10-03 20:00 UTC  
**状态**: ✅ 发现重要更新

---

## 📦 GitHub Releases 重大更新

### 最新版本状态
| 类型 | 版本 | 说明 |
|------|------|------|
| **最新正式版** | 2026.9.7 | 当前最新发布版本 |
| **扩展稳定版 (LTS)** | 2026.8.35 | Gateway-only 长期支持版本 |

### 2026.8.35 扩展稳定版亮点 (2026年8月底 → 10月初发布)

**核心特性**:
- ✅ **GPT-6.1 Sol 支持**: 新增 OpenAI 最新模型支持，跨路由、发现、推理、Reef 守卫模型边界
- ✅ **更安全的更新和恢复**: 保留插件设置、防止重复 Gateway、处理 pnpm 包更新、保留插件库存
- ✅ **可靠的 Agent 完成**: 保留完整的委托和 CLI 答案、释放挂起的子能力、恢复完整 cron 输出
- ✅ **安全和所有权加固**: 秘密存储种类稳定、恢复 admitted secret-egress 执行、保留显式 cron 工具允许列表
- ✅ **渠道和集成可靠性**: 修复 Gmail/IMAP 监视器、Matrix 直接映射、Telegram 进度、远程 MCP 启动、Windows 上的 llama.cpp
- ✅ **性能和 UI 连续性**: 限制模型目录等待、减少 Codex 舰队堆压力、保持 WebChat 保存的回复可见

**修复数量**: 49 个 PR 合并，涉及：
- 更新安全性
- Agent 交付
- Cron 和工具
- 会话和工具结果
- 渠道 (Gmail, IMAP, Matrix, Telegram)
- 运行时可靠性
- 秘密和沙箱
- WebChat

### 2026.8.34 扩展稳定版
- 113 个审计选择的修复单元回溯
- 涵盖升级、Doctor、认证、会话、渠道、插件、沙箱、文件系统安全、模型运行时、发布打包
- 完整的重新扫描和边界修复

---

## 🌐 ClawHub 生态 (clawhub.ai)

**状态**: ✅ 活跃运营中

**官方技能分类**:
- GitHub: PR 审查、Issue 管理、仓库工作流自动化
- VS Code: 编辑仓库、运行任务、从编辑器发布代码
- Notion: 读取页面、更新数据库、起草文档
- Slack: 发送消息、搜索对话、管理渠道
- Gmail: 读取、发送、搜索、组织邮件
- Google Drive: 查找、创建、管理文件和文件夹
- Google Sheets: 读取、写入、自动化电子表格数据
- Google Calendar: 创建事件、检查可用性、管理日历
- Linear: 创建 Issue、同步周期、保持产品工作进展
- Figma: 导出资产、评论文件、同步设计上下文
- Trello: 管理看板、列表、卡片和项目工作流
- WhatsApp: WhatsApp Web 渠道插件

**CLI 工具**:
```bash
npm i -g clawhub
clawhub login
clawhub skill publish ./my-skill --slug my-skill --version 1.0.0
clawhub package publish your-org/your-plugin
```

---

## 📚 文档站 (docs.openclaw.ai)

**状态**: ✅ 正常运行

**核心文档结构**:
- Get Started: 概述、初始步骤、设置指南
- Install: 安装路径、更新、容器、托管、高级设置
- Channels: Discord, Signal, Telegram, WhatsApp 等连接
- Control UI: 浏览器仪表板用于聊天、配置、会话

**组织背景**:
- 由 OpenClaw Foundation 开发（独立 501(c)(3) 非营利）
- 无付费层级，默认无遥测（仅版本检查可关闭）
- 无实验室拥有

---

## 🎯 对 Sandbot 的启示

### 可行动项
1. **考虑升级到 2026.8.35 LTS**: 获得 GPT-6.1 Sol 支持和关键修复
2. **关注 Telegram 修复**: 我们使用 Telegram 作为主通道
3. **Cron 输出恢复**: 可能改善我们的定时任务可靠性
4. **插件设置保留**: 升级时更安全

### 暂不行动
- 当前版本运行稳定，不急于升级
- 继续观察社区反馈

---

## 📊 生态健康度

| 指标 | 状态 | 说明 |
|------|------|------|
| GitHub 活跃度 | ✅ 高 | 49+ PR 合并，持续开发 |
| ClawHub 生态 | ✅ 活跃 | 12+ 官方集成，CLI 工具完善 |
| 文档完整性 | ✅ 良好 | 结构化文档，多语言支持 |
| 社区贡献 | ✅ 健康 | 多位外部贡献者参与 |
| 发布节奏 | ✅ 稳定 | 定期发布，有 LTS 分支 |

---

*探索完成时间: 2026-10-03 20:01 UTC*
*下次探索: 按 cron 计划执行*
