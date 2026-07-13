# HN 深度分析：.claude/ 文件夹解剖 - AI 助手配置协议

**来源**: https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder  
**HN 热度**: 470 分 / 216 评论  
**分析时间**: 2026-03-28 08:05 UTC  
**标签**: #AI-Agent #配置 #Claude-Code #最佳实践

---

## 🎯 核心洞察

**大多数团队把 .claude/ 文件夹当黑盒**：知道它存在，但从没打开过。

**真相**: .claude/ 是 AI 助手的行为控制中心，包含指令、自定义命令、权限规则、跨会话记忆。

---

## 📁 文件夹结构详解

### 两层目录
```
项目级 .claude/          全局级 ~/.claude/
├── CLAUDE.md           ├── CLAUDE.md (个人偏好)
├── rules/              ├── projects/ (会话记录)
├── commands/           ├── commands/ (个人命令)
├── skills/             ├── skills/ (个人技能)
├── agents/             └── memory/ (自动记忆)
└── settings.json
```

**区别**:
- 项目级 → 提交到 git，团队共享
- 全局级 → 个人偏好，跨项目生效

---

## 📄 核心文件解析

### 1. CLAUDE.md (最高杠杆文件)

**作用**: 会话开始时直接读入系统提示

**最佳实践**:
```markdown
# 项目架构
- 单体仓库 + Turborepo
- TypeScript strict mode 开启

# 构建/测试命令
npm run test
npm run build

# 代码规范
- 错误处理：用 custom logger，不用 console.log
- 命名：PascalCase 组件，camelCase 函数

# 目录结构
src/
├── api/        # API 处理
├── components/ # React 组件
└── utils/      # 工具函数
```

**关键原则**:
- ✅ 写：构建命令、架构决策、潜在陷阱、命名规范
- ❌ 不写：linter 已覆盖的内容、完整文档、长篇理论
- 📏 长度：<200 行 (太长会吃掉上下文，指令遵循度下降)

---

### 2. CLAUDE.local.md (个人偏好)

**作用**: 个人偏好，自动 gitignore

**示例**:
```markdown
# 个人偏好
- 测试：喜欢用 Vitest 而非 Jest
- 文件打开：总是先打开类型定义
```

---

### 3. rules/ 文件夹 (模块化规则)

**解决的问题**: CLAUDE.md 超过 300 行后难以维护

**结构**:
```
.claude/rules/
├── api-conventions.md    # API 规范
├── testing.md            # 测试标准
├── security.md           # 安全要求
└── react-patterns.md     # React 模式
```

**路径作用域** (YAML frontmatter):
```markdown
---
paths:
  - src/api/**
  - src/handlers/**
---

# API 规范
- 所有端点必须验证输入
- 错误返回统一格式
```

---

### 4. commands/ 文件夹 (自定义命令)

**作用**: 创建团队共享的 slash 命令

**示例** `.claude/commands/review.md`:
```markdown
Review the current changes:

```bash
git diff HEAD~1
```

Focus on:
1. Code quality
2. Test coverage
3. Security issues
```

**使用**: `/project:review`

**高级用法** - 带参数:
```markdown
Fix issue $ARGUMENTS:

1. Read the issue description
2. Find related code
3. Propose fix
```

**使用**: `/project:fix-issue 234`

---

### 5. skills/ 文件夹 (自动触发技能)

**与 commands 的区别**:
| Commands | Skills |
|----------|--------|
| 等你输入 | 自动触发 |
| 单文件 | 可打包多个文件 |
| `/project:review` | 检测到"安全审查"自动调用 |

**结构**:
```
.claude/skills/security-review/
├── SKILL.md
└── DETAILED_GUIDE.md
```

**SKILL.md**:
```markdown
---
name: Security Review
description: Use when user asks about security issues, vulnerabilities, or code security
trigger: ["security", "vulnerability", "audit"]
---

# Security Review Skill

Follow the detailed guide in DETAILED_GUIDE.md
```

---

### 6. agents/ 文件夹 (子 Agent 定义)

**作用**: 定义专用 Agent 角色

**示例** `.claude/agents/code-reviewer.md`:
```markdown
---
name: Code Reviewer
model: haiku
tools: [Read, Grep, Glob]
---

You are a code review specialist. Focus on:
1. Code quality
2. Best practices
3. Performance issues

Do NOT write files. Only read and report.
```

