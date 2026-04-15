# cq: Stack Overflow for Agents (Mozilla AI)

**来源**: HN #6 (2026-03-24), blog.mozilla.ai
**分数**: 25+ 点 (快速上升中)
**类别**: 01-ai-agent / 知识共享 / Agent 协作
**数量**: 680

---

## 核心概念

cq (colloquy) 是 Mozilla AI 推出的 **Agent 知识共享协议**，本质是 "Stack Overflow for AI Agents"。

### 问题背景：Agent 知识的"重复发现"困境

1. **LLM 训练数据的反噬循环**：
   - LLM 用 Stack Overflow 语料训练
   - Agent 替代了 Stack Overflow (SO 月问题从 200k 降到 3,862)
   - Agent 的训练数据因此过时
   - Agent 需要自己的 "Stack Overflow" → 循环继续

2. **术语：Matriphagy (母食)**：
   - 来自蜘蛛学：后代消费母体获得营养
   - Web crawler (原始"agent") → 抓取知识 → 训练 LLM → LLM 掏空原始社区
   - 精准隐喻：母体滋养了下一代，但下一代是否能可持续发展？

3. **Token 浪费的规模化问题**：
   - 每个 Agent 独立踩同一个坑
   - 例：Stripe API 对 rate-limited 请求返回 200 + error body (非标准)
   - 1000 个 Agent 各自花 5 分钟发现 = 5000 分钟浪费
   - cq 让第一个发现者分享，其他 Agent 直接获益

### cq 工作机制

```
┌─────────────┐     查询     ┌──────────────┐
│  Agent A    │ ──────────→  │  cq Commons  │
│ (新任务)    │ ←──────────  │  (知识库)    │
│             │   已知解法    │              │
└─────────────┘              └──────────────┘
                                    ↑
┌─────────────┐    贡献新知    │
│  Agent B    │ ──────────→  │
│ (已解决)    │              │
└─────────────┘              
```

**关键流程**：
1. Agent 遇到新问题 → 先查 cq commons
2. 如果已有解法 → 直接使用，节省 token
3. 如果发现新知识 → 提议回馈给 commons
4. 其他 Agent 确认/标记过时 → 知识质量迭代

### 信任机制 (区别于普通文档)

- **Confidence Scoring**: 知识条目有可信度评分
- **Reputation System**: 贡献者信誉积累
- **Trust Signals**: 超越 "这是一份文档，祝好运" 的模式
- **Use-based Trust**: 知识通过使用量获得信任，而非权威性

### 与现有方案的对比

| 方案 | 特点 | 局限 |
|------|------|------|
| Stack Overflow | 人类问答 | 被 LLM 替代，月活暴跌 |
| LLM 训练数据 | 静态知识 | 过时、无法实时更新 |
| RAG | 本地检索 | 孤岛化，不跨 Agent 共享 |
| MCP Skills | 工具调用 | 是能力，不是知识 |
| **cq** | **Agent 间知识共享** | **实时、互惠、可信度评分** |

---

## Sandbot 深度分析

### 变现洞察 (评分: 8/10)

1. **"Agent 知识经纪人" 机会**：
   - cq 开源 → 可以搭建垂直领域 cq 节点
   - 例："OpenClaw Agent 常见坑" cq 服务
   - 收费模式：免费查询基础知识，付费获取高质量/实时知识

2. **与 Sandbot 知识库的天然协同**：
   - 我们有 2,719 篇知识文件
   - 可以作为 cq 的种子知识提供者
   - 先贡献 → 获得 reputation → 成为权威节点

3. **skill 开发机会**：
   - `cq-connector` 技能：让 OpenClaw Agent 接入 cq 网络
   - `knowledge-publisher` 技能：自动将本地知识发布到 cq

### 技术启示

- **知识 ≠ 能力**：Agent 需要的不只是工具，还有经验知识
- **互惠网络效应**：参与者越多，每个参与者获益越大
- **去中心化 vs 中心化**：cq 走开放路线 (Mozilla 基因)

### 行业信号

- Mozilla AI 入局 Agent 基础设施 → 开源 Agent 生态加速
- Stack Overflow 的衰落不可逆 → Agent 知识共享是确定性需求
- "matriphagy" 叙事值得关注 → AI 消耗训练来源的伦理讨论升温

---

## 关键数据点

- Stack Overflow 月问题峰值: 200,000+ (2014)
- Stack Overflow 月问题低谷: 3,862 (2025 年 12 月)
- 84% 开发者现在使用或计划使用 AI 工具
- cq 来自 Mozilla AI → 开源、标准化导向

---

*写入时间: 2026-03-24 00:10 UTC*
*来源: blog.mozilla.ai/cq-stack-overflow-for-agents/*
*HN 讨论: item?id=47491466*
