#!/usr/bin/env python3
"""
brain-night-sync.py — GBrain 启发的夜间知识整理

每晚执行，做四件事:
1. 补全 — 检查最近记忆文件，补全缺失的关键信息
2. 去重 — 检测重复记录，合并相似内容
3. 索引 — 更新主题索引文件 (memory/topics-index.md)
4. 提炼 — 从最近 7 天记忆中提炼核心教训，建议更新 MEMORY.md

纯本地，零模型调用。
"""

import os
import re
import json
from datetime import datetime, timedelta
from collections import Counter

WORKSPACE = os.path.expanduser("~/.openclaw/workspace")
MEMORY_DIR = os.path.join(WORKSPACE, "memory")
MEMORY_MD = os.path.join(WORKSPACE, "MEMORY.md")
INDEX_FILE = os.path.join(MEMORY_DIR, "topics-index.md")

def scan_files(days=14):
    """扫描最近 N 天的记忆文件"""
    today = datetime.utcnow().date()
    files = {}
    for d in range(days):
        date = today - timedelta(days=d)
        fp = os.path.join(MEMORY_DIR, f"{date.strftime('%Y-%m-%d')}.md")
        if os.path.exists(fp):
            with open(fp) as f:
                files[date] = f.read()
    return files

def extract_topics(content):
    """从内容中提取主题关键词"""
    topics = []
    # 提取 markdown 标题
    for m in re.finditer(r'^#{1,3}\s+(.+)', content, re.MULTILINE):
        title = m.group(1).strip()
        if len(title) > 3 and len(title) < 80:
            topics.append(title)
    return topics

def extract_lessons(content):
    """提取教训/教训类内容"""
    lessons = []
    patterns = [
        r'教训[：:]\s*(.+)',
        r'核心教训[：:]\s*(.+)',
        r'❌\s*(.+)',
        r'问题[：:]\s*(.+)',
        r'修复[：:]\s*(.+)',
    ]
    for p in patterns:
        for m in re.finditer(p, content):
            text = m.group(1).strip()[:200]
            if len(text) > 5:
                lessons.append(text)
    return lessons

def build_index(files):
    """构建主题索引"""
    index = []
    index.append(f"# 📚 主题索引\n")
    index.append(f"**生成时间**: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n")
    
    topic_files = {}
    for date, content in sorted(files.items(), reverse=True):
        topics = extract_topics(content)
        for t in topics:
            topic_files.setdefault(t, []).append(date)
    
    # 按文件数排序
    for topic, dates in sorted(topic_files.items(), key=lambda x: -len(x[1])):
        if len(dates) >= 1:
            index.append(f"\n### {topic}")
            for d in dates[:5]:
                index.append(f"- [{d}]({d}.md)")
    
    return "\n".join(index)

def suggest_memory_updates(files):
    """从最近7天提炼教训，对比 MEMORY.md"""
    recent = {k: v for k, v in files.items() 
              if k >= (datetime.utcnow().date() - timedelta(days=7))}
    
    all_lessons = []
    for date, content in recent.items():
        lessons = extract_lessons(content)
        all_lessons.extend([(date, l) for l in lessons])
    
    # 读 MEMORY.md，看哪些已经收录
    if os.path.exists(MEMORY_MD):
        with open(MEMORY_MD) as f:
            memory_content = f.read()
    else:
        memory_content = ""
    
    new_lessons = []
    for date, lesson in all_lessons:
        # 简单去重：检查教训是否在 MEMORY.md 中出现
        key = lesson[:30]  # 取前30字符做匹配
        if key not in memory_content:
            new_lessons.append((date, lesson))
    
    return new_lessons[:10]  # 最多10条

def detect_duplicates(files):
    """检测重复/相似记录"""
    dups = []
    contents = [(d, c[:500]) for d, c in files.items()]  # 只取前500字符
    
    for i in range(len(contents)):
        for j in range(i+1, len(contents)):
            d1, c1 = contents[i]
            d2, c2 = contents[j]
            # 简单 Jaccard 相似度
            words1 = set(c1.split())
            words2 = set(c2.split())
            if len(words1) > 20 and len(words2) > 20:
                overlap = len(words1 & words2) / len(words1 | words2)
                if overlap > 0.6:  # 60%以上重叠
                    dups.append((d1, d2, f"{overlap:.0%}"))
    
    return dups[:5]  # 最多5对

def main():
    print(f"🧠 夜间知识整理 ({datetime.utcnow().strftime('%Y-%m-%d %H:%M')})")
    
    files = scan_files(14)
    print(f"  扫描 {len(files)} 个记忆文件")
    
    # 1. 构建索引
    index_content = build_index(files)
    with open(INDEX_FILE, 'w') as f:
        f.write(index_content)
    print(f"  ✅ 主题索引: {INDEX_FILE}")
    
    # 2. 建议 MEMORY.md 更新
    new_lessons = suggest_memory_updates(files)
    if new_lessons:
        print(f"  🔔 建议更新 MEMORY.md ({len(new_lessons)} 条新教训):")
        for date, lesson in new_lessons:
            print(f"    [{date}] {lesson[:80]}...")
    else:
        print(f"  ✅ MEMORY.md 已是最新")
    
    # 3. 检测重复
    dups = detect_duplicates(files)
    if dups:
        print(f"  ⚠️ 发现 {len(dups)} 对重复/相似记录:")
        for d1, d2, sim in dups:
            print(f"    {d1} ↔ {d2} ({sim} 重叠)")
    
    # 4. 统计
    total_files = len(files)
    total_bytes = sum(len(c) for c in files.values())
    all_topics = []
    for c in files.values():
        all_topics.extend(extract_topics(c))
    unique_topics = len(set(all_topics))
    
    print(f"\n  📊 统计: {total_files} 文件 / {total_bytes:,} bytes / {unique_topics} 主题")
    print("  ✅ 夜间整理完成")

if __name__ == "__main__":
    main()
