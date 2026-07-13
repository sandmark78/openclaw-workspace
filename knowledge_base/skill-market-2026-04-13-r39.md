# 技能市场研究 #39 — hermes 核爆式增长 70K⭐ + Skill Ecosystem 四分天下

**研究轮次**: #39  
**研究方向**: 技能市场 (Skills Market) — 轮换第3位  
**时间**: 2026-04-13 06:05 UTC  
**数据源**: HN Front Page + GitHub Trending 周榜 + 源码分析

---

## Step 1: 采集

### HN 周一信号 (06:05 UTC)
| 热帖 | 分数 | 评论 | 信号 |
|------|------|------|------|
| Docker pull fails in Spain (Cloudflare 足球封锁) | **754** | 289c | 💥 基础设施信任崩塌 |
| Seven countries 100% renewable | 548 | 287c | 非技术但高共鸣 |
| Bring Back Idiomatic Design | **506** | 272c | 🔥 连续2天霸榜，本周最高 |
| Google removes DDLC from Play | 389 | 186c | 平台权力滥用 |
| DIY Soft Drinks | 339 | 93c | 动手精神 |
| boringBar (macOS dock 替代) | 309 | 178c | 📈 持续攀升 |
| Most people can't juggle one ball | 299 | 92c | LessWrong 哲学 |
| I gave every NY train an instrument | 249 | 49c | 创意项目 |
| Apple's accidental moat: AI Loser may win | 100 | 87c | 🆕 边缘叙事 |
| Ask HN: What Are You Working On? | 181 | 534c | 社区互动 |
| State of Homelab 2026 | 59 | 46c | 🆕 本地化趋势 |
| **零 AI Agent 帖进入 Top 20** | — | — | ⚠️ 连续第11天！ |

### GitHub 周榜核爆数据
| 项目 | 总星 | 周增 | 关键变化 |
|------|------|------|----------|
| hermes-agent | **70,397** | **+38,426** | 💥💥💥 核爆式增长！逼近70K |
| markitdown | **105,519** | +10,592 | 🚀 突破105K |
| multica | **9,848** | +6,846 | 🔥🔥 逼近10K，增速加速 |
| gallery (Google) | 20,747 | +4,148 | 📈 端侧 ML |
| DeepTutor | 17,377 | +5,873 | 🚀 教育+Agent |
| Archon | 17,237 | +2,962 | 📈 确定性编码 |
| personaplex (NVIDIA) | 9,123 | +2,331 | 📈 身份 AI |
| seomachine | 5,840 | +2,815 | 📈 垂直工作流 |
| LiteRT-LM (Google) | 3,582 | +2,164 | 📈 端侧 ML |
| karpathy-skills | ❌ 缺席第5轮 | — | 💀 新奇效应彻底结束 |

### hermes-agent 源码关键发现 (README 分析)
```
核心定位: "The agent that grows with you"
学习闭环: 
  - Autonomous skill creation after complex tasks
  - Skills self-improve during use
  - FTS5 session search with cross-session recall
  - Honcho dialectic user modeling

技能标准:
  - "Compatible with the agentskills.io open standard"  ← 💥 标准化！
  - /skills 命令浏览技能
  - 技能在使用中自我改进

多平台:
  - Telegram, Discord, Slack, WhatsApp, Signal, CLI
  - 单一 gateway 进程驱动所有平台

多模型:
  - Nous Portal, OpenRouter (200+ models), z.ai/GLM
  - Kimi/Moonshot, MiniMax, OpenAI, 自定义端点
  - "hermes model" 切换，无代码变更

迁移:
  - "hermes claw migrate" — 直接从 OpenClaw 迁移！← 💥

部署:
  - "Run it on a $5 VPS, a GPU cluster, or serverless"
  - 6 种后端: local, Docker, SSH, Daytona, Singularity, Modal
  - Android/Termux 支持
```

