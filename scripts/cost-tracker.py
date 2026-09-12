#!/usr/bin/env python3
"""
成本追踪脚本 - 记录每日 token 消耗和费用
"""

import os
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path('/home/node/.openclaw/workspace')
SESSIONS_DIR = WORKSPACE / 'agents/main/sessions'
MEMORY_DIR = WORKSPACE / 'memory'

def count_session_stats():
    """统计会话数据"""
    stats = {
        'total_sessions': 0,
        'total_lines': 0,
        'today_sessions': 0,
        'today_lines': 0
    }
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    for session_file in SESSIONS_DIR.glob('*.jsonl'):
        stats['total_sessions'] += 1
        
        # 检查是否今天的文件
        mtime = datetime.fromtimestamp(session_file.stat().st_mtime)
        if mtime.strftime('%Y-%m-%d') == today:
            stats['today_sessions'] += 1
        
        # 统计行数
        with open(session_file, 'r') as f:
            lines = sum(1 for _ in f)
            stats['total_lines'] += lines
            if mtime.strftime('%Y-%m-%d') == today:
                stats['today_lines'] += lines
    
    return stats

def estimate_cost(lines):
    """估算成本（粗略）"""
    # 假设平均每行 ~2000 tokens，qwen3.5-plus 按次计费 ~¥0.05/次
    # 每次会话平均 100 行 = ~¥0.05
    estimated_calls = lines / 100
    estimated_cost = estimated_calls * 0.05
    return estimated_cost, estimated_calls

def update_daily_memory():
    """更新每日记忆文件"""
    today = datetime.now().strftime('%Y-%m-%d')
    memory_file = MEMORY_DIR / f'{today}.md'
    
    stats = count_session_stats()
    cost, calls = estimate_cost(stats['today_lines'])
    
    # 读取或创建文件
    if memory_file.exists():
        with open(memory_file, 'r') as f:
            content = f.read()
    else:
        content = f'# {today} 每日记录\n\n'
    
    # 添加成本追踪部分
    cost_section = f"""
## 💰 成本追踪 (自动更新 {datetime.now().strftime('%H:%M')})

| 指标 | 数值 |
|------|------|
| 今日会话数 | {stats['today_sessions']} |
| 今日行数 | {stats['today_lines']} |
| 估算调用次数 | {calls:.0f} |
| 估算成本 | ¥{cost:.2f} |
| 总会话数 | {stats['total_sessions']} |
| 总行数 | {stats['total_lines']} |

**成本优化目标**: 
- 单次产出成本 < ¥0.10
- 冗余调用率 < 15%
- 上下文利用率 > 60%
"""
    
    # 如果已有成本追踪部分，替换它
    if '## 💰 成本追踪' in content:
        # 找到成本追踪部分的开始和结束
        start = content.find('## 💰 成本追踪')
        # 找到下一个 ## 或文件结尾
        next_section = content.find('\n## ', start + 1)
        if next_section != -1:
            content = content[:start] + cost_section + content[next_section:]
        else:
            content = content[:start] + cost_section
    else:
        content += cost_section
    
    # 写回文件
    with open(memory_file, 'w') as f:
        f.write(content)
    
    print(f'✅ 成本追踪已更新: {memory_file}')
    print(f'   今日会话: {stats["today_sessions"]}')
    print(f'   今日行数: {stats["today_lines"]}')
    print(f'   估算成本: ¥{cost:.2f}')

if __name__ == '__main__':
    update_daily_memory()
