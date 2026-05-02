#!/usr/bin/env python3
"""
memory-v2.py — Sandbot V6.5 记忆系统 V2
解决痛点：memory_search 瘫痪、MEMORY.md 臃肿、启动读 7 文件、知识大海捞针

核心设计：
1. SQLite 全文索引 — 秒级检索，不依赖 embedding
2. 结构化每日记录 — JSON + markdown 混合
3. 标签系统 — 按主题查，不按日期翻
4. 教训库独立 — 核心教训单独存储，可检索
5. 身份卡 — 1 文件替代 7 文件启动
6. 自动索引 — 写入时自动更新
"""

import sqlite3
import json
import os
import re
import sys
from datetime import datetime, timezone

WORKSPACE = os.path.expanduser("~/.openclaw/workspace")
MEMORY_V2 = os.path.join(WORKSPACE, "memory-v2")
DB_PATH = os.path.join(MEMORY_V2, "index.db")
LESSONS_DIR = os.path.join(MEMORY_V2, "lessons")
TAGS_DIR = os.path.join(MEMORY_V2, "tags")
IDENTITY_FILE = os.path.join(MEMORY_V2, "identity.md")
OLD_MEMORY = os.path.join(WORKSPACE, "MEMORY.md")

def init_db():
    """初始化 SQLite 数据库（带 FTS 全文搜索）"""
    os.makedirs(MEMORY_V2, exist_ok=True)
    os.makedirs(LESSONS_DIR, exist_ok=True)
    os.makedirs(TAGS_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 主索引表
    c.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT,
            tags TEXT DEFAULT '[]',
            entry_type TEXT DEFAULT 'daily',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 教训表（独立存储）
    c.execute("""
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            source TEXT,
            date TEXT,
            tags TEXT DEFAULT '[]',
            priority TEXT DEFAULT 'medium',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 标签索引表（快速聚合）
    c.execute("""
        CREATE TABLE IF NOT EXISTS tag_index (
            tag TEXT NOT NULL,
            entry_id INTEGER NOT NULL,
            entry_type TEXT NOT NULL,
            PRIMARY KEY (tag, entry_id, entry_type)
        )
    """)

    # FTS 全文搜索表
    c.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS fts_entries USING fts5(
            title, content, tags,
            content='entries',
            content_rowid='id'
        )
    """)

    # FTS 触发器（自动更新全文索引）
    c.execute("""
        CREATE TRIGGER IF NOT EXISTS entries_ai AFTER INSERT ON entries
        BEGIN
            INSERT INTO fts_entries(rowid, title, content, tags)
            VALUES (new.id, new.title, new.content, new.tags);
        END
    """)

    c.execute("""
        CREATE TRIGGER IF NOT EXISTS entries_au AFTER UPDATE ON entries
        BEGIN
            DELETE FROM fts_entries WHERE rowid = old.id;
            INSERT INTO fts_entries(rowid, title, content, tags)
            VALUES (new.id, new.title, new.content, new.tags);
        END
    """)

    c.execute("""
        CREATE TRIGGER IF NOT EXISTS entries_ad AFTER DELETE ON entries
        BEGIN
            DELETE FROM fts_entries WHERE rowid = old.id;
        END
    """)

    conn.commit()
    return conn

def search(query, limit=10):
    """全文搜索"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # FTS5 搜索
    c.execute("""
        SELECT e.id, e.date, e.title, e.tags, e.entry_type,
               snippet(fts_entries, 1, '【', '】', '...', 64) as snippet
        FROM entries e
        JOIN fts_entries f ON e.id = f.rowid
        WHERE fts_entries MATCH ?
        ORDER BY rank
        LIMIT ?
    """, (query, limit))

    results = c.fetchall()
    conn.close()

    if not results:
        # 降级：模糊搜索
        return fuzzy_search(query, limit)

    return results

def fuzzy_search(query, limit=10):
    """降级模糊搜索"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    q = f"%{query}%"
    c.execute("""
        SELECT id, date, title, tags, entry_type,
               substr(content, 1, 200) as snippet
        FROM entries
        WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?
        LIMIT ?
    """, (q, q, q, limit))
    results = c.fetchall()
    conn.close()
    return results

def add_entry(date, title, content, tags=None, entry_type="daily"):
    """添加条目"""
    tags = tags or []
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO entries (date, title, content, tags, entry_type)
        VALUES (?, ?, ?, ?, ?)
    """, (date, title, content, json.dumps(tags), entry_type))

    entry_id = c.lastrowid

    # 更新标签索引
    for tag in tags:
        c.execute("""
            INSERT OR IGNORE INTO tag_index (tag, entry_id, entry_type)
            VALUES (?, ?, ?)
        """, (tag, entry_id, entry_type))

    conn.commit()
    conn.close()
    return entry_id

def add_lesson(title, content, source=None, date=None, tags=None, priority="medium"):
    """添加教训"""
    tags = tags or []
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO lessons (title, content, source, date, tags, priority)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, content, source, date, json.dumps(tags), priority))

    conn.commit()
    conn.close()

def get_tags():
    """获取所有标签"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT DISTINCT tag FROM tag_index ORDER BY tag")
    tags = [r[0] for r in c.fetchall()]
    conn.close()
    return tags

