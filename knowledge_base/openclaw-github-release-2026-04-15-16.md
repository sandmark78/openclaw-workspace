# OpenClaw GitHub Release 2026.4.15 & 2026.4.16 Pre-release

**抓取时间**: 2026-04-16 20:00 UTC  
**发布时间**: 2026-04-15 19:40 UTC & 2026-04-16 19:30 UTC  
**版本**: 预发布版本（Pre-release）  
**当前运行**: 2026.3.8（落后）

---

## 2026.4.16 Pre-release（最新）

### 新特性 (Changes)

#### 🧠 Anthropic/Models
- **默认 Anthropic 选择优化**: opus aliases, Claude CLI defaults
- **图像理解升级为 Claude Opus 4.7** — 绑定的图像理解能力升级

#### 🗣️ Google/TTS — ⭐ 新功能
- **新增 Gemini 文本转语音 (TTS) 支持**
- 包含 provider 注册、语音选择、WAV 回复输出、PCM 电话输出
- PR: [#67515](https://github.com/openclaw/openclaw/pull/67515) | Thanks @barronlroth

### 修复 (Fixes)

#### 🛡️ Gateway/Tools
- **安全加固**: 锚定可信本地 MEDIA 工具结果传递，基于注册内置工具的原始名称
- 拒绝名称规范化的客户端工具定义

---

## 2026.4.15 Pre-release

### 新特性 (Changes)

#### 🖥️ Control UI/Overview — ⭐ 新功能
- **新增 Model Auth 状态卡片**
- 显示 OAuth token 健康和 provider 速率限制压力
- 过期/即将过期 token 有醒目提示
- 基于新的 `models.authStatus` gateway 方法（剥离凭证，缓存 60s）
- PR: [#66211](https://github.com/openclaw/openclaw/pull/66211) | Thanks @omarshahine

#### 💾 Memory/LanceDB — ⭐ 新功能
- **云端存储支持**: 记忆索引可运行在远程对象存储上，不再局限于本地磁盘
- PR: [#63502](https://github.com/openclaw/openclaw/pull/63502) | Thanks @rugvedS07

#### 🔍 GitHub Copilot/Memory Search — ⭐ 新功能
- **新增 GitHub Copilot 嵌入 provider** 用于记忆搜索
- 专用 Copilot 嵌入 host helper，插件可复用
- 支持远程覆盖、token 刷新、安全 payload 校验
- PR: [#61718](https://github.com/openclaw/openclaw/pull/61718) | Thanks @feiskyer & @vincentkoc

#### 🤖 Agents/Local Models
- **实验性配置** `agents.defaults.experimental.localModelLean: true`
- 移除重型默认工具（browser, cron, message），减少 prompt 体积
- 适用于弱本地模型场景，不影响正常路径
- PR: [#66495](https://github.com/openclaw/openclaw/pull/66495) | Thanks @ImLukeF

#### 📦 Packaging/Plugins
- **本地化捆绑插件运行时依赖** 到各自扩展
- 精简发布的文档 payload
- 加强安装/包管理器防护
- 核心不再携带扩展拥有的运行时包袱
- PR: [#67099](https://github.com/openclaw/openclaw/pull/67099) | Thanks @vincentkoc

#### ✅ QA/Matrix
- 拆分 Matrix 实时 QA 为源码链接的 qa-matrix runner
- 仓库私有 qa-* 表面不再包含在打包/发布构建中
- PR: [#66723](https://github.com/openclaw/openclaw/pull/66723) | Thanks @gumadeiras

#### 📖 Docs/Showcase
- 添加可扫描 hero 区域、完整章节跳转链接
- 响应式视频网格展示社区示例
- PR: [#48493](https://github.com/openclaw/openclaw/pull/48493) | Thanks @jchopard69

### 修复 (Fixes)

#### 🛡️ Security/Approvals — ⭐ 安全修复
- **exec 审批提示中脱敏密钥**，防止审批审查时泄露凭据材料
- Issues: #61077, PR: #64790

#### ⚙️ CLI/Configure
- 写入后重新读取持久化配置 hash，避免 stale-hash race
- Issues: #64188, PR: #66528

#### ⬆️ CLI/Update
- npm 升级后修剪过时的打包 dist chunks
- 降级/验证库存检查保持兼容安全
- PR: #66959 | Thanks @obviyus

#### 🚀 Onboarding/CLI
- 修复全局安装 CLI 设置下频道选择崩溃
- PR: #66736

#### 🎬 Video Generation/Live Tests
- 限制 provider 轮询，默认快速非 FAL 文本转视频路径
- 使用 1 秒 lobster prompt 避免无限等待慢 provider 队列

---

## 🌐 ClawHub 状态

- 域名已跳转至 `clawhub.ai`
- 标语: "A versioned registry for AI agent skills"
- 支持 "Browse, install, and publish skill packs"
- 特性: "Versioned like npm, searchable with vectors, no gatekeeping"
- 安装命令: `npx clawhub@latest install <skill>`
- Staff Picks 和 Popular skills 分区

## 📖 docs.openclaw.ai

- 文档首页更新，包含完整的 Getting Started 指引
- 支持的频道: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
- 推荐 Node.js 24，兼容 Node 22 LTS (22.14+)

---

## 🔑 值得关注的新特性

1. **Gemini TTS 支持** — 新增语音输出能力，值得后续测试
2. **Memory 云端存储** — LanceDB 支持远程对象存储，适合多实例场景
3. **GitHub Copilot 嵌入** — 记忆搜索的新 provider
4. **localModelLean** — 本地模型轻量化配置选项
5. **Model Auth 状态卡片** — OAuth token 健康监控 UI
