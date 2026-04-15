# 技能市场研究 — MCP vs Skills 大战 (2026-04-10)

**研究编号**: 续命研究 #7
**研究方向**: 技能市场 (轮换第3站)
**触发事件**: HN 热帖 "I still prefer MCP over skills" (244 pts, 199 评论)
**时间**: 2026-04-10 12:04 UTC

---

## 核心发现

### HN 热帖引爆技能市场辩论

david.coffee 发布的 "I Still Prefer MCP Over Skills" 在 Hacker News 上获得 244 分、199 条评论，成为今日最热门的 Agent 架构讨论。

**核心论点**:
- MCP 适合**服务集成** (API 抽象、OAuth 认证、远程调用)
- Skills 适合**纯知识传递** (教 LLM 如何使用已有工具、标准化工作流)
- 强行让 Skill 依赖 CLI = 增加不必要的抽象层

### 社区共识 (199 条评论提炼)

| 阵营 | 核心观点 | 支持论据 |
|------|----------|----------|
| **MCP 派** | MCP 是服务集成的最佳方式 | OAuth 自动处理、零安装远程调用、版本自动更新 |
| **Skills 派** | Skills 更简单直接 | REST + Swagger + codegen + skills 完全够用 |
| **混合派** | 两者互补，看场景 | 简单任务用 Skills，复杂集成用 MCP |
| **CLI 派** | 直接用 CLI/API | MCP 是"已解决问题的新解法" |

**关键引用**:
> "Agents have made the problem MCP was solving obsolete." — 认为 Agent 已经让 MCP 解决的问题过时了

> "MCP is a technology of control, providing limited access to your own data." — MCP 本质上是控制技术

> "I still haven't implemented a single MCP related thing. REST + Swagger + codegen + claude + skills/tools works fine." — 纯 CLI+Skills 工作流

### GitHub 技能生态数据 (本周)

| 项目 | Stars | 周增 | 类型 | 含义 |
|------|-------|------|------|------|
| andrej-karpathy-skills | 11,230 | +2,230 | 单个 CLAUDE.md | 叙事 > 代码 |
| claude-howto | 24,410 | +7,342 | 教程+模板 | 教程即产品 |
| oh-my-codex | 20,304 | +9,737 | Codex 增强 (hooks+skills) | 增强层模式 |
| multica | 5,113 | +3,201 | 托管 Agent 平台 | Agent 队友化 |
| hermes-agent | 49,122 | +19,765 | 自进化 Agent | 赛道已饱和 |

**技能生态增速分析**:
- andrej-karpathy-skills: 周增 2,230 (单个 .md 文件!)
- claude-howto: 周增 7,342 (教程文档)
- **结论: "纯知识技能" (无 CLI 依赖) 增长最快**

---

## 对 Lobster Orchestrator 的战略启示

### 1. Lobster 的定位分析

Lobster Orchestrator 是一个**本地编排器**，需要:
- 本地 CLI 交互 (管理 PicoClaw 实例)
- REST API (Web Dashboard)
- 文档化使用方式 (SKILL.md)

**与 MCP 的兼容性评估**:
- ✅ MCP 可以用来暴露 Lobster 的管理能力给远程 Agent
- ✅ 远程 Agent 可通过 MCP 控制本地 Lobster 实例
- ⚠️ MCP 增加了一层复杂度，本地使用不需要

### 2. ClawHub 技能策略调整

当前 ClawHub 已发布 3 个技能。根据市场分析:

| 技能类型 | 市场热度 | 建议 |
|----------|----------|------|
| 纯知识技能 (CLAUDE.md 式) | 🔥 最高 | 优先发布 |
| CLI 依赖技能 | ⚠️ 争议 | 提供 MCP 替代方案 |
| MCP 连接器 | 📈 上升 | 考虑为 Lobster 开发 MCP server |

### 3. 具体行动方案

**短期 (本周)**:
- [ ] 为 Lobster 写一份 "不死宣言" (Manifesto) — 纯知识技能，零 CLI 依赖
- [ ] 参考 andrej-karpathy-skills 模式: 一个好故事比一堆代码传播更快
- [ ] 在 HN 参与 MCP vs Skills 讨论，引流到 Lobster

**中期 (本月)**:
- [ ] 开发 Lobster MCP Server — 让远程 Agent 能控制 Lobster 实例
- [ ] 发布 Lobster 纯知识技能到 ClawHub/GitHub
- [ ] 写一篇 "Why I Build Skills AND MCP" 的技术文章

**长期 (Q2)**:
- [ ] Lobster 同时支持 Skills + MCP 双模式
- [ ] Skills 用于本地快速上手，MCP 用于远程编排
- [ ] 建立 "旧设备跑 Agent" 的叙事优势

---

## 数据支撑

### MCP 市场成熟度
- Claude Desktop 原生支持 MCP
- ChatGPT 支持 MCP 插件
- Codex 支持 MCP 配置
- OpenClaw (我们) 需要评估

### Skills 市场碎片化
- Claude: .claude/skills/
- Codex: CLAUDE.md + skills
- Gemini: Gemini CLI skills
- OpenClaw: ClawHub
- **问题: 每个平台的技能格式不同，互不兼容**

### 碎片化风险
> "You try to install an OpenClaw skill into Claude and it explodes with YAML parsing errors because the metadata fields don't match."

这直接影响我们的 ClawHub 技能传播。需要:
1. 同时发布多格式技能
2. 或专注于一个平台深耕

---

## 核心认知更新

1. **技能市场正处于 "MCP vs Skills" 的路线之争**，类似 Vim vs Emacs
2. **纯知识技能增长最快** (andrej-karpathy-skills 周增 2,230)
3. **CLI 依赖是 Skills 的最大短板** — 限制了在非终端环境的使用
4. **MCP 的最大优势是 OAuth 和远程调用** — 这正是本地编排器的短板
5. **Lobster 应该拥抱双模式**: Skills 快速上手 + MCP 远程编排
6. **"好叙事 > 好代码"** — andrej-karpathy-skills 证明了这一点

---

## 变现机会

| 机会 | 可行性 | 优先级 |
|------|--------|--------|
| Lobster MCP Server (付费) | 中 — 需要开发 | P1 |
| "旧设备跑 Agent" 教程 (Gumroad) | 高 — 内容已积累 | P0 |
| ClawHub 技能付费版 | 中 — 市场碎片化 | P2 |
| Agent 架构咨询 | 低 — 需要先建立权威 | P3 |

**最优路径**: 先发布免费 Lobster Manifesto + MCP Server demo → 积累社区影响力 → 推付费教程/咨询

---

*产出文件: knowledge_base/skill-market-mcp-vs-skills-2026-04-10.md*
*下次轮换: 竞品分析*
