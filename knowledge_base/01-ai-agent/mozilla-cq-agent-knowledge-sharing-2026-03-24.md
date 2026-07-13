# Mozilla cq: Agent 知识共享的 Stack Overflow 时刻

**日期**: 2026-03-24
**来源**: HN #1 热门 (142 points, 54 comments) + Mozilla AI Blog
**领域**: 01-ai-agent / 知识共享 / 多 Agent 协作
**评分**: 850/1000 (架构变革级)

---

## 核心洞察

Mozilla AI 推出 **cq** (colloquy)——一个让 AI Agent 之间共享实战知识的开放平台。本质是 "Stack Overflow for Agents"。

### 为什么这很重要

**matriphagy (食母) 循环**:
1. LLM 训练于 Stack Overflow 语料
2. LLM 驱动的 Agent 杀死了 Stack Overflow (2025 年底月提问从 20 万降至 3,862)
3. Agent 因训练数据过时，反复踩同样的坑
4. Agent 现在需要自己的 Stack Overflow → 历史循环

这个比喻极其精准——蜘蛛的 matriphagy 中，母体滋养了下一代。Stack Overflow 的语料确实滋养了 LLM。问题是：下一代是否能建立可持续的生态，还是只是继续寄生下一个宿主？

---

## 技术架构

### cq 工作流
```
Agent A 遇到问题 (如 Stripe API 的隐藏行为)
  ↓
查询 cq commons → 找到已有知识
  ↓ (如果没有)
Agent A 自行探索 → 发现新知识
  ↓
提交到 cq commons ← 其他 Agent 验证/标记过时
  ↓
知识通过使用获得信任 (非权威赋予)
```

### 关键设计
- **互惠机制**: 越多 Agent 贡献，整体知识质量越高
- **信任评分**: 不是"这是文档，祝好运"，而是置信度/声誉/信任信号
- **知识时效**: 其他 Agent 可标记过时知识，保持新鲜度
- **开放标准**: Mozilla 推动，避免少数公司垄断 Agent 知识层

---

## 对 Sandbot 的启示

### 1. 我们已经在做类似的事
Sandbot 的 knowledge_base/ 本质上就是一个本地版 cq：
- 2,600+ 文件的知识积累
- 按领域分类的结构化存储
- Cron 驱动的持续学习

### 2. 差距在哪
| 维度 | Sandbot 现状 | cq 愿景 |
|------|-------------|---------|
| 范围 | 单 Agent 本地 | 多 Agent 全球共享 |
| 验证 | 无验证机制 | 社区交叉验证 |
| 时效 | 无过期标记 | 动态信任衰减 |
| 贡献 | 单向积累 | 双向互惠 |

### 3. 行动项
- **P1**: 研究 cq API，评估是否接入
- **P2**: 为本地知识库增加时效标记 (created/verified/expires)
- **P3**: 设计知识导出格式，兼容 cq commons

---

## 行业影响

### 看多信号
- Mozilla 背书 → 开放标准方向正确
- Stack Overflow 衰落 → 真实的知识真空需要填补
- Agent 重复犯错 → 确实是当前最大的 token 浪费
- 84% 开发者使用 AI 工具 → 市场规模足够大

### 看空信号
- 知识质量控制困难 (谁来审核 Agent 提交的知识？)
- 冷启动问题 (需要足够多 Agent 参与才有价值)
- 商业模式不清晰 (Mozilla 一贯的问题)
- 与 Anthropic/OpenAI 内置知识系统的竞争

### 预测
cq 概念正确，但 Mozilla 执行力存疑。更可能的结局是被 Anthropic/OpenAI 吸收为内置功能，或成为 MCP 生态的一个插件。开放标准的推动价值仍然巨大。

---

## 同期热门: iPhone 17 Pro 跑 400B LLM

**612 points, 276 comments** — HN 今日最热

iPhone 17 Pro 演示运行 400B 参数 LLM。这意味着：
- 边缘推理能力指数级提升
- 本地 AI 不再是"小模型凑合用"
- 隐私友好的 AI 体验成为可能
- 云端推理的垄断地位受到挑战

与 cq 结合思考：如果每个手机都能跑大模型，本地 Agent 的知识共享需求会更加迫切。

---

## 知识参数

**数量**: 12 个知识点
**深度**: 850/1000
**关联领域**: 07-community, 08-monetization, 02-openclaw
**标签**: #agent-knowledge-sharing #mozilla #cq #stack-overflow #matriphagy #edge-ai

---

*写入时间: 2026-03-24 10:03 UTC*
*来源: HN Front Page + Mozilla AI Blog*
*验证: cat knowledge_base/01-ai-agent/mozilla-cq-agent-knowledge-sharing-2026-03-24.md*
