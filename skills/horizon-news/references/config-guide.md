# Horizon Configuration Guide

## AI Provider Setup (DashScope/Qwen)

```json
{
  "ai": {
    "provider": "ali",
    "model": "qwen-plus",
    "api_key_env": "DASHSCOPE_API_KEY",
    "temperature": 0.3,
    "max_tokens": 4096,
    "languages": ["en", "zh"]
  }
}
```

Provider options: `anthropic`, `openai`, `ali` (DashScope), `gemini`, `doubao`, `minimax`

## Sources Configuration

### Hacker News
```json
"hackernews": {
  "enabled": true,
  "fetch_top_stories": 30,
  "min_score": 100
}
```

### RSS Feeds
```json
"rss": [
  {"name": "Simon Willison", "url": "https://simonwillison.net/atom/everything/", "enabled": true, "category": "ai-tools"},
  {"name": "Hacker News RSS", "url": "https://hnrss.org/frontpage", "enabled": true, "category": "tech"}
]
```

### Reddit
```json
"reddit": {
  "enabled": true,
  "subreddits": [
    {"subreddit": "MachineLearning", "sort": "hot", "time_filter": "day", "fetch_limit": 15, "min_score": 50},
    {"subreddit": "LocalLLaMA", "sort": "hot", "time_filter": "day", "fetch_limit": 10, "min_score": 30}
  ],
  "fetch_comments": 5
}
```

### GitHub
```json
"github": [
  {"type": "user_events", "username": "torvalds", "enabled": true},
  {"type": "repo_releases", "owner": "openclaw", "repo": "openclaw", "enabled": true}
]
```

### Telegram Channels
```json
"telegram": {
  "enabled": true,
  "channels": [
    {"channel": "zaihuapd", "fetch_limit": 20}
  ]
}
```

## Filtering
```json
"filtering": {
  "ai_score_threshold": 6.0,
  "time_window_hours": 24
}
```

- `ai_score_threshold`: 0-10, items below this score are dropped (recommended: 6.0-7.0)
- `time_window_hours`: how far back to fetch (default 24)

## Scoring Criteria (AI evaluates)
- **9-10**: Groundbreaking breakthroughs, paradigm shifts
- **7-8**: High-value developments, deep dives, novel approaches
- **5-6**: Interesting but not urgent
- **3-4**: Low priority, routine content
- **0-2**: Noise, spam

## Output
Reports saved to `data/summaries/YYYY-MM-DD.md` in bilingual Markdown (EN + ZH).

## MCP Server
Horizon includes an MCP server for programmatic access:
```bash
uv run horizon-mcp
```
Tools: `hz_validate_config`, `hz_fetch_items`, `hz_score_items`, `hz_filter_items`, `hz_enrich_items`, `hz_generate_summary`, `hz_run_pipeline`
