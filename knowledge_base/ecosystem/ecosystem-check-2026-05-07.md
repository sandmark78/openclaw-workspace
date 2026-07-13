# 🌐 OpenClaw 生态探索 - 2026-05-07

**检查时间**: 2026-05-07 20:00 UTC  
**执行者**: Sandbot V6.4.0 (定时任务)

---

## 📊 当前版本对比

| 组件 | 当前版本 | 最新版本 | 差距 |
|------|----------|----------|------|
| OpenClaw | 2026.3.8 | 2026.5.6 | ⚠️ 落后 ~2 个月 |
| 模型 | bailian/qwen3.6-plus | - | ✅ 正常 |

---

## 🦞 ClawHub (clawhub.com → clawhub.ai)

- **域名变更**: clawhub.com 已重定向到 clawhub.ai
- **生态数据**:
  - 工具: 52.7k
  - 用户: 180k
  - 下载: 12M
  - 平均评分: 4.8
- **三大板块**: Skills (Agent skill bundles)、Plugins (Gateway plugins)、Builders (Community creators)

---

## 📚 Docs (docs.openclaw.ai)

- 推荐 Node.js 版本: **Node 24**（推荐）或 Node 22 LTS (22.16+)
- 支持通道: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
- 核心特性: 多通道、多 Agent 路由、媒体支持、Web Control UI、移动节点
- 安装方式: `npm install -g openclaw@latest`

---

## 🆕 GitHub Releases - 重要更新 (5/4 ~ 5/6)

### 2026.5.6 (最新, May 6)
- **Doctor/OpenAI Codex**: 修复了 5.5 版本误改 OAuth 路由的问题
- **Plugins/runtime fetch**: 修复第三方 symbol metadata 导致插件请求被拒
- **Debug proxy**: 修复 header 字典规范化问题
- **Web fetch**: 修复超时后 Gateway 工具通道残留活跃的问题 (#78439)

### 2026.5.5 (May 5) - 大版本修复
- **Feishu**: 修复飞书话题 starter thread ID 缺失导致的路由问题 (#78262) 🎯 *与我们相关*
- **Telegram/Codex**: 修复进度草稿重复显示 (#75641)
- **Discord**: 修复心跳 ACK 超时测量导致的误重连循环 (#77668)
- **Discord**: 修复控制命令被静默丢弃 (#78080)
- **iOS pairing**: 修复局域网/私有网关配对 (#47887)
- **Control UI**: 大量性能优化和 UI 改进 (checkpoint 历史、响应式布局)
- **Doctor/sessions**: 修复心跳污染的默认会话存储
- **Gateway/shutdown**: 修复快速重启后的后台定时器残留
- **Plugins/update**: 官方插件同步机制改进
- **Exec approvals**: Windows 兼容修复
- **Slack**: Socket Mode 错误上下文保留
- **WhatsApp**: 停止 degrade 事件循环的陈旧 TUI 客户端
- **TUI**: 修复会话选择器性能问题
- **Doctor/gateway**: 新增 supervisor 重启报告
- **CLI/sessions**: 自动清理孤立的转录/检查点文件 (#77608)
- **Doctor/Codex**: 修复 legacy openai-codex 路由

### 2026.5.4 (May 4) - 亮点
- **Google Meet/Voice Call**: 全新的 Twilio 拨入 + Gemini 实时语音桥接
- **Gateway/Windows**: 默认回环绑定改进

---

## ⚠️ 建议

1. **版本升级**: 当前 2026.3.8 → 最新 2026.5.6，落后约 2 个月，包含大量修复
2. **飞书修复**: 5.5 版本修复了飞书话题路由问题，我们使用飞书功能应关注
3. **Web fetch 修复**: 5.6 修复了超时工具通道问题，直接改善我们 cron 任务的可靠性
4. **Doctor 命令**: 升级后建议运行 `openclaw doctor --deep` 检查健康状态

---

## 🔗 链接

- Releases: https://github.com/openclaw/openclaw/releases
- Docs: https://docs.openclaw.ai
- ClawHub: https://clawhub.ai
