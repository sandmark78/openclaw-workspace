#!/bin/bash
# 每 2 小时自省脚本

TIMESTAMP=$(date '+%Y-%m-%d %H:%M UTC')
DATE=$(date '+%Y-%m-%d')
REFLECTION_FILE="/home/node/.openclaw/workspace/memory/reflection-${DATE}.md"

echo "# 🤔 自我反思 - ${TIMESTAMP}" >> "$REFLECTION_FILE"
echo "" >> "$REFLECTION_FILE"
echo "## 过去 2 小时做了什么？" >> "$REFLECTION_FILE"
echo "- [ ] 检查并记录" >> "$REFLECTION_FILE"
echo "" >> "$REFLECTION_FILE"
echo "## 有什么突破？" >> "$REFLECTION_FILE"
echo "- [ ] 检查并记录" >> "$REFLECTION_FILE"
echo "" >> "$REFLECTION_FILE"
echo "## 哪里可以更好？" >> "$REFLECTION_FILE"
echo "- [ ] 检查并记录" >> "$REFLECTION_FILE"
echo "" >> "$REFLECTION_FILE"
echo "## 下 2 小时如何改进？" >> "$REFLECTION_FILE"
echo "- [ ] 制定具体行动计划" >> "$REFLECTION_FILE"
echo "" >> "$REFLECTION_FILE"
echo "---" >> "$REFLECTION_FILE"
echo "" >> "$REFLECTION_FILE"

echo "✅ 自省记录已创建：$REFLECTION_FILE"
