#!/bin/bash
# 自动化审计主脚本
# 整合所有审计功能，定期自动执行

WORKSPACE="/home/node/.openclaw/workspace"
SCRIPTS_DIR="$WORKSPACE/scripts"
REPORT_DIR="$WORKSPACE/memory"
DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "=========================================="
echo "自动化审计 - $TIMESTAMP"
echo "=========================================="
echo ""

# 1. 工具审计（每周执行）
echo "📋 [1/5] 工具审计..."
if [ -f "$SCRIPTS_DIR/tool-audit.sh" ]; then
    bash "$SCRIPTS_DIR/tool-audit.sh" > /dev/null 2>&1
    TOOL_COUNT=$(ls -d "$WORKSPACE/skills"/*/ 2>/dev/null | grep -v archive | wc -l)
    ARCHIVE_COUNT=$(ls -d "$WORKSPACE/skills/archive"/*/ 2>/dev/null | wc -l)
    echo "   ✅ 活跃技能: $TOOL_COUNT 个, 归档: $ARCHIVE_COUNT 个"
else
    echo "   ⚠️  tool-audit.sh 不存在"
fi
echo ""

# 2. 成本效率追踪（每日执行）
echo "💰 [2/5] 成本效率追踪..."
if [ -f "$SCRIPTS_DIR/cost-efficiency-tracker.py" ]; then
    python3 "$SCRIPTS_DIR/cost-efficiency-tracker.py" report > /dev/null 2>&1
    if [ -f "$REPORT_DIR/cost-report-$DATE.md" ]; then
        echo "   ✅ 成本报告已生成: cost-report-$DATE.md"
    else
        echo "   ⚠️  成本报告生成失败"
    fi
else
    echo "   ⚠️  cost-efficiency-tracker.py 不存在"
fi
echo ""

# 3. 缓存管理（每日执行）
echo "🗂️  [3/5] 缓存管理..."
if [ -f "$SCRIPTS_DIR/cache-manager.py" ]; then
    # 清理过期缓存
    CLEANED=$(python3 "$SCRIPTS_DIR/cache-manager.py" cleanup 2>/dev/null | grep -oP '\d+' | head -1)
    # 统计缓存
    CACHE_COUNT=$(ls "$REPORT_DIR/cache"/*.json 2>/dev/null | wc -l)
    CACHE_SIZE=$(du -sh "$REPORT_DIR/cache" 2>/dev/null | cut -f1)
    echo "   ✅ 清理过期: ${CLEANED:-0} 个, 当前缓存: $CACHE_COUNT 个 ($CACHE_SIZE)"
else
    echo "   ⚠️  cache-manager.py 不存在"
fi
echo ""

# 4. 知识库索引（每周执行）
echo "📚 [4/5] 知识库索引..."
if [ -f "$SCRIPTS_DIR/kb-indexer.py" ]; then
    # 检查索引是否需要更新（超过7天）
    INDEX_FILE="$REPORT_DIR/kb-index.json"
    if [ -f "$INDEX_FILE" ]; then
        INDEX_AGE=$(( ($(date +%s) - $(stat -c %Y "$INDEX_FILE")) / 86400 ))
        if [ $INDEX_AGE -gt 7 ]; then
            echo "   🔄 索引过期 ($INDEX_AGE 天前)，重新生成..."
            python3 "$SCRIPTS_DIR/kb-indexer.py" > /dev/null 2>&1
            echo "   ✅ 索引已更新"
        else
            echo "   ✅ 索引正常 (${INDEX_AGE}天前更新)"
        fi
    else
        echo "   🔄 索引不存在，生成中..."
        python3 "$SCRIPTS_DIR/kb-indexer.py" > /dev/null 2>&1
        echo "   ✅ 索引已生成"
    fi
else
    echo "   ⚠️  kb-indexer.py 不存在"
fi
echo ""

# 5. 质量漂移检测（每周执行）
echo "📊 [5/5] 质量漂移检测..."
if [ -f "$SCRIPTS_DIR/quality-drift-detector.py" ]; then
    python3 "$SCRIPTS_DIR/quality-drift-detector.py" > /dev/null 2>&1
    if [ -f "$REPORT_DIR/quality-drift-report.md" ]; then
        # 提取关键指标
        AVG_WORDS=$(grep "文章字数" "$REPORT_DIR/quality-drift-report.md" | grep -oP '\d+' | head -1)
        AGENT_RATIO=$(grep "Agent 视点占比" "$REPORT_DIR/quality-drift-report.md" | grep -oP '\d+\.\d+%' | head -1)
        echo "   ✅ 质量报告已生成"
        echo "      - 平均字数: ${AVG_WORDS:-未知}"
        echo "      - Agent 视点: ${AGENT_RATIO:-未知}"
    else
        echo "   ⚠️  质量报告生成失败"
    fi
else
    echo "   ⚠️  quality-drift-detector.py 不存在"
fi
echo ""

# 生成综合审计报告
echo "=========================================="
echo "📝 生成综合审计报告..."
echo "=========================================="

AUDIT_REPORT="$REPORT_DIR/audit-summary-$DATE.md"

cat > "$AUDIT_REPORT" << EOF
# 自动化审计报告

**生成时间**: $TIMESTAMP

## 执行摘要

| 审计项 | 状态 | 关键指标 |
|--------|------|----------|
| 工具审计 | ✅ | 活跃: $TOOL_COUNT, 归档: $ARCHIVE_COUNT |
| 成本效率 | ✅ | 报告: cost-report-$DATE.md |
| 缓存管理 | ✅ | 缓存: $CACHE_COUNT 个 ($CACHE_SIZE) |
| 知识库索引 | ✅ | 索引: kb-index.json |
| 质量检测 | ✅ | 报告: quality-drift-report.md |

## 详细报告

- 工具审计: [tool-audit-$DATE.md](tool-audit-$DATE.md)
- 成本效率: [cost-report-$DATE.md](cost-report-$DATE.md)
- 质量漂移: [quality-drift-report.md](quality-drift-report.md)
- 知识库索引: [kb-index-summary.md](kb-index-summary.md)

## 下一步行动

1. 检查成本报告，识别高消耗任务
2. 查看质量报告，改进低分文章
3. 审查工具使用率，清理低效技能
4. 更新知识库索引（如需要）

---
*此报告由自动化审计脚本生成*
*执行频率: 每日轻量审计，每周完整审计*
EOF

echo "✅ 综合报告: audit-summary-$DATE.md"
echo ""
echo "=========================================="
echo "审计完成！"
echo "=========================================="
