# OpenClaw 生态探索记录 (2026-08-03)

## 🔖 版本状态

| 项目 | 当前 | 最新 | 差距 |
|------|------|------|------|
| OpenClaw Gateway | v2026.3.8 | v2026.7.2 (pre-release) | **落后 ~4 个月** |

## 🆕 v2026.7.2 Pre-release 核心亮点

**发布日期**: 2026 年 7 月底 / 8 月初  
**状态**: Pre-release (beta)

### 1. 状态安全与恢复 (State Safety & Recovery)
- 隔离存储 (quarantine store)：主数据库损坏时数据仍能存活
- 崩溃可恢复的 SQLite 快照
- 崩溃持久化的文件系统发布 (crash-durable filesystem publication)
- Schema 升级数据丢失拒绝机制
- 回滚写入器快照恢复
- PR: #110453, #113367, #113453, #113473, #113580

### 2. 持久通道投递 (Durable Channel Delivery)
- 网关重启和本地崩溃后消息可恢复
- 共享入口排空 (ingress drain) + 死信恢复
- 覆盖通道：Telegram, Signal, Slack, QQBot, Twitch, Synology Chat, Tlon, IRC, Zalo User
- Issue: #108656, #107246, #109911
- PR: #108924, #107288, #109907, #109910, #110844, #110852 等 11 个 PR

### 3. 会话倒带与分支 (Session Rewind & Branching)
- 从单条消息倒带或分叉对话
- 跨 Web 和原生应用切换转录分支
- 分叉上游 Codex 会话
- 分支安全的排队发送

### 4. 交互式 MCP 应用和仪表板
- (详情待后续探索)

## 🏪 ClawHub 生态新发现

### 域名确认
- clawhub.com 已重定向到 clawhub.ai ✅

### 新发现的有趣技能
| 技能 | 作者 | 描述 | 热度 |
|------|------|------|------|
| humanizer-zh | liuxy951129-cpu | 去除文本 AI 生成痕迹 (中文) | 65 |
| openclaw-backup | alex3alex | OpenClaw 数据备份与恢复 | 47 |
| spendcap | receiptprotocol | AI Agent 消费限额控制 | 61 |
| wechatlayout | qomob | 微信公众号排版引擎 | 53 |
| browser-testing-toolkit | paudyyin | 浏览器测试自动化工具包 | 51 |
| privacymask | zxj2devs | 本地数据脱敏与隐私保护 | 65 |
| reddit-automation | doany-skills | Reddit 自动化工具 | - |
| design-hub | yofine | 设计系统管理中心 | 28 |
| growth-calendar | timothe | SEO 文章规划日历 | 81 |
| ai-legal-helper | lzhui998-ui | AI 法律助手 (RAG) | 28 |
| social-media-toolkit | thcjp | 专业社交网络工具箱 | 21 |
| d-writer | dragon-qx | 小说创作/续写/审计工具 | 28 |

### 值得关注的技能
1. **openclaw-backup** - 备份恢复工具，对我们有用
2. **spendcap** - 消费限额控制，符合我们的成本控制需求
3. **privacymask** - 数据脱敏，安全相关
4. **growth-calendar** (热度 81) - SEO 规划，变现相关

## 📝 与上次探索对比 (vs 2026-07-24)

| 变化项 | 上次 (07-24) | 本次 (08-03) |
|--------|-------------|-------------|
| 最新稳定版 | v2026.7.1 | v2026.7.2 (pre-release) |
| 状态安全 | 未提及 | ✅ 隔离存储+快照恢复 |
| 持久投递 | 未提及 | ✅ 死信恢复+入口排空 |
| 会话分支 | 未提及 | ✅ 倒带+分叉 |
| ClawHub 域名 | clawhub.ai | clawhub.com → clawhub.ai 重定向确认 |

## 💡 建议

1. **升级评估**: v2026.7.2 的状态安全和持久投递对我们在 Telegram 上的稳定性很有价值
2. **技能安装**: openclaw-backup 和 spendcap 值得安装测试
3. **持续监控**: v2026.7.2 目前是 pre-release，等稳定版再升级
