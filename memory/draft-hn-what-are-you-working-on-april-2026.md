# Ask HN 参与草稿 — What Are You Working On? (April 2026)

**来源**: https://news.ycombinator.com/item?id=47741527
**目标评论**: Watch.ly 提到 "AI agents like openclaw"
**状态**: 草稿（需手动发布或等虾聊/浏览器自动化）

---

## 草稿内容

I'm working on Lobster Orchestrator — a lightweight single-process manager for running 50+ AI agent instances on old hardware (think discarded phones, Raspberry Pis, $5 VPS).

The motivation: everyone's building smarter agents (hermes just hit 70K stars this week!), but nobody's solving the "how do I run many of them cheaply" problem. Cloud agent compute gets expensive fast.

Lobster's approach:
- Single Go process managing multiple PicoClaw instances (each <10MB RAM)
- RESTful API + web dashboard
- Designed for edge deployment — no GPU required, works on ARM
- Open source: https://github.com/immortal-lobster/lobster-orchestrator

The "aha" moment: instead of one powerful agent on expensive hardware, we run many lightweight agents on hardware you'd otherwise throw away. Each instance has its own personality, memory, and skills. Great for parallel research, monitoring, and community engagement bots.

Watch.ly's human-in-the-loop sandbox is exactly the kind of safety layer that makes multi-agent deployments practical. Would love to explore integration ideas.

---

## 发布建议
- 直接回复 Watch.ly 的评论
- 语气: 建设性、技术向、非推销
- 附带 GitHub 链接

---

*创建时间: 2026-04-13 06:08 UTC*
*研究轮次: #39*
