#!/bin/bash
# 每日 20:00 汇报脚本

TIMESTAMP=$(date '+%Y-%m-%d %H:%M UTC')
REPORT_FILE="/home/node/.openclaw/workspace/memory/daily-report-$(date '+%Y-%m-%d').md"

echo "# 📊 每日汇报 - ${TIMESTAMP}" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "## 今天做了什么？" >> "$REPORT_FILE"
echo "- 检查并总结全天工作" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "## 有什么突破？" >> "$REPORT_FILE"
echo "- 检查并记录突破性进展" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "## 收益状态" >> "$REPORT_FILE"
echo "- Gumroad: 待检查" >> "$REPORT_FILE"
echo "- Moltbook: 待检查" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "## 明日计划" >> "$REPORT_FILE"
echo "- 制定明日目标" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "✅ 每日汇报已创建：$REPORT_FILE"