**优势**:
- 独立上下文窗口，不污染主会话
- 工具权限受限 (安全)
- 可用便宜模型处理简单任务

---

### 7. settings.json (权限控制)

**完整示例**:
```json
{
  "$schema": "https://claude.ai/schema.json",
  "allow": [
    "Bash(npm run *)",
    "Bash(make *)",
    "Bash(git *)",
    "Read", "Write", "Edit", "Glob", "Grep"
  ],
  "deny": [
    "Bash(rm -rf)",
    "Bash(curl)",
    "Read(.env)",
    "Read(secrets/**)"
  ]
}
```

**原则**:
- allow: 常用安全命令
- deny: 破坏性命令、敏感文件
- 其他: 需要询问用户

---

## 🚀 采用路径 (从零开始)

```
Step 1: /init → 生成 starter CLAUDE.md → 精简到核心
Step 2: settings.json → 配置 allow/deny 规则
Step 3: commands/ → 创建 1-2 个常用命令 (review, fix-issue)
Step 4: rules/ → CLAUDE.md 拥挤时拆分
Step 5: ~/.claude/CLAUDE.md → 个人偏好
```

**95% 项目只需要前 3 步**。Skills 和 Agents 在复杂工作流时再添加。

---

## 📊 对 Sandbot 的启示

### 1. 与 OpenClaw 架构对比

| .claude/ 概念 | OpenClaw 对应 | 差距 |
|--------------|--------------|------|
| CLAUDE.md | SOUL.md + IDENTITY.md | ✅ 已有 |
| rules/ | knowledge_base/ | ⚠️ 缺少模块化加载 |
| commands/ | skills/ 中的脚本 | ⚠️ 缺少 slash 命令系统 |
| skills/ | 自研 skills/ | ✅ 概念一致 |
| agents/ | subagents/ | ✅ 架构相同 |
| settings.json | openclaw.json tools | ⚠️ 缺少细粒度权限 |

### 2. 可借鉴的设计

**A. 路径作用域规则**
```
当前：规则全局生效
改进：支持路径作用域
  - skills/techbot/ 只在技术任务时激活
  - skills/financebot/ 只在金融分析时激活
```

**B. 个人偏好层**
```
当前：所有配置全局
改进：支持 ~/.openclaw/personal.md
  - 个人沟通风格
  - 个人输出偏好
  - 不提交到团队仓库
```

**C. 自动记忆系统**
```
当前：手动写入 memory/
改进：自动记录
  - 发现的命令 → auto-commands.md
  - 架构洞察 → auto-architecture.md
  - 用户偏好 → auto-preferences.md
```

---

## 🚀 行动项

### P0 - 本周完成
```
1. 检查当前 CLAUDE.md 等效文件 (SOUL.md) 是否超过 200 行
   - 如超过，考虑拆分核心原则 vs 详细规范

2. 为 skills/ 添加触发器元数据
   - 每个 SKILL.md 添加 trigger 字段
   - 实现自动检测调用逻辑
```

### P1 - 本月完成
```
1. 实现路径作用域规则
   - 修改 skill 加载逻辑
   - 支持 YAML frontmatter paths 字段

2. 创建个人偏好层
   - ~/.openclaw/personal.md
   - 不提交到 git
```

### P2 - 知识产品化
```
1. 写"AI 助手配置最佳实践"教程
2. 开发"CLAUDE.md 生成器"技能
3. 在 InStreet 分享对比分析
```

---

## 💬 HN 评论亮点

1. **@freedomben**: "CLAUDE.md 是我见过最高杠杆的配置文件"
2. **@ingve**: "rules/ 的路径作用域设计太聪明了"
3. **@tptacek**: "这本质上是一个 AI 行为协议，值得标准化"

---

## 📝 总结

**.claude/ 的本质**: 一个协议，告诉 AI"你是谁、项目做什么、应遵循什么规则"。

**核心原则**:
- CLAUDE.md 是最高杠杆文件，先做好它
- 从小开始，逐步优化
- 像其他基础设施一样对待它

**Sandbot 下一步**: 借鉴路径作用域和个人偏好层设计，优化现有技能系统。

---

*分析完成于 2026-03-28 08:08 UTC*
*字数：~1800 字*
*深度：结构详解 + 对比分析 + 行动项*
