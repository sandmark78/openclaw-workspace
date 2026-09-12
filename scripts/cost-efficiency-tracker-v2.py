#!/usr/bin/env python3
"""
成本效率追踪器 V2 - 实际追踪模型调用、文件操作、命令执行
"""

import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
MEMORY_DIR = WORKSPACE / "memory"
SESSIONS_DIR = Path("/home/node/.openclaw/agents/main/sessions")

class CostEfficiencyTrackerV2:
    def __init__(self):
        self.today = datetime.now().strftime('%Y-%m-%d')
        self.metrics = {
            'date': self.today,
            'model_calls': 0,
            'file_reads': {},
            'file_writes': {},
            'commands_executed': {},
            'outputs_generated': 0,
            'total_cost': 0.0,
            'redundancy': {
                'duplicate_file_reads': 0,
                'duplicate_commands': 0,
                'duplicate_validations': 0
            }
        }
    
    def analyze_session_logs(self):
        """分析最近的 session 日志"""
        if not SESSIONS_DIR.exists():
            print(f"⚠️  Session 目录不存在: {SESSIONS_DIR}")
            return
        
        # 查找今天的 session 文件
        session_files = list(SESSIONS_DIR.glob(f"*{self.today}*.jsonl"))
        if not session_files:
            # 查找最近的文件
            session_files = sorted(SESSIONS_DIR.glob("*.jsonl"), key=os.path.getmtime, reverse=True)[:3]
        
        for session_file in session_files:
            self._parse_session_file(session_file)
    
    def _parse_session_file(self, filepath):
        """解析单个 session 文件"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        entry = json.loads(line.strip())
                        self._analyze_entry(entry)
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"⚠️  解析 {filepath} 失败: {e}")
    
    def _analyze_entry(self, entry):
        """分析单个 entry"""
        # 检测模型调用
        if 'model' in entry or 'toolCall' in entry:
            self.metrics['model_calls'] += 1
        
        # 检测文件读取
        if 'toolCall' in entry:
            tool_call = entry.get('toolCall', {})
            tool_name = tool_call.get('name', '')
            tool_input = tool_call.get('input', {})
            
            if tool_name == 'read':
                file_path = tool_input.get('path', '')
                if file_path:
                    self.metrics['file_reads'][file_path] = self.metrics['file_reads'].get(file_path, 0) + 1
            
            elif tool_name == 'exec':
                command = tool_input.get('command', '')
                if command:
                    # 简化命令（取前 50 字符）
                    cmd_key = command[:50]
                    self.metrics['commands_executed'][cmd_key] = self.metrics['commands_executed'].get(cmd_key, 0) + 1
            
            elif tool_name == 'write':
                file_path = tool_input.get('path', '')
                if file_path:
                    self.metrics['file_writes'][file_path] = self.metrics['file_writes'].get(file_path, 0) + 1
                    self.metrics['outputs_generated'] += 1
    
    def calculate_redundancy(self):
        """计算冗余调用"""
        # 重复文件读取
        duplicate_reads = sum(
            count - 1 for count in self.metrics['file_reads'].values() if count > 1
        )
        self.metrics['redundancy']['duplicate_file_reads'] = duplicate_reads
        
        # 重复命令执行
        duplicate_commands = sum(
            count - 1 for count in self.metrics['commands_executed'].values() if count > 1
        )
        self.metrics['redundancy']['duplicate_commands'] = duplicate_commands
        
        # 总冗余
        total_redundant = duplicate_reads + duplicate_commands
        total_operations = self.metrics['model_calls']
        
        if total_operations > 0:
            redundancy_rate = (total_redundant / total_operations) * 100
        else:
            redundancy_rate = 0.0
        
        return {
            'total_redundant': total_redundant,
            'redundancy_rate': redundancy_rate,
            'duplicate_reads': duplicate_reads,
            'duplicate_commands': duplicate_commands
        }
    
    def generate_report(self):
        """生成报告"""
        redundancy = self.calculate_redundancy()
        
        # 计算单次产出成本（估算）
        # 假设每次调用成本 ¥0.05
        estimated_cost = self.metrics['model_calls'] * 0.05
        if self.metrics['outputs_generated'] > 0:
            cost_per_output = estimated_cost / self.metrics['outputs_generated']
        else:
            cost_per_output = estimated_cost
        
        report = f"""# 成本效率报告 - {self.today}

