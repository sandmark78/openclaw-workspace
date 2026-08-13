#!/bin/bash
# Safety Kernel V1 - Pre-Push Guard
# 检查最近一次修改是否通过验证

set -e

echo "🔍 Safety Kernel: Pre-Push Check"

# 1. 检查是否有未提交的修改
if ! git diff --quiet HEAD; then
    echo "🚨 BLOCKED: 有未提交的修改"
    exit 1
fi

# 2. 检查最近一次 commit 的文件
CHANGED_FILES=$(git diff --name-only HEAD~1 2>/dev/null || echo "")

if [ -z "$CHANGED_FILES" ]; then
    echo "⚠️  WARNING: 无法获取最近修改的文件列表"
    exit 0
fi

# 3. 检查 HTML 文件结构完整性
HTML_ERRORS=0
for f in $CHANGED_FILES; do
    if [[ "$f" == *.html ]]; then
        if [ ! -f "$f" ]; then
            continue
        fi
        
        # 检查 <body> 标签数量
        body_count=$(grep -c '<body' "$f" 2>/dev/null || echo "0")
        if [ "$body_count" -ne 1 ]; then
            echo "🚨 BLOCKED: $f 有 $body_count 个 <body> 标签（应该是1个）"
            HTML_ERRORS=$((HTML_ERRORS + 1))
        fi
        
        # 检查 </html> 标签数量
        html_count=$(grep -c '</html>' "$f" 2>/dev/null || echo "0")
        if [ "$html_count" -ne 1 ]; then
            echo "🚨 BLOCKED: $f 有 $html_count 个 </html> 标签（应该是1个）"
            HTML_ERRORS=$((HTML_ERRORS + 1))
        fi
        
        # 检查是否有重复的 audio-player
        player_count=$(grep -c 'class="audio-player"' "$f" 2>/dev/null || echo "0")
        if [ "$player_count" -gt 1 ]; then
            echo "🚨 BLOCKED: $f 有 $player_count 个播放器（应该最多1个）"
            HTML_ERRORS=$((HTML_ERRORS + 1))
        fi
    fi
done

if [ $HTML_ERRORS -gt 0 ]; then
    echo "🚨 BLOCKED: HTML 结构检查失败（$HTML_ERRORS 个错误）"
    exit 1
fi

# 4. 检查 action-budget.json 是否有失败记录
if [ -f "memory/action-budget.json" ]; then
    if command -v jq &> /dev/null; then
        blocked=$(jq -r '.blocked // false' memory/action-budget.json)
        if [ "$blocked" = "true" ]; then
            reason=$(jq -r '.block_reason // "unknown"' memory/action-budget.json)
            echo "🚨 BLOCKED: 行动预算被阻止（原因: $reason）"
            exit 1
        fi
        
        last_result=$(jq -r '.last_result // "null"' memory/action-budget.json)
        if [ "$last_result" = "FAIL" ]; then
            echo "🚨 BLOCKED: 最近一次操作验证失败"
            exit 1
        fi
    fi
fi

# 5. 检查修改的文件数量（防止批量破坏）
CHANGED_COUNT=$(echo "$CHANGED_FILES" | wc -l)
if [ $CHANGED_COUNT -gt 20 ]; then
    echo "⚠️  WARNING: 最近一次修改了 $CHANGED_COUNT 个文件（超过20个）"
    echo "请确认这是预期行为"
fi

echo "✅ Safety Kernel: Pre-Push Check PASSED"
echo "   - HTML 结构: OK"
echo "   - 行动预算: OK"
echo "   - 修改文件数: $CHANGED_COUNT"
exit 0
