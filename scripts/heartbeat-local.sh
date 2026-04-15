#!/bin/bash
# 本地心跳脚本 - 不调用模型
# 用法：每 30 分钟执行一次

WORKSPACE="/home/node/.openclaw/workspace"
MEMORY_DIR="$WORKSPACE/memory"
LOG_FILE="$MEMORY_DIR/heartbeat.log"
TODAY=$(date '+%Y-%m-%d')
TODAY_FILE="$MEMORY_DIR/$TODAY.md"

# 简洁输出
echo "⚡ [$(date '+%H:%M')] 心跳检查"

# 1. Gateway 检查
if pgrep -f "openclaw" > /dev/null; then
    echo "✅ Gateway"
else
    echo "❌ Gateway 异常！" >> "$LOG_FILE"
    # 发送通知 (需要调用模型)
    echo "GATEWAY_DOWN"
    exit 1
fi

# 2. WebUI 检查
HTTP_CODE=$(curl -s --max-time 5 -o /dev/null -w "%{http_code}" http://172.18.0.2:18789/)
if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ WebUI (HTTP $HTTP_CODE)"
else
    echo "❌ WebUI 异常 (HTTP $HTTP_CODE)！" >> "$LOG_FILE"
    # 发送通知 (需要调用模型)
    echo "WEBUI_DOWN"
    exit 1
fi

# 3. 磁盘检查
DISK_USAGE=$(df -h / | tail -1 | awk '{print $5}' | tr -d '%')
if [ "$DISK_USAGE" -lt 80 ]; then
    echo "✅ 磁盘：${DISK_USAGE}%"
else
    echo "⚠️ 磁盘告警：${DISK_USAGE}%" >> "$LOG_FILE"
    # 发送通知 (需要调用模型)
    echo "DISK_WARNING"
fi

# 4. 进程数检查
PROCESS_COUNT=$(ps aux | grep -c "openclaw" || echo "0")
if [ "$PROCESS_COUNT" -gt 0 ]; then
    echo "✅ 进程：$PROCESS_COUNT"
else
    echo "❌ 进程异常！" >> "$LOG_FILE"
    echo "PROCESS_ERROR"
    exit 1
fi

# 5. 确保今日记忆文件存在 (避免 Cron 任务写入时报错)
if [ ! -f "$TODAY_FILE" ]; then
    cat > "$TODAY_FILE" << EOF
# $TODAY 每日记录

**日期**: $TODAY  
**开始时间**: $(date '+%H:%M UTC')  
**状态**: 🟢 运行中

---

## 📊 状态基线

| 指标 | 数值 |
|------|------|
| Gateway | ✅ 运行中 |
| WebUI | ✅ 可访问 |
| 磁盘 | ${DISK_USAGE}% |

---

*最后更新：$(date '+%Y-%m-%d %H:%M UTC')*
EOF
    echo "📝 创建今日记忆文件"
fi

# 6. 无异常时仅回复 HEARTBEAT_OK
echo "✅ 完成"
echo "HEARTBEAT_OK"
