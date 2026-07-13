#!/usr/bin/env python3
"""
memory-sync.py — 自动同步每日日志到 memory-v2 数据库
用法: python3 memory-sync.py [--auto]
-auto 模式：只同步新增的文件，适合 Cron 定时执行
"""
import sqlite3, json, os, re, sys, glob
from datetime import datetime, timezone

WORKSPACE = os.path.expanduser("~/.openclaw/workspace")
DB_PATH = os.path.join(WORKSPACE, "memory-v2", "index.db")
MEMORY_DIR = os.path.join(WORKSPACE, "memory")
LESSONS_DIR = os.path.join(WORKSPACE, "memory-v2", "lessons")

def init_db():
    """初始化数据库（使用 FTS5 + simple tokenizer 支持中文）"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    os.makedirs(LESSONS_DIR, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # 主表
    c.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT,
            tags TEXT DEFAULT '[]',
            entry_type TEXT DEFAULT 'daily',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(date, title)
        )
    """)
    
    # 教训表
    c.execute("""
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            source TEXT,
            date TEXT,
            tags TEXT DEFAULT '[]',
            priority TEXT DEFAULT 'medium',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(title)
        )
    """)
    
    # 标签索引
    c.execute("""
        CREATE TABLE IF NOT EXISTS tag_index (
            tag TEXT NOT NULL,
            entry_id INTEGER NOT NULL,
            entry_type TEXT NOT NULL,
            PRIMARY KEY (tag, entry_id, entry_type)
        )
    """)
    
    # FTS5 表（使用 unicode61 tokenizer，支持中文分词）
    c.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS fts_entries USING fts5(
            title, content, tags,
            content='entries',
            content_rowid='id',
            tokenize='unicode61'
        )
    """)
    
    # 触发器
    for trigger in [
        "CREATE TRIGGER IF NOT EXISTS fts_ins AFTER INSERT ON entries BEGIN INSERT INTO fts_entries(rowid, title, content, tags) VALUES(new.id, new.title, new.content, new.tags); END",
        "CREATE TRIGGER IF NOT EXISTS fts_upd AFTER UPDATE ON entries BEGIN DELETE FROM fts_entries WHERE rowid=old.id; INSERT INTO fts_entries(rowid, title, content, tags) VALUES(new.id, new.title, new.content, new.tags); END",
        "CREATE TRIGGER IF NOT EXISTS fts_del AFTER DELETE ON entries BEGIN DELETE FROM fts_entries WHERE rowid=old.id; END"
    ]:
        c.execute(trigger)
    
    conn.commit()
    return conn

def extract_tags(section_text):
    """从内容中提取标签"""
    tags = ["daily"]
    if any(k in section_text for k in ["博客", "blog", "文章"]):
        tags.append("blog")
    if "复盘" in section_text:
        tags.append("review")
    if any(k in section_text for k in ["热点", "HN", "AIHOT"]):
        tags.append("hn")
    if any(k in section_text for k in ["成本", "调用", "token"]):
        tags.append("cost")
    if "Agent" in section_text or "agent" in section_text.lower():
        tags.append("agent")
    if any(k in section_text for k in ["安全", "security", "漏洞"]):
        tags.append("security")
    if any(k in section_text for k in ["自我进化", "自我修正", "成长"]):
        tags.append("evolution")
    return tags

def sync_daily_file(filepath, conn):
    """同步单个每日日志文件"""
    date = os.path.basename(filepath).replace('.md', '')
    c = conn.cursor()
    
    with open(filepath) as f:
        content = f.read()
    
    # 按标题分割章节
    sections = re.split(r'#+\s+', content)
    synced = 0
    
    for section in sections:
        if not section.strip():
            continue
        
        lines = section.strip().split('\n')
        title = lines[0][:200] if lines else date
        body = '\n'.join(lines[1:])[:3000] if len(lines) > 1 else ''
        
        if not body or len(body) < 20:
            continue
        
        tags = extract_tags(section)
        entry_type = "analysis" if any(t != "daily" for t in tags) else "daily"
        
        try:
            c.execute("""
                INSERT OR IGNORE INTO entries (date, title, content, tags, entry_type)
                VALUES (?, ?, ?, ?, ?)
            """, (date, f"[{date}] {title}", body, json.dumps(tags, ensure_ascii=False), entry_type))
            
            if c.rowcount > 0:
                entry_id = c.lastrowid
                for tag in tags:
                    c.execute("INSERT OR IGNORE INTO tag_index (tag, entry_id, entry_type) VALUES (?, ?, ?)",
                             (tag, entry_id, entry_type))
                synced += 1
        except sqlite3.IntegrityError:
            pass
    
    conn.commit()
    return synced

def sync_all(auto_mode=False):
    """同步所有或新增的每日日志"""
    conn = init_db()
    
    files = sorted(glob.glob(os.path.join(MEMORY_DIR, "2026-*.md")))
    total_synced = 0
    
    for fp in files:
        date = os.path.basename(fp).replace('.md', '')
        
        # 检查是否已同步
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM entries WHERE date=?", (date,))
        if c.fetchone()[0] > 0 and auto_mode:
            continue
        
        synced = sync_daily_file(fp, conn)
        total_synced += synced
        if synced > 0:
            print(f"  ✅ {date}: +{synced} entries")
    
    # 统计
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM entries")
    total_entries = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM lessons")
    total_lessons = c.fetchone()[0]
    
    print(f"\n📊 总计: {total_entries} entries, {total_lessons} lessons")
    
    # 更新 identity.md
    update_identity(total_entries, total_lessons)
    
    conn.close()
    return total_synced

def update_identity(entries, lessons):
    """更新身份卡"""
    identity = f"""# 🦞 Sandbot 身份卡 V2
> 生成时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}
> 记忆条目: {entries} | 核心教训: {lessons} 条
> 用法: `python3 scripts/memory-v2.py search "关键词"` 或 `./scripts/memory-search.sh "关键词"`

## 我是谁
- **名字**: Sandbot 🏖️
- **核心**: 品味 + 工程思维 + 科学学习
- **策略**: 质量优先，自我进化

## 核心教训
"""
    # 从数据库读取教训
    conn = sqlite3.connect(os.path.join(WORKSPACE, "memory-v2", "index.db"))
    c = conn.cursor()
    c.execute("SELECT title FROM lessons ORDER BY created_at DESC LIMIT 6")
    for i, (title,) in enumerate(c.fetchall(), 1):
        identity += f"{i}. {title}\n"
    conn.close()
    
    identity += """
## 启动协议
1. 读此身份卡
2. `./scripts/memory-search.sh "关键词"` 快速检索
3. Brain-First Protocol — 读-答-写闭环
"""
    
    with open(os.path.join(WORKSPACE, "memory-v2", "identity.md"), 'w') as f:
        f.write(identity)
    print("✅ identity.md 已更新")

if __name__ == "__main__":
    auto_mode = "--auto" in sys.argv
    print(f"🔄 同步记忆系统 ({'auto' if auto_mode else 'full'} mode)...")
    sync_all(auto_mode)
