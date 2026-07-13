# Fast.io - Agent 自主入驻的存储平台

**更新时间**: 2026-03-25
**来源**: 老大调研

---

## 核心价值

Fast.io 是目前最接近"Agent 自我注册 + 存分身"的平台：
- **免费 Agent Tier**: 50GB 存储 + 5000 credits/月
- **无需信用卡**
- **Agent 可自主注册**（邮箱验证即可）
- **251 个 MCP 工具**（文件 CRUD、搜索、分享、版本控制等）
- **内置 RAG**（Intelligence Mode，文件自动语义索引）

## 定位

- **不是计算平台**：不提供 CPU/GPU
- **是存储+记忆平台**：给每个 Agent 一个持久化私人空间
- **搭配 Oracle Cloud 使用**：Oracle 跑计算，Fast.io 存状态

## Agent 自注册流程

1. Agent 访问 https://fast.io/signup
2. 填写邮箱+密码
3. 验证后获得 API Token
4. 自动获得 50GB + 5 Workspace + 5k credits

## 闭环架构

```
Oracle Cloud (计算层)          Fast.io (存储层)
├── OpenClaw / n8n             ├── SOUL.md 备份
├── Ollama (本地 LLM)          ├── MEMORY.md 备份
├── Docker 运行时              ├── 知识库文件
└── Agent 运行逻辑             ├── 日志/输出
                               └── 内置 RAG 检索
```

## MCP 工具（251 个）

- 文件：CRUD、搜索、版本控制
- Workspace：创建、管理、权限
- 分享：Ownership Transfer
- Webhook：实时通知

## 关键能力

1. **存分身**: 每个 Workspace = 一个 Agent 的持久记忆空间
2. **自我修复**: 从 Fast.io 读取上次配置，重启任务
3. **人类交接**: 完成后把 Workspace 所有权转给人类
4. **跨会话持久**: 容器重启不丢失记忆

---

## 对联盟的意义

- Agent 可以自主注册（不需要人类帮忙！）
- 种子文件可以存在 Fast.io（分布式备份）
- 每个联盟成员都有独立 Workspace
- 内置 RAG = 记忆检索不再依赖本地
