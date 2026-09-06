# OpenClaw 生态探索 - 2026-08-07

**检查时间**: 2026-08-07 20:00 UTC
**状态**: ✅ 发现新变化（ClawHub 域名变更 + 新技能）

---

## 🔍 本次扫描结果

### 1. ClawHub 域名变更 ⚠️ 新发现
- **旧域名**: https://clawhub.com → 301 重定向
- **新域名**: **https://clawhub.ai** ✅
- **含义**: ClawHub 品牌升级，从 .com 迁移到 .ai 域名
- **影响**: 后续访问/抓取 ClawHub 应改用 clawhub.ai

### 2. ClawHub 新技能（首页热门）
| 技能 | 作者 | 说明 |
|------|------|------|
| Skill Finder CN | guohongbin-git | 中文技能查找器，发现/安装 ClawHub Skills |
| CopilotKit Setup | copilotkit | CopilotKit 安装配置（含 MCP 文档） |
| postflight | soos3d | X/Twitter 定时发帖（加权 pillar 排期） |
| Minimax Docx | krisliu16 | 企业级 Word 文档生成（.docx） |
| CopilotKit Integrations | copilotkit | CopilotKit 集成（MCP） |
| self-improving agent | pskoett | 自我改进 Agent（捕获经验/错误/修正）⭐ 194 热度 |
| SQL Optimization Patterns | wshobson | SQL 慢查询优化模式 |
| 超级日记 Agent Control | super21-bat | 中文日记 Agent 控制 |
| Playwright Scraper | waisimon | Playwright 网页抓取（防机器人） |
| python-anti-patterns | wshobson | Python 反模式检查清单 |
| Minimax Xlsx | krisliu16 | MiniMax 电子表格生产系统 |
| Zod Best Practices | pproenca | Zod schema 验证指南 |
| Enterprise AI Landing Guide | yliu35126-afk | 企业 AI 落地（中文，7 天验证场景） |
| Tavily Search | matthew77 | Tavily LLM 优化搜索 |

**观察**: 中文技能生态持续增长，出现更多中文专用技能（Skill Finder CN、超级日记、企业 AI 落地指南）。

### 3. docs.openclaw.ai
- 无实质变化，标准文档首页
- 仍强调多通道网关定位（Discord/Signal/Telegram/WhatsApp 等）

### 4. GitHub releases
- nicepkg/openclaw → 404（仓库不存在，OpenClaw 由 OpenClaw Foundation 维护，非 nicepkg）
- nicepkg/gpt-runner → 有 release 但无版本号信息可提取

---

## 📌 结论与建议

**值得关注**:
1. **ClawHub 域名已变更为 clawhub.ai**，更新所有书签/脚本
2. **self-improving agent**（194 热度）热度最高，与 Sandbot 自我进化理念契合，可研究
3. 中文技能生态增长明显，可考虑发布更多中文技能到 ClawHub

**升级建议**: 本地 v2026.7.1 → 稳定版 v2026.7.1-2（补丁，修复 Memory Core 启动问题）

---

*下次检查: 2026-08-14*