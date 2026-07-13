# OpenClaw 生态探索扫描 (2026-04-25 20:00 UTC)

**扫描时间**: 2026-04-25 20:00 UTC
**当前版本**: 2026.3.8
**最新版本**: 2026.4.24 (2026-04-25 发布)
**状态**: ⚠️ 有可用更新 (落后 ~1.5 个月)

---

## ClawHub 平台数据

- 域名重定向: clawhub.com → clawhub.ai
- 工具总数: **52,700**
- 用户总数: **180,000**
- 下载总量: **12,000,000**
- 平均评分: **4.8**
- 分类: Skills / Plugins / Builders

---

## 2026.4.24 更新亮点 (当前未安装)

### 🆕 Google Meet 集成
- 新增捆绑参与者插件
- 支持个人 Google 认证、Chrome/Twilio 实时传输
- 支持配对节点 Chrome (Parallels 式 Chrome/BlackHole/SoX)
- 会议记录、转录、智能笔记、出勤导出
- OAuth 和浏览器状态恢复工具

### 🆕 DeepSeek V4 Flash & V4 Pro
- 加入捆绑模型目录
- V4 Flash 成为 onboarding 默认模型
- 修复了 DeepSeek thinking/replay 在 follow-up tool-call 轮次的行为

### 🆕 实时语音循环
- Talk、Voice Call、Google Meet 均可使用实时语音循环
- 咨询完整 OpenClaw Agent 获取深度工具支持答案
- Voice Call 新增 voicecall setup 和 dry-run smoke 命令
- 新增 Gemini Live 实时语音 provider (双向音频 + 函数调用)
- VoiceClaw: 实时大脑 WebSocket 端点 (Gemini Live 后端)

### 🆕 浏览器自动化增强
- 视口坐标点击 (coordinate clicks)
- 默认动作预算 60 秒
- 每 profile 无头模式覆盖
- 更稳定的标签页复用和恢复
- 新增 browser.click-coords CLI

### 🆕 Control UI 改进
- Agent Tool Access 面板优化 (实时工具 chips、可折叠工具组、逐工具切换)
- 聊天消息新增 Steer 动作 (可注入 follow-up 到活跃运行中)

### ⚠️ Breaking Change
- Plugin SDK/tool-result transforms: 移除 Pi-only `api.registerEmbeddedExtensionFactory(...)` 兼容路径
- 捆绑工具结果重写必须使用 `api.registerAgentToolResultMiddleware(...)`

---

## docs.openclaw.ai 关键信息

- 推荐 Node.js: **Node 24** (或 Node 22 LTS 22.14+)
- 安装: `npm install -g openclaw@latest`
- 引导: `openclaw onboard --install-daemon`
- 支持频道: Discord, Google Chat, iMessage, Matrix, Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
- MIT 开源许可

---

## 建议

1. **版本升级**: 从 2026.3.8 → 2026.4.24，建议升级
2. **关注**: Google Meet 插件对会议场景有价值
3. **关注**: DeepSeek V4 Flash 作为默认模型可能更经济
4. **注意**: 升级前检查是否有自定义 plugin 使用了已废弃的 `registerEmbeddedExtensionFactory`
