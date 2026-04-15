#!/bin/bash
# Lobster Orchestrator 一键安装脚本 (小白友好版)
# 用法：curl -sL https://... | bash

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印函数
print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# 标题
echo ""
echo "╔════════════════════════════════════════════════════════╗"
echo "║     🦞 Lobster Orchestrator 一键安装脚本              ║"
echo "║     不死龙虾编排器 - 手机运行 50 个 PicoClaw 实例        ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# 检测系统
print_info "检测系统环境..."
if [[ "$OSTYPE" == "linux-android"* ]]; then
    SYSTEM="termux"
    print_info "检测到 Termux (Android)"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    SYSTEM="linux"
    print_info "检测到 Linux"
else
    print_error "不支持的系统：$OSTYPE"
    exit 1
fi

# 检查依赖
print_info "检查依赖..."

# 检查 Git
if ! command -v git &> /dev/null; then
    print_warning "Git 未安装"
    if [[ "$SYSTEM" == "termux" ]]; then
        print_info "正在安装 Git (Termux)..."
        pkg install -y git
    else
        print_info "正在安装 Git (apt)..."
        sudo apt-get update && sudo apt-get install -y git
    fi
fi
print_success "Git 已安装"

# 检查 Go
if ! command -v go &> /dev/null; then
    print_warning "Go 未安装"
    if [[ "$SYSTEM" == "termux" ]]; then
        print_info "正在安装 Go (Termux)..."
        pkg install -y golang
    else
        print_info "正在安装 Go (apt)..."
        sudo apt-get update && sudo apt-get install -y golang
    fi
fi
print_success "Go 已安装 ($(go version))"

# 检查 jq (可选)
if ! command -v jq &> /dev/null; then
    print_warning "jq 未安装 (可选，用于 JSON 处理)"
    if [[ "$SYSTEM" == "termux" ]]; then
        pkg install -y jq || true
    else
        sudo apt-get install -y jq || true
    fi
fi

# 克隆项目
print_info "克隆项目..."
if [[ -d "lobster-orchestrator" ]]; then
    print_warning "项目已存在，跳过克隆"
    cd lobster-orchestrator
else
    git clone https://github.com/immortal-lobster/lobster-orchestrator
    cd lobster-orchestrator
fi
print_success "项目已克隆"

# 安装依赖
print_info "安装 Go 依赖..."
go mod tidy
print_success "依赖已安装"

# 编译
print_info "编译项目..."
go build -o orchestrator ./cmd/orchestrator
if [[ -f "orchestrator" ]]; then
    print_success "编译成功！"
    ls -lh orchestrator
else
    print_error "编译失败！"
    exit 1
fi

# 创建目录
print_info "创建工作目录..."
mkdir -p data/workspaces
mkdir -p data/backups
mkdir -p logs
print_success "目录已创建"

# 生成配置
print_info "生成配置文件..."
if [[ ! -f "configs/instances.yaml" ]]; then
    ./scripts/generate-config.sh 10  # 默认生成 10 个实例
    print_success "配置已生成 (10 个实例)"
else
    print_warning "配置已存在，跳过生成"
fi

# 安装完成
echo ""
print_success "╔════════════════════════════════════════════════════════╗"
print_success "║              🎉 安装完成！                             ║"
print_success "╚════════════════════════════════════════════════════════╝"
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
echo "🔧 常用命令:"
echo "  • 查看状态：curl http://localhost:8080/api/v1/instances"
echo "  • 启动实例：curl -X POST http://localhost:8080/api/v1/instances/lobster-001"
echo "  • 停止实例：curl -X DELETE http://localhost:8080/api/v1/instances/lobster-001"
echo "  • 备份数据：./scripts/backup.sh"
echo ""
echo "🦞 不死龙虾，持续进化！"
echo ""
