# OpenClaw 生态探索记录 — 2026-05-05

**探索时间**: 2026-05-05 20:00 UTC  
**触发**: 定时生态探索 Cron

---

## 1. ClawHub (clawhub.com → clawhub.ai)

- 域名已重定向到 clawhub.ai
- 社区统计更新:
  - **52,700** 个工具 (Skills/Plugins)
  - **180,000** 用户
  - **1,200 万** 下载量
  - **4.8** 平均评分
- 三大板块: Skills(技能包)、Plugins(网关插件)、Builders(社区创作者)

---

## 2. GitHub Releases — 最新版本 2026.5.4 (2026-05-04)

### 🌟 亮点
- **Google Meet/Voice Call 重大升级**: Twilio 拨入接入 Gemini 实时语音桥接，支持节奏化音频流、背压缓冲、打断队列清空，无 TwiML 回退 → 语音 agent 响应速度大幅提升

### 重要变更

| 类别 | 内容 |
|------|------|
| **Windows 安全** | 默认网关绑定仅限 127.0.0.1，防止 IPv6 双栈问题 |
| **插件迁移** | 未安装的外部插件会给出 `openclaw plugins install` 提示 |
| **OpenAI Codex** | 支持 Codex 音频转录，chat 模型自动路由到转录默认 |
| **依赖更新** | Pi 0.73.0、ACPX adapters、OpenAI、Anthropic、Slack、TypeScript native preview |
| **性能优化** | 工作区范围的插件元数据快照复用，避免冷启动扫描 (#77519, #77532) |
| **插件自动启用** | WeCom/Yuanbao 别名正确解析到已安装插件 ID |
| **Secret 保留** | apply 时保留 auth-profile keyRef/tokenRef 字段 |
| **QQ 频道修复** | 会话存储中带 `:` 的 channel ID 不再导致 recall 子 agent 崩溃 (#77396) |
| **Discord 外部插件** | 修复 npm 发布的 Discord 插件 SecretRef 静默失败问题 |
| **新命令** | `openclaw models auth list [--provider] [--json]` 查看已保存的 auth profile |
| **Control UI** | 面包屑显示 agent 名称；cron 新建作业侧边栏可折叠；chat session picker 支持 agent-first 筛选；连续重复消息折叠 |
| **Slack** | 流式进度支持 Block Kit rich 渲染；progress draft 行数限制 |
| **子 agent** | 直接完成回退时保留所有分组子结果 |
| **TTS 电话** | Google Meet 语音合成正确应用 provider voice/model 覆盖 |
| **实时语音** | Twilio 音频队列背压保护，过载时关闭实时流 |
| **文档** | IRC 使用原始 TCP/TLS 连接说明 |

### 对比上次记录 (2026.4.25)
- 新增 Google Meet 语音桥接（重大功能）
- 新增 `openclaw models auth list` 命令
- 新增 Control UI chat agent-first 筛选
- 修复多个 Discord/QQ 频道相关 bug
- 插件元数据性能优化

---

## 3. docs.openclaw.ai

- 文档结构无明显变化
- Node 24 推荐，Node 22 LTS (22.14+) 兼容
- 支持通道: Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
- 核心概念未变: 自托管、多通道、Agent 原生、开源 MIT

---

## 总结

**有新变化** ✅
- 版本从 2026.4.25 → 2026.5.4（约 10 天前发布）
- Google Meet 实时语音是最大亮点
- 多处 UI 改进和 bug 修复
- ClawHub 社区持续快速增长（52.7k 工具，180k 用户）

**建议关注**:
1. 考虑更新 OpenClaw 到 2026.5.4
2. `openclaw models auth list` 命令可用于审查已保存的 auth profile
3. 插件性能优化可能对多实例部署有帮助
