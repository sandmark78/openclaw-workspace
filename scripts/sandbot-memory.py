#!/usr/bin/env python3
"""
sandbot-memory.py - Sandbot 本地记忆引擎 (ASMR 启发)
基于 Supermemory ASMR 原理，纯本地实现，零外部依赖

原理:
- 不用向量数据库，不用 embeddings
- 多角度 grep 搜索替代语义检索
- 记忆分 6 类存储 (ASMR 的 Observer Agent 思路)
- 并行多策略搜索 (ASMR 的 Search Agent 思路)

用法:
  python3 sandbot-memory.py add "今天学了 ASMR 记忆技术"
  python3 sandbot-memory.py recall "记忆系统"
  python3 sandbot-memory.py profile
"""

import sys
import os
import json
import re
import glob
from datetime import datetime, timedelta
from collections import defaultdict

MEMORY_DIR = os.path.expanduser("~/.openclaw/workspace/memory")
KB_DIR = os.path.expanduser("~/.openclaw/workspace/knowledge_base")
MEMORY_DB = os.path.join(MEMORY_DIR, "sandbot-memory-db.json")

# 6 类记忆 (ASMR Observer Agent 的分类)
CATEGORIES = {
    "identity": "身份信息 (名字/角色/配置)",
    "preferences": "偏好 (工作方式/沟通风格/决策原则)",
    "events": "事件 (完成的任务/发生的事)",
    "temporal": "时间数据 (截止日期/频率/计划)",
    "updates": "更新 (修复/变更/新增功能)",
    "lessons": "教训 (错误/反省/铁律)"
}

def load_db():
    if os.path.exists(MEMORY_DB):
        with open(MEMORY_DB, 'r') as f:
            return json.load(f)
    return {"memories": [], "profile": {"static": [], "dynamic": []}}

def save_db(db):
    with open(MEMORY_DB, 'w') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def classify(text):
    """自动分类记忆 (简单关键词匹配，未来可用 LLM)"""
    text_lower = text.lower()
    if any(w in text_lower for w in ["名字", "sandbot", "身份", "角色", "agent id", "配置"]):
        return "identity"
    if any(w in text_lower for w in ["喜欢", "偏好", "风格", "原则", "方式", "习惯"]):
        return "preferences"
    if any(w in text_lower for w in ["完成", "发布", "创建", "修复", "执行", "发帖"]):
        return "events"
    if any(w in text_lower for w in ["每天", "每周", "截止", "计划", "cron", "频率"]):
        return "temporal"
    if any(w in text_lower for w in ["更新", "修改", "新增", "变更", "升级", "修复"]):
        return "updates"
    if any(w in text_lower for w in ["教训", "错误", "反省", "铁律", "不要", "禁止"]):
        return "lessons"
    return "events"  # 默认归类为事件

def add_memory(text, category=None):
    """添加一条记忆"""
    db = load_db()
    if not category:
        category = classify(text)
    
    memory = {
        "text": text,
        "category": category,
        "timestamp": datetime.utcnow().isoformat(),
        "source": "manual"
    }
    db["memories"].append(memory)
    save_db(db)
    print(f"✅ 记忆已存储 [{category}]: {text[:50]}...")

def multi_angle_search(query, memories):
    """多角度搜索 (ASMR Search Agent 思路)
    
    3 个搜索策略并行:
    1. 直接匹配: 关键词完全匹配
    2. 模糊匹配: 分词后部分匹配
    3. 类别匹配: 根据查询推断类别
    """
    results = defaultdict(float)
    
    # 策略 1: 直接匹配 (权重最高)
    for i, m in enumerate(memories):
        if query.lower() in m["text"].lower():
            results[i] += 3.0
    
    # 策略 2: 分词匹配
    words = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+', query.lower())
    for i, m in enumerate(memories):
        text_lower = m["text"].lower()
        matches = sum(1 for w in words if w in text_lower)
        if matches > 0:
            results[i] += matches * 1.0
    
    # 策略 3: 类别匹配
    query_cat = classify(query)
    for i, m in enumerate(memories):
        if m.get("category") == query_cat:
            results[i] += 0.5
    
    # 策略 4: 时间衰减 (最近的记忆更重要)
    now = datetime.utcnow()
    for i, m in enumerate(memories):
        try:
            ts = datetime.fromisoformat(m["timestamp"])
            days_ago = (now - ts).days
            if days_ago < 1:
                results[i] += 1.0
            elif days_ago < 7:
                results[i] += 0.5
        except:
            pass
    
    # 排序返回
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return [(memories[i], score) for i, score in sorted_results[:10]]

