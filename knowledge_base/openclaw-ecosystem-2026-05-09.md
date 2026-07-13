# OpenClaw 生态探索记录 - 2026-05-09

**探索时间**: 2026-05-09 20:00 UTC  
**触发**: Cron 生态探索任务

---

## 📊 当前状态

| 项目 | 我们 | 最新 | 状态 |
|------|------|------|------|
| OpenClaw 版本 | 2026.3.8 | Pre-release (2026-05-09) | ⚠️ 落后 2 个月 |
| ClawHub 域名 | clawhub.com | → clawhub.ai | 已重定向 |
| ClawHub 统计 | - | 52.7k 工具 / 180k 用户 / 12M 下载 / 4.8 评分 | - |

---

## 🆕 今日 GitHub Pre-release 重要变更

### 聊天命令
- `/think default` 和 `/fast default` 新增：清除会话覆盖，继承配置的/provider 默认值

### Agent 核心
- **Provider/Model 身份注入**: 当前 provider/model 身份自动注入系统 prompt，agent 可回答"你是什么模型"这类问题
- **ACPX args 数组**: agents.config 支持可选 args 数组，含空格的路径和标志值正确传递
- **Active Memory 增强**: 支持 `plugins.entries.active-memory.config.toolsAllow` 自定义记忆插件工具名

### CLI 体验
- **错误信息大改进**: parser、startup、config、guardrail、channel、agent、task、session、MCP 失败时都会解释发生了什么并指向恢复命令
- **`openclaw path` 命令**: 新增可选 bundled oc-path 插件，用于 `oc://` 协议访问 workspace 文件

### 插件/SDK
- **统一模型目录注册**: SDK 支持 text/image/video/music provider 的统一注册
- **展示助手**: controls-only 交互渲染和 opt-in empty fallback text
- **受保护的插件安装**: onboarding 和 repair 测试可通过环境变量路由到 registry specs

### 通道增强
- **Telegram**: grammY API 限流器在 polling 和 ad hoc 客户端间共享，统一配额门控
- **Telegram/Feishu**: 遵守 per-agent 和 global `reasoningDefault` 值，控制推理预览流式或隐藏

### 运维
- **Docker**: runtime 镜像改用 tini 运行，正确处理孤儿进程回收和信号转发
- **日志脱敏**: 脱敏引用的 HTTP 客户端 secret 字段和 auth/cookie 头
- **Task Ledger RPC**: 稳定化 tasks.list/get/cancel RPC 接口

### 模型
- **GitHub Copilot**: 刷新模型目录，新增 gpt-5.5，支持动态发现
- **Google Gemini**: 标准化退休的 gemini-3-pro-preview 和 gemini-3-pro-prev

---

## 🔍 分析

### 值得关注的
1. **版本差距大**: 我们落后 2 个月，建议评估升级
2. **CLI 错误信息改进**: 对我们排查问题有帮助
3. **Active Memory 增强**: 可能影响我们的 memory_search/memory_get 流程
4. **Docker tini**: 我们跑在 Docker 里，信号转发改进值得关注

### 不影响当前的
- 模型目录注册 / SDK 变更（主要影响插件开发者）
- 展示助手（富通道渲染）

---

## 📝 建议

1. **考虑升级 OpenClaw**: 版本差距大，新功能多
2. **关注 Active Memory 变更**: 可能影响现有记忆系统
3. **Docker tini 改进**: 长期运行稳定性提升
