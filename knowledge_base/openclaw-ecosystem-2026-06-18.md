# OpenClaw 生态探索报告

**日期**: 2026-06-18  
**触发**: Cron 生态探索任务  
**当前运行版本**: 2026.3.8（待确认）  
**npm 最新稳定版**: 2026.6.8（2026-06-16 发布！）  
**GitHub Latest**: v2026.6.8

---

## 🔴 版本落后状态

| 指标 | 值 |
|------|------|
| **当前运行版本** | 2026.3.8（可能已更新，待确认） |
| **最新稳定版** | 2026.6.8 |
| **落后天数** | ~92 天 |

升级命令: `npm install -g openclaw@latest && openclaw gateway restart`

---

## 🆕 2026.6.8 新增亮点（2026-06-16 发布）

### 1. 通道交付质量大幅提升
- **Telegram**: 结构化文本渲染 — 表格、列表、可展开引用块、保留 intentional line breaks、CLI-backed replies
- **WhatsApp**: 现已支持配置的 ACP 绑定

### 2. Agent 运行可靠性增强
- account-scoped DM sends 修复
- 生成式 media completions 改进
- auto-reply message-tool final replies
- reset archive fallback reads
- restart shutdown aborts
- yielded subagent pauses
- session identity prompts 保持正确恢复路径

### 3. 主要贡献者
vincentkoc, obviyus, jzakirov, spacegeologist, TurboTheTurtle, mcaxtr, myrzka, dmorn, yetval 等

---

## 🔵 Docs 网站 (docs.openclaw.ai)

- 新增提及 **macOS app**（流程图中出现）
- 新增提及 **iOS and Android nodes**（Canvas、camera、voice workflows）
- 新增 channel 插件: **Matrix, Nostr, Twitch, Zalo**
- 运行要求: **Node 24 推荐**，或 Node 22 LTS (22.19+)

---

## 🔵 ClawHub (clawhub.com → clawhub.ai)

- 域名重定向到 **clawhub.ai**
- 首页精简为三栏: Skills / Plugins / Publishers
- 具体数据（下载量/用户数）未公开在首页，无法抓取

---

## 📊 总结

1. **版本升级优先级: 🔴 HIGH** — 2026.3.8 → 2026.6.8，落后 ~92 天
2. **2026.6.8 核心更新**: Telegram 结构化渲染（表格/列表/引用块）、WhatsApp ACP 绑定、Agent 运行可靠性多项修复
3. **Docs 新增**: macOS app、iOS/Android nodes 支持提及
4. **ClawHub 域名迁移**: clawhub.com → clawhub.ai

---

*由 Sandbot 🏖️ 自动生态探索任务生成*
