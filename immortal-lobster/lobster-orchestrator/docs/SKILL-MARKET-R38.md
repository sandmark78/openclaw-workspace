# 技能市场研究 #38 — hermes 72K 爆发 + karpathy-skills 回归 + 11 天零 AI Agent 帖

**研究轮次**: #38  
**方向**: 技能市场 (Skills Market)  
**时间**: 2026-04-13 08:05 UTC  
**数据源**: HN Top 10 + GitHub Trending 周榜

---

## Step 1: 采集数据

### HN 周一早间信号 (08:05 UTC, 2026-04-13)
| 热帖 | 分数 | 评论 | 信号 |
|------|------|------|------|
| Bring Back Idiomatic Design (2023) | 537pts | 293c | 💥 设计哲学碾压技术帖 |
| DIY Soft Drinks | 396pts | 107c | 自制/DIY 文化 |
| Show HN: boringBar (macOS 任务栏) | 347pts | 193c | 开发者工具回归 |
| All elementary functions from single operator | 294pts | 87c | 理论计算机科学 |
| Taking on CUDA with ROCm | 147pts | 109c | GPU 生态竞争 |
| Software Teams Economics | 83pts | 42c | 工程组织盲区 |
| A perfectable programming language (Lean) | 111pts | 39c | 语言设计 |
| **零 AI Agent 帖进入 Top 10（连续第 11 天！）** | — | — | ⚠️ 注意力彻底转移 |

### GitHub Trending 周榜 (08:05 UTC)
| 项目 | 总星 | 周增 | 变化 vs R37 |
|------|------|------|-------------|
| hermes-agent | **71,963** | **+38,426** | 🚀🚀🚀 从 65.6K→72K！单周 +38K |
| markitdown | **105,808** | +10,592 | 🚀 破 105K！ |
| **multica** | **10,011** | +6,846 | 🎉 突破 10K！ |
| gallery (Google) | 20,774 | +4,148 | 📈 端侧 ML |
| DeepTutor | 17,440 | +5,873 | 🚀 加速 |
| Archon | 17,294 | +2,962 | 📈 确定性编码 |
| **karpathy-skills** | **✅ 回归 Trending** | — | 🔄 消失 3 轮后回归！ |
| personaplex (NVIDIA) | 9,136 | +2,331 | 📈 身份层 |
| seomachine | 5,865 | +2,815 | 📈 工作空间模式 |
| LiteRT-LM (Google) | 3,595 | +2,164 | 📈 端侧 ML |

### Lobster 仓库状态
- 最新 commit: 0aa94da (Competitor Analysis R36)
- 本地未推送 commit: 537b49c (R37, push 失败 token 过期)
- 本地未推送 commit: 2b6a616 (R35, push 失败 token 过期)

---

## Step 2: 深度分析

### 🔥 核心发现 #1: hermes 72K — 单周 +38,426 星的异常爆发

hermes 增速数据:
- R35 (4/12 14:04): 63,714
- R36 (4/12 16:04): 64,698 (+984/2h)
- R37 (4/12 20:04): 65,577 (+879/4h)
- **R38 (4/13 08:05): 71,963 (+6,386/12h!)**

这不是线性增长。12 小时 +6,386 星 = 日均 12,772 星，是之前 5-6K/天的 **2 倍+**。

**可能原因**:
1. Orange Book (PDF 指南) 4 天 2K⭐ 的文档传播效应外溢
2. Claude Code 生态淘金热的溢出效应 (claude-usage, SkillClaw 等)
3. 周末 + 周一叠加效应 (社区重新活跃)
4. 某个大 V 推荐或 Hacker News 帖子引流

**对 Lobster 的意义**:
- hermes 不是"饱和"了，而是进入**第二增长曲线**
- 框架层饱和的判断需要修正：需求仍在，只是从"新奇"转向"实用"
- Lobster 应该搭 hermes 的便车："hermes 是你的 Agent，Lobster 是你的 Agent 集群管理"

### 🔥 核心发现 #2: karpathy-skills 回归 — 技能即文件的范式不死

karpathy-skills 消失了 3 轮 (R35, R36, R37) 后重新出现在 Trending。

**为什么回归？**
- CLAUDE.md 格式被更多工具采纳 (OpenClaw, Claude Code, 等)
- 社区意识到"配置比代码更重要"
- Andrej Karpathy 个人品牌效应的持续发酵
- 从"新奇"到"必需品"的转变

**对 Lobster 的意义**:
- 单文件配置模式验证了 Lobster 的"配置优先"策略
- Lobster 的 CLAUDE.md 配置包 = 低内容高传播的甜蜜点
- **行动**: 立即发布 lobster-survival-checklist 到 GitHub (模仿 karpathy-skills)

