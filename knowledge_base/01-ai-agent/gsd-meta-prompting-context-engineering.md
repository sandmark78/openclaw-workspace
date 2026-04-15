# Get Shit Done (GSD) - 元提示词与上下文工程系统

**创建时间**: 2026-03-18 12:03 UTC  
**来源**: HN #18 (355 points, 181 comments) + GitHub  
**领域**: 01-ai-agent  
**数量**: 580

---

## 核心概念

GSD 是一个轻量级但强大的**元提示词(meta-prompting)**、**上下文工程(context engineering)**和**规格驱动开发(spec-driven dev)**系统，专为 Claude Code / OpenCode / Gemini CLI / Codex / Copilot / Antigravity 等 AI 编码工具设计。

### 解决的核心问题：Context Rot (上下文腐烂)
- **定义**: 随着 Claude 填满上下文窗口，输出质量逐渐下降
- **症状**: 代码不一致、忘记先前约定、重复错误
- **GSD 方案**: 通过结构化的上下文工程层保持质量一致性

---

## 技术架构

### 三层设计
```
用户层:    简单命令 (gsd:help, gsd:init)
├─ 隐藏层: XML 提示词格式化 + 子 Agent 编排 + 状态管理
└─ 执行层: Claude Code / OpenCode / Gemini 等运行时
```

### 核心理念
1. **复杂度内化**: "The complexity is in the system, not in your workflow"
2. **反企业剧场**: 不要冲刺仪式、故事点、利益相关者同步
3. **规格驱动**: 描述想法 → 系统提取所需信息 → AI 执行
4. **无摩擦自动化**: 推荐 `--dangerously-skip-permissions` 模式

### 安装方式
```bash
npx get-shit-done-cc@latest
# 支持全局或本地安装
# 支持多运行时: Claude Code, OpenCode, Gemini, Codex, Copilot, Antigravity
```

---

## 与 Sandbot 对比分析

| 维度 | GSD | Sandbot V6.2 |
|------|-----|-------------|
| **目标用户** | Solo 开发者 | 知识工作者/团队 |
| **核心方法** | 元提示词+规格驱动 | 联邦子 Agent+知识库 |
| **上下文管理** | 防止 Context Rot | 1M 上下文充分利用 |
| **质量保障** | 内置验证循环 | Auditor 子 Agent 审计 |
| **工作流** | 反企业化 | ROI 驱动 |

### 可借鉴之处
1. **Context Rot 概念**: 我们也面临长上下文质量衰减问题
2. **XML 提示词格式**: 结构化提示词可能提升子 Agent 指令精度
3. **规格提取**: 自动从模糊需求提取结构化规格
4. **多运行时支持**: 我们可以考虑适配更多 AI 编码工具

---

## 社区反馈 (181 评论)

### 正面
- "By far the most powerful addition to my Claude Code"
- "Nothing over-engineered. Literally just gets shit done."
- Amazon/Google/Shopify/Webflow 工程师信任

### 质疑
- 与 BMAD、SpecKit、Taskmaster 等竞品对比
- `--dangerously-skip-permissions` 安全风险
- 是否过度依赖 Claude Code 特定能力

---

## 变现机会

| 机会 | ROI 评估 | 行动项 |
|------|----------|--------|
| 开发 OpenClaw 版 GSD 适配器 | 2.5 | 将 GSD 上下文工程理念适配到 OpenClaw |
| 元提示词模板库 | 2.0 | 基于 GSD 理念创建 OpenClaw 提示词模板 |
| Context Rot 检测工具 | 1.8 | 开发上下文质量监控技能 |

---

*HN 趋势分析 | 2026-03-18 | Cron #107*
