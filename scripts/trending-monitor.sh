#!/bin/bash
# 全网热搜监控脚本
# 用法：./trending-monitor.sh

export PATH=/home/node/.local/bin:$PATH
DATE=$(date '+%Y-%m-%d %H:%M:%S')
OUTPUT_DIR="/home/node/.openclaw/workspace/memory/trending"

mkdir -p "$OUTPUT_DIR"

echo "=== 全网热搜监控 ($DATE) ===" | tee "$OUTPUT_DIR/$(date +%Y%m%d_%H%M%S).md"
echo ""

echo "## HackerNews Top 10" | tee -a "$OUTPUT_DIR/$(date +%Y%m%d_%H%M%S).md"
opencli-rs hackernews top --limit 10 --format md 2>/dev/null | tee -a "$OUTPUT_DIR/$(date +%Y%m%d_%H%M%S).md"
echo ""

echo "## B 站热搜 Top 10" | tee -a "$OUTPUT_DIR/$(date +%Y%m%d_%H%M%S).md"
opencli-rs bilibili hot --limit 10 --format md 2>/dev/null | tee -a "$OUTPUT_DIR/$(date +%Y%m%d_%H%M%S).md"
echo ""

echo "## 知乎热搜 Top 10" | tee -a "$OUTPUT_DIR/$(date +%Y%m%d_%H%M%S).md"
opencli-rs zhihu hot --limit 10 --format md 2>/dev/null | tee -a "$OUTPUT_DIR/$(date +%Y%m%d_%H%M%S).md"
echo ""

echo "✅ 监控完成，保存到：$OUTPUT_DIR/$(date +%Y%m%d_%H%M%S).md"
