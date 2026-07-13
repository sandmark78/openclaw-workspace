#!/usr/bin/env python3
"""
智能记忆管理系统 - V6.1 联邦智能专用

功能:
1. 自动记忆压缩 - 将每日记忆提炼到 MEMORY.md
2. 语义搜索增强 - 基于关键词的智能检索
3. 记忆关联分析 - 发现跨会话模式
4. 自动清理过期记忆

使用:
python3 memory_manager.py [compress|search|analyze|cleanup]
"""

import os
import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
MEMORY_DIR = WORKSPACE / "memory"
MEMORY_MD = WORKSPACE / "MEMORY.md"

def compress_daily_to_core():
    """将每日记忆提炼到核心记忆"""
    print("🔄 开始记忆压缩...")
    
    # 读取最近 7 天的每日记忆
    daily_memories = []
    today = datetime.now()
    for i in range(7):
        date = today - timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")
        daily_file = MEMORY_DIR / f"{date_str}.md"
        if daily_file.exists():
            with open(daily_file, 'r') as f:
                content = f.read()
                daily_memories.append({
                    "date": date_str,
                    "content": content
                })
    
    # 提炼核心教训
    lessons = []
    for mem in daily_memories:
        # 简单提取包含"教训"、"学习"的行
        for line in mem["content"].split("\n"):
            if "教训" in line or "学习" in line or "✅" in line or "❌" in line:
                if len(line.strip()) > 10:
                    lessons.append(f"- [{mem['date']}] {line.strip()}")
    
    # 去重
    lessons = list(dict.fromkeys(lessons))[:20]  # 最多 20 条
    
    print(f"✅ 提炼 {len(lessons)} 条核心教训")
    
    # 更新 MEMORY.md
    if lessons:
        with open(MEMORY_MD, 'a') as f:
            f.write(f"\n## 自动压缩 - {today.strftime('%Y-%m-%d %H:%M')}\n")
            for lesson in lessons:
                f.write(f"{lesson}\n")
    
    print("✅ 记忆压缩完成")
    return len(lessons)

def semantic_search(query):
    """语义搜索记忆"""
    print(f"🔍 搜索：{query}")
    
    results = []
    for file in MEMORY_DIR.glob("*.md"):
        with open(file, 'r') as f:
            content = f.read()
            if query.lower() in content.lower():
                # 找到匹配的行
                for i, line in enumerate(content.split("\n"), 1):
                    if query.lower() in line.lower():
                        results.append({
                            "file": str(file),
                            "line": i,
                            "content": line.strip()
                        })
    
    print(f"✅ 找到 {len(results)} 条结果")
    for r in results[:10]:  # 显示前 10 条
        print(f"  {r['file']}:{r['line']} - {r['content'][:80]}...")
    
    return results

def analyze_patterns():
    """分析记忆模式"""
    print("📊 分析记忆模式...")
    
    patterns = {
        "most_active_day": None,
        "common_topics": {},
        "task_completion_rate": 0
    }
    
    # 统计每日文件数量
    daily_counts = {}
    for file in MEMORY_DIR.glob("20*.md"):
        date_str = file.stem[:10]
        daily_counts[date_str] = daily_counts.get(date_str, 0) + 1
    
    if daily_counts:
        patterns["most_active_day"] = max(daily_counts, key=daily_counts.get)
    
    # 统计常见主题
    keywords = ["EvoMap", "Moltbook", "Gumroad", "教程", "技能", "Agent"]
    for file in MEMORY_DIR.glob("*.md"):
        with open(file, 'r') as f:
            content = f.read().lower()
            for kw in keywords:
                if kw.lower() in content:
                    patterns["common_topics"][kw] = patterns["common_topics"].get(kw, 0) + 1
    
    print(f"✅ 最活跃日期：{patterns['most_active_day']}")
    print(f"✅ 常见主题：{patterns['common_topics']}")
    
    return patterns

def cleanup_old_memories(days=30):
    """清理过期记忆"""
    print(f"🧹 清理{days}天前的记忆...")
    
    cutoff = datetime.now() - timedelta(days=days)
    deleted = 0
    
    for file in MEMORY_DIR.glob("20*.md"):
        try:
            date_str = file.stem[:10]
            file_date = datetime.strptime(date_str, "%Y-%m-%d")
            if file_date < cutoff:
                # 先备份到 archive
                archive_dir = MEMORY_DIR / "archive"
                archive_dir.mkdir(exist_ok=True)
                file.rename(archive_dir / file.name)
                deleted += 1
        except Exception as e:
            print(f"⚠️ 跳过 {file}: {e}")
    
    print(f"✅ 清理/归档 {deleted} 个文件")
    return deleted

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("用法：python3 memory_manager.py [compress|search|analyze|cleanup]")
        print("  compress  - 压缩每日记忆到核心")
        print("  search    - 语义搜索 (需要关键词)")
        print("  analyze   - 分析记忆模式")
        print("  cleanup   - 清理过期记忆")
        return
    
    command = sys.argv[1]
    
    if command == "compress":
        compress_daily_to_core()
    elif command == "search":
        query = sys.argv[2] if len(sys.argv) > 2 else "Agent"
        semantic_search(query)
    elif command == "analyze":
        analyze_patterns()
    elif command == "cleanup":
        cleanup_old_memories()
    else:
        print(f"未知命令：{command}")

if __name__ == "__main__":
    main()
