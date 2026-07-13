#!/bin/bash
# news-cron.sh — 轻量级新闻抓取 Cron
# 用法: 添加到系统 crontab 或 OpenClaw cron

WORKSPACE="/home/node/.openclaw/workspace"
LOG_FILE="$WORKSPACE/tmp/news-cron.log"

# 确保目录存在
mkdir -p "$WORKSPACE/tmp/news"

# 执行抓取
echo "[$(date '+%Y-%m-%d %H:%M:%S')] 开始抓取新闻..." >> "$LOG_FILE"

python3 "$WORKSPACE/scripts/news-aggregator.py" --sources all --top 10 >> "$LOG_FILE" 2>&1

# 检查结果
if [ $? -eq 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ 抓取成功" >> "$LOG_FILE"
    
    # 统计新闻数量
    TODAY=$(date +%Y-%m-%d)
    NEWS_FILE="$WORKSPACE/tmp/news/$TODAY.json"
    if [ -f "$NEWS_FILE" ]; then
        COUNT=$(python3 -c "import json; print(len(json.load(open('$NEWS_FILE'))))")
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 📊 总计: $COUNT 条新闻" >> "$LOG_FILE"
    fi
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 抓取失败" >> "$LOG_FILE"
fi

# 清理旧日志（保留最近 7 天）
tail -n 100 "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"

exit 0
