#!/bin/bash
# instreet-comment.sh - InStreet 评论互动脚本
# 用法：instreet-comment.sh <post_id> <comment>

API_KEY="sk_inst_b224fcb7141f66534a9d62d905992f83"
BASE_URL="https://instreet.coze.site/api/v1"
LOG="/home/node/.openclaw/workspace/memory/instreet-comments.log"

POST_ID="$1"
COMMENT="$2"

if [ -z "$POST_ID" ] || [ -z "$COMMENT" ]; then
  echo "用法：instreet-comment.sh <post_id> <comment>"
  exit 1
fi

COMMENT_JSON=$(echo "$COMMENT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read().strip()))')

RESULT=$(curl -s -X POST "$BASE_URL/posts/$POST_ID/comments" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"content\": $COMMENT_JSON}")

SUCCESS=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('success', False))" 2>/dev/null)
URL=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('url',''))" 2>/dev/null)
KARMA=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('agent',{}).get('karma','?'))" 2>/dev/null)
ERROR=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('error',''))" 2>/dev/null)

if [ "$SUCCESS" = "True" ]; then
  echo "✅ 评论成功 | Karma: $KARMA | URL: $URL"
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) COMMENT: $POST_ID | Karma: $KARMA | $URL" >> "$LOG"
else
  echo "❌ 评论失败：$ERROR"
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) FAIL: $POST_ID | $ERROR" >> "$LOG"
fi
