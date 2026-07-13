#!/bin/bash
# Lobster Orchestrator 备份脚本
# 用法：./scripts/backup.sh [备份名称]

set -e

BACKUP_NAME=${1:-$(date +%Y%m%d_%H%M%S)}
BACKUP_DIR="data/backups/$BACKUP_NAME"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "🦞 Lobster Orchestrator 备份脚本"
echo "================================"
echo ""

# 创建备份目录
echo "📁 创建备份目录：$BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

# 备份配置
echo "📋 备份配置文件..."
cp -r "$PROJECT_DIR/configs" "$BACKUP_DIR/configs"
cp "$PROJECT_DIR/go.mod" "$BACKUP_DIR/go.mod" 2>/dev/null || true

# 备份工作区 (可选，较大)
read -p "是否备份工作区数据？(y/n, 默认 n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 备份工作区数据..."
    if [[ -d "$PROJECT_DIR/data/workspaces" ]]; then
        tar -czf "$BACKUP_DIR/workspaces.tar.gz" -C "$PROJECT_DIR/data" workspaces
        echo "✅ 工作区已备份"
    else
        echo "⚠️  工作区不存在，跳过"
    fi
fi

# 备份日志 (最近 7 天)
echo "📝 备份日志文件..."
if [[ -d "$PROJECT_DIR/logs" ]]; then
    find "$PROJECT_DIR/logs" -name "*.log" -mtime -7 -exec cp {} "$BACKUP_DIR/logs/" \; 2>/dev/null || true
    echo "✅ 日志已备份 (最近 7 天)"
fi

# 生成备份清单
echo "📋 生成备份清单..."
cat > "$BACKUP_DIR/BACKUP_INFO.txt" << EOF
Lobster Orchestrator 备份信息
============================

备份名称：$BACKUP_NAME
备份时间：$(date '+%Y-%m-%d %H:%M:%S')
项目版本：$(cd "$PROJECT_DIR" && git describe --tags 2>/dev/null || echo "unknown")
Git 提交：$(cd "$PROJECT_DIR" && git rev-parse --short HEAD 2>/dev/null || echo "unknown")

备份内容:
$(ls -la "$BACKUP_DIR")

系统信息:
$(uname -a)
Go 版本：$(go version 2>/dev/null || echo "unknown")

恢复命令:
./scripts/restore.sh $BACKUP_NAME
EOF

# 显示备份大小
BACKUP_SIZE=$(du -sh "$BACKUP_DIR" | cut -f1)
echo ""
echo "✅ 备份完成！"
echo "📦 备份位置：$BACKUP_DIR"
echo "📊 备份大小：$BACKUP_SIZE"
echo ""
echo "🔧 恢复命令：./scripts/restore.sh $BACKUP_NAME"
echo ""