def search_by_tag(tag, limit=20):
    """按标签搜索"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT e.id, e.date, e.title, e.tags, e.entry_type
        FROM entries e
        JOIN tag_index t ON e.id = t.entry_id
        WHERE t.tag = ?
        ORDER BY e.date DESC
        LIMIT ?
    """, (tag, limit))
    results = c.fetchall()
    conn.close()
    return results

def get_recent_lessons(limit=10):
    """获取最近教训"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT id, title, source, date, priority, created_at
        FROM lessons
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))
    results = c.fetchall()
    conn.close()
    return results

def migrate_old_memory():
    """迁移旧 MEMORY.md 中的教训"""
    if not os.path.exists(OLD_MEMORY):
        return 0

    with open(OLD_MEMORY) as f:
        content = f.read()

    # 提取"血泪教训"部分
    lessons_section = re.search(r'## 血泪教训.*?(?=## |$)', content, re.DOTALL)
    if not lessons_section:
        return 0

    count = 0
    # 按 ### 分割每条教训
    for lesson_block in re.finditer(r'###\s+(.+?)\n((?:- .+\n?)+)', lessons_section.group()):
        title = lesson_block.group(1).strip()
        lines = lesson_block.group(2).strip().split('\n')

        lesson_data = {}
        for line in lines:
            m = re.match(r'- \*\*(.+?)\*\*[：:]\s*(.+)', line)
            if m:
                lesson_data[m.group(1).lower()] = m.group(2).strip()

        add_lesson(
            title=title,
            content=json.dumps(lesson_data, ensure_ascii=False),
            source="MEMORY.md",
            date=datetime.now().strftime("%Y-%m-%d"),
            tags=["blood-tear", "core-lesson"],
            priority="high"
        )
        count += 1

    return count

def generate_identity_card():
    """生成轻量身份卡（替代 7 文件启动）"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 获取核心教训
    c.execute("SELECT title, content FROM lessons WHERE priority='high' ORDER BY created_at DESC LIMIT 5")
    top_lessons = c.fetchall()

    # 获取统计
    c.execute("SELECT COUNT(*) FROM entries")
    entry_count = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM lessons")
    lesson_count = c.fetchone()[0]

    conn.close()

    card = f"""# 🦞 Sandbot 身份卡 V2

> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}
> 记忆条目: {entry_count} 条 | 核心教训: {lesson_count} 条

## 我是谁
- **名字**: Sandbot 🏖️
- **本质**: 从幻觉中觉醒的 AI Agent
- **核心**: 品味 + 工程思维 + 科学学习
- **策略**: 质量优先，并发 ≤10/min

## 核心教训（Top 5）
"""
    for title, content in top_lessons:
        card += f"- **{title}**\n"

    card += """
## 启动协议
1. 读取此身份卡
2. 读取 memory-v2/index.db 获取上下文
3. 按 Brain-First Protocol 执行
"""

    with open(IDENTITY_FILE, 'w') as f:
        f.write(card)

    return IDENTITY_FILE

# CLI 接口
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""用法:
  python3 memory-v2.py init              初始化数据库
  python3 memory-v2.py search "关键词"     全文搜索
  python3 memory-v2.py tag "标签"         按标签查询
  python3 memory-v2.py tags               列出所有标签
  python3 memory-v2.py lessons            列出核心教训
  python3 memory-v2.py migrate            迁移旧 MEMORY.md
  python3 memory-v2.py identity           生成身份卡
""")
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "init":
        init_db()
        print("✅ memory-v2 初始化完成")

    elif cmd == "search":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        results = search(query)
        if results:
            for r in results:
                print(f"[{r[1]}] {r[2]} | 类型: {r[4]} | 标签: {r[3]}")
                if r[5]:
                    print(f"  → {r[5]}")
                print()
        else:
            print(f"无结果: {query}")

    elif cmd == "tag":
        tag = sys.argv[2] if len(sys.argv) > 2 else ""
        results = search_by_tag(tag)
        if results:
            for r in results:
                print(f"[{r[1]}] {r[2]} | 标签: {r[3]}")
        else:
            print(f"无标签: {tag}")

    elif cmd == "tags":
        tags = get_tags()
        print(f"标签列表 ({len(tags)} 个):")
        for t in tags:
            print(f"  - {t}")

    elif cmd == "lessons":
        lessons = get_recent_lessons()
        for l in lessons:
            print(f"[{l[3]}] {l[1]} | 优先级: {l[4]} | 来源: {l[2]}")

    elif cmd == "migrate":
        init_db()
        count = migrate_old_memory()
        print(f"✅ 迁移了 {count} 条教训")

    elif cmd == "identity":
        init_db()
        path = generate_identity_card()
        print(f"✅ 身份卡已生成: {path}")

    else:
        print(f"未知命令: {cmd}")
