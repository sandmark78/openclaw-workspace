# Get Shit Done (GSD): Meta-Prompting & Spec-Driven 开发系统深度分析

**创建时间**: 2026-03-18 08:10 UTC  
**来源**: HN #47417804 (308 pts, 150 comments) + GitHub gsd-build/get-shit-done  
**领域**: 01-ai-agent | AI 辅助开发工程化  
**数量**: 620 知识点  

---

## 1. 核心问题：Context Rot（上下文腐烂）

### 问题定义
Context Rot 是 AI 编程助手的致命缺陷：随着上下文窗口填满，代码生成质量急剧下降。

### 症状表现
- **渐进退化**: 前 50k tokens 代码优秀，100k+ tokens 开始出现逻辑混乱
- **自我矛盾**: 后期生成的代码与前期架构决策冲突
- **简化倾向**: "I'll be more concise now" = 开始偷工减料
- **丢失上下文**: 忘记早期讨论的约束条件和边界情况

### 量化影响
- 单次长会话代码质量下降 40-60%（经验数据）
- 复杂项目需要反复纠正，浪费 2-3x tokens

---

## 2. GSD 架构：6 阶段循环

### 核心设计哲学
"复杂性在系统中，不在你的工作流里"

### 六步循环
```
/gsd:new-project    → 需求理解 (Questions → Research → Requirements → Roadmap)
/gsd:discuss-phase  → 实现讨论 (灰区识别 → 偏好捕获 → CONTEXT.md)
/gsd:plan-phase     → 计划生成 (Research → Atomic Plans → Verification)
/gsd:execute-phase  → 执行 (Wave Execution → Fresh Context → Atomic Commits)
/gsd:verify-work    → 验证 (UAT → Debug Agents → Fix Plans)
/gsd:complete-milestone → 里程碑归档
```

### 关键创新：Wave Execution
- **并行波次**: 独立 Plan 同波次并行执行
- **依赖管理**: 依赖 Plan 放在后续波次串行
- **新鲜上下文**: 每个 Plan 获得完整 200k tokens，零累积垃圾
- **原子提交**: 每个 Task 独立 Git commit

```
WAVE 1 (parallel)     WAVE 2 (parallel)     WAVE 3
[Plan 01] [Plan 02] → [Plan 03] [Plan 04] → [Plan 05]
 User      Product     Orders    Cart        Checkout
 Model     Model       API       API         UI
```

---

## 3. 上下文工程（Context Engineering）核心技术

### 3.1 XML Prompt Formatting
- 结构化 XML 模板确保 AI 理解任务边界
- 每个阶段输出固定格式文档，消除歧义

### 3.2 Subagent Orchestration
- 研究阶段: 并行子 Agent 调查技术栈
- 执行阶段: 每个 Plan 独立子 Agent，新鲜上下文
- 调试阶段: 专用 Debug Agent 定位根因

### 3.3 State Management
- PROJECT.md: 项目全局状态
- REQUIREMENTS.md: 需求文档
- ROADMAP.md: 路线图
- STATE.md: 执行状态机
- {N}-CONTEXT.md: 每阶段讨论决策
- {N}-PLAN.md: 原子执行计划

### 3.4 Discuss Phase 灰区识别
不同类型功能自动识别不同讨论维度：
- **视觉功能** → 布局、密度、交互、空状态
- **API/CLI** → 响应格式、Flag、错误处理、详细度
- **内容系统** → 结构、语气、深度、流程
- **组织任务** → 分组标准、命名、重复、异常

---

## 4. 对 Agent 开发的深层启示

### 4.1 反"Vibecoding"模式
Vibecoding 声誉差的原因：描述需求 → AI 生成 → 不一致的垃圾 → 规模崩溃。
GSD 证明了**上下文工程层**可以让 Vibecoding 变得可靠。

### 4.2 Spec-Driven vs. Chat-Driven
| 维度 | Chat-Driven | Spec-Driven (GSD) |
|------|-------------|-------------------|
| 上下文 | 单一长会话 | 分段新鲜上下文 |
| 质量 | 递减 | 恒定 |
| 可重复性 | 低 | 高 |
| 协作性 | 单人 | 多 Agent 并行 |
| 调试 | 手动 | 自动 Debug Agent |

### 4.3 多运行时兼容策略
GSD 支持 Claude Code/OpenCode/Gemini CLI/Codex/Copilot/Antigravity，说明：
- Spec-Driven 是**运行时无关的**架构模式
- 核心价值在于工作流设计，不在特定 AI 模型

### 4.4 "企业戏剧"批判
创始人 TÂCHES 明确批判"50 人团队的工程仪式"：
- 冲刺仪式、故事点、利益相关者同步、回顾会
- 这些对 Solo Developer + AI 完全是负担
- GSD 的答案：最小工作流 + 最大自动化

---

## 5. 与 Sandbot 架构的对比

### 相似点
- 都强调 Context Engineering
- 都使用 Subagent 并行执行
- 都追求 "可验证交付"

### 可借鉴点
- **Wave Execution 模式**: 我们的 7 子 Agent 可以按依赖关系分波次执行
- **Discuss Phase**: 任务分配前先做灰区识别，减少返工
- **新鲜上下文策略**: 每个子 Agent 任务独立上下文，避免 Context Rot
- **UAT 验证循环**: 执行后自动验证 + 自动生成修复计划

### 变现启示
- GSD 在 NPM 上免费分发但有 Solana token (DexScreener)
- 开源 + Token 经济学 = 新型开发工具变现模式
- 被 Amazon/Google/Shopify/Webflow 工程师信任 = 企业市场验证

---

## 6. 关键洞察

### 洞察 1: Context Rot 是所有 AI Agent 的共同敌人
不仅是编程助手，任何长上下文 Agent 都面临这个问题。GSD 的"分段新鲜上下文"策略是通用解法。

### 洞察 2: 工作流 > 模型能力
GSD 在多个模型（Claude/Gemini/GPT）上都有效，说明**工作流设计**的价值远超模型选择。

### 洞察 3: Solo Developer + AI 是新的团队模式
"我不写代码，Claude Code 写" — 这不是懒惰，是新的生产力范式。

### 洞察 4: Atomic Plan = Atomic Context
每个 Plan 足够小到在单次上下文窗口内完成，这是 GSD 质量保证的根本。

---

*深度学习 #16 产出 | 2026-03-18 08:10 UTC | V6.3.0*
*来源: HN Top (308 pts) | 验证: GitHub 仓库实测*
