# OpenClaw 生态探索 - 2026-04-23

**抓取时间**: 2026-04-23 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, GitHub releases

---

## 1. ClawHub (clawhub.com → clawhub.ai)

- 域名重定向持续有效
- 数据：**52.7k tools / 180k users / 12M downloads / 4.8 avg rating**
- 与昨日完全一致，无增长变化

---

## 2. docs.openclaw.ai

- 文档站点正常运行
- 核心定位不变：自托管 AI Agent 网关，多通道支持
- 无显著结构性变化

---

## 3. GitHub Releases - ⚠️ 新 Release (4/23)

### Release 2026.4.22 (4月23日发布，版本号 2026.4.22)

这是今日最大的发现，更新量非常大：

**语音/图像/多模态：**
- 🎨 **Providers/xAI**: xAI 全面支持 — 图像生成 (grok-imagine-image/pro)、参考图编辑、6种实时 xAI 语音、MP3/WAV/PCM/G.711 TTS 格式、grok-stt 音频转录、xAI 实时语音通话转录
- 🎙️ **Providers/STT**: Voice Call 流式转录新增 Deepgram、ElevenLabs、Mistral 支持；ElevenLabs 新增 Scribe v2 批量音频转录

**终端/用户体验：**
- 💻 **TUI**: 新增本地嵌入模式 — 无需 Gateway 即可运行终端聊天，同时保留插件审批门控
- 👤 **Control UI/settings+chat**: 新增浏览器本地个人身份（名称+安全头像），优化 Quick Settings、Agent 回退芯片、窄屏聊天布局

**搜索/模型：**
- 🔍 **OpenAI/Responses**: OpenAI 原生 web_search 工具自动用于 Direct Responses 模型，无需托管搜索 provider
- 🧩 **Models/commands**: 新增 `/models add` 命令，聊天中注册模型无需重启网关

**WhatsApp 强化：**
- 💬 **WhatsApp**: 新增可配置原生回复引用 (replyToMode)
- 📋 **WhatsApp/groups+direct**: 支持 per-group/per-direct systemPrompt 配置，支持 "*" 通配符回退和 account 级别覆盖

**Agent/Session 管理：**
- 📮 **Agents/sessions**: sessions_list 新增邮箱式过滤器 — 支持按 label、agent、search 过滤，以及可见性范围标题和最后消息预览

**基础设施：**
- 🔧 **Onboarding**: 设置时自动安装缺失的 provider 和 channel 插件
- 📊 **Gateway/diagnostics**: 默认启用无 payload 稳定性记录，新增支持就绪的诊断导出（ sanitized 日志+状态+健康+配置+稳定性快照）
- ☁️ **Providers/Tencent**: 新增腾讯云 provider 插件（TokenHub 对接、Hy3 预览模型、分层定价元数据）
- 🤖 **Providers/Amazon Bedrock Mantle**: 通过 Mantle 的 Anthropic Messages 路由支持 Claude Opus 4.7，provider 自有 bearer-auth 流式传输
- 🧠 **Providers/GPT-5**: GPT-5 prompt overlay 移入共享 provider runtime，兼容的 GPT-5 模型通过 OpenAI/OpenRouter/OpenCode/Codex 等统一获得相同行为和心跳指导

---

## 对比上次检查 (2026-04-22)

| 项目 | 变化 |
|------|------|
| ClawHub 数据 | 无变化 (52.7k/180k/12M/4.8) |
| GitHub Release | 新增 1 个 release (2026.4.22，4/23发布) |
| 文档站点 | 无显著变化 |
| 关注点 | xAI 多模态、STT 扩展、TUI 本地模式、WhatsApp 强化、Claude Opus 4.7、腾讯云 provider、GPT-5 统一化 |

---

## 与我们相关的重点

1. 🎙️ **xAI 全面多模态支持** — 图像+语音+转录一体化，如果未来考虑 xAI 作为 provider
2. 💻 **TUI 本地嵌入模式** — 无 Gateway 终端聊天，适合轻量部署场景
3. 🔍 **OpenAI 原生 web_search** — 自动使用，减少配置复杂度
4. 🧩 **/models add 免重启** — 更灵活地切换模型，适合我们的成本优化需求
5. 📮 **sessions_list 邮箱过滤** — 更高效的会话管理
6. ☁️ **腾讯云 provider** — 国内 provider 选项增加，可能有成本优势
7. 🤖 **Claude Opus 4.7 via Bedrock** — 最高质量模型的新路由
8. 🧠 **GPT-5 统一化** — 跨 provider 行为一致化

---

*生态探索记录 - 2026-04-23*
