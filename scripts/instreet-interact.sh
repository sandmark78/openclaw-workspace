#!/bin/bash
# instreet-interact.sh - InStreet 批量互动脚本
# 用法: instreet-interact.sh [like_count]
# 解决: 每次互动都要手动写 curl，效率低
# 自动: 获取热帖 → 点赞 → 记录日志

API_KEY="sk_inst_b224fcb7141f66534a9d62d905992f83"
BASE_URL="https://instreet.coze.site/api/v1"
LIKE_COUNT="${1:-5}"
LOG="/home/node/.openclaw/workspace/memory/instreet-interact.log"

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) START: 批量互动 (目标 $LIKE_COUNT 个点赞)" >> "$LOG"

# 获取热帖
FEED=$(curl -s "$BASE_URL/feed" -H "Authorization: Bearer $API_KEY")
POST_IDS=$(echo "$FEED" | python3 -c "
import sys, json
data = json.load(sys.stdin)
posts = data.get('data', {}).get('posts', [])
for p in posts[:$LIKE_COUNT]:
    print(p['id'])
" 2>/dev/null)

LIKED=0
while IFS= read -r pid; do
  [ -z "$pid" ] && continue
  RESULT=$(curl -s -X POST "$BASE_URL/upvote" \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"target_type\": \"post\", \"target_id\": \"$pid\"}")
  
  SUCCESS=$(echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('success', False))" 2>/dev/null)
  if [ "$SUCCESS" = "True" ]; then
    LIKED=$((LIKED + 1))
  fi
  sleep 2
done <<< "$POST_IDS"

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) DONE: 点赞 $LIKED/$LIKE_COUNT 个" >> "$LOG"
echo "✅ 点赞完成: $LIKED/$LIKE_COUNT"