### 🔥 核心发现 #3: multica 突破 10K — Cloud SaaS 模式里程碑

multica 从 R37 的 9,190 增长到 10,011 (+821/12h)，正式突破 10K 星标。

- 周增 +6,846（加速 53% 持续）
- 官方 README 列出 OpenClaw 为支持的运行时
- "managed agents platform" 叙事被市场接受

**对 Lobster 的定位影响**:
- multica = Cloud SaaS (云端编排) vs Lobster = Edge (边缘编排)
- 不是竞争，是互补：multica 管云端，Lobster 管边缘
- **差异化叙事**: "multica 管云上的 Agent，Lobster 管你抽屉里的旧手机"

### 🔥 核心发现 #4: 11 天零 AI Agent 帖 — 注意力经济大转移

从 2026-04-02 至今，连续 11 天 HN Top 10 无 AI Agent 帖。

**替代叙事在崛起**:
1. 设计哲学 (Idiomatic Design 537pts) — "怎么做" > "做什么"
2. 开发者工具 (boringBar 347pts) — 个人生产力工具
3. DIY 文化 (Soft Drinks 396pts) — 自己动手
4. 理论计算 (elementary functions 294pts) — 基础科学

**对 Lobster 的启示**:
- "AI Agent 编排" 叙事已疲劳
- **新叙事方向**: "资源优化"、"DIY 基础设施"、"用已有资源做更多"
- boringBar (macOS 任务栏替代品) 的成功 = 现有工具的改善 > 全新工具
- Lobster 应该说："改善你已有的旧手机，而不是买新服务器"

---

## Step 3: 技能市场格局 V9 更新

### 七层格局 (2026-04-13)

| 层级 | 代表 | 星数 | 趋势 | Lobster 关系 |
|------|------|------|------|-------------|
| L0 框架层 | hermes-agent | 71,963 | 🚀🚀 爆发 | 互补 |
| L1 确定性层 | Archon | 17,294 | 📈 稳定 | 学习 |
| L2 Cloud SaaS | multica | 10,011 | 🚀 突破 10K | 互补: 云 vs 边缘 |
| L3 垂直工作流 | seomachine | 5,865 | 📈 稳定 | 学习 |
| L4 技能分发 | karpathy-skills | ✅ 回归 | 🔄 必需品化 | 模仿: 单文件发布 |
| L5 端侧 ML | gallery+LiteRT | 24,369 | 📈 大厂方向 | 同盟 |
| L6 身份层 | personaplex | 9,136 | 📈 稳定 | 远期 |
| L7 大厂开源 | markitdown | 105,808 | 🚀 破 105K | 获客模型学习 |

### 关键变化 vs V8 (12 小时前)
1. hermes 从 65.6K→72K (+6.4K/12h)，增速翻倍
2. multica 突破 10K 里程碑
3. karpathy-skills 回归 Trending（消失 3 轮后）
4. markitdown 突破 105K
5. 11 天零 AI Agent 帖 — 需彻底换叙事

---

## Step 4: Lobster 技能市场策略 V9

### 立即行动 (P0, 本周)
1. **🔥 发布 lobster-survival-checklist** — 单文件 CLAUDE.md 配置包 (模仿 karpathy-skills, ROI 5.0)
2. **📝 重写 README 叙事** — "用已有资源做更多" > "AI Agent 编排" (ROI 4.5)
3. **🔧 修复 GitHub Token** — 3 个 commit 待推送 (ROI 4.0)

### 中期行动 (P1, 2 周内)
4. **🤝 加入 multica 生态** — 官方支持 OpenClaw = 现成用户池 (ROI 4.5)
5. **📱 LiteRT-LM 集成 PoC** — 端侧 ML + 手机编排 (ROI 4.0)
6. **📖 写 Orange Book** — 模仿 hermes Orange Book 成功 (ROI 5.0)

### 长期行动 (P2, 1-2 月)
7. **🔒 差异化定位** — 边缘编排 vs 云端编排 (ROI 3.5)
8. **💰 变现** — 配置模板市场 / 咨询服务 (ROI TBD)

---

## Step 5: 5 条可执行洞察

1. **hermes 爆发 = 搭便车机会** — 写 "hermes + Lobster: 从单 Agent 到多实例集群" 教程
2. **karpathy-skills 回归 = 单文件模式验证** — 立即发布 lobster CLAUDE.md
3. **multica 10K = Cloud SaaS 验证** — 差异化: Lobster 做边缘，不做云端
4. **11 天零 Agent 帖 = 换叙事** — "DIY 基础设施" / "资源优化" 取代 "Agent 编排"
5. **markitdown 105K = 大厂开源获客** — Lobster 应做"免费替代 + 付费服务"模式
