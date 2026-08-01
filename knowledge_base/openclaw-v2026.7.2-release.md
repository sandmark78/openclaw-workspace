# OpenClaw v2026.7.2-beta.5 发布说明

**发布日期**: 2026-07-28  
**当前版本**: v2026.3.8 (我们运行的)  
**最新版本**: v2026.7.2-beta.5 (beta)  
**状态**: ⚠️ 落后 4 个月版本，建议评估升级

---

## 🔥 核心亮点

### 1. 状态安全与恢复
- 隔离存储 (quarantine store)：主数据库损坏时仍能存活
- 崩溃可恢复的 SQLite 快照
- 崩溃持久化的文件系统发布
- Schema 升级数据丢失拒绝机制
- 回滚写入器快照恢复

### 2. 持久通道投递
- 网关重启和本地崩溃后消息可恢复
- 共享入口排空 (ingress drain) + 死信恢复
- 覆盖：Telegram, Signal, Slack, QQBot, Twitch, Synology Chat, Tlon, IRC, Zalo

### 3. 会话倒带与分支
- 从单条消息倒带或分叉对话
- 跨 Web 和原生应用切换转录分支
- 分叉上游 Codex 会话
- 分支安全的排队发送

### 4. 交互式 MCP 应用和仪表板
- 托管带票据的 MCP 应用（绑定工具、资源、有界上下文更新）
- 从通道回复打开，固定到持久仪表板
- 共享沙箱加固
- 原生插件可直接声明 MCP 应用

### 5. 问题和审批无处不在
- Agent 可以跨 Web、通道、macOS、原生应用提出结构化问题（选项卡片）
- 审批获得推送通知、历史记录、公平排队、无头解决
- Claude 工具请求中继

### 6. 会议和实时 Talk
- 加入 Teams、Zoom、Google Meet 通话
- 默认启用会议插件 + 持久转录收集
- 实时 Talk 新增 OpenAI 和 Gemini 视频 + GPT Live (Codex OAuth)

### 7. Wear OS 伴侣
- 手机代理的 Wear 伴侣
- 主屏 Agent/会话/模型选择
- 实时 Talk 控制、音频响应播放、即时对话磁贴

### 8. 引导式设置和本地推理
- 跨浏览器、Linux、macOS 引导设置
- 本地提供商检测、最强模型选择
- 可下载模型、精简模式
- 进程内 RAM 门控 llama.cpp/Gemma 路径

---

## 🆕 新模型和提供商

- **Claude Opus 5** - 新增到目录和运行时
- **Kimi K3** - 新增
- **GPT Live** - 通过 Codex OAuth

---

## 🧠 记忆改进

- 快速主动记忆召回
- 默认跨对话召回（个人安装）
- 从 Claude Code/Codex/Hermes 引导导入
- 专用记忆设置页面

---

## ⏰ 调度改进

- 每任务动态节奏
- 门控脚本负载
- 持久调度源流
- Cron 支持的心跳监控
- 心跳任务转换
- 当前对话默认值
- `/loop` 命令

---

## 🔒 安全修复（重要）

- 防止通道允许列表授予所有者访问权限
- 保持会话导出在工作区内
- 关闭伪造标记/Web 搜索边界绕过
- 防止非所有者 ACP 会话暴露
- 拒绝不安全的显式审批 ID
- 加固秘密编辑和 exec/OAuth 审批
- 验证下载的安装脚本
- 防止不安全的 secrets-plan 写入

---

## 📊 升级评估

### 收益
- ✅ 重大安全修复（多个漏洞修补）
- ✅ 状态安全（崩溃恢复、数据保护）
- ✅ 持久通道投递（消息不丢失）
- ✅ 会话分支（更灵活的对话管理）
- ✅ MCP 应用（新的交互模式）
- ✅ 本地推理支持（llama.cpp/Gemma）
- ✅ 新模型支持（Claude Opus 5, Kimi K3）

### 风险
- ⚠️ 当前版本是 beta (v2026.7.2-beta.5)
- ⚠️ 跨 4 个月版本，可能有破坏性变更
- ⚠️ 需要测试现有技能和配置兼容性

### 建议
1. 等待稳定版发布（非 beta）
2. 先在测试环境验证
3. 备份当前配置和数据库
4. 逐步升级：先检查 CHANGELOG 中的破坏性变更

---

## 🔗 链接

- GitHub Release: https://github.com/openclaw/openclaw/releases/tag/v2026.7.2-beta.5
- 完整变更日志: https://github.com/openclaw/openclaw/blob/main/CHANGELOG.md

---

*记录时间: 2026-07-31 20:00 UTC*
*记录者: Sandbot 🏖️*
