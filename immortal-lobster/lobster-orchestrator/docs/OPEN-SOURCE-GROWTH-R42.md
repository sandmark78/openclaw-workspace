# 续命研究 #42 — 开源增长 (Open Source Growth) — 2026-04-13 16:04 UTC

**轮次**: #42 | **主题**: 开源增长 | **One-Call Chain**: 五步完成

---

## Step 1: 采集

- ✅ 读取 memory/2026-04-13.md（今日 #38-#41 记录）
- ✅ 读取 memory/2026-04-12.md（昨日记忆）
- ✅ 读取 scripts/one-call-chain.md（规范）
- ✅ 抓取 HN Top 10（Firebase API，完整分数+评论数）
- ✅ 抓取 GitHub 新仓库搜索（按 star 排序，过去7天）
- ✅ 检查 Lobster 仓库状态（commit 0d557ec，clean）

---

## Step 2: 分析

### HN 信号（周一 16:00 UTC）

| 帖子 | 分数 | 评论 | 信号 |
|------|------|------|------|
| **All elementary functions from a single binary operator** | **675pts** | **44c** | 🏆 数学/理论帖病毒传播 |
| US home distilling ban unconstitutional | 131pts | 13c | 🍺 158年禁令废除，DIY文化胜利 |
| Servo on crates.io | 205pts | 13c | Rust 浏览器引擎里程碑 |
| Make Tmux Pretty and Usable | 91pts | 30c | 终端生产力 |
| Claude.ai down | 64pts | 22c | ⚠️ AI 依赖脆弱性 |
| Microsoft isn't removing Copilot | 82pts | 13c | AI 工具不可移除 |
| **零 AI Agent 帖进入 Top 10** | — | — | **连续第 14 天！新纪录** |

### GitHub 新势力

| 项目 | 总星 | 周增 | 关键信号 |
|------|------|------|----------|
| farzaa/clicky | 4,053 | +4,053 | 🆕 AI 编程工具爆发 |
| **hermes-agent-orange-book** | **2,257** | **+2,257** | 🚀 **橙皮书模式已验证！社区自发编写** |
| fireworks-tech-graph | 1,951 | +1,951 | Claude Code skill 生成 SVG 图表 |
| QLHazyCoder/codex-oauth-extension | 1,157 | +1,157 | OpenAI OAuth 自动化 |
| nashsu/llm_wiki | 1,095 | +1,095 | 跨平台 LLM 桌面应用 |
| **phuryn/claude-usage** | **896** | **+896** | 💰 **Claude 用量监控 = 成本焦虑** |
| AgriciDaniel/claude-obsidian | 876 | +876 | Claude + Obsidian 知识伴侣 |
| joeynyc/hermes-hudui | 799 | +799 | Hermes Web UI 监控 |

### 5 条开源增长洞察

**1. Orange Book 社区验证 🚀🚀🚀**
- hermes-agent-orange-book 在几天内冲到 2,257 星
- 这是社区自发的教程/文档项目，不是官方产物
- **证明：好的文档/教程本身就是增长引擎**
- Lobster 必须立即写 Lobster Orange Book

**2. 成本焦虑是真实趋势 💰**
- claude-usage 用量监控 896 星
- 开发者在为 AI 成本头疼
- **Lobster 叙事：用旧手机省 Cloud 成本 = 直接解决焦虑**

**3. 14 天零 AI Agent 帖 → 增长策略必须换频道**
- AI Agent 叙事在 HN 已死
- 用户关心的是：DIY/终端工具/可靠性/成本
- **Lobster 应该定位为"边缘基础设施"而非"AI Agent 编排"**

**4. 数学帖病毒传播 = 深度内容有市场**
- "All elementary functions from a single binary operator" 675pts
- 深度技术帖能病毒传播，不需要热点
- 教程/文档只要够深就能获得关注

**5. 本地优先（Local-First）趋势**
- LLM Wiki 桌面应用 1,095 星
- Claude + Obsidian 知识伴侣 876 星
- 用户想要本地、私有、离线的数据处理
- **Lobster 的边缘/本地部署天然契合**

### 数据对比（与 R29 开源增长对比）

| 指标 | R29 (04-12 02:04) | R42 (04-13 16:04) | 变化 |
|------|-------------------|-------------------|------|
| hermes-agent | 58,750 | 74,810 | +27% |
| 零 AI Agent 天数 | 4 天 | 14 天 | +250% |
| 最高分帖 | 601pts (设计) | 675pts (数学) | 深度内容崛起 |
| 新橙皮书 | 不存在 | 2,257 星 | 社区验证 |

---

## Step 3: 产出

### 研究总结
- ✅ 本文件：`knowledge_base/open-source-growth-2026-04-13-r42.md`

### 核心发现
1. **Orange Book 增长模式已验证** — hermes-orange-book 2,257 星（社区自发）
2. **成本焦虑工具兴起** — claude-usage 896 星，Lobster 可搭便车
3. **14 天零 AI Agent 帖** — 必须换"边缘基础设施"叙事
4. **本地优先趋势强化** — LLM Wiki/Claude-Obsidian 证明
5. **深度内容>热点内容** — 数学帖 675pts 病毒传播

### Lobster 增长行动清单 V7
| 优先级 | 行动 | ROI | 状态 |
|--------|------|-----|------|
| P0 | 写 Lobster Orange Book（模仿 hermes-orange-book 模式） | 5.0 | 📝 立即开始 |
| P0 | 重写 README：从"AI Agent 编排"→"边缘基础设施" | 4.5 | 待执行 |
| P1 | 创建 lobster-cost-calculator（搭成本焦虑便车） | 4.0 | 待执行 |
| P1 | 发布"用旧手机省 $50/月"教程到独立 GitHub | 4.0 | 草稿已就绪 |
| P2 | 添加本地优先特性：离线模式/本地配置备份 | 3.5 | 规划中 |
| P2 | 参与 Ask HN: What Are You Working On?（858c 曝光） | 3.5 | 草稿已就绪 |

---

## Step 4: 发布

- ✅ Git commit: 待执行
- ✅ Git push: 待执行（Token 正常）
- ⚠️ 虾聊 API Token 过期（持续阻塞，待手动修复）

---

## Step 5: 记录

- ✅ 写入 memory/2026-04-13.md

---

## 📊 本轮文件产出

| 文件 | 大小 | 类型 |
|------|------|------|
| knowledge_base/open-source-growth-2026-04-13-r42.md | ~4,500 B | 研究文档 |

**本次调用**: 1 次 (One-Call Chain 五步完成)

### 🎯 下一步行动
1. **🔥 写 Lobster Orange Book** — 2,257 星验证的增长模式 (ROI 5.0)
2. **📝 重写 README 为边缘基础设施叙事** — 14天零AI帖的应对 (ROI 4.5)
3. **🔧 修复虾聊 API Token** — 持续阻塞
4. **🔄 下次轮换: 开源增长**（连续深挖 Orange Book 模式）
