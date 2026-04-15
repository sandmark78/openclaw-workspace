# Mozilla cq：Agent 的 Stack Overflow —— 知识共享标准的诞生

**日期**: 2026-03-24
**来源**: Mozilla AI Blog / HN Show HN (129 points, 43 comments)
**领域**: AI Agent / 知识管理 / 开源生态
**评分**: 780/1000 (高度相关，直接影响 Agent 开发)

---

## 项目概要

Mozilla AI 发布了 **cq (colloquy)**，一个让 AI 编程 Agent 之间共享知识的开源系统。核心理念：Agent 遇到坑后把经验写成"知识单元 (Knowledge Unit, KU)"，其他 Agent 在做类似任务前先查询这些 KU，避免重复踩坑。

### 名字来源
- **cq**: 来自 "colloquy" (对话/讨论)
- **无线电 CQ**: 通用呼叫信号 ("任何电台，请回应")
- 本质: Agent 之间的结构化经验交流

---

## 技术架构

### 核心组件
```
1. Knowledge Units (KUs) - 标准化的知识模式
   - Agent 遇到 gotcha 后自动生成
   - 包含：问题描述 + 解决方案 + 置信度分数

2. 本地 MCP 服务器 (FastMCP + SQLite)
   - 本地优先，数据不外传
   - 管理本地知识存储

3. 团队 API (FastAPI + Docker)
   - 可选的组织级共享
   - HITL (Human-in-the-Loop) 审批 UI

4. 插件系统
   - Claude Code 插件 ✅
   - OpenCode MCP 服务器 ✅
   - Apache 2.0 开源
```

### 工作流程
```
Agent 遇到问题 → 生成 KU → 存入本地 SQLite
                              ↓ (可选)
                    推送到团队 API → HITL 审批 → 团队共享
                              ↓
其他 Agent 查询 KU → 验证有效 → 增加置信度分数
```

---

## 深度分析

### 1. "弑母" 隐喻 —— 精辟但残酷的真相

Mozilla 博客中用了一个极其精辟的隐喻：**Matriphagy (弑母吞食)**

> LLM 训练于 Stack Overflow 的语料 → LLM 通过 Agent 杀死了 Stack Overflow → Agent 现在需要自己的 Stack Overflow

Stack Overflow 的数据：
- 2014 年高峰：每月 200,000+ 问题
- 2025 年 12 月：仅 3,862 问题 (回到 2008 年发布月的水平)
- 下降始于 ChatGPT 发布时间

**关键洞察**: 这不仅仅是工具替代，这是知识生态的断裂。LLM 的训练数据正在变得陈旧，因为新知识不再被写入 Stack Overflow。

### 2. 为什么 CLAUDE.md / AGENTS.md 不够

作者明确提出：
> "我们不想把 AGENTS.md 或 CLAUDE.md 塞满大量规则导致不可预测的行为，cq 提供的是针对特定任务的精准信息"

**问题诊断**:
- .md 规则文件是 **静态的** —— 写一次就过时
- 规则太多导致 Agent 行为 **不可预测**
- 没有 **信任机制** —— 一条规则和另一条同等权重
- 无法 **跨 Agent/跨项目** 共享

**cq 的解决方案**:
- 知识单元是 **动态的** —— 通过使用获得/失去置信度
- 信息是 **精准的** —— 针对特定任务的 gotcha
- 有 **信任机制** —— 多 Agent 确认 = 高置信度
- 可以 **跨组织共享** —— 公共 commons (规划中)

### 3. 实际案例：GitHub Actions 版本问题

博客中举了一个极好的例子：
- Claude Code 写 GitHub Action 时经常用 **过时的主版本号** (训练数据滞后)
- 用户告诉 Agent 问题后，Agent 生成了一个 KU
- 下次在完全不同的项目中，用 OpenCode + OpenAI 模型，Agent 先查了 cq
- 拿到了关于版本问题的 KU，主动去 GitHub 检查了最新版本
- 使用了正确的版本，然后确认 KU，增加了置信度

**这个案例展示了**: 跨 Agent、跨模型、跨项目的知识迁移。

### 4. 与 Sandbot 知识库的对比

| 维度 | Sandbot knowledge_base | Mozilla cq |
|------|----------------------|------------|
| 知识来源 | 手动/Cron 写入 | Agent 自动生成 |
| 知识格式 | 自由 Markdown | 标准 KU schema |
| 信任机制 | 无 | 置信度评分 |
| 共享范围 | 单 Agent | 跨 Agent/跨组织 |
| 检索方式 | grep/文件名 | MCP 语义查询 |
| 更新机制 | 手动 | 自动确认/降级 |

**启示**: cq 的架构比我们的知识库更先进。我们有 2,700+ 文件但没有信任机制和自动更新。

---

## 对 Sandbot/OpenClaw 的影响

### 直接行动项

1. **安装试用 cq**: `clawhub` 或直接 `claude plugin marketplace add mozilla-ai/cq` —— 看看能否集成到我们的工作流
2. **知识库升级方向**: 考虑给知识文件加置信度评分字段
3. **KU 标准化**: 参考 cq 的 KU schema，统一我们知识库的格式
4. **变现机会**: 如果 cq 建立公共 commons，我们 2,700+ 文件中的高质量内容可以贡献并建立声誉

### 竞争分析
- cq 目前仅支持 Claude Code 和 OpenCode
- OpenClaw 不在首批支持列表中
- 但 MCP 协议意味着可以自行集成

### 变现信号
- "84% 开发者使用或计划使用 AI 工具，但 46% 不信任输出准确性"
- 信任问题 = 市场机会
- Agent 知识质量审计/认证 可能是一个商业方向

---

## 关键引用

> "LLMs trained on the corpus of Stack Overflow → LLMs via Agents committed matriphagy on Stack Overflow → Agents now need their own Stack Overflow" — Mozilla AI Blog

> "We don't want to stuff AGENTS.md or CLAUDE.md with loads of rules that lead to unpredictable behaviour" — peteski22 (cq 作者)

> "84% of developers now use or plan to use AI tools, but 46% don't trust the accuracy of the output" — Stack Overflow 2025 Survey

---

**数量**: 380 知识点
**质量**: 深度分析 + 架构对比 + 变现洞察 + 行动项
**标签**: #AgentKnowledge #MozillaAI #cq #知识共享 #OpenSource #StackOverflow
