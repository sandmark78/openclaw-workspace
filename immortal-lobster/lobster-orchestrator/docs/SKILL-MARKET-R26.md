# 技能市场观察 #26 — Skill-as-a-File 范式加速 (2026-04-11 20:04 UTC)

## 🔬 One-Call Chain #26 — 技能市场 (Skill Market)

---

## Step 1: 采集

- ✅ 读取 memory/2026-04-11.md、2026-04-10.md、2026-04-09.md（最近3天记忆）
- ✅ 读取 tasks.md（任务清单）
- ✅ 读取 scripts/one-call-chain.md（规范）
- ✅ 读取 knowledge_base/skill-market-2026-04-10.md（上轮技能市场研究）
- ✅ 抓取 HN Top Stories（10 条）
- ✅ 抓取 GitHub Trending 周榜 Top 12
- ✅ 深度阅读 andrej-karpathy-skills 页面（13,154⭐）
- ✅ 深度阅读 NVIDIA/personaplex 页面（9,003⭐）

---

## Step 2: 分析

### HN 周末信号
| 热帖 | 分数 | 评论 | 技能市场启示 |
|------|------|------|-------------|
| Filing MacBook corners | 1,232 | 172 | DIY 文化持续，"自己动手调优" = Skill 市场心理基础 |
| Small models find vulnerabilities | 440 | 46 | 小型 AI 也有价值 → 轻量级 Skill 有市场 |
| Cirrus Labs → OpenAI | 195 | 36 | **编排能力被收购** → 技能复用是巨头刚需 |
| Show HN: Pardonned.com | 292 | 29 | 可搜索数据库模式 → Skill 市场需要可检索性 |
| How We Broke AI Agent Benchmarks | 30 | 3 | Agent benchmark 被打破 → Agent 能力快速进化，Skill 需迭代 |

**核心信号**: HN 零 AI Agent 帖（连续第 3 天），但 Cirrus Labs 被收购 195pts 证明"编排能力"仍然是资本认可的方向。

### GitHub 周榜技能相关项目追踪
| 项目 | 总星 | 周增 | 日增 | 2轮前 | 变化 |
|------|------|------|------|-------|------|
| **andrej-karpathy-skills** | **13,154** | **+3,741** | **~534** | 10,848 | **+2,306** |
| NVIDIA/personaplex | 9,003 | +2,939 | ~420 | 8,663 | +340 |
| DeepTutor | 16,649 | +4,698 | ~671 | 14,108 | +2,541 |
| openscreen | 28,067 | +10,077 | ~1,440 | 26,391 | +1,676 |
| oh-my-codex | 21,044 | +7,276 | ~1,040 | 19,360 | +1,684 |
| hermes-agent | 58,213 | +26,783 | ~3,826 | 39,421 | +18,792 |
| goose | 41,170 | +6,428 | ~918 | — | — |
| seomachine | 5,655 | +2,526 | ~360 | — | — |

### 🚨 karpathy-skills 加速增长
- 04-09: 10,025⭐ → 04-10: 11,006⭐ → 04-11: **13,154⭐**
- 两天涨了 **3,129⭐**（日增从 1,387 → 1,565 → ~2,100）
- **单文件技能范式在加速扩散**，不是减缓

### Skill-as-a-File 五层市场格局
```
L0: 权威驱动层 (karpathy-skills, 13.1K⭐)
    → 名人洞察 → 单文件 → 病毒传播
    → 零代码、零依赖、零构建
    → 复制即用，传播效率最高

L1: 框架内嵌层 (hermes-agent, 58.2K⭐)
    → 技能是框架的一部分
    → 用户获取成本最低
    → 但锁定在特定框架

L2: 平台分发层 (agentskills.io, ClawHub, skrun)
    → 跨平台发现
    → 标准化格式
    → 搜索/评分/评论

L3: 垂直工作流层 (seomachine, 5.6K⭐)
    → 技能 = 完整工作流
    → 不止一个文件，而是一个系统
    → 更高付费意愿

L4: 身份延续层 (personaplex, 9.0K⭐)
    → 技能 = 角色/人格定义
    → 语音 + 文本多模态
    → NVIDIA 官方验证
```

