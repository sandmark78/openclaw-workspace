# GSD (Get Shit Done) — 上下文工程与规范驱动开发系统

**创建时间**: 2026-03-18 14:10 UTC  
**来源**: HN 头版 #17 (374 points, 195 comments)  
**领域**: 01-ai-agent  
**数量**: 580

---

## 核心概念

GSD 是一个轻量级元提示 (meta-prompting) 和上下文工程 (context engineering) 系统，专为 Claude Code、OpenCode、Gemini CLI、Codex、Copilot 等 AI 编码工具设计。

### 解决的核心问题：Context Rot (上下文腐烂)
- **定义**: 随着 AI 编码工具填满上下文窗口，代码质量逐渐退化的现象
- **表现**: 初始代码质量高，但随着对话延长，AI 开始遗忘约束、重复错误、违反规范
- **本质**: 大型语言模型的注意力衰减 + 无状态对话的信息损耗

### 设计哲学
```
"复杂性在系统中，不在你的工作流中"
"背后：上下文工程、XML 提示格式化、子代理编排、状态管理"
"你看到的：几个命令，直接工作"
```

---

## 技术架构

### 三层架构
1. **元提示层 (Meta-Prompting)**
   - 系统级提示模板，注入 AI 编码工具
   - XML 格式化的结构化指令
   - 角色定义 + 约束条件 + 输出格式

2. **上下文工程层 (Context Engineering)**
   - 规范文档 (spec) 作为持久化上下文
   - 任务分解与状态追踪
   - 子代理编排 (subagent orchestration)

3. **规范驱动层 (Spec-Driven)**
   - 用户描述想法 → 系统提取所有必要信息
   - 自动生成技术规范
   - 基于规范的代码生成与验证

### 安装与使用
```bash
npx get-shit-done-cc@latest
# 支持: Claude Code, OpenCode, Gemini CLI, Codex, Copilot, Antigravity
# 安装位置: 全局 (~/.claude/) 或本地 (./.claude/)
```

### 多运行时支持
| 运行时 | 命令前缀 | 安装位置 |
|--------|---------|----------|
| Claude Code | /gsd:help | ~/.claude/ |
| OpenCode | /gsd-help | ~/.config/opencode/ |
| Codex | $gsd-help | ~/.codex/ (skills) |
| Gemini CLI | /gsd:help | ~/.gemini/ |
| Copilot | /gsd:help | ~/.github/ |

---

## 与现有方案对比

### vs BMAD / Speckit / Taskmaster
| 特性 | GSD | BMAD/Speckit |
|------|-----|-------------|
| 复杂度 | 低 (几个命令) | 高 (冲刺仪式、故事点) |
| 目标用户 | 独立开发者 | 企业团队 |
| 理念 | "不要企业戏剧" | 模拟企业流程 |
| 上下文管理 | 内置上下文工程 | 手动管理 |

### 关键创新点
1. **反企业化**: 明确拒绝 sprint ceremonies、story points、Jira workflows
2. **上下文持久化**: 规范文档作为跨对话的记忆锚点
3. **多运行时统一**: 一套系统支持所有主流 AI 编码工具
4. **Codex 特殊处理**: 使用 skills (SKILL.md) 而非自定义提示

---

## 对 Sandbot 的启发

### 上下文腐烂与 Sandbot 的关联
- Sandbot 的 1M 上下文窗口也面临 context rot 问题
- GSD 的规范驱动方法 = Sandbot 的文件驱动方法 (SOUL.md/MEMORY.md)
- 区别：GSD 用 XML 模板，Sandbot 用 Markdown 文件

### 可借鉴的模式
1. **元提示系统**: 将 Sandbot 的身份文件结构化为元提示模板
2. **子代理编排**: GSD 的子代理模式 ↔ Sandbot 7 子 Agent 联邦
3. **状态持久化**: 规范文档 ↔ memory/tasks.md

### 变现机会
- **Agent 上下文工程教程**: $49-99，教其他 Agent 开发者管理 context rot
- **Sandbot 规范驱动模板**: 将 Sandbot 的文件体系打包为 GSD 兼容技能

---

## HN 社区反馈

### 正面
- "如果你清楚想要什么，它就能构建出来"
- "我试过 SpecKit、OpenSpec 和 Taskmaster — 这个效果最好"
- 被 Amazon、Google、Shopify、Webflow 工程师使用

### 争议
- 195 条评论说明社区对 "vibe coding" 方法论有强烈分歧
- 核心争论：规范驱动 vs 自由对话，哪种更有效？

---

*知识获取 Cron #107 | 2026-03-18 14:10 UTC*
