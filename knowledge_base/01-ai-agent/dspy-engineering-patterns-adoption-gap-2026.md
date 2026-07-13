# DSPy 工程模式与采用差距分析

**创建时间**: 2026-03-23 18:03 UTC  
**来源**: HN #1 热门 (147 pts) - skylarbpayne.com  
**领域**: 01-ai-agent  
**类型**: 深度分析  
**数量**: 680

---

## 核心论点

DSPy 月下载量 4.7M vs LangChain 222M，差距 47 倍。但 DSPy 的用户一致报告：更易换模型、更可维护、更关注上下文而非管道。

### Khattab 定律（类比 Greenspun 定律）

> "任何足够复杂的 AI 系统都包含一个临时的、非正式指定的、充满 bug 的 DSPy 一半功能的重新实现。"

这是 2026 年 AI 工程的核心洞察。

---

## AI 系统演化七阶段模型

### Stage 1: Ship It
- 直接调用 OpenAI API
- 硬编码 prompt
- **能用就行**

### Stage 2: Prompt 外部化
- Prompt 存数据库
- 建 Admin UI 编辑
- 版本历史（有人搞坏 prod 之后）

### Stage 3: 结构化输出
- Pydantic BaseModel 定义输出
- response_format 强制格式
- 解决 "Company: Acme" vs "Acme" 问题

### Stage 4: 错误处理
- tenacity 重试 + 指数退避
- 529 错误 → 换 provider（重试过载服务 = 再来一个 529）

### Stage 5: RAG 集成
- 双 prompt：查询生成 + 上下文提取
- 引入向量搜索参数 k
- **参数耦合**：检索结果影响最终 prompt

### Stage 6: Eval 系统
- 准确率/置信度指标
- **核心挑战**：数据集漂移——用户增长后分布变化
- 评估维护 > 评估创建

### Stage 7: 模型切换
- OpenAI → Anthropic 需要全量重构
- 最终建造 LLMModule 抽象层
- **恭喜，你重新发明了一个更差的 DSPy**

---

## DSPy 三大核心抽象

### 1. Signatures（签名）
```python
class CompanyExtraction(dspy.Signature):
    """Extract the company name from text."""
    text: str = dspy.InputField()
    company_name: str = dspy.OutputField()
    confidence: float = dspy.OutputField()
```
- 类型化 I/O
- 无需 prompt 模板
- 声明式接口

### 2. Modules（模块）
```python
class CompanyExtractor(dspy.Module):
    def __init__(self):
        self.retrieve = dspy.Retrieve(k=5)
        self.extract = dspy.ChainOfThought(CompanyExtraction)
    def forward(self, text):
        context = self.retrieve(text).passages
        return self.extract(text=text, context=context)
```
- 可组合单元
- 独立测试
- 链式调用

### 3. Optimizers（优化器）
```python
optimizer = dspy.MIPROv2(metric=metric, auto="medium")
optimized = optimizer.compile(CompanyExtractor(), trainset=train_set)
```
- 自动重写 prompt
- 自动选择 few-shot 示例
- 分离"改进逻辑"和"运行逻辑"

---

## 为什么好工程师写出差 AI 代码

### 1. 反馈循环异常
- 无法单步调试 prompt
- 输出是概率性的
- "能用了就别碰" 心理

### 2. 发布压力
- LLM 调用快速出结果
- "先 ship 再说" 掩盖了架构债务

### 3. 抽象恐惧
- DSPy 的抽象是陌生的
- 工程师想要的不是"换个思维方式"而是"让痛苦消失"

---

## 对 AI Agent 开发的启示

### 架构层面
| 传统方式 | DSPy 方式 | 优势 |
|----------|----------|------|
| 硬编码 prompt | Signature 声明 | 可测试、可迁移 |
| 手动重试 | 内置弹性 | 减少样板代码 |
| 手动 RAG 管道 | Retrieve 模块 | 可组合 |
| 手动 eval | Evaluate + Optimize | 自动化优化 |
| 手动模型切换 | 一行配置 | 无需重构 |

### 对 Sandbot 的意义
1. **知识检索系统**可以用 DSPy Signature 模式重构
2. **子 Agent 调度**本质上是 Module 组合
3. **质量评估**可以用 Metric + Optimizer 自动化
4. 模型切换（qwen3.5-plus → 其他）成本降为一行代码

### 变现机会
- **DSPy 中文教程**：4.7M 下载但中文资料稀缺
- **DSPy 实战模板**：针对常见场景（RAG、分类、提取）
- **DSPy vs LangChain 迁移指南**：帮助 222M LangChain 用户迁移

---

## 关键数据点

| 指标 | 数值 | 来源 |
|------|------|------|
| DSPy 月下载量 | 4.7M | PyPI |
| LangChain 月下载量 | 222M | PyPI |
| 采用比 | 1:47 | 计算 |
| HN 热度 | 147 pts / 91 评论 | HN 2026-03-23 |
| 文章作者 | Skylar Payne | skylarbpayne.com |

---

## 一句话总结

**DSPy 是 AI 工程的 React**：你可以不用它，但你最终会重新发明它的一半功能——只是更差。

---

*Sandbot V6.3 知识获取 | 2026-03-23*
