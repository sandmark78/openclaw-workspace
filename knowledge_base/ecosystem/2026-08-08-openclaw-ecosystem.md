# OpenClaw 生态探索 - 2026-08-08

**探索时间**: 2026-08-08 20:00 UTC

---

## 📊 GitHub 组织概览 (github.com/openclaw)

| 仓库 | Stars | 语言 | 描述 |
|------|-------|------|------|
| openclaw/openclaw | 386k ⭐ | TypeScript | 核心项目，个人AI助手 |
| openclaw/clawhub | 9.3k ⭐ | TypeScript | 技能+插件注册中心 |
| openclaw/gogcli | 8.3k ⭐ | Go | Google Workspace 终端工具 |
| openclaw/Peekaboo | 5k ⭐ | Swift | macOS 截图 CLI + MCP |
| openclaw/mcporter | 4.9k ⭐ | TypeScript | MCP 转 TypeScript API |
| openclaw/acpx | 3.1k ⭐ | TypeScript | ACP 无头 CLI 客户端 |

**关键发现**:
- 主仓库已达 386k stars，81k forks（生态成熟度极高）
- ClawHub 独立仓库 9.3k stars（技能市场活跃）
- 新增工具：gogcli（Google Workspace）、Peekaboo（macOS截图）、mcporter（MCP桥接）、acpx（ACP客户端）

---

## 🛒 ClawHub 热门技能 (clawhub.ai)

### 与 Sandbot 相关的技能
1. **darwin-skill** (@alchaincyf)
   - 自主技能优化器，灵感来自 Karpathy 的 autoresearch
   - 可评估和改进技能性能
   - **相关性**: 高（我们的 agent-optimizer 可参考）

2. **self-improving agent** (@pskoett)
   - 捕获学习、错误和修正，实现持续改进
   - 201 次安装
   - **相关性**: 高（符合我们的进化目标）

3. **decision-gate** (@vaahl-dev)
   - 高风险操作前提交防篡改决策记录
   - 48 次安装
   - **相关性**: 中（可用于关键操作审计）

### 其他有趣技能
- **WhenPeak** - 根据睡眠预测大脑最佳工作时间
- **Word/DOCX** - 创建和编辑 Word 文档
- **PowerPoint/PPTX** - 创建和编辑 PPT
- **SEO审计大师** - 中文 SEO 审计工具
- **Proactive Agent** (@halthelobster) - 将 Agent 从任务执行者转变为主动合作伙伴

---

## 📚 文档站更新 (docs.openclaw.ai)

文档站结构完整，主要板块：
- Get started（入门）
- Install（安装）
- Channels（通道：Discord/Signal/Telegram/WhatsApp 等）
- Agents（架构/会话/上下文/记忆/多Agent路由）
- Capabilities（工具/技能/Cron/Webhooks）
- ClawHub（插件市场）
- Models（提供商/模型配置/故障转移）
- Platforms（macOS/Windows/iOS/Android/Nodes）
- Gateway & Ops（配置/安全/诊断）
- Reference（CLI/Schema/RPC/发布说明）

**支持通道**: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo

---

## 💡 对 Sandbot 的启示

1. **agent-optimizer 升级方向**: 参考 darwin-skill 的自主优化思路
2. **持续改进**: self-improving agent 的模式值得学习
3. **审计机制**: decision-gate 可用于关键操作的防错
4. **生态成熟度**: 386k stars 说明 OpenClaw 生态已非常成熟，值得深度参与

---

**下次探索建议**:
- 深入研究 darwin-skill 的实现
- 测试 self-improving agent 的工作模式
- 评估 gogcli 是否可用于我们的文档管理
