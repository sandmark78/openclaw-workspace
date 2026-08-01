#!/bin/bash
# 本地化心跳检查脚本
# 不调用模型，纯 bash 执行
# 用法: ./scripts/heartbeat-local.sh

LOG_FILE="/home/node/.openclaw/workspace/memory/heartbeat.log"
mkdir -p "$(dirname "$LOG_FILE")"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# 1. 检查 Gateway 进程
if ! ps aux | grep -q "[o]penclaw-gateway"; then
  echo "[$TIMESTAMP] ❌ Gateway 宕机" | tee -a "$LOG_FILE"
  exit 1
fi

# 2. 检查磁盘空间（阈值 90%）
disk_usage=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$disk_usage" -gt 90 ]; then
  echo "[$TIMESTAMP] ⚠️ 磁盘空间 ${disk_usage}%" | tee -a "$LOG_FILE"
fi

# 3. 检查今天的文章
today=$(date +%Y-%m-%d)
article_count=$(ls $HOME/.openclaw/workspace/sandbot-blog/posts/${today}* 2>/dev/null | wc -l)
if [ "$article_count" -lt 3 ]; then
  echo "[$TIMESTAMP] ⚠️ 今天文章: ${article_count} 篇（应 3 篇）" | tee -a "$LOG_FILE"
fi

# 4. 检查最近的 Cron 错误（最近 1 小时）
error_count=$(grep -l "error\|failed" /home/node/.openclaw/agents/main/sessions/*.jsonl 2>/dev/null | tail -1 | xargs tail -100 2>/dev/null | grep -c "error\|failed" || echo "0")
if [ "$error_count" -gt 5 ]; then
  echo "[$TIMESTAMP] ⚠️ 最近错误: ${error_count} 个" | tee -a "$LOG_FILE"
fi

# 5. 无异常时记录正常
echo "[$TIMESTAMP] ✅ 心跳正常 | 磁盘 ${disk_usage}% | 文章 ${article_count} 篇 | 错误 ${error_count} 个" >> "$LOG_FILE"

# 6. 清理旧日志（保留最近 7 天）
if [ -f "$LOG_FILE" ]; then
  tail -n 336 "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
fi

exit 0
