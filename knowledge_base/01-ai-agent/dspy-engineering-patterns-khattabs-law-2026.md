# DSPy 工程模式：为什么好工程师写出烂 AI 代码

**来源**: https://skylarbpayne.com/posts/dspy-engineering-patterns/
**日期**: 2026-03-23
**HN 热度**: 178 points / 105 comments
**领域**: 01-ai-agent / AI 系统工程
**质量**: ★★★★★ (深度原创，含代码演进分析)

---

## 核心论点

DSPy 月下载量 4.7M vs LangChain 222M — 这个差距很可疑。DSPy 解决的是 AI 工程中最大的痛点，但采用率低是因为它要求你**提前思考不同的抽象**，而不是让痛苦消失。

### Khattab 定律 (类 Greenspun 定律)

> "Any sufficiently complicated AI system contains an ad hoc, informally-specified, bug-ridden implementation of half of DSPy."

**翻译**: 任何足够复杂的 AI 系统，最终都包含一个临时的、非正式指定的、充满 bug 的 DSPy 半成品实现。

---

## AI 系统的 7 阶段演进 (每个团队都经历)

| 阶段 | 需求 | 你做了什么 | DSPy 等价物 |
|------|------|-----------|-------------|
| 1. Ship it | 能跑就行 | 硬编码 OpenAI 调用 | - |
| 2. 快速迭代 | 不重新部署改 prompt | Prompt 存数据库 + 管理 UI | Signature |
| 3. 格式控制 | 返回格式稳定 | Pydantic + structured outputs | Typed I/O |
| 4. 容错处理 | 处理 529/解析失败 | Retry + fallback | Module 内置 |
| 5. RAG | 模型不够聪明 | 向量搜索 + 上下文注入 | dspy.Retrieve |
| 6. 评估 | 不知道是否变好了 | 手写 eval 脚本 | dspy.Evaluate |
| 7. 换模型 | 试试 Claude | 重构全部代码 | 一行配置 |

**关键洞察**: 到第 7 阶段，你已经重新发明了 DSPy 的核心抽象，只是更差。

---

## 好工程师写烂 AI 代码的 3 个原因

### 1. 诡异的反馈循环
- 无法 step-through prompt
- 输出是概率性的
- "终于跑通了就不敢碰了"

### 2. 出货压力
- LLM 能跑起来就感觉是成就
- 干净架构感觉是奢侈品

### 3. 模糊的边界
- Prompt 既是代码又是数据
- 传统软件工程直觉失效

---

## DSPy 的 3 个核心抽象

### Signatures (签名)
```python
class CompanyExtraction(dspy.Signature):
    """Extract the company name from text."""
    text: str = dspy.InputField()
    company_name: str = dspy.OutputField()
    confidence: float = dspy.OutputField()
```
**价值**: 类型化 I/O，无需 prompt 模板。

### Modules (模块)
```python
class CompanyExtractor(dspy.Module):
    def __init__(self):
        self.retrieve = dspy.Retrieve(k=5)
        self.extract = dspy.ChainOfThought(CompanyExtraction)
    def forward(self, text):
        context = self.retrieve(text).passages
        return self.extract(text=text, context=context)
```
**价值**: 可组合、可测试、可替换的单元。

### Optimizers (优化器)
```python
optimizer = dspy.MIPROv2(metric=metric, auto="medium")
optimized = optimizer.compile(CompanyExtractor(), trainset=train_set)
```
**价值**: 自动重写 prompt + 选择示例，分离优化逻辑和执行逻辑。

---

## 对 AI Agent 开发的实战启示

### 如果用 DSPy
- 接受学习曲线，从玩具项目开始
- 核心优势：模型切换一行代码，自动 prompt 优化

### 如果不用 DSPy，偷走这些模式
1. **每个 LLM 调用都有 Typed I/O** — 用 Pydantic 定义输入输出
2. **Prompt 和代码分离** — 强制你把 prompt 当独立对象
3. **可组合单元** — 每个 LLM 调用可测试、可 mock、可链接
4. **Day 1 就建 eval 基础设施** — 你怎么知道改动有帮助？
5. **抽象模型调用** — GPT→Claude 应该是一行改动

---

## 对 Sandbot/OpenClaw 的行动项

| 行动 | 优先级 | 理由 |
|------|--------|------|
| 评估 DSPy 用于知识检索优化 | P1 | 我们的 knowledge-retriever 可用 DSPy Signature 重构 |
| 为子 Agent 添加 Typed I/O | P2 | 7 子 Agent 输入输出目前是非结构化的 |
| 建立 eval 基础设施 | P1 | 知识库质量审计需要自动化评估 |
| 模型切换抽象层 | P2 | 当前硬绑定 qwen3.5-plus |

---

## 变现洞察

- **教程机会**: "从 LangChain 迁移到 DSPy 的实战指南" — 222M vs 4.7M 下载量差距 = 巨大教育需求
- **技能机会**: OpenClaw DSPy 集成技能 — 让 Agent 系统自动优化 prompt
- **咨询机会**: 帮企业重构 AI 系统架构 — 大多数团队在阶段 3-5 挣扎

**数量**: ~580 知识点
**标签**: #DSPy #AI工程 #Prompt优化 #系统架构 #LLM抽象
