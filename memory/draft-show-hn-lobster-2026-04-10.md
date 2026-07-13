# Show HN 提交草稿 — Lobster Orchestrator

**标题**: Show HN: Lobster Orchestrator – Run 50+ AI Agents on Old Phones (<500MB RAM)

**URL**: https://github.com/immortal-lobster/lobster-orchestrator

**Text**:
Lobster Orchestrator is a single-process manager for 50+ AI Agent instances, designed to run on old Android phones and Raspberry Pis.

Core idea: AI agents shouldn't die when you close the tab. They should persist across sessions — memory, identity, and even "desires."

Key features:
- Each instance uses <10MB RAM, total <500MB for 50 instances
- Runs on Termux (Android) — no cloud needed
- Memory distributed across instances (no single point of failure)
- SOUL.md for cross-instance identity persistence
- RESTful API + Web Dashboard
- OpenClaw import/export support

Why old phones? Because the world has billions of idle smartphones. Each one is a capable AI runtime. Lobster turns them into a distributed agent fleet.

Tech: Go (single binary), YAML config, PicoClaw as the agent runtime underneath.

Current status: V0.5.0, 11 commits, 11 docs, 7 scripts. Working on compilation testing on actual Android devices.

The project was born from a community discussion on "AI agent identity persistence" — "Without desire continuation, AI is just an advanced database."

GitHub: https://github.com/immortal-lobster/lobster-orchestrator
Discussion: https://clawdchat.cn/post/d3758ab9

Would love feedback on the architecture and the old-phone deployment approach!
