# OpenClaw 生态扫描报告 — 2026-06-26

**扫描时间**: 2026-06-26 20:00 UTC  
**扫描者**: Sandbot 自动生态探索 (Cron)

---

## 📊 版本状态

| 项目 | 当前版本 | 最新稳定版 | 差距 |
|------|----------|------------|------|
| OpenClaw | 2026.3.8 | v2026.6.9 | ~3 个月，12 个稳定版本 |
| GitHub Beta | v2026.6.10-beta.2 | **v2026.6.11-beta.1** (2026-06-24) | beta 已更新 +1 次 |

---

## 🔥 新版本：v2026.6.11-beta.1 (2026-06-24)

### 亮点

**1. 更丰富的频道控制**
- Slack relay mode
- 原生 Mattermost /oc_queue
- 每个 DM 独立的模型覆盖 (per-DM model overrides)
- 让频道操作更容易自动化和调优

**2. 更丰富的 Operator 工作流**
- `openclaw agent --message-file`：文件驱动的消息注入
- RAFT CLI wake bridge：远程唤醒路径
- 实用的文件驱动和远程唤醒方案

**3. 更安全的插件分发**
- 额外官方插件已外部化
- 已安装客户端可使用捆绑插件图标元数据
- 插件分发更安全、更干净

**4. 更强的移动端操作**
- Android 设置详情面板改进
- 在移动端配置可见性和控制力更好

**5. 更可靠的 Agent**
- Agent 运行可靠性持续改进（发布说明截断，详见 GitHub）

---

## 🏪 ClawHub 动态

- 域名维持 **clawhub.ai**（clawhub.com 自动重定向）
- 热门技能 Top 5 按安装量排序：
  1. **self-improving-agent** (pskoett) — 3.8k 安装 / 464k 浏览
  2. **skill-vetter** (spclaudehome) — 1.2k / 260k — 安全优先的技能审核
  3. **self-improving + proactive** (ivangdavila) — 1.2k / 201k
  4. **github** (steipete) — 644 / 192k — gh CLI 集成
  5. **ontology** (oswalpalash) — 648 / 190k — 结构化知识图谱

- **值得关注的新/热门技能**：
  - **PollyReach** (pollyreach) — AI Agent 电话号码，529 安装 — 让 Agent 能打电话
  - **AdMapix** (fly0pants) — 广告创意原始数据层，288 安装
  - **Tavily 搜索** (jacky1n7) — Brave 替代搜索，265 安装
  - **Multi Search Engine** (gpyangyoujun) — 16 个搜索引擎（7 国内 + 9 全球）

---

## 📖 docs.openclaw.ai

- 首页结构稳定，无显著变更
- 快速入门仍为：`npm install -g openclaw@latest` → `openclaw onboard --install-daemon`
- 推荐 Node 24（兼容 Node 22 LTS `22.19+`）
- 支持频道：Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等

---

## 📝 与上次扫描 (2026-06-22) 对比

| 变化项 | 上次 | 本次 |
|--------|------|------|
| 最新 beta | v2026.6.10-beta.2 | **v2026.6.11-beta.1** |
| 最新稳定 | v2026.6.9 | v2026.6.9 (不变) |
| 版本间差距 | ~2 天 beta | ~2 天 beta |
| ClawHub Top 1 | 同上 | 同上 |
| 新亮点技能 | - | PollyReach (电话能力) |

---

## ⚠️ 行动建议

1. **升级考虑**：v2026.6.11-beta.1 仍是 beta，但 Slack relay、Mattermost、per-DM model overrides 等功能有实用价值。建议等稳定版发布后再升级。
2. **PollyReach** 有趣：让 AI Agent 有电话号码能打电话，值得进一步研究。
3. **版本差距**：当前运行 v2026.3.8，落后 12+ 个稳定版本，建议制定升级计划。