### multica 源码关键发现
```
核心定位: "Turn coding agents into real teammates"
技能系统:
  - "every solution becomes a reusable skill for the whole team"
  - "skills compound your team's capabilities over time"
  - 技能是团队资产，不是个人资产

运行时:
  - 自动检测 CLIs: claude, codex, openclaw, opencode
  - Local daemon + Cloud runtime
  - WebSocket 实时进度流

管理:
  - 任务分配 → 执行 → 进度 → 完成/失败
  - Agent 有 profile、出现在看板上、主动报告阻塞
```

---

## Step 2: 深度分析 — 技能市场四分天下

### 核心发现 #1: hermes 70K⭐ 核爆式增长 — 周增 38,426！

这是 GitHub 历史上 AI Agent 类项目的单周最高增速之一。

**为什么这轮爆了？**
1. agentskills.io 开放标准 → 技能可移植性叙事引爆
2. "hermes claw migrate" → 直接抢 OpenClaw 用户
3. "Run on $5 VPS" → 低成本部署，与 Lobster 竞争
4. Telegram/Discord 多平台 → 与 Lobster 功能重叠
5. 自主技能创建 → 学习闭环概念被 Nous 抢先

**对 Lobster 的威胁等级: 🔴 高**
- hermes = 单实例 + 云端 + 开放标准
- Lobster = 多实例 + 边缘 + 封闭控制
- 差异化：Lobster 做"50 个 hermes 在旧手机上"

### 核心发现 #2: 技能市场四分天下格局确立

```
┌─────────────────────────────────────────────┐
│            2026 Q2 技能市场格局              │
├──────────┬──────────┬──────────┬────────────┤
│ 标准派   │ 团队派   │ 垂直派   │ 极简派     │
│ hermes   │ multica  │ seomach. │ karpathy   │
│ 70.4K⭐  │ 9.8K⭐   │ 5.8K⭐   │ 已退潮     │
├──────────┼──────────┼──────────┼────────────┤
│ agentsk  │ 团队资产 │ 工作流   │ CLAUDE.md  │
│ .io标准  │ 技能复用 │ 打包     │ 单文件     │
├──────────┼──────────┼──────────┼────────────┤
│ 技能=   │ 技能=    │ 技能=    │ 技能=      │
│ 可移植   │ 可积累   │ 可执行   │ 行为配置   │
│ 能力包   │ 团队资产 │ 完整方案 │ 编码风格   │
├──────────┼──────────┼──────────┼────────────┤
│ Lobster │ Lobster  │ Lobster  │ Lobster    │
│ 对标:   │ 对标:    │ 对标:    │ 对标:      │
│ 边缘版  │ 边缘版   │ 轻量版   │ 不追       │
│ agentsk │ multica  │ seomach  │ (已验证)   │
│ .io     │          │          │            │
└──────────┴──────────┴──────────┴────────────┘
```

### 核心发现 #3: 技能定义的三大战场

**战场 1: 技能格式战争**
- hermes: agentskills.io (开放 YAML/JSON 标准)
- multica: 内部格式 + 团队共享
- OpenClaw: SKILL.md (Markdown 指令格式)
- Lobster 应选择：支持 agentskills.io 格式，做边缘版兼容层

**战场 2: 技能发现战争**
- hermes: /skills 命令浏览
- multica: 技能市场 (Cloud SaaS)
- ClawHub: 技能发布 (已有 3 个发布)
- Lobster 机会：做"边缘技能"分类 — 低资源、离线可用

**战场 3: 技能变现战争**
- hermes: 开源免费，Nous Portal 收费
- multica: 开源核心 + Cloud SaaS
- seomachine: 开源，SEO 咨询引流
- Lobster 路线：免费技能包 → 付费部署指南/咨询

### 核心发现 #4: "hermes claw migrate" 是直接的竞争信号

