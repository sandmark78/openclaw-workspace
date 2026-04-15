# OpenClaw v2026.3.13-1 Release Notes

**来源**: GitHub Releases (https://github.com/openclaw/openclaw/releases)
**发布日期**: 2026-03-14
**记录时间**: 2026-03-22 20:01 UTC
**数量**: ~35 知识点

---

## 概述

v2026.3.13-1 是一个恢复版本（recovery release），因 GitHub immutable releases 不允许复用 v2026.3.13 tag。npm 版本仍为 2026.3.13。包含 35+ PR 合并，涵盖压缩修复、安全加固、移动端改进、多通道增强。

---

## 核心修复

### 1. 压缩系统 (Compaction)
- **全会话 token 计数**: 压缩后健全性检查使用全会话 token 计数 (#28347)
- **人格/语言连续性**: 压缩摘要中保留 persona 和语言连续性 (#10456) ⭐ **对多语言用户极其重要**

### 2. 会话管理
- **Session reset 保留**: 重置时保留 lastAccountId 和 lastThreadId (#44773)
- **Azure 内容过滤**: 重写 session reset prompt 避免触发 Azure 内容过滤 (#43403)
- **跨 Agent 子代理**: 修复跨 Agent subagent spawn 的目标 workspace 解析 (#40176)

### 3. Cron 系统
- **嵌套 lane 死锁**: 防止 isolated cron 嵌套 lane 死锁 (#45459) ⭐ **对我们的 Cron 任务直接相关**

---

## 安全加固

- **Docker token 泄露**: 防止 gateway token 在 Docker build context 中泄露 (#44956)
- **Telegram SSRF**: 将媒体传输策略线程化到 SSRF 防护 (#44639)

---

## 移动端改进

### Android
- **聊天设置 UI 重设计** (#44894)
- **Google Code Scanner**: onboarding QR 码使用 Google Code Scanner (#45021)
- **HttpURLConnection 泄漏修复**: TalkModeVoiceResolver 中的连接泄漏 (#43780)

### iOS
- **Onboarding welcome pager**: 新增引导欢迎页 (#45054)

---

## 通道增强

### Slack
- **Interactive reply directives**: 新增 opt-in 交互式回复指令 (#44607, #45463)

### Discord
- **Gateway metadata fetch failures**: 处理 Discord 网关元数据获取失败 (#44397)

### Signal
- **Groups config**: 添加 Signal 通道 groups 配置到 schema (#27199)

---

## 平台改进

### Docker
- **OPENCLAW_TZ**: 新增时区环境变量支持 (#34119) ⭐ **Docker 部署用户可直接设置时区**

### Windows
- **Console 窗口隐藏**: 重启和进程清理时隐藏可见的控制台窗口 (#44842)

### Ollama
- **隐藏 reasoning-only 输出**: 对原生推理模型隐藏 reasoning-only 输出 (#45330)

---

## UI 改进

- **移动端导航抽屉**: 新增移动端导航抽屉和主题变体优化 (#45107)
- **滚动提示按钮**: 恢复 chat-new-messages 类在滚动提示按钮上 (#44856)
- **Sidebar 状态优化**: Polish sidebar status, agent skills, chat rendering (#45451)
- **Control UI 认证**: 在不安全连接上保持共享认证 (#45088)

---

## 其他修复

- **Agent 兼容性**: 尊重非原生 openai-completions 的显式用户 compat 覆盖 (#44432)
- **Memory 文件去重**: 避免在大小写不敏感挂载上注入 memory 文件两次 (#26054)
- **Anthropic thinking blocks**: 在 replay 时丢弃 Anthropic thinking blocks (#44843)
- **Delivery 去重**: 解决 delivery dedupe review 后续问题 (#44666)
- **Updater 修复**: 服务重装时修复 updater refresh cwd (#45452)
- **默认模型更��**: 测试中从 gpt-5.3-codex 更新到 gpt-5.4 (#44367)

---

## 对 Sandbot 的影响

| 变更 | 影响 | 优先级 |
|------|------|--------|
| 压缩人格连续性 | 中文对话压缩后保持语言一致 | ⭐ 高 |
| Cron 死锁修复 | 我们的 Cron 任务稳定性提升 | ⭐ 高 |
| Docker TZ 支持 | 可设置 OPENCLAW_TZ=Asia/Shanghai | 中 |
| 跨 Agent workspace | 子 Agent 调用更可靠 | 中 |
| Telegram SSRF | 安全性提升 | 低 |

---

## 文档更新 (docs.openclaw.ai)

- **Node 24 推荐**: 文档现在推荐 Node 24，Node 22 LTS (22.16+) 作为兼容选项
- **Pi agent**: 文档提到 "Pi agent" 和 "Pi binary in RPC mode" 作为默认 agent
- **Signal 通道**: 文档结构中包含 Signal 通道支持

---

## ClawHub 状态

- 首页仍显示 "No highlighted skills yet" 和 "No skills yet. Be the first."
- 市场仍处于早期阶段，发布技能可获得先发优势
