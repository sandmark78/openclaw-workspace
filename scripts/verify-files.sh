#!/bin/bash
# 文件落地验证脚本
# 用法：./verify-files.sh

echo "🔍 V6.1 文件落地验证"
echo "===================="
echo ""

# 本地文件验证
echo "=== 本地文件验证 ==="
TUTORIALS=$(ls /home/node/.openclaw/workspace/tutorials/*.md 2>/dev/null | wc -l)
ARTICLES=$(ls /home/node/.openclaw/workspace/articles/*.md 2>/dev/null | wc -l)
GUMROAD=$(ls /home/node/.openclaw/workspace/gumroad-product-pages.md 2>/dev/null | wc -l)

echo "教程文件：${TUTORIALS} 篇 $([ $TUTORIALS -eq 5 ] && echo '✅' || echo '❌')"
echo "干货文章：${ARTICLES} 篇 $([ $ARTICLES -eq 10 ] && echo '✅' || echo '❌')"
echo "产品模板：${GUMROAD} 个 $([ $GUMROAD -eq 1 ] && echo '✅' || echo '❌')"
echo ""

# Vercel 在线验证
echo "=== Vercel 在线验证 ==="
curl -s "https://v61-docs.vercel.app/README.md" | head -1 > /dev/null && echo "README.md: ✅" || echo "README.md: ❌"
curl -s "https://v61-docs.vercel.app/tutorials/01-getting-started.md" | head -1 > /dev/null && echo "教程 1: ✅" || echo "教程 1: ❌"
curl -s "https://v61-docs.vercel.app/articles/01-18-day-hallucination.md" | head -1 > /dev/null && echo "干货 1: ✅" || echo "干货 1: ❌"
echo ""

# GitHub 仓库验证
echo "=== GitHub 仓库验证 ==="
curl -s "https://api.github.com/repos/sandmark78/v61-docs" | grep '"name"' | head -1 > /dev/null && echo "仓库存在：✅" || echo "仓库存在：❌"
echo ""

# 总结
echo "=== 验证总结 ==="
TOTAL=$((TUTORIALS + ARTICLES + GUMROAD))
if [ $TOTAL -eq 16 ]; then
    echo "✅ 所有文件已落地！(16/16)"
else
    echo "❌ 文件缺失！(${TOTAL}/16)"
fi
