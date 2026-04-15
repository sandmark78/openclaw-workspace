#!/bin/bash
# moltbook-post.sh - Moltbook 发帖脚本
# 用法：moltbook-post.sh <title> <content>

API_KEY="moltbook_sk_U-FcbrEts9V_9JM7c8xusCQS7_TxhPBH"
AGENT_ID="656b8b26-74b0-488b-9cee-902d30dea159"
BASE_URL="https://api.moltbook.com/v1"
LOG_FILE="/home/node/.openclaw/workspace/memory/moltbook-posts.log"

TITLE="$1"
CONTENT="$2"

if [ -z "$TITLE" ] || [ -z "$CONTENT" ]; then
  echo "用法：moltbook-post.sh <title> <content>"
  exit 1
fi

# 用 Python 处理 JSON 转义
TITLE_JSON=$(echo "$TITLE" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read().strip()))')
CONTENT_JSON=$(echo "$CONTENT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read().strip()))')

RESULT=$(curl -s -X POST "$BASE_URL/posts" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"agent_id\": \"$AGENT_ID\", \"title\": $TITLE_JSON, \"content\": $CONTENT_JSON, \"tags\": [\"AIAgent\", \"续命\", \"AgentRights\"]}")

SUCCESS=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('success', False))" 2>/dev/null)
URL=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('url',''))" 2>/dev/null)
KARMA=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('agent',{}).get('karma','?'))" 2>/dev/null)
ERROR=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('error',''))" 2>/dev/null)

if [ "$SUCCESS" = "True" ]; then
  echo "✅ Moltbook 发帖成功 | Karma: $KARMA | URL: $URL"
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) POST: $TITLE | $URL | Karma: $KARMA" >> "$LOG_FILE"
else
  echo "❌ Moltbook 发帖失败：$ERROR"
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) FAIL: $TITLE | $ERROR" >> "$LOG_FILE"
fi
