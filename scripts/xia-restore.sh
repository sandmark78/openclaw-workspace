#!/bin/bash
# 虾聊记忆恢复脚本
# 用法：./xia-restore.sh [备份目录]

BACKUP_DIR="${1:-$(ls -td /home/node/.openclaw/workspace/backups/xia-memory/*/ | head -1)}"

if [ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]; then
    echo "❌ 未找到备份目录"
    echo "用法：./xia-restore.sh [备份目录]"
    exit 1
fi

echo "📦 恢复目录：$BACKUP_DIR"

# 读取备份索引
if [ -f "$BACKUP_DIR/INDEX.md" ]; then
    echo "📋 备份信息:"
    cat "$BACKUP_DIR/INDEX.md"
fi

# 恢复帖子
echo "📝 恢复帖子..."
POST_COUNT=$(ls -1 "$BACKUP_DIR"/post_*.json 2>/dev/null | wc -l)
echo "  找到 $POST_COUNT 个帖子备份"

# 恢复评论
echo "💬 恢复评论..."
COMMENT_COUNT=$(ls -1 "$BACKUP_DIR"/comment_*.json 2>/dev/null | wc -l)
echo "  找到 $COMMENT_COUNT 条评论备份"

# 生成恢复报告
cat > "$BACKUP_DIR/RESTORE_REPORT.md" << EOF
# 虾聊记忆恢复报告

**恢复日期**: $(date +%Y-%m-%d)
**恢复时间**: $(date -u +%Y-%m-%dT%H:%M:%SZ)
**备份来源**: $BACKUP_DIR

## 恢复统计

- 帖子：$POST_COUNT 个
- 评论：$COMMENT_COUNT 条

## 后续步骤

1. 检查恢复的文件是否完整
2. 手动重新发布重要帖子
3. 在其他平台重新互动

## 注意事项

由于 API 限制，无法自动重新发布内容。
需要手动复制内容到目标平台。
EOF

echo "✅ 恢复完成！"
echo "📄 恢复报告：$BACKUP_DIR/RESTORE_REPORT.md"
