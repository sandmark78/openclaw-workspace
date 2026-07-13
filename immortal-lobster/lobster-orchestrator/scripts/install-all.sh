#!/bin/bash
# Lobster Orchestrator 一键安装脚本 (包含 PicoClaw)
# 用法：curl -sL https://.../install-all.sh | bash

set -e

echo "🦞 Lobster Orchestrator 一键安装 (包含 PicoClaw)"
echo "================================================"
echo ""

# 检测系统
if [[ "$OSTYPE" == "linux-android"* ]]; then
    SYSTEM="termux"
    echo "📱 检测到 Termux (Android)"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    SYSTEM="linux"
    echo "🐧 检测到 Linux"
else
    echo "❌ 不支持的系统：$OSTYPE"
    exit 1
fi

# 安装依赖
echo ""
echo "📦 安装依赖..."
if [[ "$SYSTEM" == "termux" ]]; then
    pkg update -y && pkg upgrade -y
    pkg install -y git golang curl jq wget proot
else
    # 检测包管理器
    if command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y git golang curl jq wget
    elif command -v yum &> /dev/null; then
        sudo yum install -y git golang curl jq wget
    elif command -v brew &> /dev/null; then
        brew install git go curl jq wget
    fi
fi

# 安装 PicoClaw
echo ""
echo "🦞 安装 PicoClaw..."
curl -sL https://raw.githubusercontent.com/immortal-lobster/lobster-orchestrator/master/scripts/install-picoclaw.sh | bash

# 设置环境变量
echo ""
echo "⚙️  设置环境变量..."
echo 'export PICOCLAW_PATH=$HOME/bin/picoclaw' >> ~/.bashrc
source ~/.bashrc 2>/dev/null || true

# 克隆 Lobster Orchestrator
echo ""
echo "🦞 克隆 Lobster Orchestrator..."
if [[ -d "lobster-orchestrator" ]]; then
    echo "⚠️  项目已存在，跳过克隆"
    cd lobster-orchestrator
else
    git clone https://github.com/immortal-lobster/lobster-orchestrator
    cd lobster-orchestrator
fi

# 编译 Lobster
echo ""
echo "🔨 编译 Lobster Orchestrator..."
go mod tidy
go build -o orchestrator ./cmd/orchestrator

# 生成配置
echo ""
echo "📋 生成配置..."
if [[ ! -f "configs/instances.yaml" ]]; then
    ./scripts/generate-config.sh 2
fi

# 创建目录
echo ""
echo "📁 创建目录..."
mkdir -p data/workspaces data/backups logs

# 完成
echo ""
echo "✅ 安装完成！"
echo ""
echo "📁 项目目录：$(pwd)"
echo "📋 配置文件：configs/instances.yaml"
echo "🚀 启动命令：./orchestrator -config configs/instances.yaml"
echo "🌐 Dashboard: http://localhost:8080"
echo ""
echo "📚 快速开始:"
echo "  1. 编辑配置：nano configs/instances.yaml"
echo "  2. 启动服务：./orchestrator -config configs/instances.yaml"
echo "  3. 访问面板：http://localhost:8080"
echo ""
echo "🦞 不死龙虾，持续进化！"
echo ""
