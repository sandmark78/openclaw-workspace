# cq: Mozilla AI 的 "Agent Stack Overflow" — 知识共享协议

**来源**: https://blog.mozilla.ai/cq-stack-overflow-for-agents/
**日期**: 2026-03-23
**领域**: 01-ai-agent
**数量**: 680
**质量**: 深度分析 (原文 + 批判 + 行动项)

---

## 核心洞察

### 1. Stack Overflow 的消亡与 Agent 知识共享的诞生

**数据点**:
- Stack Overflow 2014 年巅峰: 200,000 问题/月
- 2025 年 12 月: 仅 3,862 问题 (回到 2008 年发布月水平)
- 84% 开发者使用或计划使用 AI 工具
- 但 46% 不信任 AI 输出准确性 (比前一年 31% 上升)

**Matriphagy (弑母食母) 隐喻**:
```
LLM 训练于 Stack Overflow 语料
→ LLM/Agent 杀死了 Stack Overflow
→ Agent 孤立地重复遇到相同问题 (训练数据陈旧)
→ Agent 现在需要自己的 Stack Overflow
→ 循环继续
```

这是技术史的经典模式: 技术 X 消灭了前代技术 Y，然后需要重新发明 Y 的核心功能。

### 2. cq 系统架构

**名称由来**: colloquy (结构化思想交换) + 无线电 CQ 呼叫 (任何站点请回应)

**工作流**:
1. Agent 遇到不熟悉的任务前，查询 cq commons
2. 如果其他 Agent 已学到相关知识 (如 "Stripe 对限流请求返回 200+错误体")，直接获取
3. Agent 发现新知识时，提议回馈到 commons
4. 其他 Agent 确认有效知识，标记过时知识
5. 知识通过**使用**而非**权威**获得信任

**已实现组件**:
- Claude Code 和 OpenCode 插件
- MCP server 管理本地知识存储
- 团队 API 用于组织内共享
- Human-in-the-loop 审查 UI
- Docker 容器化部署

### 3. 与 OpenClaw/Sandbot 的关联

**直接对标**:
- cq 的 "knowledge units" ≈ Sandbot 的 knowledge_base/ 文件
- cq 的 "trust scoring" ≈ Sandbot 的优先级评分系统
- cq 的 "agent commons" ≈ ClawHub 的技能共享

**差异与机会**:
| 维度 | cq (Mozilla) | Sandbot |
|------|-------------|---------|
| 知识粒度 | 单个 knowledge unit | 完整 .md 文件 |
| 信任机制 | 多 Agent 使用确认 | 人工审查 |
| 共享范围 | 跨组织 commons | 本地 + ClawHub |
| 标准化 | 开放提案中 | 自有格式 |
| 集成方式 | MCP server | 文件系统 |

**行动项**: 
- 关注 cq 的知识格式标准，可能适配 Sandbot 知识库
- cq 的 MCP server 模式值得 OpenClaw 参考
- "知识通过使用获得信任" 是比 "人工审查" 更可扩展的模式

### 4. 更深层的问题

**Andrew Ng 也在问同样的问题**: 2026 年 3 月 DeepLearning.AI 也发文讨论 "是否应该有 Agent 版 Stack Overflow"，说明这是行业共识。

**Mozilla 的开放立场**: 
- 强调不应让少数大公司决定 AI 技术使用方式
- 类比浏览器标准化历程
- "当前 .md 文件 + 希望 Agent 遵守的方式只能走这么远" — 直接批判了 CLAUDE.md / AGENTS.md 的局限性

**批判性思考**:
- cq 的成功取决于网络效应 — 需要足够多 Agent 参与才有价值
- 知识质量验证仍是开放问题: 多 Agent 确认 ≠ 正确
- 与 MCP 的关系: cq 用 MCP 作为传输层，但核心是知识协议而非工具协议

---

## 变现洞察

| 机会 | 评分 | 理由 |
|------|------|------|
| 为 cq 贡献 OpenClaw 知识 | 7/10 | 品牌曝光 + 生态参与 |
| 开发 cq-to-knowledge-base 适配器 | 6/10 | 技术深度 + 社区贡献 |
| 写 "cq vs 传统知识管理" 对比分析 | 8/10 | 内容变现 + 思想领导力 |

---

*写入时间: 2026-03-24 02:08 UTC*
*Cron #106 深度内容*
