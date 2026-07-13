# OpenClaw GitHub Release 2026.5.11 (Pre-release)

**抓取时间**: 2026-05-11 20:00 UTC  
**发布时间**: 2026-05-11 16:38 UTC  
**版本**: Pre-release  
**上次记录版本**: 2026.4.29 (Latest) / 2026.5.4 (生态记录)

---

## 🌟 亮点

### Agent-to-Agent 对话能力大幅增强
- `session.agentToAgent.maxPingPongTurns` 上限提高到 **20**（默认保持 5），支持更长的 Agent 间多轮对话
- 新增 **per-agent tools.message.crossContext 覆盖**，沙箱/公共 Agent 可限制消息仅发送到当前会话
- 新增 **per-agent tools.message.actions.allow 覆盖**，可暴露和强制执行仅发送消息工具

### 图像生成/编辑增强 (Fal Provider)
- GPT Image 2 和 Nano Banana 2 参考图像编辑路由到 /edit，支持 image_urls 数组
- NB2 编辑强制使用 aspect_ratio 和 resolution 参数
- 输入图像上限提升：GPT Image 2 到 **10 张**，Nano Banana 2 到 **14 张**

### 上下文可视化
- 新增 **`/context` map 命令**：发送当前会话上下文贡献者的树状图 (treemap image)

---

## 重要变更

| 类别 | 内容 |
|------|------|
| **CI** | 非阻塞 plugin-inspector-advisory 工件，捕获插件兼容性分类 |
| **Runtime/Fly** | 从环境变量检测 Fly Machines 为容器环境，网关绑定和 Bonjour 默认值适配 |
| **Control UI** | 空白页面显示纯 HTML 恢复面板，含重试路径和浏览器扩展排障链接 |
| **Build** | 升级到 **pnpm 11** 工作区管理，对齐 Docker/install/update/release 流程 |
| **Build** | oxlint 新增低损耗规则 (promise/TypeScript/runtime footgun) |
| **Build** | Vitest 更严格 lint 规则 (focused/disabled/conditional/hook/matcher 危险) |
| **TypeScript** | 更严格编译器检查 (implicit returns/side-effect imports/overrides/unused code) |
| **Logging** | 定向模型传输/payload/SSE/code-mode 诊断，含 URL 脱敏 |
| **Agents** | 沙箱工作区标记从 compact 进度预览中隐藏 |
| **Agents** | Discord 内联工具更新进度草稿预览行宽增加 **50%** |
| **Codex** | 超时后终止 app-server 客户端，防止 Discord Agent 复用 CPU 空转进程 |
| **Telegram QA** | 对齐 pnpm 11 工作区构建白名单 |
| **Models** | 新增 provider 级 localService 启动，OpenAI 兼容请求前按需启动本地模型服务器 |
| **Slack** | 新增 unfurlLinks/unfurlMedia 配置，支持 per-account 覆盖 |
| **System Prompt** | 裁剪默认系统提示指导和仅发送消息工具 schema，减少 prompt token |

---

## 对我们 Sandbot 的影响分析

1. **Agent-to-Agent 增强**: 联邦架构子 Agent 间多轮对话能力提升到 20 轮，复杂协作场景受益
2. **`/context` map**: 新的上下文可视化工具，可用于诊断和优化上下文使用
3. **pnpm 11 升级**: 构建工具链更新，未来 install/update 流程可能变化
4. **localService**: 本地模型按需启动，为本地推理铺路
5. **Prompt 优化**: 默认系统提示裁剪减少 token 消耗，与我们的成本控制目标一致

---

## ClawHub 状态 (对比上次)

- 52,700 工具 — 与上次一致
- 180,000 用户 — 与上次一致
- 1,200 万 下载 — 与上次一致
- 4.8 平均评分 — 与上次一致
- 域名 clawhub.com → clawhub.ai 重定向 — 保持

---

## OpenClaw Docs 状态

- docs.openclaw.ai 正常运行
- 文档结构保持：快速开始/频道/插件/多 Agent/媒体/WebUI/移动节点
