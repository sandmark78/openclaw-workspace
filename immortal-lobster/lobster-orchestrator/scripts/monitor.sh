#!/bin/bash
# 监控脚本 - 记录性能指标
# 用法：./monitor.sh > logs/monitor.log

LOG_FILE="${1:-logs/monitor.log}"

mkdir -p logs

echo "🦞 Lobster Orchestrator 监控开始" | tee -a "$LOG_FILE"
echo "时间：$(date)" | tee -a "$LOG_FILE"
echo "================================" | tee -a "$LOG_FILE"

while true; do
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    
    # 内存使用
    if command -v ps &> /dev/null; then
        MEMORY=$(ps aux 2>/dev/null | grep -E "(orchestrator|picoclaw)" | awk '{sum+=$6} END {printf "%.2f", sum/1024}')
    else
        MEMORY="N/A"
    fi
    
    # CPU 使用
    if command -v top &> /dev/null; then
        CPU=$(top -bn1 2>/dev/null | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    else
        CPU="N/A"
    fi
    
    # 实例状态
    if command -v curl &> /dev/null; then
        RUNNING=$(curl -s http://localhost:8080/api/v1/instances 2>/dev/null | grep -c '"status": "running"' || echo 0)
        TOTAL=$(curl -s http://localhost:8080/api/v1/instances 2>/dev/null | grep -c '"id":' || echo 0)
    else
        RUNNING="N/A"
        TOTAL="N/A"
    fi
    
    # 输出
    echo "[$TIMESTAMP] 内存：${MEMORY}MB | CPU: ${CPU}% | 实例：$RUNNING/$TOTAL" | tee -a "$LOG_FILE"
    
    sleep 10
done
