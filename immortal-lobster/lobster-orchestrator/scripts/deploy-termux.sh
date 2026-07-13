#!/bin/bash
# Lobster Orchestrator 部署脚本 (Termux/Android)
# 用法：./deploy-termux.sh

set -e

echo "🦞 Lobster Orchestrator 部署脚本"
echo "================================"

# 1. 检查 Go 环境
if ! command -v go &> /dev/null; then
    echo "❌ Go 未安装，请先安装 Go 1.21+"
    echo "   Termux: pkg install golang"
    exit 1
fi
echo "✅ Go 版本：$(go version)"

# 2. 安装依赖
echo "📦 安装依赖..."
go mod tidy

# 3. 编译
echo "🔨 编译中..."
go build -o orchestrator ./cmd/orchestrator

if [ -f "orchestrator" ]; then
    echo "✅ 编译成功！"
    ls -lh orchestrator
else
    echo "❌ 编译失败"
    exit 1
fi

# 4. 创建工作目录
echo "📁 创建工作目录..."
mkdir -p /data/workspaces
for i in $(seq 1 50); do
    mkdir -p /data/workspaces/lobster-$(printf "%03d" $i)
done
echo "✅ 创建 50 个工作目录"

# 5. 生成 50 实例配置
echo "📝 生成 50 实例配置..."
cat > configs/instances.yaml << 'EOF'
# Lobster Orchestrator 配置文件 - 50 实例版本
instances:
EOF

for i in $(seq 1 50); do
    id=$(printf "lobster-%03d" $i)
    port=$((18789 + $i))
    cat >> configs/instances.yaml << EOF
  - id: "$id"
    name: "Sandbot #$i"
    workspace: "/data/workspaces/$id"
    port: $port
    model: "qwen3.5-plus"
    api_key_env: "BAILOU_API_KEY_$i"
    memory_limit_mb: 10
    auto_start: true

EOF
done

cat >> configs/instances.yaml << 'EOF'
global:
  orchestrator_port: 8080
  health_check_interval_s: 30
  log_level: "info"
  max_instances: 50
EOF

echo "✅ 配置生成完成"

# 6. 启动服务
echo "🚀 启动服务..."
./orchestrator -config configs/instances.yaml -port 8080 &
echo "✅ 服务已启动 (PID: $!)"
echo ""
echo "🌐 访问 Dashboard: http://localhost:8080"
echo "📊 API: http://localhost:8080/api/v1/instances"
echo ""
echo "🦞 不死龙虾编排器部署完成！"
