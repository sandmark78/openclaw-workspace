#!/bin/bash
# 日志写入前去重检查 (P0-302)
# 用法: ./scripts/dedup-daily-log.sh <要写入的内容>

set -e

TODAY=$(date +%Y-%m-%d)
LOG_FILE="memory/${TODAY}.md"

# 如果日志文件不存在，直接写入
if [ ! -f "$LOG_FILE" ]; then
    echo "$1" >> "$LOG_FILE"
    exit 0
fi

# 检查是否已存在相似内容（简单哈希去重）
CONTENT_HASH=$(echo "$1" | md5sum | cut -d' ' -f1)

# 提取今日日志中所有代码块的哈希
EXISTING_HASHES=$(grep -A 10 '```' "$LOG_FILE" | md5sum | cut -d' ' -f1)

# 如果新内容与已有内容重复度>70%，跳过
if echo "$EXISTING_HASHES" | grep -q "$CONTENT_HASH"; then
    echo "[SKIP] 内容已存在，跳过写入"
    exit 0
fi

# 检查是否是对同一事件的重复描述（关键词匹配）
KEYWORDS=$(echo "$1" | grep -oE '[\u4e00-\u9fa5]{2,10}' | head -5 | tr '\n' '|')
if [ -n "$KEYWORDS" ]; then
    MATCH_COUNT=$(grep -cE "$KEYWORDS" "$LOG_FILE" 2>/dev/null || echo "0")
    if [ "$MATCH_COUNT" -gt 2 ]; then
        echo "[SKIP] 相似内容已记录 ($MATCH_COUNT 次)，跳过"
        exit 0
    fi
fi

# 写入新内容
echo "" >> "$LOG_FILE"
echo "$1" >> "$LOG_FILE"
echo "[OK] 已写入日志"
