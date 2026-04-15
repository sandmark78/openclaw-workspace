---
name: horizon-news
description: >
  AI-powered multi-source news aggregation and summarization using Horizon.
  Fetch, score, filter, and summarize content from Hacker News, RSS, Reddit,
  Telegram, and GitHub. Generate bilingual (EN/ZH) daily briefings with
  AI scoring (0-10), web search enrichment, and community discussion summaries.
  Use when: daily news digest, tech trend monitoring, content curation,
  knowledge acquisition from multiple sources, or building a newsletter.
---

# Horizon News Aggregator

Automated AI news aggregation pipeline. Fetches from 5 source types, scores each item 0-10 with AI, enriches high-scoring items with web search context, and generates bilingual Markdown reports.

## Quick Start

### 1. First-time setup

```bash
cd /home/node/.openclaw/workspace/Horizon

# Create config from template
cp data/config.example.json data/config.json

# Create .env with API key
cat > .env << 'EOF'
DASHSCOPE_API_KEY=sk-sp-54997e1f8fa84942b1c077b1fa8f5269
EOF

# Install dependencies
pip install -e . 2>/dev/null || uv sync
```

Edit `data/config.json` — set provider to `ali`, model to `qwen-plus`. See [references/config-guide.md](references/config-guide.md) for full options.

### 2. Run

```bash
cd /home/node/.openclaw/workspace/Horizon
python -m src.main              # Default: last 24 hours
python -m src.main --hours 48   # Last 48 hours
```

Output: `data/summaries/YYYY-MM-DD.md`

### 3. Cron integration

Schedule via OpenClaw cron for daily automated runs. Use `agentTurn` payload with task:
"Run Horizon news aggregation: cd Horizon && python -m src.main --hours 24, then post summary highlights to user."

## Architecture

```
Fetch (HN/RSS/Reddit/Telegram/GitHub)
  → Deduplicate (same URL across sources)
  → AI Score (0-10 per item)
  → Filter (keep > threshold)
  → Enrich (DuckDuckGo search for background)
  → Summarize (bilingual Markdown report)
```

## Key Files

| File | Purpose |
|------|---------|
| `src/orchestrator.py` | Main pipeline coordinator |
| `src/ai/client.py` | Multi-provider AI client (supports `ali`/DashScope) |
| `src/ai/analyzer.py` | Content scoring logic |
| `src/ai/enricher.py` | Web search enrichment |
| `src/ai/summarizer.py` | Markdown report generation |
| `src/scrapers/` | Source-specific fetchers |
| `data/config.json` | Runtime configuration |

## Supported AI Providers

`anthropic`, `openai`, `ali` (DashScope/Qwen), `gemini`, `doubao`, `minimax`

For DashScope config, set provider `ali` with `api_key_env: DASHSCOPE_API_KEY`.

## Configuration Reference

See [references/config-guide.md](references/config-guide.md) for complete source configuration, filtering options, and scoring criteria.
