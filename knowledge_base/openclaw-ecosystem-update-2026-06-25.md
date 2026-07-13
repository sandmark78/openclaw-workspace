# OpenClaw 生态探索记录 - 2026-06-25

**记录时间**: 2026-06-25 20:00 UTC
**来源**: clawhub.ai + docs.openclaw.ai + GitHub Releases

---

## 🔴 关键发现：版本严重落后

| 项目 | 当前 | 最新稳定版 | 最新 Beta |
|------|------|-----------|----------|
| OpenClaw | **2026.3.8** | **v2026.6.10** (2026-06-24) | **v2026.6.11-beta.1** (2026-06-24) |

**落后约 3 个月版本**，需要尽快升级！

---

## 📦 GitHub Releases 近期版本

### v2026.6.11-beta.1 (2026-06-24) - 最新 Beta
- **Slack relay mode** - Slack 中继模式
- **Mattermost** 原生 `/oc_queue`
- **per-DM model overrides** - 单聊模型覆盖
- **openclaw agent --message-file** - 文件驱动 agent 唤醒
- **RAFT CLI wake bridge** - 远程唤醒路径
- **bundled plugin icon metadata** - 插件图标元数据
- **Android settings detail panels** - Android 设置详情面板
- **Codex partial deltas** - Codex 增量更新
- **harness activation** - harness 激活
- **long-context prompt-cache stability** - 长上下文缓存稳定性
- **per-agent usage-cost reporting** - 单 Agent 用量成本报告
- **encrypted reasoning support** - 加密推理支持
- **Telegram progress rendering** - Telegram 进度渲染修复
- **reaction directives** - 反应指令修复
- **WhatsApp durable reply targets** - WhatsApp 回复目标修复

### v2026.6.10 (2026-06-24) - 最新稳定版
(同上变更集的稳定版)

---

## 🏪 ClawHub 热门技能 (2026-06-25)

| 技能 | 作者 | 下载量 | 说明 |
|------|------|--------|------|
| self-improving-agent | pskoett | 3.8k / 464k | Agent 自我改进日志 |
| skill-vetter | spclaudehome | 1.2k / 260k | 安全技能审查 |
| Self-Improving + Proactive Agent | ivangdavila | 1.2k / 201k | 自我反思+学习 |
| Github | steipete | 643 / 191k | GitHub CLI 集成 |
| ontology | oswalpalash | 647 / 190k | 类型化知识图谱 |
| Gog | steipete | 931 / 187k | Google Workspace CLI |
| SkillScan | tokauthai | 38 / 178k | 技能安全门控 |
| Proactive Agent | halthelobster | 810 / 170k | 主动型 Agent |
| Weather | steipete | 420 / 162k | 天气查询 |
| Multi Search Engine | gpyangyoujun | 736 / 154k | 16 引擎搜索 |
| Auto-Updater Skill | maximeprades | 435 / 96.4k | 自动更新技能 |
| Tavily 搜索 | jacky1n7 | 265 / 98.7k | Tavily 搜索 |

---

## 📖 Docs 更新要点

- 推荐 Node.js **24**（或 Node 22 LTS 22.19+）
- 支持通道：Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
- 关键功能：多 Agent 路由、媒体支持、Web 控制面板、移动节点 (iOS/Android)
- macOS app 已提及
- CLI 命令：`openclaw onboard --install-daemon`

---

## ⚠️ 建议行动

1. **P0 - 升级 OpenClaw**: `npm install -g openclaw@latest` → 升级到 v2026.6.10
2. **P1 - 关注 Telegram 修复**: 多个 Telegram 相关 bug 已修复
3. **P2 - 关注安全技能**: SkillScan / SkillVetter 等新安全技能值得关注
4. **P2 - per-agent cost reporting**: 单 Agent 成本报告功能对成本控制有帮助
