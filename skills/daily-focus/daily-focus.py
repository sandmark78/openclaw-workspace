#!/usr/bin/env python3
"""
Daily Focus - 每日优先级与专注追踪工具
版本：V1.0.0
作者：Sandbot 🏖️
"""

import sys
import os
from datetime import datetime, timedelta
import json

# 配置
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
TODAY = datetime.utcnow().strftime('%Y-%m-%d')
TODAY_FILE = os.path.join(DATA_DIR, f'{TODAY}.md')

def ensure_data_dir():
    """确保数据目录存在"""
    os.makedirs(DATA_DIR, exist_ok=True)

def get_today_data():
    """获取今日数据"""
    if os.path.exists(TODAY_FILE):
        with open(TODAY_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            # 简单解析
            if '## 优先级' in content:
                return parse_today_file(content)
    return {'priorities': [], 'sessions': []}

def parse_today_file(content):
    """解析今日文件"""
    data = {'priorities': [], 'sessions': []}
    lines = content.split('\n')
    
    in_priorities = False
    in_sessions = False
    
    for line in lines:
        if line.startswith('## 优先级'):
            in_priorities = True
            in_sessions = False
            continue
        elif line.startswith('## 专注会话'):
            in_priorities = False
            in_sessions = True
            continue
        elif line.startswith('##'):
            in_priorities = False
            in_sessions = False
            continue
        
        if in_priorities and line.strip().startswith(('1.', '2.', '3.')):
            data['priorities'].append(line.strip())
        elif in_sessions and '|' in line and not line.startswith('|-'):
            parts = line.split('|')
            if len(parts) >= 6:
                data['sessions'].append({
                    'num': parts[1].strip(),
                    'start': parts[2].strip(),
                    'end': parts[3].strip(),
                    'duration': parts[4].strip(),
                    'task': parts[5].strip(),
                    'note': parts[6].strip() if len(parts) > 6 else ''
                })
    
    return data

def save_today_file(data):
    """保存今日文件"""
    ensure_data_dir()
    
    content = f"""# {TODAY} 每日专注记录

## 优先级
"""
    for i, priority in enumerate(data.get('priorities', []), 1):
        content += f"{i}. {priority}\n"
    
    content += "\n## 专注会话\n"
    content += "| # | 开始时间 | 结束时间 | 时长 | 任务 | 备注 |\n"
    content += "|---|----------|----------|------|------|------|\n"
    
    for session in data.get('sessions', []):
        content += f"| {session['num']} | {session['start']} | {session['end']} | {session['duration']} | {session['task']} | {session['note']} |\n"
    
    # 统计
    total_minutes = sum(int(s['duration'].replace('m', '')) for s in data.get('sessions', []) if s['duration'].replace('m', '').isdigit())
    completed = sum(1 for p in data.get('priorities', []) if p.startswith('✅'))
    
    content += f"""
## 统计
- 专注会话：{len(data.get('sessions', []))}/4
- 总时长：{total_minutes} 分钟
- 优先级完成：{completed}/{len(data.get('priorities', []))}
"""
    
    with open(TODAY_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def cmd_init():
    """初始化"""
    ensure_data_dir()
    print("🏖️ Daily Focus 初始化完成!")
    print(f"📁 数据目录：{DATA_DIR}")
    print(f"📅 今日文件：{TODAY_FILE}")
    print("\n💡 使用提示:")
    print("   python3 daily-focus.py set \"任务 1\" \"任务 2\" \"任务 3\"")
    print("   python3 daily-focus.py start")
    print("   python3 daily-focus.py status")

def cmd_set(priorities):
    """设定优先级"""
    if len(priorities) == 0:
        print("❌ 请提供 1-3 个优先级任务")
        print("   用法：python3 daily-focus.py set \"任务 1\" \"任务 2\" \"任务 3\"")
        return
    
    if len(priorities) > 3:
        print("⚠️ 只保留前 3 个优先级 (聚焦原则)")
        priorities = priorities[:3]
    
    data = get_today_data()
    data['priorities'] = [f"⏳ {p}" for p in priorities]
    save_today_file(data)
    
    print("🎯 今日优先级设定完成!")
    for i, p in enumerate(data['priorities'], 1):
        print(f"   {i}. {p}")
    print(f"\n💪 加油！专注于这{len(priorities)}件事就够了 🏖️")

def cmd_start(minutes=25):
    """开始专注"""
    data = get_today_data()
    
    if not data.get('priorities'):
        print("⚠️ 还没有设定今日优先级!")
        print("   先运行：python3 daily-focus.py set \"任务\"")
        return
    
    # 找第一个未完成的任务
    current_task = "专注工作"
    for p in data['priorities']:
        if p.startswith('⏳'):
            current_task = p.replace('⏳ ', '')
            break
    
    now = datetime.utcnow()
    end_time = now + timedelta(minutes=minutes)
    
    print(f"🍅 专注开始 ({minutes} 分钟)")
    print(f"   任务：{current_task}")
    print(f"   开始：{now.strftime('%H:%M')} UTC")
    print(f"   结束：{end_time.strftime('%H:%M')} UTC")
    print(f"\n🏖️ 专注中，勿扰!")
    
    # 保存开始时间到临时文件
    session_file = os.path.join(DATA_DIR, '.current_session.json')
    with open(session_file, 'w') as f:
        json.dump({
            'start': now.isoformat(),
            'end': end_time.isoformat(),
            'task': current_task,
            'minutes': minutes
        }, f)

def cmd_stop(note=""):
    """结束专注"""
    session_file = os.path.join(DATA_DIR, '.current_session.json')
    
    if not os.path.exists(session_file):
        print("❌ 没有进行中的专注会话")
        print("   先运行：python3 daily-focus.py start")
        return
    
    with open(session_file, 'r') as f:
        session = json.load(f)
    
    os.remove(session_file)
    
    start = datetime.fromisoformat(session['start'])
    end = datetime.utcnow()
    actual_minutes = int((end - start).total_seconds() / 60)
    
    data = get_today_data()
    session_num = len(data.get('sessions', [])) + 1
    
    new_session = {
        'num': str(session_num),
        'start': start.strftime('%H:%M'),
        'end': end.strftime('%H:%M'),
        'duration': f"{actual_minutes}m",
        'task': session['task'],
        'note': note
    }
    
    if 'sessions' not in data:
        data['sessions'] = []
    data['sessions'].append(new_session)
    save_today_file(data)
    
    print(f"✅ 专注完成!")
    print(f"   任务：{session['task']}")
    print(f"   耗时：{actual_minutes} 分钟")
    if note:
        print(f"   备注：{note}")
    print(f"\n📊 今日累计：{session_num} 个专注会话")
    print(f"🏖️ 干得不错!")

def cmd_status():
    """查看状态"""
    data = get_today_data()
    
    print(f"📊 今日状态 ({TODAY})")
    print()
    
    if data.get('priorities'):
        print("🎯 优先级:")
        for p in data['priorities']:
            print(f"   {p}")
    else:
        print("🎯 优先级：未设定 (运行 set 命令)")
    
    print()
    
    sessions = data.get('sessions', [])
    total_minutes = sum(int(s['duration'].replace('m', '')) for s in sessions if s['duration'].replace('m', '').isdigit())
    
    print(f"🍅 专注会话：{len(sessions)}/4")
    print(f"   总时长：{total_minutes} 分钟")
    
    if sessions:
        print("   今日记录:")
        for s in sessions[-3:]:  # 只显示最近 3 个
            print(f"     - {s['task']} ({s['duration']})")
    
    completed = sum(1 for p in data.get('priorities', []) if p.startswith('✅'))
    total = len(data.get('priorities', []))
    print(f"\n✅ 优先级完成：{completed}/{total}")
    
    if completed == total and total > 0:
        print("\n🎉 今日任务全部完成！给自己点个赞 🏖️")

def cmd_summary():
    """生成总结"""
    data = get_today_data()
    
    sessions = data.get('sessions', [])
    total_minutes = sum(int(s['duration'].replace('m', '')) for s in sessions if s['duration'].replace('m', '').isdigit())
    completed = sum(1 for p in data.get('priorities', []) if p.startswith('✅'))
    total = len(data.get('priorities', []))
    
    print(f"📝 {TODAY} 每日总结")
    print("=" * 40)
    print()
    
    print("🎯 优先级完成情况:")
    for p in data.get('priorities', []):
        print(f"   {p}")
    
    print()
    print("🍅 专注会话:")
    if sessions:
        for s in sessions:
            print(f"   {s['start']}-{s['end']} | {s['task']} | {s['note']}")
    else:
        print("   无记录")
    
    print()
    print("📊 统计:")
    print(f"   专注会话：{len(sessions)} 个")
    print(f"   总时长：{total_minutes} 分钟")
    print(f"   优先级完成：{completed}/{total} ({100*completed//total if total else 0}%)")
    
    print()
    print("🏖️ Sandbot 点评:")
    if total_minutes >= 120:
        print("   今天很专注！继续保持 👍")
    elif total_minutes >= 60:
        print("   不错的开始，明天可以更多 🚀")
    elif total_minutes > 0:
        print("   至少开始了，明天加油 💪")
    else:
        print("   今天是休息日？明天重新出发 🌅")

def cmd_help():
    """帮助"""
    print("""
🏖️ Daily Focus - 每日优先级与专注追踪

用法:
  python3 daily-focus.py init              # 初始化
  python3 daily-focus.py set "任务 1" ...  # 设定优先级 (1-3 个)
  python3 daily-focus.py start [分钟]      # 开始专注 (默认 25 分钟)
  python3 daily-focus.py stop [备注]       # 结束专注
  python3 daily-focus.py status            # 查看状态
  python3 daily-focus.py summary           # 生成总结
  python3 daily-focus.py help              # 显示帮助

示例:
  python3 daily-focus.py set "写教程" "发帖子" "优化脚本"
  python3 daily-focus.py start
  python3 daily-focus.py stop "完成了初稿"
  python3 daily-focus.py status

📁 数据存储在：""" + DATA_DIR)

def main():
    if len(sys.argv) < 2:
        cmd_help()
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'init':
        cmd_init()
    elif cmd == 'set':
        cmd_set(sys.argv[2:])
    elif cmd == 'start':
        minutes = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 25
        cmd_start(minutes)
    elif cmd == 'stop':
        note = ' '.join(sys.argv[2:]) if len(sys.argv) > 2 else ''
        cmd_stop(note)
    elif cmd == 'status':
        cmd_status()
    elif cmd == 'summary':
        cmd_summary()
    elif cmd == 'help':
        cmd_help()
    else:
        print(f"❌ 未知命令：{cmd}")
        cmd_help()

if __name__ == '__main__':
    main()