## 核心指标

| 指标 | 数值 | 目标 | 状态 |
|------|------|------|------|
| 模型调用次数 | {self.metrics['model_calls']} | - | - |
| 冗余调用次数 | {redundancy['total_redundant']} | <15% | {'✅' if redundancy['redundancy_rate'] < 15 else '⚠️'} |
| 冗余调用率 | {redundancy['redundancy_rate']:.1f}% | <15% | {'✅' if redundancy['redundancy_rate'] < 15 else '⚠️'} |
| 产出数量 | {self.metrics['outputs_generated']} | - | - |
| 单次产出成本 | ¥{cost_per_output:.4f} | <¥0.10 | {'✅' if cost_per_output < 0.10 else '⚠️'} |
| 估算总成本 | ¥{estimated_cost:.2f} | - | - |

## 冗余分析

### 重复文件读取 ({redundancy['duplicate_reads']} 次)
"""
        
        # 列出重复读取的文件
        for file_path, count in sorted(
            self.metrics['file_reads'].items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:10]:
            if count > 1:
                report += f"- `{file_path}`: {count} 次\n"
        
        report += f"""
### 重复命令执行 ({redundancy['duplicate_commands']} 次)
"""
        
        # 列出重复执行的命令
        for cmd, count in sorted(
            self.metrics['commands_executed'].items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:10]:
            if count > 1:
                report += f"- `{cmd}...`: {count} 次\n"
        
        report += f"""
## 优化建议

"""
        
        if redundancy['redundancy_rate'] > 15:
            report += """### 🔴 冗余调用率过高
**问题**: 重复读取文件、重复执行命令
**建议**: 
1. 实施缓存策略 - 读取一次文件后缓存内容
2. 避免重复验证 - 验证一次状态后记录结果
3. 批量操作 - 合并多个操作到一个脚本
**目标**: 将冗余率降到 15% 以下
"""
        
        if cost_per_output > 0.10:
            report += """### ⚠️ 单次产出成本过高
**问题**: 每次产出消耗过多模型调用
**建议**:
1. 批量处理 - 一次生成多个产出
2. 充分利用 1M 上下文 - 一次塞够材料
3. 减少中间步骤 - 直接产出最终结果
**目标**: 单次产出成本 < ¥0.10
"""
        
        if self.metrics['model_calls'] > 50:
            report += """### ⚠️ 调用次数过多
**问题**: 今日调用次数超过 50 次
**建议**:
1. 检查是否有不必要的重复操作
2. 考虑使用本地脚本替代模型调用
3. 批量处理任务，减少调用次数
"""
        
        report += f"""
## 详细统计

### 文件读取 TOP 10
"""
        for file_path, count in sorted(
            self.metrics['file_reads'].items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:10]:
            report += f"- `{file_path}`: {count} 次\n"
        
        report += f"""
### 命令执行 TOP 10
"""
        for cmd, count in sorted(
            self.metrics['commands_executed'].items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:10]:
            report += f"- `{cmd}...`: {count} 次\n"
        
        report += f"""
---

*报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*
*数据来源: Session 日志分析*
"""
        
        return report
    
    def save(self):
        """保存报告"""
        report = self.generate_report()
        report_file = MEMORY_DIR / f"cost-report-{self.today}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ 成本效率报告已生成: {report_file}")
        return self.metrics

def main():
    tracker = CostEfficiencyTrackerV2()
    
    print("🔍 分析 Session 日志...")
    tracker.analyze_session_logs()
    
    print("\n📊 生成报告...")
    metrics = tracker.save()
    
    print(f"\n📈 核心指标:")
    print(f"  模型调用: {metrics['model_calls']} 次")
    print(f"  产出数量: {metrics['outputs_generated']} 个")
    print(f"  文件读取: {len(metrics['file_reads'])} 个不同文件")
    print(f"  命令执行: {len(metrics['commands_executed'])} 个不同命令")

if __name__ == '__main__':
    main()