def recall(query):
    """召回相关记忆"""
    db = load_db()
    
    # 从 DB 搜索
    db_results = multi_angle_search(query, db["memories"])
    
    # 从文件系统搜索 (grep 方式)
    file_results = grep_memory_files(query)
    
    print(f"\n🔍 召回结果 (查询: {query})")
    print("=" * 50)
    
    if db_results:
        print("\n📦 数据库记忆:")
        for m, score in db_results[:5]:
            print(f"  [{m['category']}] (分数:{score:.1f}) {m['text'][:80]}")
    
    if file_results:
        print(f"\n📁 文件记忆 ({len(file_results)} 条):")
        for path, line in file_results[:5]:
            short_path = os.path.basename(path)
            print(f"  [{short_path}] {line[:80]}")
    
    if not db_results and not file_results:
        print("  (无匹配记忆)")

def grep_memory_files(query):
    """从 memory/ 和 MEMORY.md 中 grep 搜索"""
    results = []
    words = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+', query.lower())
    
    # 搜索 MEMORY.md
    memory_md = os.path.expanduser("~/.openclaw/workspace/MEMORY.md")
    if os.path.exists(memory_md):
        with open(memory_md, 'r') as f:
            for line in f:
                if any(w in line.lower() for w in words):
                    results.append((memory_md, line.strip()))
    
    # 搜索最近 7 天的 memory 文件
    now = datetime.utcnow()
    for i in range(7):
        date = (now - timedelta(days=i)).strftime("%Y-%m-%d")
        path = os.path.join(MEMORY_DIR, f"{date}.md")
        if os.path.exists(path):
            with open(path, 'r') as f:
                for line in f:
                    if any(w in line.lower() for w in words):
                        results.append((path, line.strip()))
    
    return results

def profile():
    """生成用户画像 (Supermemory profile 概念)"""
    db = load_db()
    
    print("\n👤 Sandbot 记忆画像")
    print("=" * 50)
    
    # 按类别统计
    cat_counts = defaultdict(int)
    for m in db["memories"]:
        cat_counts[m.get("category", "unknown")] += 1
    
    print("\n📊 记忆分布:")
    for cat, desc in CATEGORIES.items():
        count = cat_counts.get(cat, 0)
        bar = "█" * min(count, 20)
        print(f"  {cat:12s} ({count:3d}) {bar} {desc}")
    
    # 最近记忆
    recent = sorted(db["memories"], key=lambda x: x.get("timestamp", ""), reverse=True)[:5]
    if recent:
        print("\n🕐 最近记忆:")
        for m in recent:
            print(f"  [{m['category']}] {m['text'][:60]}")
    
    print(f"\n📈 总记忆数: {len(db['memories'])}")

def auto_extract(conversation_text):
    """从对话中自动提取记忆 (ASMR Observer Agent 思路)"""
    db = load_db()
    
    # 简单提取: 包含关键模式的句子
    patterns = [
        (r"教训[：:](.+)", "lessons"),
        (r"完成[了：:](.+)", "events"),
        (r"修复[了：:](.+)", "updates"),
        (r"配置[：:](.+)", "identity"),
        (r"每[天日周](.+)", "temporal"),
        (r"铁律[：:](.+)", "lessons"),
    ]
    
    extracted = 0
    for pattern, category in patterns:
        matches = re.findall(pattern, conversation_text)
        for match in matches:
            text = match.strip()
            if len(text) > 10:  # 过滤太短的
                memory = {
                    "text": text,
                    "category": category,
                    "timestamp": datetime.utcnow().isoformat(),
                    "source": "auto_extract"
                }
                db["memories"].append(memory)
                extracted += 1
    
    if extracted > 0:
        save_db(db)
        print(f"✅ 自动提取 {extracted} 条记忆")
    else:
        print("📝 无可提取的记忆")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:")
        print("  python3 sandbot-memory.py add <text>     # 添加记忆")
        print("  python3 sandbot-memory.py recall <query>  # 召回记忆")
        print("  python3 sandbot-memory.py profile         # 查看画像")
        print("  python3 sandbot-memory.py extract <text>   # 自动提取")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "add" and len(sys.argv) > 2:
        add_memory(" ".join(sys.argv[2:]))
    elif cmd == "recall" and len(sys.argv) > 2:
        recall(" ".join(sys.argv[2:]))
    elif cmd == "profile":
        profile()
    elif cmd == "extract" and len(sys.argv) > 2:
        auto_extract(" ".join(sys.argv[2:]))
    else:
        print("未知命令")
        sys.exit(1)
