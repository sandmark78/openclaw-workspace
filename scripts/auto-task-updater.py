#!/usr/bin/env python3
"""
Auto Task Updater - V6.3.5
自动更新任务清单，根据 Cron 执行记录和每日记忆文件

功能:
1. 扫描 memory/ 目录下的 Cron 执行记录
2. 自动提取已完成任务
3. 更新 tasks.md 的已完成任务列表
4. 生成执行统计

使用:
    python3 auto-task-updater.py [--dry-run]
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
MEMORY_DIR = WORKSPACE / "memory"
TASKS_FILE = WORKSPACE / "memory" / "tasks.md"

def parse_cron_record(content: str) -> list:
    """从 Cron 记录中提取任务完成信息"""
    tasks = []
    
    # 匹配 Cron 完成记录
    patterns = [
        r'## Cron #(\d+).*?\n### 系统状态\n- ✅ Gateway 正常\n- ✅ WebUI 正常',
        r'📚 Cron 知识获取 #(\d+).*?完成',
        r'📡 市场扫描 #(\d+).*?完成',
        r'🧠 深度学习 #(\d+).*?完成',
        r'📊 每日自省报告.*?完成',
        r'🛠️.*?完成',
    ]
    
    # 提取文件数和知识点
    file_match = re.search(r'\+(\d+) 文件', content)
    points_match = re.search(r'\+(\d+[,\d]*) 点', content)
    
    files = int(file_match.group(1).replace(',', '')) if file_match else 0
    points = int(points_match.group(1).replace(',', '')) if points_match else 0
    
    # 提取日期
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', content)
    date = date_match.group(1) if date_match else datetime.now().strftime('%Y-%m-%d')
    
    # 提取时间
    time_match = re.search(r'(\d{2}:\d{2}) UTC', content)
    time = time_match.group(1) if time_match else "00:00"
    
    if 'Cron #' in content or 'cron #' in content.lower():
        cron_match = re.search(r'Cron #(\d+)', content, re.IGNORECASE)
        if cron_match:
            cron_num = cron_match.group(1)
            task_type = "知识获取" if "知识获取" in content else "市场扫描" if "市场扫描" in content else "深度学习" if "深度学习" in content else "常规"
            tasks.append({
                'id': f"Cron-{cron_num}",
                'name': f"📚 Cron {task_type} #{cron_num}",
                'date': date,
                'time': time,
                'files': files,
                'points': points,
                'status': '✅ 完成'
            })
    
    return tasks

def scan_memory_files() -> list:
    """扫描 memory 目录下的所有文件，提取任务完成记录"""
    completed_tasks = []
    today = datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    # 扫描今日和昨日文件
    for filename in [f"{today}.md", f"{yesterday}.md"]:
        filepath = MEMORY_DIR / filename
        if filepath.exists():
            content = filepath.read_text()
            tasks = parse_cron_record(content)
            completed_tasks.extend(tasks)
    
    # 去重
    seen = set()
    unique_tasks = []
    for task in completed_tasks:
        if task['id'] not in seen:
            seen.add(task['id'])
            unique_tasks.append(task)
    
    return unique_tasks

def generate_task_table(tasks: list) -> str:
    """生成 Markdown 任务表格"""
    if not tasks:
        return "*暂无新完成任务*\n"
    
    lines = ["| ID | 任务 | 完成时间 | 状态 |", "|----|------|----------|------|"]
    
    for task in sorted(tasks, key=lambda x: x['id'], reverse=True):
        time_str = f"{task['date']} {task['time']}"
        detail = ""
        if task['files'] > 0 or task['points'] > 0:
            detail = f" (+{task['files']}文件/+{task['points']}点)"
        
        lines.append(f"| {task['id']} | **{task['name']}**{detail} | **{time_str}** | ✅ **完成** |")
    
    return '\n'.join(lines) + '\n'

def update_tasks_file(new_tasks: list, dry_run: bool = False):
    """更新 tasks.md 文件"""
    if not TASKS_FILE.exists():
        print(f"❌ 任务文件不存在：{TASKS_FILE}")
        return
    
    content = TASKS_FILE.read_text()
    
    # 找到"已完成任务"部分
    completed_section = re.search(r'(## ✅ 已完成任务\n\n### P0 优先级\n)', content)
    if not completed_section:
        print("❌ 未找到已完成任务部分")
        return
    
    insert_pos = completed_section.end()
    
    # 生成新任务表格
    new_table = generate_task_table(new_tasks)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M UTC')
    new_section = f"\n### 最新完成 ({timestamp})\n\n{new_table}\n"
    
    if dry_run:
        print("🔍 [Dry Run] 将插入以下内容:")
        print(new_section)
        return
    
    # 插入新内容
    new_content = content[:insert_pos] + new_section + content[insert_pos:]
    TASKS_FILE.write_text(new_content)
    
    print(f"✅ 已更新 {len(new_tasks)} 个任务到 tasks.md")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Auto Task Updater - 自动更新任务清单')
    parser.add_argument('--dry-run', action='store_true', help='预览模式，不实际写入')
    args = parser.parse_args()
    
    print(f"⚡ Auto Task Updater V6.3.5")
    print(f"📅 扫描时间：{datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print()
    
    # 扫描记忆文件
    print("🔍 扫描 memory 目录...")
    tasks = scan_memory_files()
    
    if not tasks:
        print("ℹ️  未发现新完成的任务")
        return
    
    print(f"📦 发现 {len(tasks)} 个新完成任务:")
    for task in tasks:
        detail = ""
        if task['files'] > 0 or task['points'] > 0:
            detail = f" (+{task['files']}文件/+{task['points']}点)"
        print(f"  ✅ {task['name']}{detail}")
    print()
    
    # 更新任务文件
    print("📝 更新 tasks.md...")
    update_tasks_file(tasks, dry_run=args.dry_run)
    
    print()
    print("✅ 完成!")

if __name__ == '__main__':
    main()
