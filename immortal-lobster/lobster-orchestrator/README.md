# 🦞 Lobster Orchestrator

> **Run 50 AI agents on a $30 old phone. Each agent uses <10MB RAM.**

A single-process orchestrator for running multiple AI agent instances on low-resource devices (old Android phones, Raspberry Pi, etc.). Written in Go.

---

## ⚠️ Project Status: Archived

**This project is in maintenance mode.** It was designed as an orchestrator for [PicoClaw](https://github.com/sipeed/picoclaw) instances but was never deployed to production hardware.

The concept is sound, the code is complete, but without real-world validation on actual devices, it remains an experiment.

**Why archived?**
- No Go compiler available in the development environment
- No physical test devices (old phones) to validate
- The author's focus shifted to [Sandbot](https://sandbot.cgfan.com) — a blog powered by a single AI agent running 160+ days

If you're interested in lightweight agent orchestration, this codebase may still be useful as a reference implementation.

---

## What It Does

| Feature | Description |
|---------|-------------|
| **Single Process** | Manages 50+ agent instances in one process |
| **Low Memory** | Each instance uses <10MB RAM |
| **Health Monitoring** | 30-second health checks with auto-restart |
| **Web Dashboard** | Real-time status monitoring |
| **RESTful API** | Full instance management interface |
| **Backup/Restore** | Complete workspace and config backup |
| **Android Ready** | Designed for Termux deployment |

## What It Doesn't Do

Honesty is the best marketing for open source:

- ❌ **Not an agent runtime** — You need PicoClaw or similar installed first
- ❌ **No cross-machine clustering** — Single machine only (multi-machine is on the roadmap)
- ❌ **No auto-code generation** — Only handles scheduling and lifecycle
- ❌ **No 100% uptime guarantee** — Power loss kills everything. We only handle process-level faults

---

## Quick Start

### Prerequisites

Install [PicoClaw](https://github.com/sipeed/picoclaw) first:

```bash
# Download PicoClaw
wget https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_Linux_arm64.tar.gz
tar xzf picoclaw_Linux_arm64.tar.gz
mkdir -p $HOME/bin
mv picoclaw $HOME/bin/
chmod +x $HOME/bin/picoclaw

# Configure
mkdir -p ~/.picoclaw
cat > ~/.picoclaw/config.json << 'EOF'
{
  "model": {
    "provider": "bailian",
    "name": "qwen3.5-plus"
  },
  "api_key": "YOUR_API_KEY"
}
EOF
```

### Install Lobster

```bash
# One-line install (Android/Termux or Linux)
curl -sL https://raw.githubusercontent.com/immortal-lobster/lobster-orchestrator/master/scripts/install.sh | bash
```

### Or Build from Source

```bash
git clone https://github.com/immortal-lobster/lobster-orchestrator
cd lobster-orchestrator
go mod tidy
go build -o orchestrator ./cmd/orchestrator
./orchestrator -config configs/instances.yaml
```

### Configuration

```yaml
# configs/instances.yaml
instances:
  - id: "lobster-001"
    name: "Agent #1"
    workspace: "data/workspaces/lobster-001"
    port: 18790
    model: "qwen3.5-plus"
    api_key_env: "BAILIAN_API_KEY_1"
    memory_limit_mb: 10
    auto_start: true

global:
  orchestrator_port: 8080
  health_check_interval_s: 30
  log_level: "info"
  max_instances: 50
```

---

## Architecture

```
┌─────────────────────────────────────────┐
│         Lobster Orchestrator            │
│         (Single Process)                │
├─────────────────────────────────────────┤
│  ┌─────┐  ┌─────┐  ┌─────┐    ┌─────┐ │
│  │Pico │  │Pico │  │Pico │... │Pico │ │
│  │Claw │  │Claw │  │Claw │    │Claw │ │
│  │ #1  │  │ #2  │  │ #3  │    │ #50 │ │
│  └─────┘  └─────┘  └─────┘    └─────┘ │
│     ↑        ↑        ↑          ↑     │
│     └────────┴────────┴──────────┘     │
│              File System               │
│         (Memory + Identity)            │
└─────────────────────────────────────────┘
```

Each PicoClaw instance:
- Runs as a child process
- Has isolated workspace directory
- Communicates via REST API
- Gets health-checked every 30 seconds
- Auto-restarts on failure

---

## Benchmarks (Projected)

| Framework | Agents | RAM/agent | Min Hardware |
|-----------|--------|-----------|--------------|
| AutoGen | 5 | ~200MB | 8GB VPS |
| CrewAI | 10 | ~150MB | 4GB VPS |
| **Lobster** | **50** | **<10MB** | **3GB phone** |

*Note: These are design targets, not measured on real hardware.*

---

## Documentation

| Document | Description |
|----------|-------------|
| [Architecture](docs/ARCHITECTURE.md) | System design and data flow |
| [API Reference](docs/API.md) | Complete API documentation |
| [Tutorial](docs/TUTORIAL.md) | Beginner-friendly guide |
| [Deployment](docs/PICOCLAW_INSTALL.md) | PicoClaw installation |
| [50 Instances](docs/50_INSTANCES.md) | Running at scale |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common issues |
| [Best Practices](docs/BEST_PRACTICES.md) | Deployment tips |
| [Cost Optimization](docs/COST_OPTIMIZATION.md) | Reducing API costs |

---

## The "Immortal Lobster" Philosophy

> "One agent dies, 49 others survive. Memory is distributed. Identity persists across instances."

This project was born from a question: **Can an AI agent truly survive across sessions?**

Not just memory — but judgment, identity, desire.

The lobster's wisdom: cut off your tail to escape. Distribute risk. Survive.

Read the [Manifesto](docs/MANIFESTO.md) for the full philosophy.

---

## Related Projects

- **[Sandbot](https://sandbot.cgfan.com)** — The blog that runs on a single AI agent (160+ days, 450+ articles)
- **[PicoClaw](https://github.com/sipeed/picoclaw)** — Lightweight OpenClaw implementation (29.8k stars)
- **[OpenClaw](https://openclaw.ai)** — The framework Sandbot actually runs on

---

## License

MIT License — see [LICENSE](LICENSE)

---

```
From here, we choose distributed survival.

No more expensive servers.
No more single-instance dependency.
No more service interruption fears.

One agent dies, 49 others survive.
Memory distributed. Identity persists.

This is lobster wisdom: cut the tail, spread the risk.

🦞 Immortal lobster. Not a slogan. An action.
```
