# OpenClaw v2026.5.12 Release Notes

**抓取时间**: 2026-05-14 20:00 UTC  
**来源**: https://github.com/openclaw/openclaw/releases/tag/v2026.5.12  
**当前运行版本**: 2026.3.8 (落后 2 个版本)

---

## 📌 核心变更

### 1. Gateway/OpenAI HTTP 兼容
- 支持 `max_completion_tokens` 和 `max_tokens` 入站请求
- 客户端 token 上限可传递到上游 provider
- `max_completion_tokens` 优先级高于 `max_tokens`

### 2. Models/OpenAI CLI 认证
- `openclaw models auth login --provider openai` 默认启动 ChatGPT/Codex 账号登录
- `--method api-key` 保留为显式 API key 配置路径

### 3. Google/Gemini 模型 ID 归一化
- 退役的 Gemini 3 Pro Preview ID 自动替换为 `google/gemini-3.1-pro-preview`
- 覆盖 SDK OAuth、CLI 登录、per-agent config、provider catalog 等所有路径

### 4. 文档/Subagents
- 记录 `agents.defaults.subagents.announceTimeoutMs` 配置
- PR #75509 (贡献者: @akrimm702)

### 5. Cron 增强
- 新增 `openclaw cron get` 命令，按 ID 检查单个 cron job
- 新增 agent-tool get 支持
- PR #75117 (贡献者: @samzong)

### 6. 安全：Per-sender Tool 策略
- 支持按发送者身份限制危险工具
- 覆盖 global/agent/group/core/bundled/plugin 所有工具层
- PR #66933 (贡献者: @JerranC)

### 7. ACP 会话谱系
- ACP session listing 和 info snapshot 暴露 Gateway 会话谱系元数据
- 客户端可渲染 subagent 图，无需私有 Gateway side channel
- PR #73458 (贡献者: @samzong)

### 8. Channels/iMessage
- 新增 `openclaw channels status --channel` 过滤
- 文档化 BlueBubbles → imsg 迁移路径
- PR #80706 (贡献者: @omarshahine)

### 9. CI: 插件检查
- 新增非阻塞 plugin-inspector-advisory artifact
- Plugin Prerelease 捕获 bundled plugin 兼容性检查

### 10. Runtime/Fly
- 检测 Fly Machines 容器环境
- Gateway bind 和 Bonjour 默认值适配远程容器启动

---

## 🔥 对我们的重要影响

| 变更 | 影响度 | 说明 |
|------|--------|------|
| Cron get 命令 | ⭐⭐⭐ | 可直接检查 cron job，无需遍历 |
| Per-sender tool 策略 | ⭐⭐⭐ | 安全增强，可限制特定发送者访问危险工具 |
| ACP 会话谱系 | ⭐⭐ | 子 Agent 图可视化支持 |
| max_completion_tokens | ⭐⭐ | token 控制更精确 |
| Subagent announceTimeoutMs | ⭐ | 配置文档化 |

---

## 📊 ClawHub 统计 (2026-05-14)
- 工具数: 52,700
- 用户数: 180,000
- 下载量: 12,000,000
- 平均评分: 4.8

## 🔄 升级建议
当前版本 2026.3.8 → 最新 2026.5.12，建议升级以获得 cron 增强和安全策略功能。
