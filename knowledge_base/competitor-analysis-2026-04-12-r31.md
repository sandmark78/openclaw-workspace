# 竞品分析 R31 — 小模型安全革命 + 新品类爆发

**研究轮次**: #31
**研究方向**: 竞品分析 (Competitor Analysis)
**时间**: 2026-04-12 06:04 UTC
**数据来源**: HN Front Page (Algolia) + GitHub Trending 周榜 + GitHub 新创搜索

---

## Step 1: 采集摘要

### HN 周日/周一信号 (2026-04-12 06:04 UTC)

| 排名 | 标题 | 分数 | 评论 | Lobster 关联 |
|------|------|------|------|-------------|
| 🔥 #1 | Small models also found Mythos vulns | **964pts** | **261** | 💥 直接验证 |
| #2 | Show HN: Pardonned.com (赦免数据库) | 409pts | 227 | 开源工具模式 |
| #3 | Berkeley: Broke AI Agent Benchmarks (续篇) | 317pts | 86 | 基准信任危机 |
| #4 | Apple Silicon VM 突破 2 台限制 | 178pts | 123 | 资源复用刚需 |
| #5 | Dark Castle | 163pts | 20 | 极简传播 |
| #6 | How Complex is my Code? | 80pts | 15 | 代码质量 |

**关键信号**:
- 零 AI Agent 帖进入 Top 10（**连续第 5 天！**）
- Small models / Mythos 从昨天 906pts → 今天 964pts，**仍在上涨**
- Berkeley 基准破解续篇 (What Comes Next) 317pts，讨论升级

### GitHub 周榜 Top 12

| 项目 | 总星 | 周增 | 趋势 | 变化 vs R30 |
|------|------|------|------|-------------|
| hermes-agent | **60,765** | +32,572 | 🚀 | +492 星 |
| markitdown | 102,758 | +8,202 | 🚀 加速 57% | +186 |
| openscreen | 28,316 | +8,964 | 📉 减速 11% | +71 |
| goose | 41,251 | +5,832 | 📉 减速 9% | +23 |
| multica | **8,289** | +5,362 | 🚀 加速 53% | +149 |
| DeepTutor | 16,919 | +5,560 | 🚀 加速 18% | +54 |
| karpathy-skills | 13,991 | +4,969 | 🚀 加速 33% | +144 |
| personaplex (NVIDIA) | 9,034 | +2,905 | 📈 稳定 | +28 |
| seomachine | 5,710 | +2,698 | 📈 稳定 7% | +27 |
| LiteRT-LM (Google) | 3,450 | +2,196 | 🆕 | +13 |
| Google AI Edge Gallery | 20,482 | +4,369 | 🆕 | +26 |

### 🆕 GitHub 新创项目 (created > 2026-04-05, sorted by stars)

| 项目 | 语言 | 星 | Fork | 创建 | 分析 |
|------|------|-----|------|------|------|
| farzaa/clicky | Swift | **3,815** | 673 | 04-07 | 5 天 3.8K — 极客名人效应 |
| awesome-persona-distill-skills | — | ~新星 | — | 04-07 | "同事/女娲/前任" 技能集合 — **新品类** |

### Lobster 仓库状态
- Commit: `704b6e0` (无新提交)
- 分支: master
- 上次推送: 2026-04-11 (commit 704b6e0)

---

## Step 2: 深度分析

### 🔥 信号 #1: Small models / Mythos — 964pts, 261 评论

**为什么这是本周最大信号**:
- 从昨天 906pts 涨到 964pts — **仍在上涨，接近 1000 分大关**
- 261 条评论 — 本周最多讨论
- 核心论点: 小模型 (不是 GPT-4/Claude Opus) 也能发现 Mythos 级安全漏洞
- 这意味着: **安全审计不需要大模型，小模型 + 正确方法 = 同等效果**

**对 Lobster 的直接影响**:
1. 我们的"旧手机跑小模型"定位 = **安全审计的最优解**
2. 边缘部署 = 物理隔离 = 安全测试的天然优势
3. 50 个实例 = 50 个独立安全审计 Agent

**竞品影响**:
- hermes (60K⭐): 自进化叙事 → 需要证明"进化出安全能力"
- multica (8.3K⭐): 管理队友 → 队友能发现漏洞吗？
- goose (41K⭐): 通用 Agent → 安全是子集
- **Lobster 机会**: 唯一聚焦"边缘安全审计"的编排器

### 🔥 信号 #2: Berkeley 基准破解续篇 — 317pts

"What Comes Next" — 说明基准信任危机远未结束：
- R27 分析了第一篇 (8 个基准全破)
- 续篇讨论"然后呢" — 社区在寻找替代方案
- **Lobster 叙事升级**: "基准可黑，边缘部署不可黑"
  - 50 实例在旧手机上 = 真实物理指标
  - 无法用 conftest.py 作弊
  - 无法用 curl wrapper 骗过

### 🔥 信号 #3: awesome-persona-distill-skills — 新品类

**描述**: "同事.skill, 女娲.skill, 前任.skill… Curated list of Agent Skills centered on people, relationships, commemorative scenes"

