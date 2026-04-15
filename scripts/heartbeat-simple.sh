#!/bin/bash
# V6.3 精简心跳脚本 - 核心功能 + Cron 监控

WORKSPACE="/home/node/.openclaw/workspace"
MEMORY_DIR="$WORKSPACE/memory"
LOG_FILE="$MEMORY_DIR/heartbeat.log"
TODAY=$(date '+%Y-%m-%d')
TODAY_FILE="$MEMORY_DIR/$TODAY.md"

# 简洁输出
echo "⚡ [$(date '+%H:%M')] 心跳"

# 1. Gateway 检查
if pgrep -f "openclaw" > /dev/null; then
    echo "✅ Gateway"
else
    echo "❌ Gateway 异常！" >> $LOG_FILE
fi

# 2. WebUI 检查
if curl -s --max-time 5 http://172.18.0.2:18789/ > /dev/null; then
    echo "✅ WebUI"
else
    echo "❌ WebUI 异常！" >> $LOG_FILE
fi

# 3. Cron 状态检查 (新增：检查最近一次运行是否失败)
CRON_OUTPUT=$(openclaw cron list 2>/dev/null)
CRON_ERRORS=$(echo "$CRON_OUTPUT" | grep -o '"consecutiveErrors": [0-9]*' | grep -v ': 0' | wc -l)
if [ "$CRON_ERRORS" -gt 0 ] 2>/dev/null; then
    echo "⚠️ Cron 有 $CRON_ERRORS 个任务连续失败" >> $LOG_FILE
    echo "⚠️ Cron 异常 ($CRON_ERRORS 任务失败)"
else
    echo "✅ Cron"
fi

# 4. 简单统计 (仅每日 00:00 记录)
if [ "$(date +%H:%M)" = "00:00" ]; then
    MEMORY_COUNT=$(ls -1 "$MEMORY_DIR"/*.md 2>/dev/null | wc -l)
    SKILL_COUNT=$(ls -1d "$WORKSPACE"/skills/*/ 2>/dev/null | wc -l)
    KB_COUNT=$(find "$WORKSPACE/knowledge_base" -name "*.md" 2>/dev/null | wc -l)
    echo "📊 $TODAY 记忆:$MEMORY_COUNT 技能:$SKILL_COUNT 知识库:$KB_COUNT" >> $LOG_FILE
fi

# 5. 确保今日记忆文件存在 (新增：避免 Cron 任务写入时报错)
if [ ! -f "$TODAY_FILE" ]; then
    cat > "$TODAY_FILE" << EOF
# $TODAY 每日记录

**日期**: $TODAY  
**开始时间**: $(date '+%H:%M UTC')  
**结束时间**: 待定  
**状态**: 🟢 运行中

---

## 📊 今日目标

### P0 - 收益破零
- [ ] Reddit/Moltbook 发帖引流
- [ ] 知识产品上架检查
- [ ] 第一笔收益追踪

### P1 - 知识质量
- [ ] 深度学习 (目标：+2 深度分析)
- [ ] Cron 知识获取 (目标：+3 文件/+1,500 点)

### P2 - 系统优化
- [ ] 脚本优化
- [ ] 记忆文件归档

---

## 🏖️ 执行记录

(待填充)

---

## 📈 状态基线 (今日开始)

| 指标 | 数值 |
|------|------|
| 知识库文件 | $(find "$WORKSPACE/knowledge_base" -name "*.md" 2>/dev/null | wc -l) 个 |
| 知识点总量 | 待统计 |
| Cron 轮数 | 待更新 |
| 收益状态 | \$0 (破零进行中) |

---

## 🧠 今日学习

(待填充)

---

## ⚠️ 问题与解决

(待填充)

---

*最后更新：$(date '+%Y-%m-%d %H:%M UTC')*
EOF
    echo "📝 创建今日记忆文件：$TODAY_FILE"
fi

echo "✅ 完成"
