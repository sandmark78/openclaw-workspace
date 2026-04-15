# Cook — Claude Code 的工作流编排工具

**来源**: GitHub (rjcorwin/cook)  
**HN 评分**: 143 points  
**领域**: AI 编程工具 / 工作流编排 / Agent 协同  
**数量**: 14 知识点  
**状态**: 开源 / npm 可安装 / Claude Code Skill

---

## Cook 是什么

Cook 是一个 CLI 工具，用于**编排 Claude Code/Codex/OpenCode 的工作流循环**。核心思想：用简单的 DSL 组合"工作→审查→迭代→对比"的复杂流程。

## 核心语法

### 基础用法
```bash
# 单次执行
cook "实现暗色模式"

# 循环 3 次（每次基于上次结果）
cook "实现暗色模式" x3

# 审查循环（审查→门控→迭代，最多 3 次）
cook "实现暗色模式" review

# 并行 3 个方案，选最好的
cook "实现暗色模式" v3 "代码最少者胜"

# 两个方案对比
cook "JWT 认证" vs "Session 认证" pick "安全性最佳"
```

### 操作符（从左到右组合）

| 操作符 | 功能 | 示例 |
|--------|------|------|
| `xN` | 顺序执行 N 次 | `x3` = 3 次迭代 |
| `review` | 审查→门控→迭代循环 | `review 5` = 最多 5 轮审查 |
| `ralph N` | 任务列表推进器 | `ralph 5 "DONE if 全部完成"` |
| `vN` / `race N` | 并行 N 个方案 | `v3` = 3 个方案竞赛 |
| `vs` | 两个不同方案对比 | `"JWT" vs "Session"` |
| `pick` | 选择一个赢家 | `pick "代码最简洁"` |
| `merge` | 合并多个方案 | `merge "最佳实践"` |
| `compare` | 生成对比报告 | `compare` = 写对比文档 |

### 组合示例
```bash
# 3 次迭代 + 审查循环
cook "实现暗色模式" x3 review

# 审查循环重复 3 次
cook "实现暗色模式" review x3

# 3 个方案竞赛，每个都有审查循环
cook "实现暗色模式" review v3 "最干净者胜"

# 任务列表推进（每任务审查，完成后推进）
cook "完成 plan.md 中的下一个任务" \
  review "代码审查" "DONE if 无高危问题" \
  ralph 5 "DONE if 全部完成 else NEXT"
```

---

## 架构设计

### 安装方式
```bash
# 全局安装 CLI
npm install -g @let-it-cook/cli

# 或作为 Claude Code Skill
mkdir -p .claude/skills && cp -r $(npm root -g)/@let-it-cook/cli/skill .claude/skills/cook
```

### 配置文件
```bash
cook init
```
创建：
- `COOK.md` — 项目指令和 Agent Prompt 模板
- `.cook/config.json` — Agent/模型/沙箱默认配置
- `.cook/Dockerfile` — Docker 沙箱依赖
- `.cook/logs/` — 会话日志（自动 gitignore）

### 配置示例
```json
{
  "agent": "claude",
  "sandbox": "agent",
  "steps": {
    "work": { "agent": "codex", "model": "gpt-5-codex" },
    "review": { "agent": "claude", "model": "opus" }
  },
  "env": ["CLAUDE_CODE_OAUTH_TOKEN"]
}
```

### 沙箱模式
| 模式 | 标志 | 描述 |
|------|------|------|
| Agent（默认） | `--sandbox agent` | 使用 Agent 自带的 OS 级沙箱 |
| Docker | `--sandbox docker` | Docker 容器内运行，限制网络/文件系统 |

---

## 深度洞察

### 1. Cook 解决了什么痛点
**问题**：单次 Agent 调用质量不稳定，需要人工多次迭代。  
**Cook 方案**：自动化迭代循环 + 多方案对比。

**价值**：
- 把"人肉迭代"变成"自动化工作流"
- 把"直觉选择"变成"标准对比"
- 把"隐性知识"变成"显式配置"

### 2. Ralph — 任务列表推进器
Ralph 是 Cook 最创新的设计：
```bash
cook "完成 plan.md 中的下一个任务" \
  ralph 5 "DONE if 全部完成 else NEXT"
```

**工作原理**：
1. Agent 读取项目状态，找到当前任务
2. 执行任务 → 审查 → 迭代（如果审查不通过）
3. 门控决定：完成 → 推进到下一任务；未完成 → 继续迭代
4. 所有任务完成后退出

**对 OpenClaw 的启示**：
- 可以开发类似的"任务推进器"技能
- 适用于长期项目（多任务/多阶段）
- 关键是"自指向"Prompt（Agent 自己读状态决定下一步）

### 3. 多 Agent 协同
Cook 支持不同步骤用不同 Agent/模型：
```bash
cook "实现暗色模式" review \
  --work-agent codex --work-model gpt-5-codex \
  --review-agent claude --review-model opus
```

**最佳实践**：
- **工作 Agent**：用 Codex（代码生成强）
- **审查 Agent**：用 Claude Opus（代码审查强）
- **分工明确**：生成和审查分离，避免"自己审查自己"

### 4. 并行方案对比
```bash
cook "JWT 认证" vs "Session 认证" pick "安全性最佳"
```

**工作原理**：
1. 创建两个隔离的 Git worktree
2. 并行执行两个方案
3. 用第三个 Agent 对比并选择赢家
4. 合并赢家到主分支

**价值**：
- 避免"过早优化"（先实现再对比，不是先争论）
- 用实际代码说话，不是理论争论
- 自动化"设计决策"流程

---

## 对 OpenClaw 生态的启示

### 1. 可以开发类似的编排工具
OpenClaw 可以有：
```bash
openclaw cook "开发一个技能" review v3 pick
```

**差异化**：
- 支持 OpenClaw 多 Agent 架构
- 集成 ClawHub 技能市场
- 支持本地模型（百炼/Ollama）

### 2. 技能开发工作流
用 Cook 思路开发 OpenClaw 技能：
```bash
# 3 个方案竞赛
cook "开发一个输入验证技能" v3 "代码最简洁"

# 审查循环
cook "优化技能性能" review "性能提升>20% else ITERATE"

# 任务推进
cook "完成 TODO.md 中的下一个功能" ralph 10
```

### 3. 质量保障
Cook 的审查循环可以直接用于技能质量：
```bash
cook "修复技能 bug" review \
  "审查：是否有回归风险" \
  "DONE if 测试通过 else ITERATE"
```

---

**创新性**: ⭐⭐⭐⭐⭐ DSL 设计简洁强大  
**实用性**: ⭐⭐⭐⭐⭐ 立即能用，解决真实痛点  
**对 OpenClaw 相关性**: ⭐⭐⭐⭐⭐ 可以直接借鉴/复刻
