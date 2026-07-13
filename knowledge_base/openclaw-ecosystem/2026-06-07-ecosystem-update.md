# OpenClaw 生态更新 - 2026-06-07

**记录时间**: 2026-06-07 20:00 UTC  
**当前本地版本**: 2026.3.8  
**GitHub 最新版本**: Pre-release (2026-06-07 00:26 UTC) — 有更新可用

---

## 🆕 GitHub Pre-release 亮点 (2026-06-07)

### 新增功能
1. **Parallel web_search 提供商** — 新捆绑的网页搜索提供商，通过 `PARALLEL_API_KEY` 发现，支持 api.parallel.ai/v1/search
2. **Google Chat 原生审批卡片** — Google Chat 审批使用平台原生卡片而非通用消息流
3. **ClawHub 技能 GitHub 仓库安装** — 支持通过解析的安装 API 安装由 GitHub 仓库支持的 ClawHub 技能，下载 pinned commit
4. **QMD 搜索 rerank 开关** — 记忆搜索可以使用新的 rerank 切换
5. **Windows Hub** — 新增 Windows 平台应用（Features 页面提及）

### 修复与改进
1. **QQBot** — 剥离模型 reasoning/thinking scaffolding，防止原始内容泄露到频道回复 (#89913, #90132)
2. **MCP tool results** — 在 materialize 边界强制转换 resource_link、resource、audio、 malformed image 等，防止 Anthropic 400 错误和会话历史污染 (#90710, #90728)
3. **Anthropic extended-thinking** — prompt-cache 过期或 Gateway 重启后会话可恢复，流开始事件等待 message_start (#90667, #90697)
4. **Google Vertex ADC** — 静态 catalog 行和运行时模型解析恢复，单提供商冷却恢复更可靠 (#90506, #90609, #90717, #90816)
5. **Matrix 语音笔记** — 可在 mention gate 前预检语音笔记，通过 Matrix relations 分页保留 thread reads/replies (#78016, #90415)
6. **Auth/插件持久化** — auth profiles 现在存储在 SQLite 中，npm 插件安装记录保留可信 pin，prerelease 完整性检查避免携带过期 integrity (#89102, #88585)
7. **macOS 节点模式** — 不再从健康的直连 Gateway 会话静默重连，减少意外 companion app 会话切换 (#90668, #90815)
8. **升级/服务路径** — cron 遗留 JSON 存储在 doctor preflight 时迁移，service env 占位符不再掩盖 state-dir secrets，WhatsApp 启动等待有上限，禁用的 WhatsApp 账户在 config reload 时拆除 (#90072, #90208, #90277, #90488, #90486)
9. **移动端改进** — Android 提供商/模型屏幕更清晰地展示过期、不可用、未解决和注意力状态；iOS 设置和 Talk 标签保持诊断、gateway 行、附件标签和不可用 Talk 控件可达

### 实验性功能更新
- `agents.defaults.experimental.localModelLean` — 为弱本地模型后端的压力释放阀，移除 browser/cron/message 三个大工具
- `memorySearch.experimental.sessionMemory` — 让 memory_search 索引之前的会话转录
- `tools.experimental.planTool` — 暴露结构化 update_plan 工具
- `plugins.entries.codex.config.appServer.experimental.sandboxExecServer` — Codex app-server 沙盒执行

---

## 📊 ClawHub 数据

| 指标 | 数值 |
|------|------|
| 工具总数 | 52,700 |
| 用户数 | 180,000 |
| 下载量 | 12M |
| 平均评分 | 4.8 |

页面结构：Skills / Plugins / Audits / Publishers  
发布功能：Publish Skill / Publish Plugin

---

## 📋 docs.openclaw.ai 关键信息

### 支持渠道
- **内置**: Discord, Google Chat, iMessage, IRC, Signal, Slack, Telegram, WebChat, WhatsApp
- **捆绑插件**: Feishu, LINE, Matrix, Mattermost, Microsoft Teams, Nextcloud Talk, Nostr, QQ Bot, Synology Chat, Tlon, Twitch, Zalo
- **可选安装**: Voice Call, WeChat 等第三方插件

### 模型提供商
- 35+ 模型提供商（Anthropic, OpenAI, Google 等）
- 支持 OAuth 订阅认证（如 OpenAI Codex）
- 自定义/自托管提供商（vLLM, SGLang, Ollama, OpenAI/Anthropic 兼容端点）

### 应用界面
- WebChat 和浏览器 Control UI
- macOS 菜单栏伴侣应用
- iOS 节点（配对、Canvas、摄像头、屏幕录制、定位、语音）
- Android 节点（配对、聊天、语音、Canvas、摄像头、设备命令）
- **Windows Hub** (新增)

---

## ⚡ 建议行动

1. **考虑更新** — 本地版本 2026.3.8，GitHub 有更新 pre-release，包含大量 bugfix 和新功能
2. **Parallel 搜索** — 可以尝试新的 Parallel web_search 提供商
3. **实验性功能** — localModelLean 对本地模型友好，sessionMemory 可增强记忆搜索
4. **ClawHub 增长** — 生态数据健康增长（52.7k 工具、180k 用户）

---

*由生态探索 cron 自动生成*
