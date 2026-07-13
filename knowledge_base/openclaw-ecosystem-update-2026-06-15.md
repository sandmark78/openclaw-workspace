# OpenClaw 生态探索 - 2026-06-15

**探索时间**: 2026-06-15 20:00 UTC
**来源**: clawhub.ai / docs.openclaw.ai / GitHub Releases
**状态**: 🆕 有新版本

---

## 变更摘要

| 来源 | 状态 | 详情 |
|------|------|------|
| ClawHub.ai | 📭 无变化 | 52.7k 工具 / 180k 用户 / 12M 下载 / 4.8 评分 |
| docs.openclaw.ai | 📭 无变化 | 文档内容未更新 |
| GitHub OpenClaw Releases | 🆕 **新版本** | 预发布 **2026.6.8** (2026-06-14) ← **新发布** |
| GitHub ClawHub Releases | 🆕 **多版本** | 0.21.0 / 0.20.2 / 0.20.0 / 0.19.x (6月3日以来) |

---

## 🆕 GitHub OpenClaw Release 2026.6.8 要点 (Pre-release, 2026-06-14)

### 1. Telegram & WhatsApp 频道交付增强 🔥
- Telegram 可发送结构化富文本（表格、列表、可扩展 blockquotes）
- 支持 prompt-preserving CLI 后端交付
- 已退役 native draft 迁移
- 更安全的富媒体边界处理
- **WhatsApp 现在尊重配置的 ACP 绑定** 🔒

### 2. Agent & Gateway 恢复能力全面升级
- 账号作用域 DM 发送修复
- 生成媒体补全改进
- 自动回复消息工具最终回复优化
- 重置归档 fallback 读取修复
- 重启关闭中止处理
- 生成的子 agent 暂停处理
- 可信子 agent thinking 覆盖 fallback
- **心跳去重 (heartbeat dedupe)** ⚡
- 会话身份提示优化
- 未知 OpenAI agent selector 拒绝

### 3. 提供商/模型处理扩展与收紧
- **GLM-5.2 上线** 🆕
- **Claude Haiku 4.5 上线** 🆕
- OpenRouter 和 Google Vertex 提供商前缀规范化
- Managed SecretRef auth 支持
- OAuth image-default routing 通过 Codex
- 有界模型 browse 发现
- LM Studio 二进制 thinking-off 交付
- Storeless OpenAI Responses replay gating
- **Anthropic thinking-signature 恢复** (通用化) 🔧
- Claude 4.5 Copilot 工具流安全
- OpenAI/Anthropic 负载隔离（不可读或后 hook 工具 schema）

### 4. /usage & 回复 payload 钩子
- **原生全 footer 渲染器** 🆕
- 默认模板支持
- 固定小数点格式化
- 凭证感知限制
- 改进的部分计数处理
- 模板错误警告（不再静默失败）

### 5. UI & 移动端优化
- 工作区文件可折叠和默认折叠
- WebChat 回滚在流式传输中存活
- 侧边栏会话选择器在桌面工作区上方保持交互
- 重置软参数在 UI 分发中存活
- 过时仪表板会话父系保留
- **iOS 重新连接过时的前台 Gateway** 📱

---

## 🆕 ClawHub CLI 近期版本 (6月3日以来)

| 版本 | 日期 | 要点 |
|------|------|------|
| **0.21.0** | 2026-06-11 | 新增 trusted-publisher set/delete 命令 (GitHub Actions OIDC 信任发布) |
| **0.20.2** | 2026-06-11 | Node.js 要求升至 ≥22，新增 `clawhub package validate` 本地验证 |
| **0.20.0** | 2026-06-06 | 扫描报告改为存储下载模式 (`clawhub scan download --version`) |
| **0.19.2** | 2026-06-05 | `clawhub skill verify --json` 兼容层 |
| **0.19.1** | 2026-06-05 | 源备份 GitHub skill 安装修复 |
| **0.19.0** | 2026-06-03 | 认证扫描提交/轮询、Skill Card 验证、ClawScan 判决 |

---

## 当前运行版本提醒

- **运行版本**: OpenClaw 2026.3.8
- **最新正式版**: 2026.6.5 (估计)
- **最新预发布**: **2026.6.8** 🆕 (2026-06-14)
- **落后**: 约 3 个月

---

## 🎯 值得关注的新变化

1. **心跳去重** — 我们的定时心跳 cron 可能受益于这个修复，减少重复触发
2. **Telegram 富文本** — 我们使用 Telegram 通道，这个增强可能改善消息格式
3. **GLM-5.2 & Claude Haiku 4.5** — 新的模型选项
4. **ClawHub CLI 0.20.2** — 要求 Node.js ≥22，我们运行的是 v22，需要确认兼容性
5. **iOS 重连修复** — 如果老大使用 iOS node 值得关注

---

## 建议

预发布 2026.6.8 包含大量 Telegram 增强（我们直接受益）、心跳去重修复和模型扩展。建议关注正式版 2026.6.x 发布后考虑升级。
