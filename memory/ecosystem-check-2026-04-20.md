# 生态探索记录 2026-04-20

## 检查时间
2026-04-20 20:00 UTC

## 当前安装版本
**OpenClaw 2026.3.8**

## 发现新变化

### 1. ClawHub 平台数据
- 工具数：**52,700+**
- 用户数：**180,000+**
- 下载量：**12,000,000+**
- 平均评分：**4.8**
- 域名已从 clawhub.com 重定向到 clawhub.ai

### 2. GitHub Releases — 新稳定版 2026.4.16 (Apr 16)
**当前版本落后约 1 个月，建议升级！**

核心更新：
- **Claude Opus 4.7** 成为 Anthropic 默认模型（含 opus 别名和 CLI 默认）
- **Google TTS 新增 Gemini 语音合成**支持（WAV 回复输出、PCM 电话输出）
- **Control UI 新增 Model Auth 状态卡片**（OAuth token 健康度、提供商限压状态展示，过期警告）
- **Memory/LanceDB 支持云存储**（远程对象存储替代仅本地磁盘）
- **GitHub Copilot 嵌入提供者**用于 memory search（新传输层复用）

### 3. Pre-release 2026.4.19-beta.1 (Apr 19)
- **跨 Agent 子 Agent 生成修复**：跨 Agent subagent spawn 通过目标 Agent 绑定的 channel 账号路由
- **Telegram 回调修复**：永久性回调编辑错误不再阻塞更新水印
- **Browser/CDP 改进**：WSL-to-Windows Chrome 端点修复 + 阶段特定 CDP 就绪诊断
- **Codex 上下文使用修复**：停止将 app-server 累计 token 当作新上下文使用

### 4. Pre-release 2026.4.19-beta.2 (Apr 19)
- **Agents/OpenAI completions**：流式请求始终发送 stream_options.include_usage
- **Agents/nested lanes**：嵌套 Agent 工作按目标会话隔离，不再阻塞无关会话
- **Agents/status**：保留会话 token 总计，提供商省略 usage metadata 时仍显示上次已知上下文使用
- **Install/update**：保持旧版更新验证与 QA Lab runtime shim 兼容

## 建议
1. **升级 OpenClaw 到 2026.4.16**（稳定版）可获得 Claude Opus 4.7、Google TTS Gemini、Model Auth 状态卡等新功能
2. 如需 Telegram 回调修复和跨 Agent 路由修复，可考虑 beta.2
3. 升级前备份 openclaw.json
