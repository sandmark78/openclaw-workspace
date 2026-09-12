#!/usr/bin/env python3
"""
成本效率追踪器 V2 - 实用版
在每次对话结束时调用，记录当日指标
"""

import json
import os
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
METRICS_FILE = WORKSPACE / "memory" / "cost-metrics.json"

def load_metrics():
    if METRICS_FILE.exists():
        with open(METRICS_FILE) as f:
            return json.load(f)
    return {}

def save_metrics(data):
    with open(METRICS_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_today():
    return datetime.now().strftime('%Y-%m-%d')

def record_daily(output_count=0, call_count=0, redundant_count=0, notes=""):
    """记录每日指标"""
    data = load_metrics()
    today = get_today()
    
    if today not in data:
        data[today] = {
            'outputs': 0,
            'calls': 0,
            'redundant': 0,
            'notes': []
        }
    
    data[today]['outputs'] += output_count
    data[today]['calls'] += call_count
    data[today]['redundant'] += redundant_count
    if notes:
        data[today]['notes'].append(notes)
    
    save_metrics(data)
    return data[today]

def generate_report():
    """生成效率报告"""
    data = load_metrics()
    today = get_today()
    
    # 计算汇总
    total_days = len(data)
    total_outputs = sum(d['outputs'] for d in data.values())
    total_calls = sum(d['calls'] for d in data.values())
    total_redundant = sum(d['redundant'] for d in data.values())
    
    # 计算效率指标
    if total_calls > 0:
        redundancy_rate = (total_redundant / total_calls) * 100
        calls_per_output = total_calls / max(total_outputs, 1)
    else:
        redundancy_rate = 0
        calls_per_output = 0
    
    # 估算成本 (每次调用约 ¥0.05)
    estimated_cost = total_calls * 0.05
    cost_per_output = estimated_cost / max(total_outputs, 1)
    
    report = f"""# 成本效率追踪报告

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}
**追踪天数**: {total_days} 天

## 核心指标

| 指标 | 数值 | 目标 | 状态 |
|------|------|------|------|
| 总调用次数 | {total_calls} | - | - |
| 总产出数量 | {total_outputs} | - | - |
| 冗余调用次数 | {total_redundant} | <15% | {'✅' if redundancy_rate < 15 else '⚠️'} |
| 冗余调用率 | {redundancy_rate:.1f}% | <15% | {'✅' if redundancy_rate < 15 else '⚠️'} |
| 每次产出调用数 | {calls_per_output:.1f} | <3 | {'✅' if calls_per_output < 3 else '⚠️'} |
| 单次产出成本 | ¥{cost_per_output:.3f} | <¥0.10 | {'✅' if cost_per_output < 0.10 else '⚠️'} |
| 估算总成本 | ¥{estimated_cost:.2f} | - | - |

## 每日明细

| 日期 | 产出 | 调用 | 冗余 | 冗余率 | 单次成本 |
|------|------|------|------|--------|----------|
"""
    
    for date in sorted(data.keys(), reverse=True)[:14]:
        d = data[date]
        day_calls = d['calls']
        day_redundant = d['redundant']
        day_outputs = d['outputs']
        
        if day_calls > 0:
            day_rate = (day_redundant / day_calls) * 100
            day_cost = (day_calls * 0.05) / max(day_outputs, 1)
        else:
            day_rate = 0
            day_cost = 0
        
        report += f"| {date} | {day_outputs} | {day_calls} | {day_redundant} | {day_rate:.0f}% | ¥{day_cost:.3f} |\n"
    
    report += f"""
## 优化建议

"""
    
    if redundancy_rate > 15:
        report += """### 🔴 冗余率过高
- 重复读取文件 → 缓存读取结果
- 重复执行命令 → 合并到脚本
- 重复验证状态 → 验证一次记录结果
"""
    
    if calls_per_output > 3:
        report += """### ⚠️ 每次产出调用过多
- 批量处理：一次调用产出多个结果
- 减少中间验证：合并操作步骤
- 脚本化：能脚本化的不手动做
"""
    
    if cost_per_output > 0.10:
        report += """### ⚠️ 单次产出成本过高
- 利用 1M 上下文：一次塞够材料
- 减少不必要的读取
- 优先本地处理
"""
    
    if redundancy_rate <= 15 and calls_per_output <= 3 and cost_per_output <= 0.10:
        report += "✅ 所有指标达标！继续保持。\n"
    
    report += f"""
## 使用方法

```bash
# 记录一次产出
python3 scripts/cost-efficiency-tracker.py record --outputs 1 --calls 2

# 记录冗余
python3 scripts/cost-efficiency-tracker.py record --redundant 1 --notes "重复读取 MEMORY.md"

# 生成报告
python3 scripts/cost-efficiency-tracker.py report
```

---
*自动追踪，每日更新*
"""
    
    return report

def main():
    import sys
    
    if len(sys.argv) < 2:
        print(generate_report())
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'record':
        outputs = 0
        calls = 0
        redundant = 0
        notes = ""
        
        for i, arg in enumerate(sys.argv[2:], 2):
            if arg == '--outputs' and i+1 < len(sys.argv):
                outputs = int(sys.argv[i+1])
            elif arg == '--calls' and i+1 < len(sys.argv):
                calls = int(sys.argv[i+1])
            elif arg == '--redundant' and i+1 < len(sys.argv):
                redundant = int(sys.argv[i+1])
            elif arg == '--notes' and i+1 < len(sys.argv):
                notes = sys.argv[i+1]
        
        result = record_daily(outputs, calls, redundant, notes)
        print(f"✅ 已记录: 产出+{outputs}, 调用+{calls}, 冗余+{redundant}")
        print(f"   今日累计: 产出={result['outputs']}, 调用={result['calls']}, 冗余={result['redundant']}")
    
    elif cmd == 'report':
        report = generate_report()
        report_file = WORKSPACE / "memory" / f"cost-report-{get_today()}.md"
        with open(report_file, 'w') as f:
            f.write(report)
        print(f"✅ 报告已生成: {report_file}")
        print(report)

if __name__ == '__main__':
    main()
