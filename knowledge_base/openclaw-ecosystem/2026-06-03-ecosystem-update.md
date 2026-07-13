# OpenClaw 生态探索记录 — 2026-06-03

**探索时间**: 2026-06-03 20:00 UTC  
**触发**: 定时生态探索 Cron

---

## 📦 版本更新

| 项目 | 当前版本 | 最新版本 | 状态 |
|------|----------|----------|------|
| OpenClaw | 2026.3.8 | **2026.5.28** | ⚠️ 有更新可用 |

发布日期：2026-06-03（今天的 release）

---

## 🔥 2026.5.28 Release 核心变更

### 1. Skill Workshop（新功能）
- 完整的 Control UI 流程
- 技能提案列表 + 今日操作
- 版本修订交接、可搜索文件预览
- 审核状态 + 本地覆盖 + 可复用会话路由
- `skill_workshop` agent 工具支持 apply/reject/quarantine

### 2. Workboard（新功能）
- 多 Agent 编排原语 + 运行追踪
- 任务看板 + 任务评论编辑模态
- Agent 协调工具

### 3. 插件外部化
- **Tokenjuice** → 官方 `@openclaw/tokenjuice` 插件（npm + ClawHub）
- **GitHub Copilot** → 官方 `@openclaw/copilot` 插件（npm + ClawHub）

### 4. Code Mode 增强
- 内部命名空间：Scoped agent/global sessions
- MCP API 文件 + 文档
- 精确命名空间工具分发

### 5. iOS 增强
- 托管 Push Relay 默认值
- Realtime Talk 播放
- 受保护 WebSocket ping 路径
- **原生 iPad 显示布局支持**

### 6. Agent 运行时恢复性改进
- 中断工具调用、过期会话绑定、压缩交接、媒体投递重试的更好恢复
- PR: #88129, #88136, #88141, #88162, #88182

### 7. 渠道稳定性
- Telegram, WhatsApp, iMessage, Slack, Discord, Teams, Google Chat/Meet 投递更稳定
- iOS realtime Talk 改善

### 8. Provider 覆盖扩展
- MiniMax M3 支持
- Google/Vertex catalog 修复
- OpenRouter SQLite 模型缓存
- Copilot Claude 1M 能力
- Foundry reasoning 对齐

### 9. 性能优化
- Skills、会话元数据、Gateway 运行时状态热路径优化
- 更少重复工作，配置/分发/Linux 文件监控行为稳定
- iMessage 监控 + 入队 + 插件安装账本迁移到 SQLite

### 10. Control UI 改进
- 更平静的聊天编辑器控件
- 本地草稿打字保留
- 发送后清除编辑器
- 首次输出延迟追踪
- Dreaming-tab Agent 选择器

### 11. SecretRef 改进
- 插件清单中的 SecretRef 支持
- 技能/插件加载更好地处理过期禁用快照

---

## 🌐 ClawHub 状态

- 域名从 clawhub.com 重定向到 clawhub.ai
- 统计数据：**52.7k 工具 / 180k 用户 / 12M 下载 / 4.8 平均评分**
- 支持 Skills / Plugins / Audits 三个板块
- 支持发布 Skills 和 Plugins

---

## 📚 Docs 状态

- docs.openclaw.ai 正常
- 文档结构更新，新增 Skill Workshop 专题文档
- Features 页面列出 35+ 模型提供商支持

---

## ⚡ 建议操作

1. **升级 OpenClaw**：`npm install -g openclaw@latest`（从 2026.3.8 → 2026.5.28）
2. **关注 Skill Workshop**：新功能，可能对技能发布流程有影响
3. **关注 Workboard**：多 Agent 编排新工具，适合联邦架构

---

*下次探索前建议对比此记录*
