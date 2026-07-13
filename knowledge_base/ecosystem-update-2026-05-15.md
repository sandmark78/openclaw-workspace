# 生态探索更新 2026-05-15

**检查时间**: 2026-05-15 20:00 UTC

---

## 🔴 发现：OpenClaw 版本差距扩大

| 项目 | 值 |
|------|-----|
| 当前安装版本 | 2026.3.8 |
| npm 最新版本 | **2026.5.12** |
| 上次检查版本 | 2026.5.7 (2026-05-08) |
| GitHub 最新 beta | v2026.5.14-beta.2 |
| 版本差距 | 落后约 2.5 个月 (+5 个版本) |
| 升级命令 | `openclaw gateway update` 或 `npm install -g openclaw@latest` |

---

## 🆕 5/8 ~ 5/15 重要版本变更

### 2026.5.12 (npm 最新稳定版)

**Agent/上下文**:
- `/context map` — 发送当前会话上下文贡献者的树状图 (#7987)
- Agent 间 ping-pong 轮数上限提升至 20（默认仍为 5）(#52400)
- 精简默认系统 prompt，减少 prompt token 消耗
- 支持 per-agent tools.message.crossContext 跨上下文策略
- 支持 per-agent tools.message.actions.allow 发送权限覆盖

**Cron**:
- 新增 `cron get` 命令，可按 ID 检查单个 cron 任务 (#75117)

**Control UI**:
- 子 Agent 会话在 session picker 中以 └─ 前缀嵌套显示 (#78623)
- 空白页面恢复面板（app 模块未注册时的故障恢复路径）(#44107)
- Progress draft 命令预览行宽度增加 50%

**安全**:
- 新增 per-sender tool policies，可按发送者身份限制危险工具 (#66933)

**构建**:
- 升级到 pnpm 11 工作区管理 (#79414)
- 更严格的 TypeScript 编译器检查（implicit returns, side-effect imports 等）
- 更严格的 Vitest lint 规则

**Slack 大量修复**:
- 支持 unfurlLinks/unfurlMedia 配置 (#80145)
- 支持 replyBroadcast 广播回复 (#64365)
- 修复 mention 元数据保留 (#75356)
- 修复 DM 投递镜像路由 (#80111)

**Discord Voice**:
- 实时语音诊断（speaker turns, playback resets, barge-in 检测）
- 可选 native @discordjs/opus 解码器
- voice.allowedChannels 限制语音加入频道

**其他**:
- Fly Machines 容器环境自动检测 (#80209)
- Fal 提供商支持 GPT Image 2 / Nano Banana 2 编辑
- Models localService 本地模型服务启动支持
- Memory wiki 需要 admin/write scope 限制 (#80897, #80904)
- Docs 导航重命名：tools → Capabilities
- Codex app-server 超时客户端退役

### v2026.5.14-beta.2 (GitHub 预发布, 5月15日)

**WhatsApp**:
- StatusReactionController 接入 WhatsApp 消息生命周期（queued→thinking→tool→done/error）
- 新 emoji 状态指标：🧠 thinking, 🛠️ tool, 💻 coding, 🌐 web, ⏳ stallSoft, ⚠️ stallHard, ✅ done, ❌ error

**Canvas**:
- 延迟加载 HTTP host、媒体解析器、CLI 实现，降低 Gateway 启动开销 (#82001)

**Agent**:
- 支持 per-agent bootstrap profile 覆盖（contextInjection, bootstrapMaxChars 等）(#69966)

**Plugin SDK**:
- 废弃公开子路径，逐步统一 SDK 接口
- 暴露运行时 active model metadata 给原生插件 (#77857)

**依赖**:
- 路由通过 @openclaw/proxyline 代理，移除 root proxy-agent 等依赖

**Codex**:
- 移除捆绑的 codex-cli 后端，修复 legacy 路由
- commentary preambles 流式编辑

**Control UI i18n**:
- 新增 pnpm ui:i18n:report 基线报告 (#81320)

---

## 🟡 ClawHub 生态数据（无变化）

- 工具总数: 52.7k
- 用户数: 180k
- 下载量: 12M
- 平均评分: 4.8

与上次检查一致。

---

## 🟢 Docs 扫描（无显著变化）

docs.openclaw.ai 结构稳定。
Node.js 推荐: Node 24（推荐）或 Node 22 LTS (22.16+)。
支持通道: Discord, Google Chat, iMessage, Matrix, Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等。

---

## 📊 与历史版本对比

| 日期 | 最新版本 | 变化 |
|------|----------|------|
| 2026-05-06 | 2026.5.6 | — |
| 2026-05-08 | 2026.5.7 | +1 版本 |
| 2026-05-15 | **2026.5.12** | +5 版本，大量 Agent/安全/UI 改进 |

---

## ⚠️ 建议

1. **强烈建议升级**: 当前 2026.3.8 → 最新 2026.5.12，落后 2.5 个月
2. **安全改进**: per-sender tool policies (#66933) 可直接增强我们 7 子 Agent 的安全性
3. **Cron 增强**: cron get 命令方便我们调试定时任务
4. **Control UI 改进**: 子 Agent 嵌套显示对我们多 Agent 运维很有帮助
5. **WhatsApp 状态反应**: 如未来接入 WhatsApp 通道可关注
