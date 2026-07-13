#!/bin/bash
# Lobster Orchestrator 压力测试脚本
# 用途：测试 50 实例并发性能

set -e

echo "🦞 Lobster Orchestrator 压力测试"
echo "================================="

API_BASE="${API_BASE:-http://localhost:8080/api/v1}"

# 1. 健康检查
echo "🔍 检查服务状态..."
if curl -s "$API_BASE/health" | grep -q "healthy"; then
    echo "✅ 服务正常"
else
    echo "❌ 服务未运行"
    exit 1
fi

# 2. 获取所有实例
echo "📊 获取实例列表..."
INSTANCES=$(curl -s "$API_BASE/instances" | jq -r '.instances[].id')
COUNT=$(echo "$INSTANCES" | wc -l)
echo "📦 共 $COUNT 个实例"

# 3. 启动所有实例
echo "🚀 启动所有实例..."
START_TIME=$(date +%s)

for id in $INSTANCES; do
    curl -s -X POST "$API_BASE/instances/$id" > /dev/null &
done
wait

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
echo "✅ 启动完成 (耗时：${DURATION}s)"

# 4. 等待实例就绪
echo "⏳ 等待实例就绪 (30s)..."
sleep 30

# 5. 检查运行状态
echo "📊 检查运行状态..."
RUNNING=0
STOPPED=0
CRASHED=0

for id in $INSTANCES; do
    STATUS=$(curl -s "$API_BASE/instances/$id" | jq -r '.instance.status')
    case $STATUS in
        running) RUNNING=$((RUNNING + 1)) ;;
        stopped) STOPPED=$((STOPPED + 1)) ;;
        crashed) CRASHED=$((CRASHED + 1)) ;;
    esac
done

echo ""
echo "📈 测试结果:"
echo "  ✅ 运行中：$RUNNING / $COUNT"
echo "  ⏹️  已停止：$STOPPED / $COUNT"
echo "  💥 已崩溃：$CRASHED / $COUNT"
echo ""

# 6. 性能指标
if [ $RUNNING -eq $COUNT ]; then
    echo "🎉 测试通过！所有实例正常运行"
    echo ""
    echo "📊 性能指标:"
    echo "  启动时间：${DURATION}s"
    echo "  平均每实例：$(echo "scale=2; $DURATION / $COUNT" | bc)s"
    echo "  成功率：100%"
else
    echo "⚠️  测试未通过，$((COUNT - RUNNING)) 个实例启动失败"
fi

# 7. 停止所有实例
echo ""
echo "⏹️  停止所有实例..."
for id in $INSTANCES; do
    curl -s -X DELETE "$API_BASE/instances/$id" > /dev/null &
done
wait
echo "✅ 已停止"
