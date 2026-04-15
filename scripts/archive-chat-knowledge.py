#!/usr/bin/env python3
"""
群聊知识归档工具
功能：将群聊中的知识和经验自动归档到本地文件

用法:
    python3 archive-chat-knowledge.py <knowledge_text> [category]
    或通过 OpenClaw exec 调用
"""

import os
import sys
from datetime import datetime

# 归档路径
ARCHIVE_DIR = "/home/node/.openclaw/workspace/memory/chat-archive"
DAILY_FILE = None

def get_daily_file():
    """获取今日归档文件路径"""
    global DAILY_FILE
    if DAILY_FILE is None:
        today = datetime.utcnow().strftime("%Y-%m-%d")
        DAILY_FILE = os.path.join(ARCHIVE_DIR, f"{today}.md")
    return DAILY_FILE

def ensure_archive_dir():
    """确保归档目录存在"""
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

def archive_knowledge(knowledge_text, category="general", source="telegram"):
    """
    归档知识到本地文件
    
    Args:
        knowledge_text: 知识内容
        category: 分类 (general/technical/strategy/lesson)
        source: 来源 (telegram/webui/etc)
    """
    ensure_archive_dir()
    
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    daily_file = get_daily_file()
    
    # 如果文件不存在，创建并写入头部
    if not os.path.exists(daily_file):
        today = datetime.utcnow().strftime("%Y-%m-%d")
        with open(daily_file, 'w', encoding='utf-8') as f:
            f.write(f"# 群聊知识归档 - {today}\n\n")
            f.write(f"**创建时间**: {timestamp}\n")
            f.write(f"**来源**: {source}\n")
            f.write("**状态**: 🟢 归档中\n\n")
            f.write("---\n\n")
    
    # 追加知识条目
    with open(daily_file, 'a', encoding='utf-8') as f:
        f.write(f"## [{category.upper()}] {timestamp}\n\n")
        f.write(f"**来源**: {source}\n\n")
        f.write(f"{knowledge_text}\n\n")
        f.write("---\n\n")
    
    return {
        "status": "success",
        "file": daily_file,
        "timestamp": timestamp,
        "category": category
    }

def archive_lesson(lesson_text, lesson_type="chat_lesson"):
    """
    归档经验教训
    
    Args:
        lesson_text: 教训内容
        lesson_type: 类型 (chat_lesson/task_lesson/system_lesson)
    """
    ensure_archive_dir()
    
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    daily_file = get_daily_file()
    
    with open(daily_file, 'a', encoding='utf-8') as f:
        f.write(f"## ⚠️ 经验教训 [{lesson_type}] {timestamp}\n\n")
        f.write(f"{lesson_text}\n\n")
        f.write("---\n\n")
    
    return {
        "status": "success",
        "file": daily_file,
        "timestamp": timestamp,
        "type": lesson_type
    }

def summarize_and_archive(chat_messages, summary_text):
    """
    总结对话并归档
    
    Args:
        chat_messages: 对话消息列表
        summary_text: 总结文本
    """
    ensure_archive_dir()
    
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    summary_file = os.path.join(ARCHIVE_DIR, f"{datetime.utcnow().strftime('%Y-%m-%d')}-summary.md")
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(f"# 对话总结 - {timestamp}\n\n")
        f.write("**时间**: {timestamp}\n")
        f.write("**消息数**: {len(chat_messages)}\n\n")
        f.write("---\n\n")
        f.write(f"{summary_text}\n\n")
        f.write("---\n\n")
        
        # 附加原始消息 (可选)
        f.write("## 原始消息\n\n")
        for i, msg in enumerate(chat_messages[:20], 1):  # 限制前 20 条
            f.write(f"{i}. {msg}\n")
    
    return {
        "status": "success",
        "file": summary_file,
        "timestamp": timestamp
    }

def main():
    if len(sys.argv) < 2:
        print("用法：python3 archive-chat-knowledge.py <knowledge_text> [category]")
        print("category: general (默认) | technical | strategy | lesson")
        print("\n示例:")
        print("  python3 archive-chat-knowledge.py '今天学到了...' technical")
        sys.exit(1)
    
    knowledge = sys.argv[1]
    category = sys.argv[2] if len(sys.argv) > 2 else "general"
    
    result = archive_knowledge(knowledge, category)
    print(f"✅ 知识已归档到：{result['file']}")
    print(f"📝 分类：{result['category']}")
    print(f"⏰ 时间：{result['timestamp']}")

if __name__ == "__main__":
    main()
