# 竞品分析 R36 — Mythos 破 1200pts + 周日效应

**研究轮次**: #36
**研究方向**: 竞品分析 (Competitor Analysis)
**时间**: 2026-04-12 16:04 UTC
**数据来源**: HN Front Page (Algolia) + GitHub Trending 周榜

---

## Step 1: 采集摘要

### HN 周一/周日信号 (2026-04-12 16:04 UTC)

| 排名 | 标题 | 分数 | 评论 | Lobster 关联 |
|------|------|------|------|-------------|
| 🔥 #1 | Small models also found Mythos vulns | **1179pts** | **317** | 💥 仍在涨！1107→1179 |
| #2 | $10K MRR on $20/month tech stack | ~300+pts | ~50+ | 独立开发者路径 |
| #3 | JVM Options Explorer | 109pts | 53 | 工具类产品 |
| #4 | Seven countries generate 100% electricity | 161pts | 63 | 能源话题 |
| #5 | 周日热门帖 | 192pts | 67 | 周日效应 |

**关键信号**:
- Mythos 小模型安全帖 **1179pts**，连续第 8 天霸榜！从 ~906→1179 持续攀升
- 评论数 317，说明讨论深度持续加深
- URL 已更新为 aisle.com 的深度分析文 — 从论文变成了产业评论
- 周日/周一交替，非技术帖开始回流

### GitHub 周榜 vs R35 (9小时前)

| 项目 | 当前总星 | 周增 | 变化 vs R35 | 趋势 |
|------|----------|------|-------------|------|
| hermes-agent | **64,698** | +32,572 | +984/9h | 📈 增速放缓 |
| markitdown | **104,015** | +8,202 | +314/9h | 🚀 加速57% |
| openscreen | 28,446→**缺失** | — | ⚠️ 跌出首页 | 热度退潮 |
| goose | 41,263→**缺失** | — | ⚠️ 跌出首页 | 热度退潮 |
| multica | **8,989** | +5,362 | +165/9h | 🚀 加速53% |
| DeepTutor | **17,149** | +5,560 | +43/9h | 🚀 加速18% |
| karpathy-skills | ❌ **跌出首页** | — | 连续第2轮 | ⚠️ 新奇效应结束 |
| gallery (Google) | **20,615** | +4,369 | +35/9h | 📈 端侧 ML |
| Archon | **16,836** | +2,410 | +58/9h | 📈 确定性编码 |
| LiteRT-LM (Google) | **3,511** | +2,196 | +57/9h | 🆕 端侧 ML |
| personaplex (NVIDIA) | **9,058** | +2,905 | +34/9h | 📈 身份层 |
| seomachine | **5,756** | +2,698 | +46/9h | 📈 稳定7% |

### 变化检测

**重要变化**:
1. **openscreen + goose 跌出 Trending 首页** — 免费替代/增强层热度下降
2. **karpathy-skills 连续第2轮缺席** — 单文件配置叙事基本结束
3. **multica 逼近 9K⭐** — 管理型 Agent 平台持续加速，+165/9h
4. **hermes 64.7K⭐** — 仍在涨但增速从 8.2K/天 → ~5.5K/天

---

## Step 2: 深度分析

### 信号 1: Mythos 安全帖 1179pts — 史上最长霸榜之一

这是 HN 上最持久的 AI 安全话题之一。从 ~906pts 起步，8 天后 1179pts，317 条评论。

**为什么持续上涨**:
- 触及 AI 安全核心恐惧: 小模型也能发现大模型发现不了的漏洞
- 从学术论文 (Anthropic Mythos) → 产业评论 (aisle.com) → HN 持续讨论
- 每轮新读者都在重新点燃讨论

**Lobster 机会**:
- 边缘部署 = 最确定的安全审计平台 (旧手机 = 无法被奖励黑客攻击)
- "用旧手机跑安全审计 Agent" 是 Lobster 最强叙事

### 信号 2: openscreen + goose 跌出首页 — 周期轮转

openscreen (免费替代, 28.4K⭐) 和 goose (增强层, 41.3K⭐) 同时跌出 Trending 首页。

**解读**:
- GitHub Trending 是注意力经济，不是价值评估
- 免费替代叙事已经充分传播 (openscreen 已达 28K⭐)
- 增强层叙事 (oh-my-codex, goose) 进入成熟期
- **注意力转向**: 管理型 (multica) + 确定性 (Archon) + 端侧 (Google)

**Lobster 启示**:
-  Lobster 不在 Trending 首页 = 正常，还没到爆发期
- 应该关注的是 multica 和 Archon 的方向 (管理/确定性)
- 端侧 ML (Google gallery/LiteRT-LM) = 天然盟友

