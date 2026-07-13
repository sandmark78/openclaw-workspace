# OpenClaw GitHub Release 2026.4.25

**抓取时间**: 2026-04-26 20:00 UTC  
**发布时间**: 2026-04-25 13:24 UTC  
**版本**: 预发布版本（Pre-release）  
**上次已知版本**: 2026.4.19-beta.2  
**当前运行**: 2026.3.8（落后 3 个大版本）

---

## 2026.4.25 亮点

### 🎙️ TTS 全面升级
- **/tts latest**: 新增 TTS 功能
- **chat-scoped auto-TTS controls**: 聊天级自动 TTS 控制
- **personas**: 语音角色系统
- **per-agent/per-account overrides**: 每个 Agent/账号可独立覆盖
- **新增 TTS 提供商**:
  - Azure Speech（新捆绑，支持 SSML 转义、原生 Ogg/Opus 输出）
  - Xiaomi
  - Local CLI
  - Inworld
  - Volcengine
  - ElevenLabs v3
- **WhatsApp**: /tts 朗读支持 + 重复抑制 + 会话级 auto-TTS 开关
- **Feishu/QQBot**: 支持账户级 TTS 覆盖
- 修复: [#66032](https://github.com/openclaw/openclaw/issues/66032)

### 🔌 Plugin 启动优化
- 插件启动和安装路径迁移到**冷持久化注册表**
- 减少广泛的 manifest 扫描
- 插件更新/修复/提供商发现/安装元数据更加确定性

### 📊 OpenTelemetry 覆盖扩展
- 覆盖范围扩展到：模型调用、token 用量、工具循环、harness 运行、exec 进程、出站交付、上下文组装、内存压力
- 有界低基数属性

### 🌐 浏览器自动化安全增强
- 更安全的标签页 URL
- iframe 感知的 role snapshot
- CDP 就绪调优
- headless 一次性启动
- 更深层的 browser doctor 探测（针对慢速主机）

### 🖥️ Control UI 更新
- **PWA 安装支持** + **Web Push 通知**（Gateway 聊天）
- Crestodian 首次运行修复
- TUI 设置向导
- 上下文模式选择
- 更短的启动问候语

### 🔒 安装/升级加固
- 覆盖 Windows、macOS、Linux、Docker
- 捆绑插件运行时依赖
- Node 服务重启
- LaunchAgent token 轮换
- 混合版本 gateway 验证

### 📅 Google Meet
- 日历支持的出勤导出工作流
- 导出 manifest
- dry-run 预览
- 会议记录工具奇偶校验

---

## 详细变更

| 类别 | 变更内容 | PR/Issue |
|------|----------|----------|
| TTS/WhatsApp | /tts latest 朗读 + 重复抑制 + chat on/off/default | #66032 |
| TTS/channels | Feishu/QQBot 账户级 TTS 覆盖 | - |
| TTS/agents | per-agent 语音覆盖 + /tts audio/status 支持 | - |
| Azure Speech | 捆绑 TTS 提供商，SSML 转义，Ogg/Opus 输出 | #51776 |
| Google Meet | 日历出勤导出 + dry-run 预览 | - |
| Control UI | PWA + Web Push 通知 | #44590 |
| 浏览器自动化 | 安全 tab URL + CDP role snapshot + iframe 感知 | - |
| CLI/图像生成 | --background 通用化 + fal image generate | - |

---

## ClawHub 统计（2026-04-26 抓取）

| 指标 | 数值 |
|------|------|
| 工具总数 | 52,700 |
| 用户数 | 180,000 |
| 下载量 | 12,000,000 |
| 平均评分 | 4.8 |

> 注：ClawHub 域名已改为 **clawhub.ai**（原 clawhub.com 重定向）

---

## 升级建议

⚠️ **当前运行 2026.3.8，落后 3 个大版本**

推荐升级到的版本：待正式版发布（当前 2026.4.25 为 pre-release）

### 升级收益评估
| 功能 | 对我们有用？ | 优先级 |
|------|-------------|--------|
| TTS 多提供商 | 中等（我们已有 tts 技能） | P2 |
| PWA + Web Push | 低（主要用 Telegram） | P3 |
| 浏览器安全增强 | 高（浏览器自动化常用） | P1 |
| OpenTelemetry | 中（有助于监控成本） | P2 |
| Plugin 注册表优化 | 高（启动更快更稳定） | P1 |
| Google Meet 导出 | 低（暂不使用） | P3 |

---

*此文件由生态探索 cron 自动生成*
*下次探索：2026-04-27 20:00 UTC*
