#!/bin/bash
# Lobster Orchestrator 升级脚本
# 用法：./scripts/update.sh

set -e

echo "🦞 Lobster Orchestrator 升级脚本"
echo "================================"
echo ""

# 检查 Git
if ! command -v git &> /dev/null; then
    echo "❌ Git 未安装，无法升级"
    exit 1
fi

# 当前版本
CURRENT_VERSION="0.3.5"
echo "📊 当前版本：v$CURRENT_VERSION"

# 获取最新版本
echo "🔍 检查最新版本..."
LATEST_TAG=$(curl -s https://api.github.com/repos/immortal-lobster/lobster-orchestrator/releases/latest | grep '"tag_name"' | cut -d'"' -f4)
LATEST_VERSION=${LATEST_TAG#v}

echo "📦 最新版本：v$LATEST_VERSION"

# 比较版本
if [ "$CURRENT_VERSION" = "$LATEST_VERSION" ]; then
    echo "✅ 已是最新版本"
    exit 0
fi

# 确认升级
read -p "是否升级到 v$LATEST_VERSION？(y/n): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ 升级已取消"
    exit 0
fi

# 备份当前配置
echo "📦 备份当前配置..."
BACKUP_DIR="data/backups/pre-update-$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp configs/instances.yaml "$BACKUP_DIR/" 2>/dev/null || true
cp -r data/workspaces "$BACKUP_DIR/" 2>/dev/null || true
echo "✅ 备份完成：$BACKUP_DIR"

# 拉取最新代码
echo "🔄 拉取最新代码..."
git fetch origin master
git reset --hard origin/master

# 重新编译
echo "🔨 重新编译..."
go mod tidy
go build -o orchestrator ./cmd/orchestrator

# 恢复配置
echo "📋 恢复配置..."
if [[ -f "$BACKUP_DIR/instances.yaml" ]]; then
    cp "$BACKUP_DIR/instances.yaml" configs/instances.yaml
    echo "✅ 配置已恢复"
fi

# 显示更新日志
echo ""
echo "📝 更新日志:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
curl -s https://raw.githubusercontent.com/immortal-lobster/lobster-orchestrator/master/CHANGELOG.md | head -50
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📚 完整升级指南：https://github.com/immortal-lobster/lobster-orchestrator/blob/main/docs/UPGRADE.md"
echo ""
echo "✅ 升级完成！"
echo "📊 新版本：v$LATEST_VERSION"
echo ""
echo "🚀 重启服务:"
echo "   ./orchestrator -config configs/instances.yaml"
echo ""
echo "🔍 检查版本:"
echo "   curl http://localhost:8080/api/v1/version"
echo ""
