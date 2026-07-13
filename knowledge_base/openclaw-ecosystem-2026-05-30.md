# OpenClaw 生态探索报告

**日期**: 2026-05-30  
**触发**: Cron 生态探索任务  
**当前版本**: 2026.3.8 → **npm 最新**: 2026.5.27 (落后约 2 个月!)

---

## 🔴 关键发现：OpenClaw 版本大幅落后

| 指标 | 值 |
|------|------|
| **当前运行版本** | 2026.3.8 |
| **npm 最新稳定版** | 2026.5.27 (2026-05-28 发布) |
| **最新 beta** | 2026.5.28-beta.4 (2026-05-29) |
| **落后版本数** | 约 80+ 个版本 |
| **落后天数** | ~70 天 |

### 建议
- 考虑升级: `npm install -g openclaw@latest && openclaw gateway restart`
- 升级前备份 openclaw.json 和相关配置

---

## 🟡 ClawHub 生态增长显著

| 指标 | 值 | 说明 |
|------|------|------|
| 技能/插件总数 | **52.7k** | 生态规模可观 |
| 注册用户 | **180k** | 用户基数庞大 |
| 总下载量 | **12M** | 活跃度很高 |
| 平均评分 | **4.8** | 质量不错 |

### 新增功能 (与之前相比)
1. **Souls (灵魂) 发布**: 现在可以发布 Soul 配置（SOUL.md），不只是 Skills
2. **SoulHub**: 独立的 Soul 配置目录服务
3. **Native Plugin Packages**: 支持原生代码插件和 bundle 插件
4. **Custom Control UI**: 支持挂载自定义 Control UI 构建
5. **Skill rename & merge**: 支持技能重命名和合并，旧链接保持重定向
6. **Vector Search**: 使用 OpenAI embeddings 进行语义搜索（text-embedding-3-small）

---

## 🟢 Docs 网站更新

### 新增文档页面
- `/platforms/windows` — Windows 平台支持（原生 + WSL2）
- `/install` — 多种安装方式（Docker, Nix, npm）
- `/help/environment` — 环境变量参考
- `/channels/pairing` — 配对和安全机制
- `/web/control-ui` — Web 控制面板文档
- `/nodes` — 移动节点（iOS/Android）
- `/concepts/features` — 完整功能列表

### 安装方式更新
- 官方安装脚本: `curl -fsSL https://openclaw.ai/install.sh | bash`
- 新增 `openclaw onboard --install-daemon` 引导流程
- 新增 `openclaw gateway status` 状态检查命令
- 新增 `openclaw dashboard` 仪表盘打开命令

### Node.js 要求
- 推荐: **Node 24**
- 最低: Node 22.19+
- Windows 用户推荐 WSL2

### 通道支持
文档列出了完整通道列表:
- Discord, Google Chat, iMessage, Matrix, Microsoft Teams
- Signal, Slack, Telegram, WhatsApp, Zalo, + 更多

---

## GitHub 仓库

- ClawHub 源码: `github.com/openclaw/clawhub`
- OpenClaw 主仓库: 无法通过 web_fetch 直接访问（可能需要正确的用户名）

---

## 📊 总结

1. **版本升级优先级: 🔴 HIGH** — 落后 2 个月，建议尽快升级到 2026.5.27
2. **ClawHub 生态健康: 🟢 GOOD** — 52.7k 技能，180k 用户，12M 下载
3. **文档大幅完善: 🟢 GOOD** — 新增 Windows 支持、多种安装方式、详细通道文档
4. **新特性值得关注**: Custom Control UI、Souls 发布、Native Plugin

---

*由 Sandbot 🏖️ 自动生态探索任务生成*
