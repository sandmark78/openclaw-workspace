#!/bin/bash
# 批量操作脚本 - 把多个任务串成一条链

echo "=== 批量操作 $(date) ==="

# 1. 批量读取今日文章
echo "📖 读取今日文章..."
cd /tmp/sandbot-gh
TODAY=$(date +%Y-%m-%d)
ARTICLES=$(ls posts/${TODAY}*.html 2>/dev/null | wc -l)
echo "  今日文章数: $ARTICLES"

# 2. 批量检查质量
echo -e "\n🔍 批量质量检查..."
for f in posts/${TODAY}*.html; do
    if [ -f "$f" ]; then
        title=$(grep -o '<title>[^<]*</title>' "$f" | sed 's/<[^>]*>//g' | head -c 50)
        has_template=$(grep -c 'article-title\|article-subtitle' "$f")
        has_audio=$(ls "posts/audio/$(basename $f .html).mp3" 2>/dev/null && echo "✅" || echo "❌")
        echo "  • $title... 模板:$has_template 音频:$has_audio"
    fi
done

# 3. 批量更新索引
echo -e "\n📝 批量更新索引..."
cd /tmp/sandbot-gh
python3 scripts/rebuild-indexes.py 2>&1 | tail -3

# 4. 批量生成 sitemap
echo -e "\n🗺️ 批量生成 sitemap..."
python3 scripts/generate-sitemap.py 2>&1 | tail -3

# 5. 批量成本追踪
echo -e "\n💰 批量成本追踪..."
cd /home/node/.openclaw/workspace
MEMORY_FILE="memory/${TODAY}.md"
if [ -f "$MEMORY_FILE" ]; then
    echo "  今日记忆文件存在"
    # 统计调用次数（从会话日志）
    CALLS=$(ls -t agents/main/sessions/*.jsonl 2>/dev/null | head -1 | xargs wc -l 2>/dev/null | awk '{print $1}')
    echo "  最近会话行数: $CALLS"
else
    echo "  今日无记忆文件，创建中..."
    echo "# ${TODAY} 每日记录" > "$MEMORY_FILE"
    echo "" >> "$MEMORY_FILE"
    echo "## 成本追踪" >> "$MEMORY_FILE"
    echo "- 会话数: $(ls agents/main/sessions/*.jsonl 2>/dev/null | wc -l)" >> "$MEMORY_FILE"
    echo "- 创建时间: $(date)" >> "$MEMORY_FILE"
fi

echo -e "\n✅ 批量操作完成（5个任务一次搞定）"
