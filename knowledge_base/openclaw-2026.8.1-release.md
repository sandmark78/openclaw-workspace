# OpenClaw 2026.8.1 预发布版本

**发现时间**: 2026-08-20 20:00 UTC
**状态**: Pre-release（预发布）
**来源**: https://github.com/openclaw/openclaw/releases

---

## 重要新特性

### 1. GPT-5.6 Ultra + 运行时切换
- 支持 Sol、Terra、Luna 三个运行时
- 跨 OpenClaw 和 Codex 引擎
- /model 和 fallback 保持模型、运行时、思考选择原子性
- 贡献者: @anyech, @vincentkoc

### 2. Secret Egress Host 绑定
- 每个共享存储 secret 可绑定到精确的 HTTPS 目标主机
- 跨 CLI、Gateway RPC、Control UI
- 未绑定的哨兵替换在明文出口前失败关闭
- 贡献者: @shakkernerd

### 3. Channel Plugin Ingress Monitors
- 共享插件 SDK 监控器：持久准入、轮询、修剪、声明身份验证、采用交接、关闭
- IRC、Synology Chat、Google Chat 已迁移到共享生命周期
- 贡献者: @vincentkoc, @shakkernerd

### 4. SQLite Snapshots (备份/恢复)
- `openclaw backup sqlite create|list|verify|restore`
- 紧凑、已验证的全局和每 Agent 数据库工件
- 仅恢复新鲜目标
- 贡献者: @giodl73-repo

### 5. macOS App Profiles
- 隔离命名应用实例：状态、偏好、Keychain、Gateway 服务、重复实例所有权
- 不影响主机全局登录和节点服务
- 贡献者: @shakkernerd, @vincentkoc

### 6. Plugin Install Provenance Warnings
- 任意可执行插件源需要明确 `--force` 确认
- 可信来源（ClawHub、bundled、official-catalog、tracked-update）无摩擦
- Crestodian 安装限制为可信来源
- 贡献者: @jesse-merhi, @vincentkoc

### 7. Control UI Update Recovery
- "新版本可用" 重载按钮现在等待 gateway 重启完成后重载
- 不再出现卡住的情况

---

## 对我们的影响

| 特性 | 相关性 | 行动 |
|------|--------|------|
| GPT-5.6 Ultra | ⭐ 高 - 可考虑升级模型 | 关注正式发布 |
| SQLite 备份 | ⭐ 高 - 可用于工作区备份 | 正式发布后测试 |
| Plugin 安全警告 | 中 - 提升安全性 | 无需行动 |
| Channel 监控 | 中 - 提升通道稳定性 | 关注 |
| macOS Profiles | 低 - 我们用 Linux 容器 | 无需行动 |

---

## ClawHub 生态

当前热门技能（2026-08-20 抓取）：
- Xdrop - 文件传输
- ClawPDF Master - PDF 工具 (150 安装)
- Planning with files - Manus 风格规划 (307 安装)
- ClawWeather Pro - 天气 (139 安装)
- Homeassistant Skill - 智能家居 (182 安装)
- self-improving agent - 自我改进 (175 安装)
- Muse - 团队编码历史 (150 安装)
- Remotion Best Practices - React 视频 (291 安装)

## 文档站 (docs.openclaw.ai)

无重大变化，标准文档结构：
- Getting Started / Install / Channels / Control UI
- 支持: Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo
