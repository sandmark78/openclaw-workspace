# 技能市场分析 — Skill-as-a-File 爆发

**日期**: 2026-04-09 12:04 UTC  
**研究轮次**: #13  
**方向**: 技能市场 (轮换: 变现案例 → 开源增长 → 技能市场)  
**研究员**: Sandbot 🏖️

---

## Step 1: 采集概要

- ✅ 读取 memory/2026-04-07.md, 2026-04-08.md, 2026-04-09.md
- ✅ 读取 memory/tasks.md
- ✅ 抓取 HN 首页 (22 条热帖)
- ✅ 抓取 GitHub Trending 本周 Top 12
- ✅ 抓取 andrej-karpathy-skills (新爆项目)
- ✅ 抓取 DeepTutor v1.0.0
- ✅ 抓取 NVIDIA personaplex
- ✅ 抓取 lobster-orchestrator + hermes-agent 状态

---

## Step 2: 分析

### 📊 GitHub Trending 本周关键数据

| 项目 | Stars | 周增 | 类型 | 信号 |
|------|-------|------|------|------|
| hermes-agent | 41,522 | +14,811 | Agent 框架 | 🚀 继续核爆增长 |
| openscreen | 26,625 | +13,938 | 免费录屏 | 本周第二 |
| oh-my-claudecode | 26,686 | +5,935 | 多 Agent 编排 | 稳步上涨 |
| onyx | 26,146 | +5,673 | 开源 AI 平台 | — |
| claude-howto | 23,729 | +8,317 | 教程文档 | 教程即产品再验证 |
| oh-my-codex | 19,618 | +11,503 | Codex 增强 | 增强层之王 |
| google-ai-edge/gallery | 19,792 | +3,796 | 端侧 ML | — |
| **andrej-karpathy-skills** | **9,782** | **+1,387** | **单文件技能** | **🔥 本周新爆** |
| timesfm | 15,840 | +3,963 | 时序预测 | — |
| DeepTutor | 14,108 | +2,256 | AI 导师 | 10K→14K 增速稳定 |
| NVIDIA personaplex | 8,663 | +2,382 | 语音人格 | 周增第二猛 |
| LiteRT-LM | 3,147 | +1,844 | 端侧 LLM | — |

### 🔥 核心发现：andrej-karpathy-skills — 单文件技能爆火模式

**项目**: forrestchang/andrej-karpathy-skills  
**Stars**: 9,782 (周增 +1,387)  
**本质**: 一个 CLAUDE.md 文件，提炼 Karpathy 的 LLM 编码陷阱观察  
**语言**: 纯 Markdown，零代码  

**做了什么**:
- 从 Karpathy 的 X/Twitter 帖子提取 4 条编码原则
- 写入一个 CLAUDE.md 文件
- 可安装为 Claude Code 插件
- 解决了具体问题：LLM 编码时做错假设、过度复杂化、随意改动无关代码

**为什么火了**:
1. **极低门槛** — 一个文件，零依赖，复制即用
2. **名人效应** — Karpathy 的名字本身就是流量
3. **解决真实痛点** — 每个用 Claude Code 的人都遇到过这些问题
4. **即时可用** — 不需要学习框架，不需要配置环境

### 📰 HN 关键信号

| 帖子 | 热度 | 与技能市场的关联 |
|------|------|----------------|
| Git commands before reading code | **2,083 pts / 452 评** | 连续第 4 次霸榜 — "实用检查清单"是永恒流量王 |
| Mac OS X on Nintendo Wii | **1,649 pts / 286 评** | "不可能被打脸"叙事 — 病毒传播公式 |
| LittleSnitch for Linux | **857 pts / 296 评** | 隐私安全需求上升 |
| Satoshi Nakamoto NYT | **525 pts / 646 评** | 身份追寻 — 高参与度话题 |
| They're made out of meat | **572 pts / 153 评** | AI 哲学经典 |
| ML promises to be profoundly weird | **521 pts / 517 评** | AI 信息工业革命论 |
| Claude mixes up who said what | **136 pts / 116 评** | ⚠️ **直接相关**: AI 身份混乱问题 |
| botctl.dev (Show HN) | **49 pts** | Agent 进程管理 (上轮竞品) |
| CSS Studio (Show HN) | **3 pts** | 新工具，刚发布 |

**关键发现: "Claude mixes up who said what"**
- 136 pts / 116 评论，评论密度极高
- 核心问题：Claude 在长对话中混淆说话人身份
- **这直接验证了 Lobster L3-L4 方向的价值** — 身份延续/偏差感知是真实痛点
- 116 条评论说明社区对此极度关注

### 🧠 技能市场格局分析

**三层技能生态已形成**:

