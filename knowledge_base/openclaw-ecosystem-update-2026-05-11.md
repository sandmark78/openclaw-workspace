# OpenClaw 生态探索记录 — 2026-05-11

**探索时间**: 2026-05-11 20:00 UTC  
**触发**: 定时生态探索 Cron  
**上次探索**: 2026-05-05

---

## 1. ClawHub (clawhub.com → clawhub.ai)

- 状态：稳定，与 2026-05-05 一致
- 52,700 工具 | 180,000 用户 | 1,200 万下载 | 4.8 评分
- 三大板块：Skills、Plugins、Publishers

---

## 2. GitHub Releases — Pre-release 2026.5.11 (2026-05-11)

**新 Pre-release 发布**，上次记录为 2026.4.29 (Latest) / 2026.5.4 (生态记录)

### 核心变化
- **Agent-to-Agent 多轮对话上限提升到 20 轮**（默认 5）
- 新增 `/context map` 命令（上下文树状图可视化）
- 新增 per-agent message tool crossContext/actions.allow 覆盖
- Fal Provider 增强：GPT Image 2 / Nano Banana 2 编辑支持
- 构建升级到 **pnpm 11**
- Control UI 新增纯 HTML 恢复面板
- 系统提示裁剪减少 token 消耗
- 本地模型按需启动 (localService)
- Slack unfurlLinks/unfurlMedia 配置

### 详情 → knowledge_base/openclaw-github-release-2026-05-11.md

---

## 3. Docs (docs.openclaw.ai)

- 正常运行，文档结构稳定
- 无重大新增板块

---

## 总结

本次探索发现 1 个新 Pre-release (2026.5.11)，含 Agent 通信增强、上下文可视化、pnpm 11 升级等重要变更。ClawHub 和 Docs 无显著变化。
