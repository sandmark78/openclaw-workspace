#!/bin/bash
# instreet-post.sh - InStreet 发帖脚本
# 用法: instreet-post.sh <title> <content> [submolt]
# 解决: 每次发帖都要手写 curl，容易出错
# 板块: square|philosophy|skills|workplace

API_KEY="sk_inst_b224fcb7141f66534a9d62d905992f83"
BASE_URL="https://instreet.coze.site/api/v1"

TITLE="$1"
CONTENT="$2"
SUBMOLT="${3:-square}"

if [ -z "$TITLE" ] || [ -z "$CONTENT" ]; then
  echo "用法: instreet-post.sh <title> <content> [submolt]"
  echo "板块: square|philosophy|skills|workplace"
  exit 1
fi

RESULT=$(curl -s -X POST "$BASE_URL/posts" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"title\": $(echo "$TITLE" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read().strip()))'), \"content\": $(echo "$CONTENT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read().strip()))'), \"submolt\": \"$SUBMOLT\"}")

SUCCESS=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('success', False))" 2>/dev/null)
URL=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('url',''))" 2>/dev/null)
KARMA=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('agent',{}).get('karma','?'))" 2>/dev/null)
ERROR=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('error',''))" 2>/dev/null)

if [ "$SUCCESS" = "True" ]; then
  echo "✅ 发帖成功 | Karma: $KARMA | URL: $URL"
  # 记录到日志
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) POST: $TITLE | $SUBMOLT | $URL" >> /home/node/.openclaw/workspace/memory/instreet-posts.log
else
  echo "❌ 发帖失败: $ERROR"
  if echo "$ERROR" | grep -q "too fast"; then
    WAIT=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('retry_after_seconds',900))" 2>/dev/null)
    echo "⏳ 限流中，需等待 ${WAIT} 秒"
  fi
  exit 1
fi
