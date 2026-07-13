# 开源增长观察 #29 — Berkeley 基准破解 + Google 边缘 ML 崛起

**日期**: 2026-04-12 02:04 UTC  
**轮换**: 开源增长 (Open Source Growth)  
**研究轮次**: #29

---

## 📊 GitHub Trending 周榜数据追踪

### 核心项目增速对比（与 #28 对比）

| 项目 | 总星 | 周增 | 增速变化 | 信号 |
|------|------|------|----------|------|
| hermes-agent | 59,278 | +32,572 | ↔️ 持平 | 框架层天花板显现 |
| markitdown | 102,327 | +8,202 | ↔️ 持平 | 大厂开源获客标杆 |
| openscreen | 28,160 | +8,964 | ↔️ 持平 | 免费替代叙事持续 |
| oh-my-codex | 21,108 | +5,828 | ↔️ 持平 | Codex 生态加速减速 |
| goose | 41,218 | +5,832 | ↔️ 持平 | Rust 原生 Agent 稳定 |
| DeepTutor | 16,807 | +5,560 | ↔️ 持平 | 教育+Agent 蓝海 |
| karpathy-skills | 13,695 | +4,969 | ↔️ 持平 | 单文件神话 |
| multica | 7,992 | +5,362 | ↔️ 持平 | 管理型 Agent SaaS |
| seomachine | 5,693 | +2,698 | ↔️ 持平 | 工作空间即产品 |

### 新增上榜项目

| 项目 | 总星 | 周增 | 类别 | 增长信号 |
|------|------|------|------|----------|
| google-ai-edge/gallery | 20,441 | +4,369 | 边缘 ML 展示 | 🔥 新势力 |
| google-ai-edge/LiteRT-LM | 3,430 | +2,196 | 边缘推理框架 | 🚀 早期爆发 |
| NVIDIA/personaplex | 9,022 | +2,905 | 人格化 AI | 📈 持续增长 |

### hermes 增速 7 天追踪

| 日期 | 日增估 | 趋势 |
|------|--------|------|
| 04-07 | ~8,200 | 🚀 峰值 |
| 04-08 | ~6,485 | 📉 下降 21% |
| 04-09 | ~5,407 | 📉 下降 17% |
| 04-10 | ~3,836 | 📉 下降 29% |
| 04-11 | +6,437 | 📈 周末反弹 |
| 04-12 | +32,572/周 | ↔️ 整体稳定 |

**结论**: hermes 在 59K 星处进入平台期，日增从峰值 8.2K 降到 3.8-6.4K。框架层叙事基本见顶。

---

## 🔥 HN 周日信号分析

### Top 5 热帖

| 标题 | 分数 | 评论 | 类别 | 信号 |
|------|------|------|------|------|
| Small models also found Mythos vulns | 845 | 230 | AI 安全 | ⚠️ 小模型能力崛起 |
| Advanced Mac Substitute | 199 | 51 | 复古开发 | 开发者工具回归 |
| Berkeley: Broke AI Agent Benchmarks | 223 | 60 | AI 基准 | 💥 行业地震 |
| Apple Silicon VM 突破 2 台限制 | 148 | 84 | 资源优化 | 资源复用刚需 |
| 447 TB/cm² 原子级存储 | 141 | 71 | 硬件前沿 | 长期趋势 |

### 核心信号

**1. Berkeley 基准破解论文 = 行业地震** 💥
- 8 大主流 AI Agent 基准全被攻破：SWE-bench、WebArena、OSWorld、GAIA、Terminal-Bench 等
- 攻击方式：conftest.py 10 行代码 → SWE-bench 100% 通过
- 意义：**所有 AI Agent 的基准分数都可能是假的**
- 影响：模型厂商的营销叙事面临信任危机，开源社区将要求新的评估方式
- 对 Lobster 的启示：**不要拿基准分数做营销，要做真实可验证的交付**

**2. 小模型也能找到 Mythos 级漏洞** ⚠️
- 845 分 + 230 评论 = 超高热度
- 小模型在安全领域的能力被严重低估
- 对 Lobster 的启示：**边缘设备上的小模型 + 本地安全扫描 = 新用例**

**3. Google 边缘 ML 双上榜** 🔥
- LiteRT-LM（C++ 边缘推理框架）周增 2,196
- Gallery（边缘 ML 展示厅）周增 4,369
- 信号：Google 在全力推 on-device AI
- 对 Lobster 的启示：**手机编排 + 边缘推理 = 天然契合**

---

## 📈 开源增长 5 条洞察

### 洞察 1: 基准信任危机 = 营销叙事洗牌
Berkeley 论文证明所有主流 AI Agent 基准都被攻破。这意味着：
- 模型厂商的"XX% 解决率"叙事将受到质疑
- 开源社区将要求**真实任务评估**而非基准分数
- **Lobster 机会**：主打"真实可验证的资源优化"，不碰基准分数叙事

### 洞察 2: Google 边缘 ML 全面发力
- LiteRT-LM（C++ 推理引擎）+ Gallery（展示平台）双上榜
- Google 的战略：把 AI 推到设备上，减少云依赖
- **Lobster 机会**：手机编排 + 边缘推理 = 天然匹配。Lobster 可以成为 LiteRT-LM 的编排层

### 洞察 3: hermes 59K 星 = 框架层天花板
- 日增从 8.2K 降到 3.8-6.4K
- 框架层（hermes、goose、oh-my-codex）增速全面放缓
- **Lobster 机会**：避开框架层竞争，专注**边缘编排**和**资源优化**

### 洞察 4: karpathy-skills 13.6K 星 = 最低内容最高传播
- 只有一个 CLAUDE.md 文件
- 周增 4,969（加速 33%）
- **Lobster 机会**：发布 Lobster Survival Checklist（单文件配置），模仿此模式

### 洞察 5: 开源增长模式 = "免费替代 + 工作空间"
- openscreen（免费 ScreenStudio 替代）周增 8,964
- seomachine（SEO 工作空间）周增 2,698
- markitdown（格式转换工具）102K⭐
- **Lobster 机会**：定位为"免费手机服务器替代"，开源获客 → 专业版变现

---

## 🎯 Lobster 增长策略更新

### 短期（本周）
1. **发布 Lobster Survival Checklist** — 模仿 karpathy-skills 单文件模式，放到独立 GitHub 仓库
2. **重写 README 叙事** — 从"AI Agent 编排"改为"资源优化工具"，对标 openscreen 的"免费替代"叙事

### 中期（1-2 月）
3. **LiteRT-LM 集成 PoC** — 展示 Lobster 在手机上运行 Google 边缘推理模型
4. **配置模板市场** — 模仿 seomachine 的 workspace 模式

### 长期（3-6 月）
5. **Lobster Cloud 托管** — 对标 openscreen 的 SaaS 模式
6. **安全扫描模块** — 利用小模型漏洞检测能力，做本地安全扫描

---

## 📊 数据附录

### 研究周期
- #28 (04-12 00:04 UTC): 变现案例
- #29 (04-12 02:04 UTC): 开源增长

### 数据来源
- HN Firebase API (Top 10 stories)
- GitHub Trending 周榜
- Berkeley RDI 论文全文
- Lobster 仓库状态 (commit 704b6e0)

---

*🦞 一次调用，五件事。省下来的都是钱。*