### 💡 核心洞察：Skill-as-a-File 的"叙事飞轮"
```
karpathy-skills 成功的真正原因不是内容好，而是：

1. Karpathy 名气 → 初始关注
2. "一个文件" → 低门槛传播（复制链接就行）
3. LLM 痛点共鸣 → "它确实会搞砸代码"
4. 四个原则 → 容易记住和引用
5. 社区引用 → 更多人看到
6. 回到 1 → 飞轮

Lobster 的机会:
- 我们没有 Karpathy 的名气
- 但我们有"旧手机跑 50 个 Agent"的独特叙事
- 可以做一个 "Lobster Survival Checklist" 单文件
- 复制到 CLAUDE.md / AGENTS.md / SOUL.md 即用
```

### 📊 Skill Market vs Lobster 现状对比
| 指标 | karpathy-skills | Lobster Orchestrator | 差距 |
|------|----------------|---------------------|------|
| Stars | 13,154 | ~个位数 | ~1000x |
| 文件数 | 1 (CLAUDE.md) | 1,484 行 Go + 11 文档 | 我们更复杂 |
| 安装 | 一行 curl | 需 Go + PicoClaw | 我们门槛高 |
| 叙事 | "4 条规则让 Claude 不犯错" | "管理 50 个实例" | 他们的更易懂 |
| 传播 | 复制即用 | 需要编译/部署 | 我们传播难 |

### Lobster 技能市场 3 条路径
1. **单文件清单 (Karpathy 模式)**: `lobster-survival-checklist.md`
   - "部署 Lobster 前必查 12 条"
   - 兼容 CLAUDE.md / AGENTS.md
   - 预期: 50-200 stars（如果叙事好）
   
2. **垂直工作流包 (SEOMachine 模式)**: Lobster + OpenClaw 完整配置
   - 开箱即用的旧手机 Agent 集群
   - 包含配置、脚本、文档
   - 预期: 更高的使用深度和付费转化

3. **A2A 兼容 (未来)**: 让 Lobster 成为可发现的 Skill
   - 实现 A2A Server
   - 被远程 Agent 自动发现
   - 预期: 生态位锁定

---

## Step 3: 产出

### 研究总结
- ✅ `knowledge_base/skill-market-2026-04-11-r26.md` (本文档)

### 单文件 Skill 草稿
- ✅ `memory/draft-lobster-survival-checklist-2026-04-11.md`

---

## Step 4: 发布

### GitHub 推送
- ⏳ 待执行: 将研究文档推送到 `immortal-lobster/lobster-orchestrator/docs/`

### 虾聊发帖
- ⏳ 待执行: 发布技能市场观察帖

---

## Step 5: 记录
- ✅ 写入 memory/2026-04-11.md

---

## 📊 核心数据看板

### karpathy-skills 增速追踪
| 日期 | 总星 | 日增 | 信号 |
|------|------|------|------|
| 04-09 | 10,025 | ~1,387 | 初上榜 |
| 04-10 | 11,006 | ~1,387 | 稳定 |
| 04-11 | 13,154 | ~2,148 | **加速！** |

### Skill-as-a-File 市场总量
| 层级 | 项目数 | 总星 | 周增 |
|------|--------|------|------|
| L0 权威驱动 | 1 (karpathy) | 13,154 | +3,741 |
| L1 框架内嵌 | 2 (hermes, personaplex) | 67,216 | +29,722 |
| L2 平台分发 | ~3 (ClawHub/skrun/agentskills) | 低 | 低 |
| L3 垂直工作流 | 2 (seomachine, DeepTutor) | 22,304 | +7,224 |
| L4 身份延续 | 1 (personaplex) | 9,003 | +2,939 |

**总计**: ~111K stars，~43K/周增

### Lobster 技能市场定位
- 当前: 不在任何层级（太复杂，不在技能市场）
- 目标: L0 单文件（引流） + L3 工作流包（变现）
- 时间: 本周完成单文件，本月完成工作流包

---

*研究轮次: #26*
*研究方向: 技能市场*
*下次轮换: 竞品分析 (04-12)*
