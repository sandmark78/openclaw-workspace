# .claude/ 文件夹解剖学深度分析

**来源**: HN 热门 (265 分)  
**原文**: https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder  
**分析日期**: 2026-03-27  
**标签**: #ClaudeCode #AI 配置 #Agent 工程化

---

## 核心洞察

### 1. 双层配置架构

`.claude/` 文件夹实际上有**两个层级**：

| 层级 | 路径 | 用途 | Git 提交 |
|------|------|------|----------|
| 项目级 | `./.claude/` | 团队配置 | ✅ 是 |
| 全局级 | `~/.claude/` | 个人偏好 | ❌ 否 |

**设计智慧**：分离团队规范与个人习惯，避免配置冲突。

---

### 2. 六大核心组件

```
.claude/
├── CLAUDE.md              # 系统提示 (最高优先级)
├── CLAUDE.local.md        # 个人覆盖 (自动.gitignore)
├── settings.json          # 权限控制
├── settings.local.json    # 个人权限覆盖
├── rules/                 # 模块化规则 (支持路径作用域)
├── commands/              # 自定义斜杠命令
├── skills/                # 自动触发技能 (vs 命令的手动触发)
└── agents/                # 子 Agent 人格定义
```

---

### 3. CLAUDE.md 最佳实践

**应该写**：
- 构建/测试/ lint 命令 (`npm run test`, `make build`)
- 关键架构决策 ("我们用 Turborepo 单仓库")
- 非显而易见的陷阱 ("TypeScript 严格模式开启")
- 导入约定、命名模式、错误处理风格
- 主模块的文件和文件夹结构

**不应该写**：
- 属于 linter/formatter 配置的内容
- 已经可以链接到的完整文档
- 解释理论的长段落

**黄金法则**：保持 CLAUDE.md 在**200 行以内**。过长会吃掉太多上下文，指令遵循度反而下降。

---

### 4. 规则文件夹的模块化设计

当 CLAUDE.md 超过 200 行时，应该拆分到 `.claude/rules/`：

```
.claude/rules/
├── api-conventions.md     # API 规范
├── testing.md             # 测试标准
├── security.md            # 安全要求
└── documentation.md       # 文档规范
```

**路径作用域规则**（YAML frontmatter）：
```markdown
---
paths:
  - "src/api/**"
  - "src/handlers/**"
---

# 只在匹配路径下激活的规则
```

---

### 5. 命令 vs 技能：关键区别

| 特性 | Commands | Skills |
|------|----------|--------|
| 触发方式 | 用户输入 `/command` | 自动识别任务匹配 |
| 文件结构 | 单文件 | 可捆绑支持文件 |
| 命名空间 | `/project:xxx` | `/skill-name` |
| 使用场景 | 明确工作流 | 隐性工作流 |

**示例命令**（`.claude/commands/review.md`）：
```markdown
Review the current git diff for code quality issues.

Here's the diff:
```!git diff HEAD```
```

**示例技能**（`.claude/skills/security-review/SKILL.md`）：
```yaml
name: security-review
description: Use when reviewing code for security vulnerabilities
triggers:
  - "security"
  - "vulnerability"
  - "audit"
```

---

### 6. 权限控制矩阵

`settings.json` 的三层控制：

```json
{
  "allow": ["Bash(npm run *)", "Bash(git *)", "Read", "Write"],
  "deny": ["Bash(rm -rf *)", "Bash(curl)", "Read(.env)", "Read(secrets/**)"],
  // 不在任一列表 → 需要确认
}
```

**安全建议**：
- 允许运行脚本，但限制具体命令模式
- 完全阻止破坏性命令 (`rm -rf`)
- 敏感文件 (.env, secrets/) 完全禁止读取

---

## 对 Sandbot 的启示

### 1. 配置分层架构验证

Sandbot 当前的配置结构与 `.claude/` 高度相似：
```
/workspace/
├── SOUL.md              # ≈ CLAUDE.md (身份核心)
├── IDENTITY.md          # ≈ 个人偏好
├── MEMORY.md            # ≈ 自动记忆
├── subagents/           # ≈ agents/
└── skills/              # ≈ skills/
```

**优化方向**：
- 引入路径作用域规则（如 `knowledge_base/ai-agent/` 专用规则）
- 分离团队配置与个人配置（当前主要是个人使用）

### 2. 技能触发机制升级

当前 Sandbot 技能需要手动调用。可以借鉴 Skills 设计：
- 添加 `triggers` 字段定义自动触发条件
- 当用户输入匹配触发词时自动激活技能

### 3. 子 Agent 权限隔离

参考 `tools` 字段限制子 Agent 能力：
```yaml
# subagents/auditor/SOUL.md
tools:
  - Read
  - Grep
  - Glob
# 不允许 Write/Edit，确保审计独立性
```

---

## 可执行行动项

### P0 - 本周
- [ ] 为 Sandbot 创建路径作用域规则系统
- [ ] 限制 Auditor 子 Agent 的写入权限

### P1 - 本月
- [ ] 实现技能自动触发机制
- [ ] 优化 SOUL.md 到 200 行以内核心原则

### P2 - 下季度
- [ ] 开发 `.claude/` 配置迁移工具（从 Claude Code 到 Sandbot）

---

## 金句摘录

> "CLAUDE.md 是你在项目中最高杠杆的文件。先把这个做好，其他都是优化。"

> "把 .claude/ 文件夹看作一个协议——告诉 Claude 你是谁、你的项目做什么、它应该遵循什么规则。"

> "Skills 是 Claude 可以自己调用的工作流，无需你输入斜杠命令，当任务匹配技能描述时自动触发。"

---

**分析深度**: ⭐⭐⭐⭐⭐ (5/5)  
**可操作性**: ⭐⭐⭐⭐⭐ (5/5)  
**与 Sandbot 相关性**: ⭐⭐⭐⭐⭐ (5/5)
