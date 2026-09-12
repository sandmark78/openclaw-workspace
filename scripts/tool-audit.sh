#!/bin/bash
# 工具审计脚本 - 每周检查工具使用率

WORKSPACE="/home/node/.openclaw/workspace"
SKILLS_DIR="$WORKSPACE/skills"
REPORT_FILE="$WORKSPACE/memory/tool-audit-$(date +%Y-%m-%d).md"

echo "# 工具审计报告" > "$REPORT_FILE"
echo "**生成时间**: $(date '+%Y-%m-%d %H:%M:%S UTC')" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 统计技能总数
TOTAL_SKILLS=$(ls -d "$SKILLS_DIR"/*/ 2>/dev/null | wc -l)
echo "## 概览" >> "$REPORT_FILE"
echo "- 技能总数: $TOTAL_SKILLS" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 分类统计
echo "## 技能分类" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 检查每个技能的使用情况
echo "## 详细分析" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    
    # 跳过非技能目录
    [[ "$skill_name" == "README.md" ]] && continue
    [[ "$skill_name" == *.md ]] && continue
    
    # 检查是否有 SKILL.md
    if [[ -f "$skill_dir/SKILL.md" ]]; then
        skill_size=$(du -sh "$skill_dir" 2>/dev/null | cut -f1)
        file_count=$(find "$skill_dir" -type f 2>/dev/null | wc -l)
        
        echo "### $skill_name" >> "$REPORT_FILE"
        echo "- 路径: \`$skill_dir\`" >> "$REPORT_FILE"
        echo "- 大小: $skill_size" >> "$REPORT_FILE"
        echo "- 文件数: $file_count" >> "$REPORT_FILE"
        
        # 检查最后修改时间
        last_modified=$(stat -c %y "$skill_dir/SKILL.md" 2>/dev/null | cut -d' ' -f1)
        echo "- 最后修改: $last_modified" >> "$REPORT_FILE"
        
        # 检查是否有脚本
        script_count=$(find "$skill_dir" -name "*.sh" -o -name "*.py" 2>/dev/null | wc -l)
        echo "- 脚本数: $script_count" >> "$REPORT_FILE"
        
        echo "" >> "$REPORT_FILE"
    fi
done

# 生成优化建议
echo "## 优化建议" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 检查大文件技能
echo "### 大文件技能 (>1MB)" >> "$REPORT_FILE"
find "$SKILLS_DIR" -type d -exec du -sm {} \; 2>/dev/null | awk '$1 > 1 {print "- " $2 ": " $1 "MB"}' | sort -t: -k2 -nr >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 检查长期未更新的技能
echo "### 长期未更新技能 (>30天)" >> "$REPORT_FILE"
find "$SKILLS_DIR" -name "SKILL.md" -mtime +30 -exec dirname {} \; 2>/dev/null | while read dir; do
    skill_name=$(basename "$dir")
    days_old=$(( ($(date +%s) - $(stat -c %Y "$dir/SKILL.md")) / 86400 ))
    echo "- $skill_name: ${days_old}天未更新" >> "$REPORT_FILE"
done
echo "" >> "$REPORT_FILE"

echo "✅ 审计报告已生成: $REPORT_FILE"
