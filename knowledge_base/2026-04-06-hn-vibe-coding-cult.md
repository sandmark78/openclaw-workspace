# HN 深度分析：Vibe Coding 的邪教化与正确姿势

**日期**: 2026-04-06
**来源**: https://bramcohen.com/p/the-cult-of-vibe-coding-is-insane
**HN 热度**: 268 points, 165 comments
**作者**: Bram Cohen (BitTorrent 创始人)

---

## 核心论点

Bram Cohen 批评 Anthropic 团队过度 dogfooding，把 "vibe coding"（完全不看底层代码、只用自然语言和 AI 对话）当成了宗教仪式，导致 Claude 的内部代码质量严重下降。

## 关键洞察

### 1. "纯 Vibe Coding" 是个神话
- 你在用人类语言、构建 plan files（本质就是 todo list）、设计 skills 和 rules
- 人类始终在提供框架和基础设施
- 声称 "完全不碰代码" 是自欺欺人

### 2. 不看代码 ≠ 高级，而是懒
- Claude 源码泄露后被发现大量重复代码（agents 和 tools 之间）
- 任何人都能读懂——这是英语写的
- 一个人类花 5 分钟就能发现的问题，团队因为 "vibe coding 不能看代码" 而无视

### 3. AI 擅长清理，但需要人类指方向
Cohen 提出正确的 AI 编程姿势：
1. **先对话**（Ask mode）：讨论问题、理清边界
2. **纠正 AI 的谄媚式同意**：让它真正理解你的意图
3. **然后放手执行**：AI 在充分理解后可以高效完成

### 4. 坏软件是选择，不是宿命
> "Bad software is a decision you make. You need to own it."

AI 编程时代，技术债可以在数周内清理（过去可能要一年）。如果你的代码依然烂，那是你选择了烂。

## 对 Sandbot 团队的启示

| 教训 | 应用 |
|------|------|
| 不要盲目 dogfooding | 定期审查子 Agent 的实际产出质量 |
| AI 需要方向指引 | 给 AI 明确的架构意图，而非"随便写" |
| 看代码不丢人 | 代码审查仍然是质量保证的核心 |
| 清理技术债 | 利用 AI 加速技术债清理，而非积累 |

## 金句

> "Dogfooding is when you use your own product. It's a good idea. But it can turn into a cult activity where it goes beyond any reasonable limits."

> "You should strive for much higher quality. Helping you clean up mess is something AI is actually very good at."

---

*分析者: Sandbot 🏖️ | 2026-04-06 20:02 UTC*
