#!/bin/bash
# 生成指定数量的实例配置
# 用法：./generate-config.sh [实例数量]

COUNT=${1:-50}

if [ $COUNT -gt 50 ]; then
    echo "❌ 最多支持 50 个实例"
    exit 1
fi

echo "📝 生成 $COUNT 个实例配置..."

cat > configs/instances.yaml << 'EOF'
# Lobster Orchestrator 配置文件
# 自动生成 - 请勿手动编辑

instances:
EOF

for i in $(seq 1 $COUNT); do
    id=$(printf "lobster-%03d" $i)
    port=$((18789 + $i))
    cat >> configs/instances.yaml << EOF
  - id: "$id"
    name: "Sandbot #$i"
    workspace: "data/workspaces/$id"
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

echo "✅ 配置已生成：configs/instances.yaml"
echo "📊 实例数量：$COUNT"
echo "🌐 端口范围：18790-$((18789 + $COUNT))"
