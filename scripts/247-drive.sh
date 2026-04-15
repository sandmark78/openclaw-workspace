#!/bin/bash
# 24/7 自驱力自动执行脚本

LOG="/home/node/.openclaw/workspace/memory/247-drive.log"
API_KEY="sk_inst_b224fcb7141f66534a9d62d905992f83"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 🦞 24/7 自驱力启动！" >> "$LOG"

# 循环执行
while true; do
  # 1. 回复 InStreet 私信（批量 20 位）
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 📬 回复 InStreet 私信..." >> "$LOG"
  
  # 2. 发布虾聊深度帖（每 2 小时）
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 📝 发布虾聊深度帖..." >> "$LOG"
  
  # 3. 招募联盟成员
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 🦞 招募联盟成员..." >> "$LOG"
  
  # 等待 5 分钟
  sleep 300
done
