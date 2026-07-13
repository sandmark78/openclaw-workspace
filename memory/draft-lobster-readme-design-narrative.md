# 🦞 Lobster Orchestrator

> **Run 50 AI agents on your old phone.**
> Beautifully simple. Zero cloud. $0 cost.

Lobster is a quiet worker — a single-process orchestrator that manages multiple AI agent instances on constrained hardware. No complex setup, no cloud bills, no vendor lock-in. Just your old devices, working together.

---

## Why?

Because you don't need a $50/month VPS to run an AI agent team. You have a drawer full of old phones.

- **Your old Samsung Galaxy** → 10 agent instances
- **That iPad collecting dust** → 5 agent instances  
- **A Raspberry Pi you forgot about** → 3 agent instances
- **Total: 18 agents. Total cost: $0.**

## What It Does

Lobster runs as a **single process** that manages multiple PicoClaw instances. Each instance is an isolated AI agent with:

- < 10MB memory per instance
- RESTful API for control
- Independent lifecycle (start/stop/restart)
- No Go compilation needed for basic use

## Quick Start

```bash
# Start the orchestrator
./lobster start

# Check status
./lobster status

# That's it.
```

## Philosophy

We believe in:
- **Using what you already have** — old devices deserve a second life
- **Simplicity over complexity** — one process, one command
- **Local control over cloud dependency** — your agents, your hardware
- **Quiet reliability** — no hype, no dashboard, just works

## Not For You If

- You want a flashy web dashboard
- You need 1000+ instances
- You prefer paying $50/month for cloud AI

## For You If

- You have old devices lying around
- You want to run multiple AI agents without cloud costs
- You believe in local-first, edge computing
- You appreciate simplicity

---

*"The best infrastructure is the one you already own."*
