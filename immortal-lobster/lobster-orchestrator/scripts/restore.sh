#!/bin/bash
# Lobster Orchestrator 恢复脚本
# 用法：./scripts/restore.sh [备份名称]

set -e

if [[ -z "$1" ]]; then
    echo "🦞 Lobster Orchestrator 恢复脚本"
    echo "================================"
    echo ""
    echo "可用备份:"
    ls -1 data/backups/ 2>/dev/null || echo "  无备份"
    echo ""
    echo "用法：./scripts/restore.sh [备份名称]"
    echo ""
    exit 1
fi

BACKUP_NAME=$1
BACKUP_DIR="data/backups/$BACKUP_NAME"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "🦞 Lobster Orchestrator 恢复脚本"
echo "================================"
echo ""

# 检查备份是否存在
if [[ ! -d "$BACKUP_DIR" ]]; then
    echo "❌ 备份不存在：$BACKUP_NAME"
    echo ""
    echo "可用备份:"
    ls -1 data/backups/ 2>/dev/null || echo "  无备份"
    exit 1
fi

echo "📁 备份位置：$BACKUP_DIR"
echo ""

# 确认恢复
read -p "⚠️  确定要恢复到备份 $BACKUP_NAME 吗？(当前配置将被覆盖) (y/n): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ 恢复已取消"
    exit 0
fi

# 停止服务
echo "⏹️  停止服务..."
if pgrep -f "orchestrator" > /dev/null; then
    pkill -f "orchestrator" || true
    sleep 2
    echo "✅ 服务已停止"
else
    echo "⚠️  服务未运行"
fi

# 恢复配置
echo "📋 恢复配置文件..."
if [[ -d "$BACKUP_DIR/configs" ]]; then
    cp -r "$BACKUP_DIR/configs" "$PROJECT_DIR/"
    echo "✅ 配置已恢复"
else
    echo "⚠️  配置备份不存在，跳过"
fi

# 恢复 go.mod
if [[ -f "$BACKUP_DIR/go.mod" ]]; then
    cp "$BACKUP_DIR/go.mod" "$PROJECT_DIR/"
    echo "✅ go.mod 已恢复"
fi

# 恢复工作区 (可选)
if [[ -f "$BACKUP_DIR/workspaces.tar.gz" ]]; then
    read -p "是否恢复工作区数据？(y/n, 默认 n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📦 恢复工作区数据..."
        tar -xzf "$BACKUP_DIR/workspaces.tar.gz" -C "$PROJECT_DIR/data/"
        echo "✅ 工作区已恢复"
    fi
fi

# 恢复日志
if [[ -d "$BACKUP_DIR/logs" ]]; then
    echo "📝 恢复日志文件..."
    mkdir -p "$PROJECT_DIR/logs"
    cp "$BACKUP_DIR/logs"/*.log "$PROJECT_DIR/logs/" 2>/dev/null || true
    echo "✅ 日志已恢复"
fi

# 显示备份信息
if [[ -f "$BACKUP_DIR/BACKUP_INFO.txt" ]]; then
    echo ""
    echo "📋 备份信息:"
    cat "$BACKUP_DIR/BACKUP_INFO.txt"
fi

echo ""
echo "✅ 恢复完成！"
echo ""
echo "🚀 启动命令：./orchestrator -config configs/instances.yaml"
echo ""