**解读**:
- 技能市场正在从"技术技能"扩展到"人际/情感技能"
- 中文语境下的 Skill 命名 (.skill 后缀)
- karpathy-skills (13.9K⭐) 范式正在被模仿和扩展
- **Lobster 启示**: 技能分类需要扩展 — 不只是技术，还有人际/方法论

### 🔥 信号 #4: farzaa/clicky — 5 天 3.8K 星

- Swift 项目，无描述 (description: null)
- 创建者 farzaa 是知名开发者 (Replit 联合创始人)
- 5 天 3.8K = 名人效应 > 产品价值
- **启示**: 叙事和创始人声誉比代码更重要

### 五层竞品格局 V4 更新

| 层 | 代表 | 规模 | 趋势 | Lobster 位置 |
|----|------|------|------|-------------|
| L0 框架层 | hermes 60.8K⭐ | 饱和 | 加速中 | 互补/寄生 |
| L1 增强层 | goose 41.3K⭐, oh-my-codex 21K⭐ | 增长中 | 减速 | 互补 |
| L2 管理层 | multica 8.3K⭐ | 快速扩张 | 加速 53% | 直接竞争 |
| L3 垂直层 | seomachine 5.7K⭐, DeepTutor 16.9K⭐ | 稳定 | 加速 | 不同赛道 |
| L4 身份层 | karpathy-skills 14K⭐, personaplex 9K⭐ | 扩散中 | 加速 33% | 学习传播 |
| L5 边缘层 | Lobster, LiteRT-LM 3.5K⭐, Gallery 20.5K⭐ | 萌芽 | 新势力 | **主场** |

**V4 关键变化**:
1. hermes 突破 60K — 框架层彻底饱和，不是竞争对手而是标准
2. multica 8.3K — 2 周增速从 +3.5K → +5.4K，**加速中**
3. Google 边缘 ML 双上榜 (LiteRT-LM + Gallery) — **边缘层不再是 Lobster 独角戏**
4. 新品类出现: persona-distill-skills — 技能市场扩展

---

## Step 3: 5 条可执行洞察

### 洞察 #1: 小模型安全审计 = Lobster 最佳变现路径 (ROI 5.0)
- Mythos 帖 964pts 且持续上涨
- 小模型 = 同等安全效果
- Lobster = 小模型编排 → 天然匹配
- **行动**: 写"旧手机安全审计 Agent 集群"方案文档

### 洞察 #2: 基准信任危机 = Lobster 营销金矿 (ROI 4.5)
- Berkeley 续篇 317pts 讨论升级
- "真实部署 vs 基准作弊" 是顶级叙事
- **行动**: README 加入"benchmark-proof"叙事

### 洞察 #3: multica 加速是最大威胁 (ROI 4.0)
- 8.3K⭐，周增 5.4K，2 周 +47%
- 支持 OpenClaw 作为一等 runtime
- **差异化**: Lobster 做边缘，multica 做云端

### 洞察 #4: 技能品类扩展 = 新机会 (ROI 3.5)
- persona-distill-skills 证明技能不止技术
- Lobster 技能市场应包含方法论/人际类
- **行动**: 更新技能分类体系

### 洞察 #5: Google 边缘 ML = 同盟不是竞争 (ROI 3.0)
- LiteRT-LM + Gallery 双上榜
- Google 在验证边缘 ML 方向
- **行动**: 调研 LiteRT-LM + Lobster 集成

---

## Step 4: Lobster 竞品应对策略更新

### 短期 (本周)
- [ ] 写"旧手机安全审计 Agent 集群"方案 (基于 Mythos 964pts 信号)
- [ ] README 加入 benchmark-proof 叙事
- [ ] 监控 multica 增速 (已突破 8K)

### 中期 (本月)
- [ ] 技能分类体系扩展 (加入方法论/人际类)
- [ ] LiteRT-LM 集成调研
- [ ] 发布 Lobster 配置包到 GitHub

### 长期 (季度)
- [ ] 边缘安全审计产品线
- [ ] 与 Google 边缘 ML 生态集成
- [ ] 对标 multica 的"Agent 即队友"叙事

---

## Step 5: 竞品增速追踪 (7 天)

| 项目 | R25(04-11) | R31(04-12) | 变化 | 日均增速 |
|------|------------|------------|------|---------|
| hermes-agent | 58,456 | 60,765 | +2,309 | ~330/天 |
| markitdown | 101,989 | 102,758 | +769 | ~110/天 |
| openscreen | 28,097 | 28,316 | +219 | ~31/天 |
| goose | 41,185 | 41,251 | +66 | ~9/天 |
| multica | 7,773 | 8,289 | +516 | ~74/天 |
| karpathy-skills | 13,357 | 13,991 | +634 | ~91/天 |
| DeepTutor | 16,697 | 16,919 | +222 | ~32/天 |
| personaplex | 9,006 | 9,034 | +28 | ~4/天 |
| seomachine | 5,675 | 5,710 | +35 | ~5/天 |

**关键发现**: hermes 日增从 ~6.4K (周末) 降到 ~330/天 (周一)，**工作日回归正常增速**。multica 和 karpathy-skills 仍保持高增速。

---

*研究轮次: #31*
*下次轮换: 独立开发者路径*
*文件: knowledge_base/competitor-analysis-2026-04-12-r31.md*