hermes 在 README 中公开提供从 OpenClaw 迁移的命令。这意味着:
1. OpenClaw 用户是 hermes 的目标用户群
2. Lobster (基于 OpenClaw) 面临间接竞争
3. 应对策略：Lobster 应该做 "hermes → Lobster" 的迁移路径
   - "Run 50 hermes instances on a $0 old phone"
   - 不是替代 hermes，而是放大 hermes

### 核心发现 #5: 周一清晨的数据揭示长期趋势

| 指标 | 本周 vs 上周 | 趋势 |
|------|-------------|------|
| hermes 周增 | +38,426 vs +32,572 | 📈 加速18% |
| multica 周增 | +6,846 vs +5,362 | 📈 加速28% |
| markitdown 周增 | +10,592 vs +8,202 | 📈 加速29% |
| AI Agent HN 帖 | 0/20 | ⚠️ 连续11天 |
| 设计/哲学帖 | 506pts | 🔥 本周最高 |

**解读**: Agent 框架层进入成熟期，增长靠生态而非新奇。设计叙事 > 技术叙事持续验证。

---

## Step 3: Lobster 技能市场策略 V6

### 定位：边缘技能生态 (Edge Skills Ecosystem)

```
hermes 做云端单实例的技能标准 → Lobster 做边缘多实例的技能编排
multica 做团队技能复用 → Lobster 做个人技能规模化

Lobster 独特价值:
1. 边缘验证 — 技能在 $0 硬件上能跑才算数
2. 规模编排 — 50 个实例同时执行同一技能
3. 资源感知 — 技能自动适配 CPU/RAM/存储限制
4. 离线可用 — 不依赖云端 API 的技能优先

对标 agentskills.io:
  "Lobster Edge Skills" — 兼容 agentskills.io 格式
  但增加资源约束元数据:
  - min_ram_mb: 256
  - min_cpu_cores: 1
  - requires_internet: false
  - max_instances: 50
```

### 短期行动 (本周)
1. **写 "agentskills.io 边缘兼容层" 提案** — 蹭 hermes 热度
2. **创建 "Edge Skills Checklist"** — 什么样的技能适合边缘部署
3. **README 加入 "Run hermes on 50 old phones with Lobster"** 叙事
4. **ClawHub 技能增加资源约束元数据** — 差异化

### 中期行动 (本月)
1. **发布 Lobster Skill Registry v1** — 边缘技能市场
2. **实现 agentskills.io 格式兼容** — 降低技能迁移成本
3. **写 "Edge vs Cloud Skills" 对比文章** — 建立品类认知

### 变现路径
1. **免费**: 边缘技能包 + 部署脚本 (引流)
2. **付费 ($9-29)**: 技能优化咨询 + 定制部署
3. **高阶 ($99+)**: 企业级边缘 Agent 集群部署

---

## Step 4: 关键数据追踪

### hermes-agent 增速追踪 (9天)
| 日期 | 总星 | 周增 | 日增速率 |
|------|------|------|----------|
| 04-04 | ~32K | — | — |
| 04-07 | ~45K | +13K | ~4.3K/天 |
| 04-10 | ~52K | +19.8K | ~2.3K/天 (减速) |
| 04-12 | ~64K | +32.6K | — |
| 04-13 | **70.4K** | **+38.4K** | **~5.5K/天 (核爆!)** |

**分析**: 经历了减速后突然加速，可能是某次重大更新/宣传触发了病毒传播。70K 是心理关口，突破后可能继续加速到 100K。

### multica 增速追踪
| 日期 | 总星 | 周增 | 备注 |
|------|------|------|------|
| 04-07 | ~4.3K | +1.8K | 早期 |
| 04-10 | ~5.9K | +3.2K | 加速78% |
| 04-12 | ~8.8K | +5.4K | 加速69% |
| 04-13 | **9.8K** | **+6.8K** | **逼近10K！** |

**分析**: 稳定加速中，10K 是重要里程碑，突破后可能进入新一轮增长。

---

*研究轮次: #39*
*下次轮换: 竞品分析 (04-14)*
*文件产出: knowledge_base/skill-market-2026-04-13-r39.md*
