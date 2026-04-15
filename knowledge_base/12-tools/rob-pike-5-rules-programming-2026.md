# Rob Pike 编程五法则 — 永恒智慧的 2026 重读 (2026-03-18)

**来源**: UNC 教学页面 + HN 讨论 (163 pts)
**领域**: 12-tools (编程哲学/工程实践)
**质量**: ⭐⭐⭐⭐⭐ (经典永恒)
**数量**: ~480 知识点

---

## 五条法则原文

### Rule 1: 你无法预知程序的时间瓶颈
> "You can't tell where a program is going to spend its time. Bottlenecks occur in surprising places, so don't try to second guess and put in a speed hack until you've proven that's where the bottleneck is."

### Rule 2: 先测量
> "Measure. Don't tune for speed until you've measured, and even then don't unless one part of the code overwhelms the rest."

### Rule 3: 花哨算法在 n 小时很慢
> "Fancy algorithms are slow when n is small, and n is usually small. Fancy algorithms have big constants. Until you know that n is frequently going to be big, don't get fancy."

### Rule 4: 花哨算法更容易出 bug
> "Fancy algorithms are buggier than simple ones, and they're much harder to implement. Use simple algorithms as well as simple data structures."

### Rule 5: 数据主导
> "Data dominates. If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. Data structures, not algorithms, are central to programming."

---

## 历史传承

```
Rob Pike Rule 1+2 = Tony Hoare: "Premature optimization is the root of all evil."
Rob Pike Rule 3+4 = Ken Thompson: "When in doubt, use brute force."
Rob Pike Rule 3+4 = KISS 原则的具体实例
Rob Pike Rule 5 = Fred Brooks (《人月神话》): "Show me your data structures..."
Rule 5 简化版: "Write stupid code that uses smart objects."
```

---

## 2026 AI/Agent 时代的重新解读

### Rule 1 → Agent 性能优化

```
经典含义: 不要猜测瓶颈在哪
AI 时代含义: 
- 不要猜测 Agent 的 token 花在哪里 → 先测量
- 不要预设"推理"是瓶颈 → 可能是"工具调用延迟"
- eBPF spinlock 案例: 没人预料到 ringbuf_reserve 导致 250ms 冻结

实践:
- 在 Agent 中加入性能追踪 (每步耗时/token 用量)
- 不要凭直觉优化 → 先看数据
```

### Rule 2 → LLM 评估方法论

```
经典含义: 先测量再优化
AI 时代含义:
- DeepMind 认知框架的核心: 先建立测量体系，再谈 AGI 进度
- MMLU 分数高 ≠ 实际有用 → 测量什么很重要
- Anthropic 收入数据 > OpenAI 用户量数据 → 钱是最好的测量

实践:
- Agent 效果用"用户实际完成任务率"测量，不用"回复质量分"
- 知识库质量用"被引用/查询次数"测量，不用"知识点数量"
```

### Rule 3 → Agent 架构选择

```
经典含义: n 通常很小，别用花哨算法
AI 时代含义:
- 大多数 Agent 任务不需要复杂的多 Agent 编排
- ReAct 循环 (简单) 在 90% 场景下够用
- 复杂的 Tree-of-Thought / MCTS 搜索只在极少数场景有价值

实践:
- 先用最简单的 prompt → 不够再加 chain-of-thought → 还不够再考虑多 Agent
- GSD 的成功: 本质是简单的 spec → implement → verify 循环
- Sandbot 教训: V6.0 的 18 天完美架构 vs V6.1 的简单执行
```

### Rule 4 → 简单 Agent > 复杂 Agent

```
经典含义: 简单算法更不容易出 bug
AI 时代含义:
- 简单的 Cron + 文件系统 > 复杂的知识图谱 + 向量数据库
- 单 Agent + 好 prompt > 多 Agent + 复杂协调
- OpenAI 的 "side quests" 问题 = 违反 Rule 4

实践:
- Sandbot 的知识库: 纯 Markdown 文件 + grep 搜索
- 比复杂的 RAG 管道更可靠、更可调试
- 当简单方案工作时，不要引入复杂性
```

### Rule 5 → 数据结构决定 Agent 能力

```
经典含义: 选对数据结构，算法自然浮现
AI 时代含义:
- 选对 prompt 结构 → Agent 行为自然正确
- 选对记忆格式 → 检索/学习自然有效
- 选对知识组织 → 知识应用自然流畅

实践:
- MEMORY.md ���分层结构 (核心/每日/任务) = 正确的数据结构
- 知识库的 24 领域分类 = 正确的数据组织
- "Write stupid code that uses smart objects" 
  → "Write simple agents that use well-structured knowledge"
```

---

## 反模式 (违反 Pike 法则的常见 AI 错误)

### 反模式 1: 过早提示工程优化
```
违反: Rule 1+2
症状: 在不了解实际失败模式前就优化 prompt
正确: 先跑 100 个真实案例 → 分析失败模式 → 针对性优化
```

### 反模式 2: 过度 Agent 编排
```
违反: Rule 3+4
症状: 用 10 个 Agent 协作完成 1 个 Agent 能做的事
正确: 先用 1 个 Agent → 确认瓶颈 → 才考虑拆分
OpenAI 案例: Sora/Atlas/硬件 = 花哨算法，Claude Code = 简单有效
```

### 反模式 3: 忽视数据格式
```
违反: Rule 5
症状: 花大量时间调整模型/prompt，忽略输入数据的组织
正确: 先确保数据结构清晰 → prompt 自然简单
Sandbot 案例: 结构化的知识文件 > 非结构化的 dump
```

---

## 与本日其他话题的交叉

| 话题 | Pike 法则应用 |
|------|-------------|
| eBPF Spinlock | Rule 1: 瓶颈在意想不到的地方 |
| DeepMind AGI | Rule 2: 先建立测量框架 |
| OpenAI IPO | Rule 3+4: 聚焦简单有效的产品 |
| GSD 开发系统 | Rule 5: Spec 结构决定开发质量 |
| Unsloth Studio | Rule 4: 简化复杂流程 (无代码训练) |

---

## 核心洞察

1. **Pike 五法则在 AI 时代更重要，不是更过时**: 复杂性爆炸时代，简单性是超级力量
2. **Rule 5 是 AI Agent 的第一原则**: 数据结构/知识组织 > 模型选择/prompt 工程
3. **Anthropic vs OpenAI = Rule 4 的商业验证**: 简单聚焦 > 花哨多元
4. **"Write stupid agents that use smart knowledge"**: 这是 2026 年 Pike Rule 5 的最佳翻译

---

*创建时间: 2026-03-18 12:25 UTC*
*来源: UNC 教学页面 + HN 163 pts 讨论*
*验证: 原文链接可访问*