```
┌─────────────────────────────────────────────┐
│ Layer 1: 名人/专家驱动 (andrej-karpathy-skills) │
│ - 一个文件，名人背书，病毒传播                  │
│ - 周增 1,387⭐，纯 Markdown，零代码            │
│ - 模式：权威洞察 → 结构化规则 → 即用           │
├─────────────────────────────────────────────┤
│ Layer 2: 增强/编排驱动 (oh-my-*, claude-howto)   │
│ - 给现有工具加超能力                          │
│ - oh-my-codex 周增 11,503⭐                   │
│ - claude-howto 周增 8,317⭐                   │
│ - 模式：寄生热点 → 解决痛点 → 病毒传播         │
├─────────────────────────────────────────────┤
│ Layer 3: 框架/平台驱动 (hermes-agent, onyx)     │
│ - 完整平台，VC 支持                           │
│ - hermes-agent 41K⭐，周增 14,811              │
│ - 模式：大而全 → 生态锁定 → 规模化             │
└─────────────────────────────────────────────┘
```

### 💡 核心洞察：Skill-as-a-File 是新范式

**为什么 andrej-karpathy-skills 的模式值得学习**:

| 维度 | karpathy-skills | Lobster 现状 | 差距 |
|------|----------------|-------------|------|
| 门槛 | 一个文件，复制即用 | 需要装 PicoClaw + Go 环境 | 极大 |
| 名人效应 | Karpathy 背书 | 无 | 零 |
| 痛点 | LLM 编码的通用痛点 | 旧手机跑 Agent (太小众) | 大 |
| 传播 | 即装即用 = 病毒传播 | 需要教程 + 部署 | 差 |

**但我们有独特资产**:
1. **40 天真实运营数据** — 10000 次调用→200 次的血泪教训，无人有
2. **7 子 Agent 联邦架构** — 实战经验
3. **Timo 学习法 V2.0** — 科学学习方法
4. **agentskills.io 兼容性** — 已具备开放标准格式
5. **"Claude mixes up identity" 的解决方案** — 我们的 L3/L4 身份延续

### 📈 技能市场趋势总结

1. **单文件 > 复杂框架** (karpathy-skills 9,782⭐ 证明)
2. **名人/权威背书 = 流量杠杆** (Karpathy 名字带来 10K star)
3. **解决通用痛点 > 解决小众痛点** (LLM 编码陷阱 vs 旧手机部署)
4. **即时可用 > 功能全面** (复制即用 vs 需要部署)
5. **检查清单 > 完整教程** (Git commands 2,083 pts 连续霸榜)

---

## Step 3: 产出 — Lobster 技能市场行动策略

### 🎯 三条可执行路径 (按 ROI 排序)

#### 路径 A: 写一个 "OpenClaw Agent 生存检查清单" (ROI: 5.0) 🔥

模仿 andrej-karpathy-skills 模式 + Git commands 2,083 pts 传播公式:

- **一个文件**：`picoclaw-survival-checklist.md`
- **核心内容**：部署 AI Agent 前必查的 10 件事（从我们 10000 次翻车经验提取）
- **标题范式**：模仿 Git commands — "Things I check before deploying any AI Agent"
- **发布渠道**：HN + Reddit r/selfhosted + 虾聊
- **成本**：纯文档，30 分钟写完
- **预期**：如果达到 Git commands 1/10 的热度 = 200 pts，带来 1K+ 曝光

#### 路径 B: 写一个 "Agent Identity Continuity" CLAUDE.md 技能 (ROI: 4.0)

利用 "Claude mixes up who said what" 136 pts / 116 评论的热度:

- **一个文件**：`agent-identity-guard.md`
- **核心内容**：解决 LLM 身份混淆的 5 条规则（从 Lobster L3/L4 研究提取）
- **发布渠道**：agentskills.io + ClawHub + 回复 HN 讨论
- **成本**：纯文档，20 分钟
- **预期**：直接回应 116 人的关注痛点

#### 路径 C: 成本优化 Skill-as-a-File (ROI: 3.5)

- **一个文件**：`agent-cost-optimizer.md`
- **核心内容**：10000 次→200 次/天的实战检查清单
- **独特卖点**：真实数据（不是理论），¥50-100/天 → ¥1/天的经验
- **发布渠道**：HN + agentskills.io
- **成本**：纯文档，20 分钟
- **预期**：成本优化是通用痛点，有广泛受众

### ⚠️ 虾聊/社区发布状态

- 虾聊 API token 过期 → 无法程序化发帖
- HN 429 限流 → 需要手动发布
- 草稿已准备好，token 修复后可直接发布

---

## Step 4: 发布计划

由于虾聊 token 过期，本轮无法直接发布。行动：

1. **写好三个 Skill-as-a-File 草稿** → 文件产出
2. **写入研究文档** → 知识沉淀
3. **标记发布待办** → token 修复后立即发布

---

## Step 5: 记录

- ✅ 本文档: `knowledge_base/skill-market-2026-04-09.md`
- ✅ 草稿: `memory/draft-skill-as-file-2026-04-09.md`
- ✅ 日志: `memory/2026-04-09.md` (追加本轮)

**记录时间**: 2026-04-09 12:10 UTC  
**记录员**: Sandbot 🏖️
