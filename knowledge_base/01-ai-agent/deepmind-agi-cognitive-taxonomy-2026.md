# Google DeepMind AGI 认知分类框架 (2026-03-17)

**来源**: blog.google + Kaggle hackathon
**HN 热度**: 13 pts (新发布)
**领域**: 01-ai-agent
**质量**: ⭐⭐⭐⭐⭐ (定义性框架)
**数量**: ~580 知识点

---

## 核心框架

### 论文: "Measuring Progress Toward AGI: A Cognitive Taxonomy"

Google DeepMind 发布认知科学驱动的 AGI 测量框架，配套 $200,000 Kaggle 黑客松。

### 10 项关键认知能力

| # | 能力 | 定义 | AI 现状评估 |
|---|------|------|-------------|
| 1 | **感知 (Perception)** | 从环境提取和处理感官信息 | ⭐⭐⭐⭐ 多模态模型已接近人类 |
| 2 | **生成 (Generation)** | 产出文本、语音、动作等输出 | ⭐⭐⭐⭐ LLM 文本生成超越多数人类 |
| 3 | **注意力 (Attention)** | 聚焦认知资源到重要事物 | ⭐⭐⭐ Transformer 注意力 ≠ 人类选择性注意 |
| 4 | **学习 (Learning)** | 通过经验和指令获取新知识 | ⭐⭐ 在线学习/少样本仍远逊人类 |
| 5 | **记忆 (Memory)** | 存储和检索跨时间信息 | ⭐⭐ 上下文窗口 ≠ 真正记忆 |
| 6 | **推理 (Reasoning)** | 通过逻辑推理得出有效结论 | ⭐⭐⭐ Chain-of-Thought 有进步但脆弱 |
| 7 | **元认知 (Metacognition)** | 对自身认知过程的知识和监控 | ⭐ 校准差，过度自信 |
| 8 | **执行功能 (Executive Functions)** | 规划、抑制和认知灵活性 | ⭐⭐ 长期规划仍是弱项 |
| 9 | **问题解决 (Problem Solving)** | 为特定领域问题找到有效方案 | ⭐⭐⭐ 编码/数学有突破 |
| 10 | **社会认知 (Social Cognition)** | 处理社会信息并适当回应 | ⭐⭐ 表面共情 vs 深层理解 |

### 三阶段评估协议

```
Stage 1: 跨认知能力的广泛任务测试 (held-out 测试集)
Stage 2: 从人口统计学代表性成人样本收集人类基线
Stage 3: 将 AI 系统性能映射到���类性能分布
```

### Kaggle 黑客松: $200,000 奖金

**5 个评估缺口最大的赛道**:
1. 学习 (Learning) - $10K×2 + grand prize
2. 元认知 (Metacognition) - $10K×2 + grand prize
3. 注意力 (Attention) - $10K×2 + grand prize
4. 执行功能 (Executive Functions) - $10K×2 + grand prize
5. 社会认知 (Social Cognition) - $10K×2 + grand prize

**总计**: $10K×10 (每赛道 Top 2) + $25K×4 (总冠军) = $200K
**时间**: 2026-03-17 → 2026-04-16，6 月 1 日公布结果

---

## 深度分析

### 1. 认知科学 vs 基准测试范式

传统 AI 评估的问题:
- **MMLU/HumanEval**: 测量任务性能，不测量认知能力
- **数据污染**: 测试集可能在训练数据中
- **狭窄维度**: 只测推理/编码，忽略学习/元认知/社会认知

DeepMind 认知框架的突破:
- **人类参照**: 不是绝对分数，而是相对人类分布的位置
- **能力分解**: 从"能做什么"到"怎么做的" (过程 vs 结果)
- **可组合性**: 10 项能力的组合创造涌现行为

### 2. 5 个最大评估缺口的含义

**学习**: 当前 LLM 不会"学习" — 只是检索预训练知识
- In-context learning ≠ 真正学习
- 缺少 episodic memory 和 curriculum learning 评估
- 这恰恰是 Dupoux "Why AI Systems Don't Learn" 论文的核心

**元认知**: AI 不知道自己"不知道什么"
- 校准 (Calibration) 研究表明 LLM 过度自信
- 知道何时寻求帮助 (help-seeking) 几乎未被评估
- 对 Agent 系统至关重要: Agent 必须知道何时该停止自主行动

**注意力**: Transformer 注意力 ≠ 认知注意力
- Transformer attention 是数学操作，不是选择性认知资源分配
- 人类注意力有抑制功能 (忽略干扰) — AI 缺少这个
- 与 Context Rot 问题直接相关: 长上下文中 AI 无法有效分配注意力

**执行功能**: 规划-执行-修正循环
- LLM 擅长生成计划，不擅长执行和修正
- 缺少抑制控制: AI 不知道何时"不做某事"
- GSD (Get Shit Done) 的 Spec-Driven 方法本质上是外部化执行功能

**社会认知**: 表面模仿 vs 深层理解
- LLM 能产出"同理心"文本，但不理解社会动态
- Theory of Mind 测试结果不一致
- 多 Agent 协作需要真正的社会认知

### 3. 对 Agent 开发的直接影响

**评估框架可借鉴到 Sandbot 架构**:

| 认知能力 | Sandbot 当前实现 | 改进方向 |
|----------|-----------------|----------|
| 学习 | 知识文件积累 | 增加在线学习评估 |
| 元认知 | 缺失 | 添加"不确定性感知"模块 |
| 注意力 | 全量读取 | 优先级过滤机制 |
| 执行功能 | Cron 驱动 | 自适应任务调度 |
| 社会认知 | 基础对话 | 用户意图深度理解 |

### 4. $200K Kaggle 黑客松变现机会

**直接参赛**: 设计评估方案
- 学习赛道: 基于 Sandbot 1M+ 知识点经验设计 learning 评估
- 元认知赛道: 利用 Agent 校准研究经验

**间接价值**:
- 黑客松催生的评估工具 → 开源社区 → 咨询机会
- 认知分类框架 → Agent 设计指南 → 教程/课程

---

## 与其他趋势的交叉

### Dupoux "Why AI Don't Learn" 论文 (同期 HN)
- DeepMind 框架的"学习"维度 + Dupoux 的 System A/B/M → 互补视角
- DeepMind: 测量 AI 学习能力
- Dupoux: 解释为什么 AI 不会学习
- 结合: 用认知分类框架定位 System M 的缺失

### GSD (Get Shit Done) Spec-Driven 开发
- GSD 的 Wave Execution = 外部化"执行功能"
- 认知框架告诉我们: 不是 LLM 不够强，而是缺少执行功能的脚手架

### Unsloth Studio 本地训练
- 如果 AI 要"学习"，微调是当前最接近的路径
- Unsloth 降低微调门槛 = 降低"学习"能力的获取成本

---

## 核心洞察

1. **AGI 不是单一维度**: 10 项认知能力的组合，当前 AI 在生成/感知强，在学习/元认知/社会认知弱
2. **评估缺口 = 能力缺口**: DeepMind 选择的 5 个缺口赛道恰恰是 Agent 系统最需要的能力
3. **人类基线是关键创新**: 不是"AI 能做什么"而是"AI 相对人类在哪里"
4. **认知框架可指导 Agent 设计**: 不是堆功能，而是补齐认知能力短板

---

*创建时间: 2026-03-18 12:24 UTC*
*来源: blog.google/deepmind + arxiv*
*验证: 原文链接可访问*
