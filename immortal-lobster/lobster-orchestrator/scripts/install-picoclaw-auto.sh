#!/bin/bash
# PicoClaw 一键安装脚本
# 自动安装 Go、依赖库、编译并安装 PicoClaw

set -e

echo "🦞 PicoClaw 一键安装脚本"
echo "========================"
echo ""

# 检测系统架构
ARCH=$(uname -m)
echo "📊 系统架构：$ARCH"

# 检测操作系统
if [[ -f /etc/os-release ]]; then
    . /etc/os-release
    OS=$ID
    echo "📊 操作系统：$OS $VERSION_ID"
else
    OS="unknown"
    echo "⚠️  无法检测操作系统"
fi

# 检查并安装 Go
echo ""
echo "🔧 检查 Go 环境..."
if command -v go &> /dev/null; then
    GO_VERSION=$(go version)
    echo "✅ Go 已安装：$GO_VERSION"
else
    echo "⚠️  Go 未安装，开始安装..."
    
    # 下载并安装 Go
    GO_VERSION="1.25.8"
    GO_DOWNLOAD_URL="https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz"
    
    echo "📥 下载 Go $GO_VERSION..."
    curl -sL "$GO_DOWNLOAD_URL" -o /tmp/go.tar.gz
    
    echo "📦 安装 Go..."
    sudo tar -xzf /tmp/go.tar.gz -C /usr/local
    rm /tmp/go.tar.gz
    
    # 设置环境变量
    export PATH=$PATH:/usr/local/go/bin
    echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
    
    echo "✅ Go 安装完成"
fi

# 检查并安装依赖
echo ""
echo "🔧 检查依赖..."

# 检查 git
if ! command -v git &> /dev/null; then
    echo "⚠️  Git 未安装，开始安装..."
    if [[ "$OS" == "ubuntu" || "$OS" == "debian" ]]; then
        sudo apt-get update && sudo apt-get install -y git
    elif [[ "$OS" == "centos" || "$OS" == "fedora" ]]; then
        sudo yum install -y git
    fi
    echo "✅ Git 安装完成"
else
    echo "✅ Git 已安装"
fi

# 检查 make
if ! command -v make &> /dev/null; then
    echo "⚠️  Make 未安装，开始安装..."
    if [[ "$OS" == "ubuntu" || "$OS" == "debian" ]]; then
        sudo apt-get install -y make
    elif [[ "$OS" == "centos" || "$OS" == "fedora" ]]; then
        sudo yum install -y make
    fi
    echo "✅ Make 安装完成"
else
    echo "✅ Make 已安装"
fi

# 克隆并编译 PicoClaw
echo ""
echo "🦞 安装 PicoClaw..."

# 创建临时目录
TMP_DIR="/tmp/picoclaw-install-$$"
mkdir -p "$TMP_DIR"
cd "$TMP_DIR"

# 克隆源码
echo "📥 克隆 PicoClaw 源码..."
git clone --depth 1 https://github.com/sipeed/picoclaw.git
cd picoclaw

# 生成 embed 文件
echo "🔧 生成嵌入文件..."
go generate ./cmd/picoclaw/internal/onboard/...

# 编译
echo "🔨 编译 PicoClaw..."
export GOCACHE=/tmp/go-cache
go build -o picoclaw-bin ./cmd/picoclaw

# 安装
echo "📦 安装 PicoClaw..."
sudo mv picoclaw-bin /usr/local/bin/picoclaw
sudo chmod +x /usr/local/bin/picoclaw

# 验证
echo ""
echo "✅ PicoClaw 安装完成！"
picoclaw --version

# 清理
echo ""
echo "🧹 清理临时文件..."
cd /
rm -rf "$TMP_DIR"

echo ""
echo "🎉 PicoClaw 安装完成！"
echo ""
echo "📝 下一步："
echo "1. 运行 'picoclaw onboard' 进行初始化"
echo "2. 配置 ~/.picoclaw/config.json"
echo "3. 运行 'picoclaw gateway' 启动服务"
echo ""
