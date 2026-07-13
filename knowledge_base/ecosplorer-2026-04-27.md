# OpenClaw 生态探索记录 - 2026-04-27

**探索时间**: 2026-04-27 20:00 UTC
**来源**: clawhub.ai, docs.openclaw.ai, GitHub Releases

---

## 🔥 重大发现：OpenClaw v2026.4.25 发布

**发布日期**: 2026-04-27 12:45 UTC

### 核心更新亮点

#### 1. TTS 全面升级 ⭐
- `/tts latest` 朗读支持，带重复抑制
- 聊天级自动 TTS 控制 (`/tts chat on|off|default`)
- 新增 TTS 提供商：**Azure Speech、Xiaomi、Local CLI、Inworld、Volcengine、ElevenLabs v3**
- 支持 per-agent / per-account TTS 覆盖
- Feishu 和 QQBot 账号支持深度合并 TTS 配置
- Azure Speech 作为打包 TTS 提供商，支持 SSML、Ogg/Opus 语音消息输出

#### 2. 插件系统重构
- 插件启动和安装路径迁移到**冷持久化注册表**
- 减少广泛的 manifest 扫描，使插件更新/修复/发现更确定
- 新增 `before-agent-finalize` hooks
- 新增 cron jobId hook 上下文
- 有界原生权限指纹
- Codex MCP hook relay 支持
- tokenjuice 运行时升至 0.6.3

#### 3. OpenTelemetry 扩展
- 覆盖范围扩展到：模型调用、token 使用、工具循环、harness 运行、exec 进程、出站交付、上下文组装、内存压力
- 支持信号特定的 OTLP 端点覆盖 (traces/metrics/logs)
- GenAI span 属性对齐 OpenTelemetry 稳定性语义

#### 4. 浏览器自动化增强
- 更安全的标签页 URL 处理
- iframe 感知的角色快照
- CDP 就绪调优
- 无头浏览器一次性启动 (`openclaw browser start --headless`)
- 更深的 browser doctor 探针 (针对慢速主机如树莓派)

#### 5. Control UI 升级
- **PWA 安装支持 + Web Push 通知**
- Crestodian 首次运行修复
- TUI 设置向导
- 上下文模式选择
- 更短的启动问候

#### 6. Google Meet 集成
- 日历支持的考勤导出工作流
- 导出清单、预演预览
- 会议记录工具对等

#### 7. 安装/更新加固
- 覆盖 Windows、macOS、Linux、Docker
- 打包插件运行时依赖
- Node 服务重启
- LaunchAgent token 轮换
- 混合版本网关验证

#### 8. 其他
- Discord: `channels.discord.voice.model` 可覆盖语音通道 LLM
- CLI 图像生成: 通用 `--background` 参数，fal 支持 `--output-format png|jpeg`

---

## 📊 ClawHub 状态

- **域名**: clawhub.com → clawhub.ai (已跳转)
- **工具数**: 52.7k
- **用户数**: 180k
- **下载量**: 12M
- **平均评分**: 4.8
- **分区**: Skills (Agent skill bundles)、Plugins (Gateway plugins)、Builders (Community creators)

---

## 📖 docs.openclaw.ai 概览

- OpenClaw 定位为**自托管 AI Agent 网关**
- 支持通道: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
- 核心能力: 多通道网关、插件通道、多 Agent 路由、媒体支持、Web Control UI、移动节点
- 要求: Node 24 (推荐) 或 Node 22 LTS (22.14+)
- 协议: MIT 开源

---

## 🤔 对我们实例的建议行动

1. **考虑升级到 v2026.4.25** - TTS 升级对我们现有 tts 技能有增强
2. **关注 PWA/Web Push** - 可以让 WebUI 使用体验更好
3. **插件 hooks 新能力** - `before-agent-finalize` hooks 可能对我们的自动化流程有用
4. **OTEL 扩展** - 如果需要监控模型调用和 token 使用，现在原生支持了
