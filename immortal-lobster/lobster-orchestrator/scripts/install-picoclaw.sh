#!/bin/bash
# PicoClaw 自动安装脚本
# 用法：./scripts/install-picoclaw.sh [版本]

set -e

VERSION="${1:-latest}"
INSTALL_DIR="${PICOCLAW_INSTALL_DIR:-$HOME/bin}"
LOG="/home/node/.openclaw/workspace/memory/picoclaw-install.log"

echo "🦞 PicoClaw 安装脚本"
echo "===================="
echo ""

# 检测系统架构
ARCH=$(uname -m)
case $ARCH in
    x86_64) ARCH_FILE="amd64" ;;
    aarch64|arm64) ARCH_FILE="arm64" ;;
    *) echo "❌ 不支持的架构：$ARCH"; exit 1 ;;
esac

# 检测操作系统
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
case $OS in
    linux) OS_FILE="linux" ;;
    darwin) OS_FILE="darwin" ;;
    *) echo "❌ 不支持的系统：$OS"; exit 1 ;;
esac

echo "📊 系统信息：$OS_FILE/$ARCH_FILE"

# 创建安装目录
mkdir -p "$INSTALL_DIR"

# 检查是否已安装
if command -v picoclaw &> /dev/null; then
    CURRENT_VERSION=$(picoclaw version 2>&1 | grep -oP 'v\K[0-9.]+' || echo "unknown")
    echo "📦 当前版本：v$CURRENT_VERSION"
    
    if [ "$VERSION" = "latest" ]; then
        # 获取最新版本
        LATEST_VERSION=$(curl -s https://api.github.com/repos/sipeed/picoclaw/releases/latest | grep '"tag_name"' | cut -d'"' -f4 | tr -d 'v')
        echo "📦 最新版本：v$LATEST_VERSION"
        
        if [ "$CURRENT_VERSION" = "$LATEST_VERSION" ]; then
            echo "✅ 已是最新版本"
            exit 0
        fi
        
        read -p "是否升级到 v$LATEST_VERSION？(y/n): " -n 1 -r
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "❌ 升级已取消"
            exit 0
        fi
    fi
fi

# 下载
if [ "$VERSION" = "latest" ]; then
    DOWNLOAD_URL="https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_${OS_FILE}_${ARCH_FILE}.tar.gz"
else
    DOWNLOAD_URL="https://github.com/sipeed/picoclaw/releases/download/v$VERSION/picoclaw_${OS_FILE}_${ARCH_FILE}.tar.gz"
fi

echo "🔄 下载 PicoClaw $VERSION..."
echo "   URL: $DOWNLOAD_URL"

TMP_FILE="/tmp/picoclaw-${VERSION}.tar.gz"
curl -sL "$DOWNLOAD_URL" -o "$TMP_FILE"

if [ ! -f "$TMP_FILE" ] || [ ! -s "$TMP_FILE" ]; then
    echo "❌ 下载失败"
    exit 1
fi

# 解压
echo "📦 解压..."
tar xzf "$TMP_FILE" -C "$INSTALL_DIR"
rm -f "$TMP_FILE"

# 添加执行权限
chmod +x "$INSTALL_DIR/picoclaw"

# 验证安装
echo "✅ 验证安装..."
"$INSTALL_DIR/picoclaw" version

# 添加到 PATH (如果不在 PATH 中)
if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    echo ""
    echo "⚠️  $INSTALL_DIR 不在 PATH 中"
    echo "请添加到 ~/.bashrc 或 ~/.zshrc:"
    echo "   export PATH=\$PATH:$INSTALL_DIR"
fi

# 记录日志
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) INSTALLED: picoclaw $VERSION" >> "$LOG"

echo ""
echo "✅ PicoClaw 安装完成！"
echo "📍 安装位置：$INSTALL_DIR/picoclaw"
echo ""
echo "🚀 测试运行:"
echo "   picoclaw version"
echo "   picoclaw onboard"
echo ""
