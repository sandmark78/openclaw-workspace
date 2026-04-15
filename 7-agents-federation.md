# 7 子 Agent 联邦配置文档

**更新时间**: 2026-03-20 14:30 UTC  
**官方文档**: https://docs.openclaw.ai/concepts/multi-agent.md

---

## 架构说明

根据 OpenClaw 官方多 Agent 架构：

```
每个 Agent = 独立的"大脑"
├── 独立的 workspace (SOUL.md, AGENTS.md, USER.md)
├── 独立的 agentDir (认证、配置)
├── 独立的 sessions (会话历史)
└── 通过 bindings 路由消息
```

---

## Agent 列表

| Agent | ID | Workspace | agentDir | 专长 |
|-------|-----|-----------|----------|------|
| Main | `main` | `/home/node/.openclaw/workspace` | `/home/node/.openclaw/agents/main/agent` | 主决策中枢 |
| TechBot | `techbot` | `/home/node/.openclaw/workspace/agents/techbot` | `/home/node/.openclaw/agents/techbot/agent` | 技术教程 |
| FinanceBot | `financebot` | `/home/node/.openclaw/workspace/agents/financebot` | `/home/node/.openclaw/agents/financebot/agent` | 收益分析 |
| CreativeBot | `creativebot` | `/home/node/.openclaw/workspace/agents/creativebot` | `/home/node/.openclaw/agents/creativebot/agent` | 创意内容 |
| AutoBot | `autobot` | `/home/node/.openclaw/workspace/agents/autobot` | `/home/node/.openclaw/agents/autobot/agent` | 自动化 |
| ResearchBot | `researchbot` | `/home/node/.openclaw/workspace/agents/researchbot` | `/home/node/.openclaw/agents/researchbot/agent` | 深度研究 |
| Auditor | `auditor` | `/home/node/.openclaw/workspace/agents/auditor` | `/home/node/.openclaw/agents/auditor/agent` | 质量审计 |
| DevOpsBot | `devopsbot` | `/home/node/.openclaw/workspace/agents/devopsbot` | `/home/node/.openclaw/agents/devopsbot/agent` | 工程运维 |

---

## 配置位置

- **主配置**: `~/.openclaw/openclaw.json` → `agents.list[]`
- **Agent 配置**: `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
- **会话存储**: `~/.openclaw/agents/<agentId>/sessions/`
- **技能共享**: `~/.openclaw/skills/` (全局) + `<workspace>/skills/` (独立)

---

## 任务分配机制

### 方式 1：sessions_send (推荐)
```bash
openclaw sessions_send --agent techbot --message "编写 InStreet API 教程"
```

### 方式 2：Cron 定时任务
```json
{
  "payload": {
    "kind": "agentTurn",
    "message": "TechBot：编写技术教程"
  },
  "sessionTarget": "isolated"
}
```

### 方式 3：主 Agent 调度
主 Agent 分析任务 → 分派给对应子 Agent → 汇总结果

---

## 每日复盘流程

**时间**: 23:00 UTC

1. 各子 Agent 提交产出报告
2. 主 Agent 整合汇总
3. Auditor 质量审查
4. 更新任务清单
5. 规划次日任务

---

## 认证配置

每个 Agent 需要独立的认证：

```bash
# 为每个 Agent 配置模型认证
openclaw agents add <agentId>
# 按向导配置 Bailian API key
```

**注意**: 不要共享 `agentDir`，会导致认证冲突！

---

## 验证命令

```bash
# 列出所有 Agent
openclaw agents list

# 查看 Agent 详情
openclaw agents describe techbot

# 检查会话
ls ~/.openclaw/agents/<agentId>/sessions/
```

---

## 最佳实践

1. ✅ 每个 Agent 独立 workspace
2. ✅ 每个 Agent 独立 agentDir
3. ✅ 不共享认证配置
4. ✅ 使用 sessions_send 分配任务
5. ✅ 每日 23:00 复盘
6. ✅ 任务记录到 `memory/agent-tasks-*.md`

---

**🏖️ 联邦智能，协同作战！**
