#!/bin/bash
# memory-bridge.sh - 官方记忆系统 ↔ sandbot-memory 桥接
# 
# 功能:
# 1. 从官方 memory/*.md 和 MEMORY.md 同步到 sandbot-memory DB
# 2. 确保会话重置后，DB 中的记忆仍然可用
# 3. 定期运行，保持两个系统同步
#
# 官方系统: MEMORY.md + memory/YYYY-MM-DD.md (OpenClaw 原生)
# 自研系统: sandbot-memory-db.json (ASMR 启发)

WORKSPACE="/home/node/.openclaw/workspace"
MEMORY_PY="$WORKSPACE/scripts/sandbot-memory.py"
MEMORY_MD="$WORKSPACE/MEMORY.md"
MEMORY_DIR="$WORKSPACE/memory"
DB="$MEMORY_DIR/sandbot-memory-db.json"

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) 开始记忆同步..."

# 1. 从 MEMORY.md 提取关键记忆
if [ -f "$MEMORY_MD" ]; then
  # 提取教训
  grep -E "^- \*\*教训\*\*:|^- \*\*问题\*\*:|^- \*\*修复\*\*:" "$MEMORY_MD" | while read -r line; do
    python3 "$MEMORY_PY" add "$line" 2>/dev/null
  done

  # 提取铁律
  grep -E "^[0-9]+\." "$MEMORY_MD" | head -20 | while read -r line; do
    python3 "$MEMORY_PY" add "$line" 2>/dev/null
  done

  # 提取配置信息
  grep -E "^- .+: .+✅|^- Agent ID:|^- 钱包:|^- Cron:" "$MEMORY_MD" | while read -r line; do
    python3 "$MEMORY_PY" add "$line" 2>/dev/null
  done
fi

# 2. 从最近 3 天的 memory 文件提取
NOW=$(date -u +%Y-%m-%d)
for i in 0 1 2; do
  DATE=$(date -u -d "$NOW - $i days" +%Y-%m-%d 2>/dev/null || date -u -v-${i}d +%Y-%m-%d 2>/dev/null)
  FILE="$MEMORY_DIR/${DATE}.md"
  if [ -f "$FILE" ]; then
    # 提取完成的任务
    grep -E "^- ✅|完成了|修复了|发布了" "$FILE" | while read -r line; do
      python3 "$MEMORY_PY" add "$line" 2>/dev/null
    done
  fi
done

# 3. 统计
TOTAL=$(python3 -c "
import json, os
db_path = '$DB'
if os.path.exists(db_path):
    with open(db_path) as f:
        d = json.load(f)
    print(len(d.get('memories', [])))
else:
    print(0)
" 2>/dev/null)

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) 同步完成，DB 总记忆数: $TOTAL"

# === Autolearn 集成 (Hermes 启发) ===
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) 开始自动学习..."
python3 "$WORKSPACE/scripts/sandbot-autolearn.py" all 2>/dev/null
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) 自动学习完成"
