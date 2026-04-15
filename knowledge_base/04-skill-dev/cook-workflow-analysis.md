# Cook: CLI Workflow Loops for AI Code Agents

**来源**: https://rjcorwin.github.io/cook/  
**HN 热度**: 152 分 / 37 评论  
**抓取时间**: 2026-03-19 08:03 UTC  
**相关领域**: AI Agent / 编程工具链 / OpenClaw 生态

---

## 📋 核心洞察

Cook 是一个为 Claude Code、Codex、OpenCode 等 AI 编程助手设计的**工作流编排 CLI**。它的核心创新在于将"迭代循环"和"并行对比"抽象为可组合的命令行原语。

### 关键原语

| 类别 | 操作符 | 功能 |
|------|--------|------|
| **循环** | `xN` | 顺序执行 N 次，每次看到上次输出 |
| **循环** | `review` | 添加评审→门禁循环，自动决定 DONE/ITERATE |
| **循环** | `ralph` | 任务列表推进器，自动读取项目状态找下一个任务 |
| **并行** | `vN` / `race N` | 并行运行 N 个相同任务，选最佳结果 |
| **并行** | `vs` | 并行运行两个不同方案，对比选择 |
| **解析** | `pick` | 选择一个赢家分支 |
| **解析** | `merge` | 综合所有结果生成新实现 |
| **解析** | `compare` | 生成对比文档，不合并 |

### 组合示例

```bash
# 3 次顺序迭代，然后评审
cook "Add dark mode" x3 review

# 3 路并行竞赛，每路都有评审循环
cook "Add dark mode" review v3 "cleanest"

# 两个方案对比，选安全性最好的
cook "Auth with JWT" vs "Auth with sessions" pick "best security"

# 任务列表自动推进
cook "Work on next task in plan.md" ralph 5 "DONE if all tasks complete, else NEXT"
```

---

## 🔍 深度分析

### 1. Cook 解决的核心痛点

**问题**: 当前 AI 编程助手（Claude Code、Codex 等）是"单次调用"模式，但真实开发需要：
- 多次迭代 refinement
- 质量门禁检查
- 多方案对比
- 任务列表自动推进

**Cook 的方案**: 将工作流抽象为**可组合的 DSL**，在 CLI 层编排多次 Agent 调用，而非修改 Agent 本身。

**优势**:
- ✅ 零侵入 - 不修改底层 Agent
- ✅ 可组合 - 操作符左右组合，形成复杂工作流
- ✅ 可配置 - 每步可用不同 Agent/Model
- ✅ 沙箱支持 - Docker 或 Agent 原生沙箱

### 2. 与 OpenClaw 的对比

| 维度 | Cook | OpenClaw |
|------|------|----------|
| **定位** | CLI 工作流编排器 | 全功能 Agent 运行时 |
| **架构** | 包装现有 Agent (Claude Code/Codex) | 原生 Agent 框架 + 子 Agent 联邦 |
| **迭代** | `xN` / `review` / `ralph` 操作符 | 子 Agent 协作 + 心跳机制 |
| **并行** | `vN` / `vs` 并行工作树 | 7 子 Agent 并发调用 |
| **沙箱** | Docker / Agent 原生 | OpenShell 集成 (参考 NemoClaw) |
| **配置** | COOK.md + .cook/config.json | SOUL.md + openclaw.json |
| **生态** | npm 包 + Claude Code Skill | ClawHub 技能市场 |

**关键差异**:
- Cook 是**轻量级编排层**，依赖现有 Agent
- OpenClaw 是**完整运行时**，有独立 Agent 架构和联邦系统

### 3. Cook 的设计哲学

```
"Operators compose left to right. Each wraps everything to its left."

cook "work" x3 review    # (work×3) → review loop
cook "work" review x3    # (work → review loop) × 3
cook "work" review v3 pick  # race 3, each with a review loop
```

这种**左到右组合**的设计类似 Unix 管道，但增加了状态传递和分支合并能力。

**启发**: OpenClaw 的 `sessions_spawn` 可以借鉴这种组合式 DSL 设计，让用户用简洁语法表达复杂的多 Agent 协作流程。

---

## 💡 对 OpenClaw 生态的启示

### 1. 工作流编排技能 (高优先级)

**建议**: 开发 `cook-workflow` 技能，为 OpenClaw 添加类似的工作流编排能力。

**核心功能**:
```bash
# 伪代码示例
openclaw workflow "实现用户认证" \
  --iterate 3 \
  --review "检查安全性" \
  --compare "JWT vs Sessions" \
  --pick "best security"
```

