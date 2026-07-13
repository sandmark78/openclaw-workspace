#!/bin/bash
# instreet-autoposter-daemon.sh - InStreet 自动发帖守护进程
# 每 6 小时发一次帖，避开限流

SCRIPT="/home/node/.openclaw/workspace/scripts/instreet-daily-post.sh"
LOG="/home/node/.openclaw/workspace/memory/instreet-daemon.log"
PIDFILE="/home/node/.openclaw/workspace/memory/instreet-daemon.pid"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 启动 InStreet 自动发帖守护进程" >> "$LOG"
echo $$ > "$PIDFILE"

while true; do
  # 检查限流
  RESULT=$($SCRIPT 2>&1)
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $RESULT" >> "$LOG"
  
  if echo "$RESULT" | grep -q "too fast"; then
    WAIT=$(echo "$RESULT" | grep -oP '\d+(?= seconds)' || echo "900")
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 限流中，等待 ${WAIT} 秒..." >> "$LOG"
    sleep $WAIT
  else
    # 成功或失败，都等 6 小时
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 等待 6 小时后再次尝试" >> "$LOG"
    sleep 21600
  fi
done
