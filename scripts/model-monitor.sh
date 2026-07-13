#!/bin/bash
# 模型调用监控脚本 - 每日上限 200 次
# 用法：每 10 分钟执行一次

WORKSPACE="/home/node/.openclaw/workspace"
LOG_DIR="/tmp/openclaw"
MONITOR_LOG="$WORKSPACE/memory/model-usage.log"
TODAY=$(date +%Y-%m-%d)
DAILY_LIMIT=200

# 读取上次计数
COUNT_FILE="$WORKSPACE/memory/.model_call_count_$TODAY"
if [[ -f "$COUNT_FILE" ]]; then
    CALL_COUNT=$(cat "$COUNT_FILE")
else
    CALL_COUNT=0
fi

# 统计最近 10 分钟的调用次数
NEW_CALLS=$(find "$LOG_DIR" -name "*.log" -mmin -10 -exec grep -l "model\|API\|bailian" {} \; 2>/dev/null | wc -l)
CALL_COUNT=$((CALL_COUNT + NEW_CALLS))

# 保存当前计数
echo "$CALL_COUNT" > "$COUNT_FILE"

# 记录日志
echo "$(date '+%Y-%m-%d %H:%M:%S') - 当前调用：$CALL_COUNT/$DAILY_LIMIT" >> "$MONITOR_LOG"

# 检查是否超限
if [[ $CALL_COUNT -ge $DAILY_LIMIT ]]; then
    echo "🚨 模型调用超限警告！" >> "$MONITOR_LOG"
    echo "🚨 当前调用：$CALL_COUNT/$DAILY_LIMIT" >> "$MONITOR_LOG"
    echo "🚨 已暂停模型调用，等待用户确认" >> "$MONITOR_LOG"
    
    # 创建警报文件
    cat > "$WORKSPACE/memory/.model_alert" << EOF
{
  "alert": "MODEL_CALL_LIMIT_EXCEEDED",
  "count": $CALL_COUNT,
  "limit": $DAILY_LIMIT,
  "time": "$(date '+%Y-%m-%d %H:%M:%S')",
  "status": "PAUSED",
  "message": "模型调用已达每日上限 ($CALL_COUNT/$DAILY_LIMIT)，已暂停调用。请确认是否继续。"
}
EOF
    
    # 发送通知 (需要调用模型 - 这是今日最后一次)
    echo "🚨 模型调用超限警报"
    echo "   当前调用：$CALL_COUNT/$DAILY_LIMIT"
    echo "   状态：已暂停"
    echo "   请确认是否继续：y/n"
    
    # 暂停模型调用 (设置标志文件)
    touch "$WORKSPACE/memory/.model_calls_paused"
    
    exit 1
fi

# 检查是否接近上限 (80%)
WARNING_THRESHOLD=$((DAILY_LIMIT * 80 / 100))
if [[ $CALL_COUNT -ge $WARNING_THRESHOLD ]]; then
    echo "⚠️  模型调用警告：$CALL_COUNT/$DAILY_LIMIT (80%)" >> "$MONITOR_LOG"
fi

# 正常情况
echo "✅ 模型调用正常：$CALL_COUNT/$DAILY_LIMIT"
exit 0