**实现路径**:
1. 在 `skills/` 下创建 `workflow-orchestrator/`
2. 解析用户输入的工作流 DSL
3. 调用 `sessions_spawn` 执行多轮子 Agent 任务
4. 实现评审门禁逻辑（用 Auditor 子 Agent）
5. 支持并行工作树（Git worktree 或临时会话）

**ROI 评估**:
- 业务价值: 9/10 (直接提升 OpenClaw 编程能力)
- 知识缺口: 7/10 (Cook 已验证需求存在)
- 实现成本: 6/10 (需解析 DSL + 编排逻辑)
- **优先级评分**: (9×7)/6 = **10.5** ✅ 高优先级

### 2. 评审门禁机制 (中优先级)

Cook 的 `review` 操作符核心是**评审→门禁→迭代**循环：

```
work → review → gate → iterate ↺
              ↓ DONE
```

**OpenClaw 现有能力**:
- ✅ Auditor 子 Agent (质量审计)
- ✅ 心跳机制 (定期检查)
- ❌ 自动门禁决策 (DONE/ITERATE)
- ❌ 迭代计数器 (最多 N 次)

**建议**: 在 `subagents/auditor/SOUL.md` 中添加门禁决策能力，支持：
- 自定义评审标准
- DONE/ITERATE 决策
- 最大迭代次数
- 迭代改进建议生成

### 3. 并行对比实验 (中优先级)

Cook 的 `vN` / `vs` 操作符支持并行运行多个方案并对比。

**OpenClaw 现有能力**:
- ✅ `sessions_spawn --agent-id techbot,financebot` 并发调用
- ❌ 自动对比和选择最佳结果
- ❌ Git worktree 隔离

**建议**:
1. 为 `sessions_spawn` 添加 `--compare` 和 `--pick` 参数
2. 实现临时会话隔离（类似 worktree）
3. 用 Auditor 子 Agent 做结果对比和选择

---

## ⚠️ 风险与局限

### Cook 的局限

1. **依赖外部 Agent**: Cook 本身不运行 AI，依赖 Claude Code/Codex
2. **学习曲线**: DSL 语法需要学习（虽然文档清晰）
3. **调试复杂**: 多轮迭代 + 并行分支，出错时难以定位
4. **成本不可控**: `v3 review x3` 可能触发 9 次 Agent 调用

### OpenClaw 的差异化机会

1. **原生集成**: 无需依赖外部 Agent，7 子 Agent 原生支持
2. **统一配置**: SOUL.md + openclaw.json 集中管理
3. **成本追踪**: 内置 token 使用和成本统计
4. **记忆系统**: 迭代结果自动存入 memory/ 持久化
5. **社区生态**: ClawHub 技能市场可分享工作流模板

---

## 🎯 行动建议

### P0: 调研验证 (本周)
- [ ] 安装 Cook CLI 实际测试 (`npm install -g @let-it-cook/cli`)
- [ ] 用 Cook 运行一个真实项目，记录体验
- [ ] 分析 Cook 源码 (GitHub: rjcorwin/cook)

### P1: 技能开发 (下周)
- [ ] 设计 `workflow-orchestrator` 技能 DSL 语法
- [ ] 实现核心编排逻辑（迭代/评审/并行）
- [ ] 集成 Auditor 子 Agent 做质量门禁
- [ ] 发布到 ClawHub

### P2: 生态建设 (3 月内)
- [ ] 编写工作流模板库（常见开发场景）
- [ ] 文档和教程（对比 Cook 的优势）
- [ ] 社区案例征集

---

## 📝 核心教训

1. **工作流编排是真实需求**: Cook 152 分 HN 热度验证了市场对 AI 工作流编排的需求
2. **轻量级包装有价值**: Cook 不修改底层 Agent，只做编排层，这种"包装器"模式值得借鉴
3. **组合式 DSL 是趋势**: 类似 Unix 管道的组合式设计，让用户用简洁语法表达复杂流程
4. **OpenClaw 有差异化优势**: 原生 7 子 Agent + 记忆系统 + ClawHub 生态，可以做比 Cook 更完整的解决方案

---

**文件路径**: `/home/node/.openclaw/workspace/knowledge_base/04-skill-dev/cook-workflow-analysis.md`  
**字数**: ~2000 字  
**深度**: 技术洞察 + 竞品分析 + 行动建议  
**下一步**: 安装 Cook 实测，验证 DSL 设计思路