### 信号 3: multica 8,989⭐ — 最接近 Lobster 的直接竞品

multica 是 "open-source managed agents platform"，与 Lobster 的核心定位 (Agent 编排管理) 直接竞争。

**multica vs Lobster 对比**:
| 维度 | multica | Lobster |
|------|---------|---------|
| 定位 | 云端管理平台 | 边缘编排器 |
| 语言 | TypeScript | Go |
| 架构 | 云端 SaaS | 本地/旧手机 |
| 周增速 | +5,362 (53%加速) | 0 (未公开发布) |
| 生态 | 支持 OpenClaw 等运行时 | PicoClaw |
| 商业模式 | 可能 Cloud SaaS | 开源 + 配置市场 |

**结论**: multica 走云端 SaaS 路线，Lobster 走边缘部署路线。两者是**差异化竞争**，不是零和博弈。

### 信号 4: 竞品增速追踪表 (9 天数据)

| 项目 | Day 1 | Day 5 | Day 9 (当前) | 9天变化 | 趋势 |
|------|-------|-------|-------------|---------|------|
| hermes | ~46.7K | ~58.5K | 64.7K | +18K | 📈 增速放缓 |
| markitdown | ~96K | ~102K | 104K | +8K | 🚀 加速 |
| multica | ~3.6K | ~7.8K | 9.0K | +5.4K | 🚀🚀 加速53% |
| DeepTutor | ~11.6K | ~16.7K | 17.1K | +5.5K | 🚀 加速18% |
| gallery | — | ~16K | 20.6K | +4.6K | 🆕 爆发 |
| Archon | ~14.4K | ~16.8K | 16.8K | +2.4K | 📈 稳定 |
| seomachine | ~3.1K | ~5.7K | 5.8K | +2.7K | 📈 稳定 |
| karpathy | ~10K | ~14K | ❌跌出 | — | ⚠️ 退潮 |

---

## Step 3: 5 条竞品分析洞察

### 洞察 1: 注意力正在从"框架"转向"平台"
hermes 64K⭐ 但增速腰斩 (8.2K→5.5K/天)。multica +5,362/周 (加速53%) 说明管理/编排层是下一阶段。
**Lobster 行动**: 边缘编排 = 管理层的差异化版本。叙事应从"运行实例"升级为"管理 50 个 Agent"。

### 洞察 2: 免费替代热度退潮 = 机会窗口关闭
openscreen + goose 同时跌出首页。免费替代的黄金窗口已打开过 (openscreen 28K⭐ 证明)。
**Lobster 行动**: "$0 基础设施" 仍然是卖点，但不能作为唯一叙事。需要叠加"安全审计" + "确定性执行"。

### 洞察 3: Google 端侧 ML = 最大同盟
gallery 20.6K⭐ + LiteRT-LM 3.5K⭐，Google 全力押注端侧/本地 ML。
**Lobster 行动**: 主动寻求集成 LiteRT-LM。"Lobster + LiteRT-LM = 旧手机跑本地 AI Agent 集群" 是独特叙事。

### 洞察 4: 确定性编码 (Archon) = 新范式
Archon 16.8K⭐，"The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable."
**Lobster 行动**: 边缘部署 = 最确定性的运行方式。加入 "deterministic execution" 到 README 叙事。

### 洞察 5: Mythos 1179pts 连续 8 天 = 变现金矿
小模型安全审计是 HN 当前最持久的话题。旧手机 + 小模型 + 安全审计 = Lobster 完美定位。
**Lobster 行动**: P0 — 写"旧手机安全审计 Agent" 方案并开源。

---

## 五层竞品格局 V7 (更新)

| 层级 | 代表项目 | 星 | 趋势 | Lobster 关系 |
|------|---------|-----|------|-------------|
| L0 框架层 | hermes-agent | 64.7K | 📈 增速放缓 | 互补 |
| L1 确定性层 | Archon | 16.8K | 📈 新范式 | 学习+互补 |
| L2 管理平台 | multica | 9.0K | 🚀🚀 加速53% | **直接竞争** |
| L3 垂直工作流 | seomachine, DeepTutor | 5.8K, 17.1K | 📈 | 不同赛道 |
| L4 端侧 ML | gallery, LiteRT-LM | 20.6K, 3.5K | 🆕 | **天然盟友** |
| L5 身份层 | personaplex | 9.1K | 📈 | 远期 |
| L6 免费替代 | openscreen | 28.4K | ⚠️ 跌出首页 | 窗口已过 |
| L7 技能分发 | karpathy-skills | ❌ 跌出 | ⚠️ 退潮 | 升级到工作空间 |

---

*研究时间: 2026-04-12 16:04 UTC | 调用: 1 次 | 文件产出: ~4KB*
