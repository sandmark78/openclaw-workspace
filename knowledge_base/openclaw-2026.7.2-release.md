# OpenClaw 2026.7.2 发布说明

**抓取时间**: 2026-08-11 20:01 UTC  
**当前版本**: 2026.7.1  
**最新版本**: 2026.7.2  
**状态**: ⚠️ 落后一个版本

---

## 🎯 核心亮点

### 1. 状态安全与恢复
- 隔离存储区：主数据库损坏时仍可存活
- 崩溃可恢复的 SQLite 快照
- 崩溃持久的文件系统发布
- Schema 升级数据丢失拒绝
- 回滚写入器快照恢复

### 2. 持久通道投递
- 接受的消息在 Gateway 重启和本地崩溃时可恢复
- 共享入口排水 + 死信恢复
- 覆盖：Telegram, Signal, Slack, QQBot, Twitch, Synology Chat, Tlon, IRC, Zalo User

### 3. 会话倒带与分支
- 从单条消息倒带或分叉对话
- 跨 Web 和原生应用切换转录分支
- 分叉上游 Codex 会话
- 分支安全排队发送
- 拒绝过时面板写入
- 分叉后恢复提示图像

### 4. 交互式 MCP 应用和仪表板
- 托管带工具、资源和有界上下文更新的票务 MCP 应用
- 从通道回复打开，固定到持久仪表板
- 强化共享沙箱
- 原生插件可直接声明

### 5. 问题和审批无处不在
- Agent 可跨 Web、通道、macOS 和原生应用提出带选项卡的结构化问题
- 审批获得推送通知、历史、公平排队、无头解决
- Claude 工具请求中继、审阅者详情、更清晰的格式化提示

### 6. 会议和实时 Talk
- 加入 Teams、Zoom 和 Google Meet 通话
- 默认启用会议插件 + 持久转录收集
- 实时 Talk 添加 OpenAI 和 Gemini 视频
- 需要支持的 OpenAI Platform API 密钥

### 7. Wear OS 伴侣
- 手机代理 Wear 伴侣
- 主屏 Agent/会话/模型选择
- 实时 Talk 控制、音频响应播放
- 即时对话磁贴

### 8. 引导设置和本地推理
- 跨浏览器、Linux 和 macOS 引导设置
- 本地提供商检测、最强模型选择
- 可下载模型、精简模式、记忆导入
- 进程内 RAM 门控 llama.cpp/Gemma 路径

---

## 📦 模型与提供商

- **Claude Opus 5**: 跨目录和运行时添加
- **Kimi K3**: 新增支持
- **GPT Live 实时支持**: 使用支持的 Platform API 认证路径

---

## 🧠 本地推理

- 在 onboarding 期间检测本地推理提供商
- 添加进程内 llama.cpp GGUF 推理
- Baseten Model API 支持
- 从实时提供商目录发现模型
- 从 Web 和 macOS 设置提供模型下载

---

## 💬 通道更新

- **Buzz 插件**: 新增
- **Slack**: 用户身份和 Agent View 模式
- **Telegram**: Bot API 富块和原生 Markdown 列表
- **Matrix**: 更丰富的格式

---

## 🌐 浏览器与 MCP 应用

- 安全的每标签浏览器副驾驶
- 批量浏览器 CLI
- 有界页面问题提取
- 票务 MCP 应用主机和控制 UI 桥
- 清单声明的 MCP 应用（原生插件）

---

## 🧬 记忆系统

- 快速活动记忆召回
- 个人安装的默认跨对话召回
- 从 Claude Code/Codex/Hermes 引导导入
- 专用记忆设置页面

---

## ⏰ 调度系统

- 每作业动态节奏
- 门控脚本负载
- 持久调度源流
- Cron 支持的心跳监视器
- 心跳任务转换
- 当前对话默认值
- /loop 命令

---

## 🎙️ 语音

- **Fish Audio 语音**: 添加托管 S2.1 合成
  - 流式传输、语音笔记、语音发现、电话
  - 本地 Fish S2 Pro 参考语音流（原生 macOS Talk）

---

## 🔧 其他变更

- **自动化命名**: 将调度器面向 cron 的 Agent 工具和可见 CLI/UI 表面重命名为"Automations"
- **DuckDuckGo 搜索**: 移入插件边界
- **Control UI 设置**: 继续验证模型设置到 Custodian

---

## 📊 ClawHub 新技能

抓取时发现的新技能：
1. **self-improving-agent** (@pskoett) - 捕获学习、错误和修正以实现持续改进
2. **skill-vetter** (@spclaudehome) - 安全优先的技能审查
3. **office-toolkit** (@axelhu) - 处理 Office 文档（Word/Excel/PPT/PDF）
4. **tcm-jingfang** (@ahfai1) - 倪海厦人纪经方开药（中医）
5. **ai-video-generation** (@skills-101) - AI 视频生成
6. **ai-image-generation** (@skills-101) - AI 图像生成

---

## ⚠️ 升级建议

**当前状态**: 2026.7.1 → 最新 2026.7.2

**建议**: 
- 2026.7.2 包含大量状态安全和恢复改进
- 会话倒带/分支功能对开发很有价值
- 建议在下一次维护窗口升级

**升级命令**:
```bash
# 检查更新
openclaw update check

# 执行升级（需老大批准）
openclaw update run
```

---

*此文件已真实写入服务器*
*路径: knowledge_base/openclaw-2026.7.2-release.md*
*验证: cat /home/node/.openclaw/workspace/knowledge_base/openclaw-2026.7.2-release.md*
