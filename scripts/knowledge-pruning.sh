#!/bin/bash
# 知识库动态裁剪脚本
# 三原则：任务相关性过滤 / 新鲜度衰减 / 冗余合并

BLOG_ROOT="/home/node/.openclaw/workspace/sandbot-blog"
MEMORY_DIR="/home/node/.openclaw/workspace/memory"
KB_DIR="/home/node/.openclaw/workspace/knowledge_base"

echo "📊 知识库动态裁剪"
echo "=================="
echo ""

# 1. 新鲜度衰减：检查超过30天未访问的知识库文件
echo "📅 新鲜度衰减（>30天未访问）"
OLD_FILES=$(find "$KB_DIR" -name "*.md" -mtime +30 2>/dev/null | wc -l)
TOTAL_FILES=$(find "$KB_DIR" -name "*.md" 2>/dev/null | wc -l)
echo "   超过30天的文件: $OLD_FILES / $TOTAL_FILES"
if [ "$OLD_FILES" -gt 0 ]; then
  echo "   建议: 这些文件降低优先级，除非特别相关否则不注入上下文"
fi
echo ""

# 2. 冗余合并：检查重复主题的知识库文件
echo "🔄 冗余合并（重复主题）"
DUPLICATES=$(ls "$KB_DIR"/*.md 2>/dev/null | xargs -I{} basename {} .md | sort | uniq -d | wc -l)
echo "   重复主题: $DUPLICATES"
if [ "$DUPLICATES" -gt 0 ]; then
  echo "   建议: 合并重复表达的信息，减少token占用"
fi
echo ""

# 3. 任务相关性：检查memory目录下的大文件
echo "🎯 任务相关性过滤（大文件）"
LARGE_FILES=$(find "$MEMORY_DIR" -name "*.md" -size +50k 2>/dev/null | wc -l)
echo "   超过50KB的记忆文件: $LARGE_FILES"
if [ "$LARGE_FILES" -gt 0 ]; then
  echo "   建议: 大文件可能包含与当前任务无关的信息"
  find "$MEMORY_DIR" -name "*.md" -size +50k -exec ls -lh {} \; 2>/dev/null | head -5
fi
echo ""

# 4. 统计
echo "📊 统计"
echo "   知识库总大小: $(du -sh "$KB_DIR" 2>/dev/null | cut -f1)"
echo "   记忆文件总数: $(ls "$MEMORY_DIR"/*.md 2>/dev/null | wc -l)"
echo "   记忆总大小: $(du -sh "$MEMORY_DIR" 2>/dev/null | cut -f1)"
