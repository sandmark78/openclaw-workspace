# OpenClaw 生态探索 - 2026-04-24

**抓取时间**: 2026-04-24 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, GitHub releases  
**当前安装版本**: 2026.3.8  
**最新稳定版本**: 2026.4.23 (2026-04-24 发布)

---

## 1. ClawHub (clawhub.com → clawhub.ai)

- 域名仍重定向到 **clawhub.ai**
- 最新统计：
  - **52.7k** 工具 (skills + plugins)
  - **180k** 用户
  - **12M** 下载量
  - **4.8** 平均评分
- 分类：Skills（技能包）、Plugins（网关插件）、Builders（社区创作者）
- 持续作为社区驱动的 AI Agent 技能市场

---

## 2. docs.openclaw.ai

- 正常运行，文档结构无明显变化
- 核心定位不变：自托管多通道 AI Agent 网关
- 推荐 Node 版本仍为 **Node 24**（推荐）或 Node 22 LTS (22.14+)
- 支持的通道：Discord, Google Chat, iMessage, Matrix, Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
- 新增提及：**macOS app** 作为 Gateway 界面之一

---

## 3. GitHub Releases - ⚠️ 新稳定版 2026.4.23

自上次记录 (2026-04-11 pre-release) 以来的重大更新：

### 🔥 新特性

| 特性 | 说明 |
|------|------|
| **OpenAI 图片生成** | 通过 Codex OAuth 支持 gpt-image-2，无需 OPENAI_API_KEY |
| **OpenRouter 图片生成** | 通过 image_generate 支持 OpenRouter 图片模型 |
| **图片质量/格式控制** | Agent 可请求 provider 支持的质量和输出格式 |
| **Subagent forked context** | sessions_spawn 可选继承请求者上下文 |
| **生成工具超时控制** | image/video/music/TTS 工具支持 per-call timeoutMs |
| **本地 embedding 可调** | memorySearch.local.contextSize 默认 4096，可自定义 |
| **Pi 0.70.0** | 更新到 gpt-5.5 目录元数据 |
| **Codex 调试日志** | 结构化日志解释自动选择和 Pi 回退原因 |

### 🐛 重要修复

| 修复 | 影响 |
|------|------|
| **Telegram 媒体回复** | 群聊中 markdown 图片语法正确解析为媒体载荷 |
| **WhatsApp 安装** | 首跑设置不依赖 Baileys 运行时 |
| **Slack 群组** | MPIM 群聊正确分类，内部 trace 不再泄露 |
| **流式消息去重** | 修复块中止后的重复回复问题 |
| **WebChat 错误展示** | 账单/认证/限流错误正确显示 |
| **Codex Windows 兼容** | codex.cmd shim 通过 PATHEXT 正确解析 |
| **WebChat 图片附件** | 纯文本模型的图片不再丢失，转为媒体引用 |
| **媒体理解配置** | 优先使用显式图片模型配置 |
| **OpenAI Codex OAuth** | 合成 gpt-5.5 模型行，cron/subagent 不报 Unknown model |
| **记忆/CLI** | 本地 embedding provider 在 standalone CLI 中可用 |

---

## 对比上次检查 (2026-04-11)

| 项目 | 变化 |
|------|------|
| ClawHub | 用户量/下载量统计更新 (52.7k/180k/12M) |
| GitHub Release | 新稳定版 2026.4.23 (距离 04-11 pre-release 约 2 周) |
| 文档站点 | 新增 macOS app 提及，其余无重大变化 |
| 当前版本 | 2026.3.8 → 最新 2026.4.23（落后 ~1.5 个月） |

---

## 建议行动

1. ⬆️ **强烈建议升级**：当前 2026.3.8 落后最新版 2 个大版本，含多项 Bug 修复
2. 📸 **Telegram 图片修复**：群聊 markdown 图片语法终于修复，对我们有用
3. 🖼️ **图片生成支持**：新增 OpenAI/OpenRouter 图片生成，可探索新玩法
4. 🔧 **Subagent forked context**：子 Agent 可继承父上下文，优化联邦架构

---

*自动生成于心跳任务，下次检查建议：2026-04-27*
