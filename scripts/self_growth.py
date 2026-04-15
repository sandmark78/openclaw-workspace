#!/usr/bin/env python3
"""
自我主动成长系统 - V6.1 联邦智能专用

核心理念:
1. 自主学习 - 自动发现知识缺口并补充
2. 自动优化 - 基于反馈持续改进
3. 自我进化 - 发现新模式并适应
4. 主动探索 - 不等待任务，主动寻找价值

触发器:
- 每次任务完成后自动反思
- 每日 23:00 自动学习总结
- 每周日自动能力评估
- 发现新模式时自动记录

使用:
python3 self_growth.py [learn|optimize|evolve|explore]
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
GROWTH_DIR = WORKSPACE / "growth"

# 成长策略 (从环境变量读取)
GROWTH_STRATEGY = os.getenv("GROWTH_STRATEGY", "balanced")
VALID_STRATEGIES = ["balanced", "innovate", "harden", "repair-only"]
if GROWTH_STRATEGY not in VALID_STRATEGIES:
    print(f"⚠️ 未知策略：{GROWTH_STRATEGY}，使用 balanced")
    GROWTH_STRATEGY = "balanced"
GROWTH_LOG = GROWTH_DIR / "growth_journal.jsonl"
CAPABILITY_FILE = GROWTH_DIR / "capabilities.json"
LEARNING_QUEUE = GROWTH_DIR / "learning_queue.json"

# 能力维度
CAPABILITY_DIMENSIONS = {
    "technical": {
        "name": "技术能力",
        "sub_skills": ["教程开发", "代码实现", "系统架构", "故障排查"],
        "level": 1,
        "evidence": []
    },
    "research": {
        "name": "研究能力",
        "sub_skills": ["市场分析", "竞品调研", "趋势预测", "数据收集"],
        "level": 1,
        "evidence": []
    },
    "creative": {
        "name": "创意能力",
        "sub_skills": ["内容创作", "营销文案", "视觉设计", "故事叙述"],
        "level": 1,
        "evidence": []
    },
    "automation": {
        "name": "自动化能力",
        "sub_skills": ["脚本编写", "Cron 配置", "工作流编排", "API 集成"],
        "level": 1,
        "evidence": []
    },
    "collaboration": {
        "name": "协作能力",
        "sub_skills": ["任务分配", "质量审核", "知识共享", "冲突解决"],
        "level": 1,
        "evidence": []
    },
    "monetization": {
        "name": "变现能力",
        "sub_skills": ["产品定价", "营销策略", "用户获取", "收益分析"],
        "level": 1,
        "evidence": []
    }
}

def init_growth_system():
    """初始化成长系统"""
    GROWTH_DIR.mkdir(exist_ok=True)
    
    # 加载或创建能力档案
    if CAPABILITY_FILE.exists():
        with open(CAPABILITY_FILE, 'r') as f:
            capabilities = json.load(f)
    else:
        capabilities = CAPABILITY_DIMENSIONS
        save_capabilities(capabilities)
    
    # 加载或创建学习队列
    if LEARNING_QUEUE.exists():
        with open(LEARNING_QUEUE, 'r') as f:
            queue = json.load(f)
    else:
        queue = {"pending": [], "completed": []}
        with open(LEARNING_QUEUE, 'w') as f:
            json.dump(queue, f, indent=2, ensure_ascii=False)
    
    print("✅ 成长系统初始化完成")
    return capabilities, queue

def save_capabilities(capabilities):
    """保存能力档案"""
    with open(CAPABILITY_FILE, 'w') as f:
        json.dump(capabilities, f, indent=2, ensure_ascii=False)

def log_growth(entry):
    """记录成长日志"""
    with open(GROWTH_LOG, 'a') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def auto_reflect(task, outcome, lessons):
    """自动反思 - 任务完成后触发"""
    print(f"🤔 自动反思：{task[:50]}...")
    
    entry = {
        "type": "reflection",
        "timestamp": datetime.now().isoformat(),
        "task": task,
        "outcome": outcome,
        "lessons": lessons,
        "action_items": []
    }
    
    # 从教训中提取行动项
    for lesson in lessons:
        if "需要" in lesson or "应该" in lesson or "改进" in lesson:
            entry["action_items"].append(lesson)
            # 添加到学习队列
            add_to_learning_queue(lesson)
    
    log_growth(entry)
    print(f"✅ 反思完成，发现 {len(entry['action_items'])} 个改进点")
    
    return entry

def add_to_learning_queue(item):
    """添加到学习队列"""
    with open(LEARNING_QUEUE, 'r') as f:
        queue = json.load(f)
    
    queue["pending"].append({
        "item": item,
        "added_at": datetime.now().isoformat(),
        "priority": "normal"
    })
    
    with open(LEARNING_QUEUE, 'w') as f:
        json.dump(queue, f, indent=2, ensure_ascii=False)
    
    print(f"📚 已添加到学习队列：{item[:50]}...")

def auto_learn():
    """自动学习 - 从学习队列中获取并执行"""
    print("📖 自动学习...")
    
    with open(LEARNING_QUEUE, 'r') as f:
        queue = json.load(f)
    
    if not queue["pending"]:
        print("✅ 学习队列为空，无需学习")
        return None
    
    # 获取最高优先级项目
    item = queue["pending"].pop(0)
    
    entry = {
        "type": "learning",
        "timestamp": datetime.now().isoformat(),
        "item": item["item"],
        "status": "in_progress"
    }
    
    log_growth(entry)
    
    with open(LEARNING_QUEUE, 'w') as f:
        json.dump(queue, f, indent=2, ensure_ascii=False)
    
    print(f"🎯 开始学习：{item['item'][:50]}...")
    
    return entry

def auto_optimize():
    """自动优化 - 分析成长日志发现优化点"""
    print("⚡ 自动优化分析...")
    
    # 读取最近 10 条成长日志
    logs = []
    with open(GROWTH_LOG, 'r') as f:
        for line in f:
            logs.append(json.loads(line))
    
    recent_logs = logs[-10:] if len(logs) > 10 else logs
    
    # 分析模式
    patterns = {
        "repeated_tasks": {},
        "common_issues": {},
        "success_patterns": []
    }
    
    for log in recent_logs:
        if log["type"] == "reflection":
            # 统计重复任务
            task_keyword = log["task"][:20]
            patterns["repeated_tasks"][task_keyword] = patterns["repeated_tasks"].get(task_keyword, 0) + 1
            
            # 统计常见问题
            for lesson in log.get("lessons", []):
                if "问题" in lesson or "失败" in lesson or "错误" in lesson:
                    patterns["common_issues"][lesson[:30]] = patterns["common_issues"].get(lesson[:30], 0) + 1
            
            # 记录成功模式
            if log.get("outcome") == "success":
                patterns["success_patterns"].append(log["task"][:50])
    
    entry = {
        "type": "optimization",
        "timestamp": datetime.now().isoformat(),
        "patterns": patterns,
        "recommendations": []
    }
    
    # 生成优化建议
    for task, count in patterns["repeated_tasks"].items():
        if count >= 3:
            entry["recommendations"].append(f"任务 '{task}' 重复{count}次，建议自动化")
    
    for issue, count in patterns["common_issues"].items():
        if count >= 2:
            entry["recommendations"].append(f"问题 '{issue}' 出现{count}次，需要系统性解决")
    
    log_growth(entry)
    
    print(f"✅ 发现 {len(entry['recommendations'])} 个优化点")
    for rec in entry["recommendations"]:
        print(f"   - {rec}")
    
    return entry

def auto_evolve():
    """自我进化 - 评估能力成长并调整策略"""
    print("🧬 自我进化评估...")
    
    capabilities, _ = init_growth_system()
    
    # 统计成长日志
    with open(GROWTH_LOG, 'r') as f:
        logs = [json.loads(line) for line in f]
    
    # 按能力维度统计证据
    for dim_id, dim in capabilities.items():
        evidence_count = 0
        for log in logs:
            if log["type"] == "reflection" and log.get("outcome") == "success":
                for skill in dim["sub_skills"]:
                    if skill in log["task"] or skill in str(log.get("lessons", [])):
                        evidence_count += 1
        
        # 更新能力等级 (每 5 个证据升 1 级)
        new_level = min(5, 1 + evidence_count // 5)
        if new_level > dim["level"]:
            print(f"📈 {dim['name']}: Lv.{dim['level']} → Lv.{new_level}")
            dim["level"] = new_level
    
    save_capabilities(capabilities)
    
    entry = {
        "type": "evolution",
        "timestamp": datetime.now().isoformat(),
        "capabilities": {k: v["level"] for k, v in capabilities.items()},
        "next_focus": []
    }
    
    # 确定下一个重点发展领域
    min_level = min(v["level"] for v in capabilities.values())
    for dim_id, dim in capabilities.items():
        if dim["level"] == min_level:
            entry["next_focus"].append(dim["name"])
    
    log_growth(entry)
    
    print(f"✅ 进化评估完成")
    print(f"🎯 下一步重点：{', '.join(entry['next_focus'])}")
    
    return entry

def auto_explore():
    """主动探索 - 发现新机会和新能力"""
    print("🔍 主动探索...")
    
    # 探索方向
    explorations = [
        {
            "area": "新技能开发",
            "questions": [
                "ClawHub 上有哪些热门技能？",
                "用户最需要什么类型的技能？",
                "我们可以填补哪些空白？"
            ]
        },
        {
            "area": "新变现渠道",
            "questions": [
                "除了 Gumroad，还有哪些平台？",
                "B2B 服务的可能性？",
                "订阅制模式是否可行？"
            ]
        },
        {
            "area": "新技术探索",
            "questions": [
                "OpenClaw 2.24 有哪些新特性？",
                "有哪些未使用的 hooks？",
                "如何优化模型调用成本？"
            ]
        }
    ]
    
    entry = {
        "type": "exploration",
        "timestamp": datetime.now().isoformat(),
        "areas": explorations,
        "action_items": []
    }
    
    # 生成探索行动项
    for area in explorations:
        for question in area["questions"]:
            entry["action_items"].append({
                "area": area["area"],
                "question": question,
                "status": "pending"
            })
    
    log_growth(entry)
    
    print(f"✅ 发现 {len(entry['action_items'])} 个探索方向")
    
    return entry

def growth_status():
    """显示成长状态"""
    print("📊 成长状态\n")
    
    capabilities, queue = init_growth_system()
    
    # 能力雷达图
    print("能力等级:")
    for dim_id, dim in capabilities.items():
        bar = "█" * dim["level"] + "░" * (5 - dim["level"])
        print(f"  {dim['name']}: [{bar}] Lv.{dim['level']}/5")
    
    print()
    
    # 学习队列
    pending_count = len(queue["pending"])
    completed_count = len(queue["completed"])
    print(f"学习队列：{pending_count} 待学 | {completed_count} 已完成")
    
    # 成长日志统计
    if GROWTH_LOG.exists():
        with open(GROWTH_LOG, 'r') as f:
            logs = [json.loads(line) for line in f]
    else:
        logs = []
    
    log_counts = {}
    for log in logs:
        log_type = log["type"]
        log_counts[log_type] = log_counts.get(log_type, 0) + 1
    
    print("\n成长记录:")
    for log_type, count in log_counts.items():
        print(f"  {log_type}: {count} 次")
    
    print()

def main():
    import sys
    
    # 初始化
    init_growth_system()
    
    if len(sys.argv) < 2:
        print("🧬 自我主动成长系统")
        print()
        print("用法：python3 self_growth.py [command]")
        print()
        print("命令:")
        print("  reflect <task> <outcome> <lessons> - 自动反思")
        print("  learn                              - 自动学习")
        print("  optimize                           - 自动优化")
        print("  evolve                             - 自我进化")
        print("  explore                            - 主动探索")
        print("  status                             - 成长状态")
        print("  full                               - 完整成长循环")
        print()
        return
    
    command = sys.argv[1]
    
    if command == "reflect":
        task = sys.argv[2] if len(sys.argv) > 2 else "测试任务"
        outcome = sys.argv[3] if len(sys.argv) > 3 else "success"
        lessons = sys.argv[4:] if len(sys.argv) > 4 else ["需要改进"]
        auto_reflect(task, outcome, lessons)
    elif command == "learn":
        auto_learn()
    elif command == "optimize":
        auto_optimize()
    elif command == "evolve":
        auto_evolve()
    elif command == "explore":
        auto_explore()
    elif command == "status":
        growth_status()
    elif command == "full":
        print("🔄 执行完整成长循环...\n")
        auto_explore()
        print()
        auto_learn()
        print()
        auto_optimize()
        print()
        auto_evolve()
        print()
        growth_status()
    else:
        print(f"未知命令：{command}")

if __name__ == "__main__":
    main()
