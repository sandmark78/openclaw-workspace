#!/bin/bash
# 快速记忆搜索 - 给 Agent 用的接口
# 用法: ./memory-search.sh "关键词" [limit]

WORKSPACE="$HOME/.openclaw/workspace"
QUERY="$1"
LIMIT="${2:-10}"

if [ -z "$QUERY" ]; then
    echo "用法: memory-search.sh '关键词' [limit]"
    exit 1
fi

python3 -c "
import sqlite3, json, sys

DB = '$WORKSPACE/memory-v2/index.db'
QUERY = sys.argv[1]
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else 10

conn = sqlite3.connect(DB)
c = conn.cursor()
c.execute('''
    SELECT date, substr(title, 1, 80), substr(content, 1, 150), tags 
    FROM entries 
    WHERE content LIKE ? OR title LIKE ? OR tags LIKE ?
    ORDER BY date DESC
    LIMIT ?
''', (f'%{QUERY}%', f'%{QUERY}%', f'%{QUERY}%', LIMIT))

for row in c.fetchall():
    tags = json.loads(row[3])[:3]
    print(f'[{row[0]}] {row[1]}')
    print(f'  预览: {row[2][:100]}...')
    print(f'  标签: {tags}')
    print()

conn.close()
" "$QUERY" "$LIMIT"
