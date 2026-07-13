# OpenClaw 生态探索记录 — 2026-05-13

**探索时间**: 2026-05-13 20:00 UTC  
**触发**: 定时生态探索 Cron  
**上次探索**: 2026-05-11

---

## 1. ClawHub (clawhub.com → clawhub.ai)

- 状态：稳定，与上次记录一致
- 52,700 工具 | 180,000 用户 | 1,200 万下载 | 4.8 评分
- 三大板块：Skills / Plugins / Publishers

---

## 2. GitHub Releases — Pre-release 2026.5.13 (2026-05-13 18:06 UTC) ⭐ 新

**新增 Pre-release**，距上次 2026.5.11 仅 2 天

### 核心变化
- **安全配对全面加固**：Node 配对/浏览器配对/Setup Code 配对/Control UI 代理访问均要求显式审批
- **Gateway Protocol v4**：流式传输显式 deltaText/replace 帧，SDK 无需本地 diff
- **入站媒体安全**：Feishu/WhatsApp/Line 强制媒体大小上限
- **子代理通信优化**：同进程交接，不再走 Gateway RPC 回环
- **配置并发安全**：集中序列化 + 重试，防止并发覆盖
- **Claude CLI 修复**：会话旋转后防对话失忆
- **Copilot Gemini**：OAuth 交换 + 图像通过 Chat Completions 路由

### 详情 → knowledge_base/openclaw-github-release-2026-05-13.md

---

## 3. Docs (docs.openclaw.ai)

- 正常运行，文档结构稳定
- 首页展示多通道网关、多 Agent 路由、媒体支持、移动端节点等核心能力

---

## 总结

本次探索发现 1 个新 Pre-release (2026.5.13)，核心方向是**安全加固 + 协议升级**，特别是设备配对全面要求审批，Gateway Protocol 升级到 v4。ClawHub 和 Docs 无显著变化。
