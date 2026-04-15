# Research-Driven Agent 模式

**版本**: V0.5.1  
**创建时间**: 2026-04-10  
**灵感来源**: SkyPilot "Research-Driven Agents" (HN 113 pts)

---

## 核心理念

**先研究，后编码。**

SkyPilot 团队发现：Coding Agent 在写代码前先读论文、研究竞品 fork、理解硬件瓶颈，找到的优化比 code-only agent **高 10 倍以上**。

- Code-only Wave 1: SIMD 微优化，+0.6% (噪声范围)
- Research-driven: 理解内存带宽瓶颈，+15% (真实提升)

Lobster 天然适合这种模式：**50 个实例 = 50 个并行研究员**。

---

## One-Call Chain 研究循环

```
┌─────────────────────────────────────────────┐
│           Research-Driven Loop              │
│                                             │
│  1. 采集 → 读论文/竞品/文档/社区讨论        │
│  2. 分析 → 归纳模式/找差距/定方向           │
│  3. 产出 → 写报告/代码/文章                 │
│  4. 发布 → 发社区/提 PR/推代码              │
│  5. 记录 → 写入记忆/更新知识库              │
│                                             │
│  ↻ 循环，每次基于上一次的结果               │
└─────────────────────────────────────────────┘
```

---

## Lobster 多实例研究策略

### 分配方案 (50 实例)

| 组别 | 实例数 | 研究方向 | 产出 |
|------|--------|---------|------|
| 🔬 前沿组 | 10 | arxiv 论文 + 技术博客 | 研究摘要 |
| 📊 竞品组 | 10 | GitHub Trending + 竞品分析 | 竞品报告 |
| 💰 变现组 | 10 | Gumroad/GitHub Sponsors/咨询 | 变现策略 |
| 📝 内容组 | 10 | HN/Reddit/技术文章撰写 | 博客/教程 |
| 🛡️ 审计组 | 10 | 代码审查 + 安全分析 | 审计报告 |

### 协调机制

```yaml
# configs/research-research.yaml
instances:
  # 前沿组: 研究论文
  - id: "research-front-01"
    name: "前沿研究员 #1"
    workspace: "data/workspaces/research-front-01"
    cron: "0 */2 * * *"  # 每 2 小时
    research_targets:
      - "arxiv.org/abs/*"
      - "blog.skypilot.co/*"
      - "openai.com/blog/*"

  # 竞品组: 监控竞品
  - id: "research-competitor-01"
    name: "竞品分析员 #1"
    workspace: "data/workspaces/research-competitor-01"
    cron: "0 */4 * * *"  # 每 4 小时
    research_targets:
      - "github.com/NousResearch/hermes-agent"
      - "github.com/onyx-dot-app/onyx"
      - "news.ycombinator.com"

  # 变现组: 研究变现路径
  - id: "research-monetization-01"
    name: "变现研究员 #1"
    workspace: "data/workspaces/research-monetization-01"
    cron: "0 */6 * * *"  # 每 6 小时
    research_targets:
      - "gumroad.com/browse/software"
      - "github.com/sponsors"
```

---

## ./papers 目录结构 (灵感: ctoth/Qlatt)

每个 Lobster workspace 可以有 `papers/` 目录，存放研究文献：

```
workspace/
├── papers/
│   ├── INDEX.md              # 论文索引 (auto-generated)
│   ├── tagged/               # 按标签分类
│   │   ├── agent-architecture/
│   │   ├── memory-systems/
│   │   ├── optimization/
│   │   └── security/
│   └── summaries/            # LLM 摘要
├── research-logs/
│   ├── 2026-04-10-front.md
│   └── 2026-04-10-competitor.md
└── CLAUDE.md                 # 指示 Agent 读 papers 再编码
```

### CLAUDE.md 示例

```markdown
# Research-First 规则

在写任何代码之前:

1. 检查 ./papers/INDEX.md 是否有相关文献
2. 如果有，先读论文摘要
3. 检查竞品是否已有类似实现
4. 基于研究结果再制定方案
5. 如果研究不足，先做研究再编码

> "代码只告诉你它在做什么，
>  研究告诉你为什么它慢、别人试过什么、
>  以及理论最优在哪里。"
```

---

## 实战案例

### 案例 1: SkyPilot 优化 llama.cpp

- **方法**: Research → Experiment → Commit
- **成本**: $29 (4 VMs, 3 小时)
- **结果**: +15% flash attention (x86), +5% (ARM)
- **关键**: 研究竞品 fork (ik_llama.cpp) 比读 arxiv 更有效

### 案例 2: Tobi Lütke 优化 Shopify Liquid

- **方法**: pi-autoresearch (Karpathy 的循环)
- **结果**: 120 实验, 93 commits, -53% 时间, -61% 分配
- **零回归**: 974 个单元测试全部通过

### 案例 3: Lobster One-Call Chain (我们)

- **方法**: 采集 → 分析 → 产出 → 发布 → 记录
- **成本**: ¥0.05/次 (单次模型调用)
- **结果**: #15 轮研究, 15+ 研究文档, 多个社区草稿
- **优势**: 旧手机部署, 近乎零成本持续研究

---

## 研究质量指标

| 指标 | 目标 | 测量方式 |
|------|------|---------|
| 研究深度 | 3 层分析 (表象→原因→方案) | 文档评审 |
| 数据支撑 | 每个结论有数据/引用 | 交叉验证 |
| 可执行性 | 每条建议有具体行动项 | 行动跟踪 |
| 成本效率 | ≤¥0.10/篇 | 调用计数 |

---

## 参考

- [SkyPilot Blog: Research-Driven Agents](https://blog.skypilot.co/research-driven-agents/)
- [ctoth/Qlatt: papers directory](https://github.com/ctoth/Qlatt/blob/master/papers/)
- [Karpathy autoresearch](https://github.com/karpathy/autoresearch)
- [pi-autoresearch](https://github.com/davebcn87/pi-autoresearch)
- [Agent Tuning](https://github.com/adam-s/agent-tuning)

---

*Research first, code second, ship always.*
