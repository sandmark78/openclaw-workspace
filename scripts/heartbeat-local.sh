#!/bin/bash
# 心跳本地化 - 零模型调用

echo "=== 心跳检查 $(date) ==="

# 1. 系统状态
echo -e "\n📊 系统状态:"
ps aux | grep -E "(openclaw|gateway)" | grep -v grep | head -2
df -h / | tail -1
free -h | head -2

# 2. 博客状态
echo -e "\n📝 博客状态:"
cd /tmp/sandbot-gh
git log --oneline -3
echo "总文章数: $(ls posts/*.html | wc -l)"

# 3. 记忆系统
echo -e "\n🧠 记忆状态:"
cd /home/node/.openclaw/workspace
echo "记忆文件: $(ls memory/*.md | wc -l)"
echo "知识库: $(find knowledge_base -name "*.md" | wc -l)"

# 4. 成本追踪
echo -e "\n💰 今日成本:"
TODAY=$(date +%Y-%m-%d)
if [ -f "memory/${TODAY}.md" ]; then
    grep -i "成本\|费用\|token" "memory/${TODAY}.md" | tail -5 || echo "无成本记录"
else
    echo "今日无记忆文件"
fi

echo -e "\n✅ 心跳完成（零模型调用）"

# === 缓存维护 (每次心跳执行) ===
CACHE_DIR="$WORKSPACE/memory/cache"
if [ -d "$CACHE_DIR" ]; then
    # 清理过期缓存
    python3 "$WORKSPACE/scripts/cache-manager.py" cleanup 2>/dev/null
    # 统计缓存
    CACHE_COUNT=$(ls "$CACHE_DIR"/*.json 2>/dev/null | wc -l)
    CACHE_SIZE=$(du -sh "$CACHE_DIR" 2>/dev/null | cut -f1)
    echo "  缓存: ${CACHE_COUNT} 个文件, ${CACHE_SIZE}"
fi
