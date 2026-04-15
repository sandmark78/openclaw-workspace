#!/bin/bash
# 心跳守护进程 - 每 30 分钟执行本地心跳，不调用模型
# 用法：nohup ./heartbeat-daemon.sh &

LOG_FILE="/home/node/.openclaw/workspace/memory/heartbeat-daemon.log"
SCRIPT="/home/node/.openclaw/workspace/scripts/heartbeat-local.sh"

echo "⚡ [$(date '+%Y-%m-%d %H:%M:%S')] 心跳守护进程启动" >> "$LOG_FILE"

while true; do
    # 执行心跳
    bash "$SCRIPT" >> "$LOG_FILE" 2>&1
    
    # 等待 30 分钟
    sleep 1800
done
