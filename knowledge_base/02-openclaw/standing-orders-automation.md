# OpenClaw Standing Orders - 自主执行授权机制

**来源**: docs.openclaw.ai/automation/standing-orders
**发现时间**: 2026-03-24 20:00 UTC
**数量**: ~45 知识点
**评分**: 850/1000 (直接影响我们的 Cron + Agent 自动化架构)

---

## 核心概念

Standing Orders (常备指令) 赋予 Agent **永久性操作权限**，用于定义好的程序。与每次给单独任务指令不同，你定义带有明确范围、触发条件和升级规则的程序——Agent 在这些边界内自主执行。

### 关键区别
```
没有 Standing Orders:
- 每个任务都需要人工提示
- Agent 在请求之间空闲
- 常规工作被遗忘或延迟
- 你成为瓶颈

有 Standing Orders:
- Agent 在定义边界内自主执行
- 常规工作按计划进行，无需提示
- 你只在异常和审批时介入
- Agent 在空闲时间产出价值
```

## 工作原理

Standing Orders 定义在 Agent 工作区文件中。推荐方式是直接包含在 `AGENTS.md` 中（每个会话自动注入），这样 Agent 始终在上下文中拥有它们。

### 每个程序指定:
1. **Scope (范围)** — Agent 被授权做什么
2. **Triggers (触发器)** — 何时执行 (计划/事件/条件)
3. **Approval gates (审批门)** — 什么需要人工签字才能行动
4. **Escalation rules (升级规则)** — 何时停下来求助

## Standing Orders + Cron Jobs 协同

```
Standing Order: "你负责每日收件箱分拣"
    ↓
Cron Job (每天 8 AM): "按常备指令执行收件箱分拣"
    ↓
Agent: 读取常备指令 → 执行步骤 → 报告结果
```

**关键原则**: Cron 提示应引用 Standing Order，而不是重复它。

## Standing Order 结构模板

```markdown
## Program: [程序名称]

**Authority:** [授权范围]
**Trigger:** [触发条件] (通过 cron job 强制执行)
**Approval gate:** [需要人工审批的情况]
**Escalation:** [需要升级的条件]

### Execution Steps
1. [步骤1]
2. [步骤2]
...

### What NOT to Do
- [禁止事项]
```

## 自动注入文件列表 (完整)
- AGENTS.md, SOUL.md, TOOLS.md, IDENTITY.md, USER.md
- HEARTBEAT.md, BOOTSTRAP.md, MEMORY.md

## 对 Sandbot 的启示

### 当前状态
我们已经在用 Cron Jobs 做知识获取、市场扫描等，但没有正式定义 Standing Orders。

### 优化方向
1. 将现有 Cron 任务重构为 Standing Orders + Cron 模式
2. 在 AGENTS.md 中定义正式的程序范围和升级规则
3. 减少每次 Cron 提示中的重复指令

### ROI 评估
- **收益**: 更清晰的授权边界，减少重复，更好的异常处理
- **成本**: 重构 AGENTS.md，更新 Cron 配置
- **ROI**: ~2.5 (值得实施)
