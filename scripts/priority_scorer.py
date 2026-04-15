#!/usr/bin/env python3
"""
V6.1 优先级评分系统
基于 Timo 硅基主动学习法 V2.0

使用:
python3 priority_scorer.py <任务描述>
"""

import sys
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
PRIORITY_LOG = WORKSPACE / "memory" / "priority_scores.jsonl"

# 评分标准
def rate_business_value(task: str) -> int:
    """评估业务价值 (1-5 分)"""
    keywords = {
        5: ["变现", "收益", "赚钱", "销售", "发布", "clawhub", "gumroad"],
        4: ["技能", "开发", "社区", "互动", "moltbook", "github"],
        3: ["学习", "研究", "分析", "文档", "优化"],
        2: ["整理", "清理", "修复", "测试"],
        1: ["日常", "维护", "心跳"]
    }
    
    task_lower = task.lower()
    for score, kws in keywords.items():
        for kw in kws:
            if kw in task_lower:
                return score
    return 3

def rate_knowledge_gap(task: str) -> int:
    """评估知识缺口 (1-5 分)"""
    # 简化版：根据任务类型判断
    if any(kw in task.lower() for kw in ["新", "首次", "探索", "研究"]):
        return 5
    elif any(kw in task.lower() for kw in ["学习", "改进", "增强"]):
        return 4
    elif any(kw in task.lower() for kw in ["继续", "继续", "完成"]):
        return 3
    elif any(kw in task.lower() for kw in ["修复", "优化", "整理"]):
        return 2
    else:
        return 1

def rate_learning_cost(task: str) -> int:
    """评估学习成本 (1-5 分，1=最低)"""
    # 简化版：根据任务复杂度判断
    if any(kw in task.lower() for kw in ["简单", "快速", "小"]):
        return 1
    elif any(kw in task.lower() for kw in ["中等", "标准"]):
        return 2
    elif any(kw in task.lower() for kw in ["复杂", "大型", "系统"]):
        return 3
    elif any(kw in task.lower() for kw in ["困难", "挑战"]):
        return 4
    else:
        return 2

def calculate_priority(business_value: int, knowledge_gap: int, learning_cost: int) -> float:
    """计算优先级分数"""
    if learning_cost == 0:
        learning_cost = 1  # 避免除零
    return (business_value * knowledge_gap) / learning_cost

def get_priority_level(score: float) -> str:
    """获取优先级等级"""
    if score >= 10:
        return "P0 - 最高优先级"
    elif score >= 6:
        return "P1 - 高优先级"
    elif score >= 4:
        return "P2 - 中优先级"
    else:
        return "P3 - 低优先级"

def log_priority(task: str, bv: int, kg: int, lc: int, score: float):
    """记录优先级评分"""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "task": task,
        "business_value": bv,
        "knowledge_gap": kg,
        "learning_cost": lc,
        "priority_score": score,
        "level": get_priority_level(score)
    }
    
    PRIORITY_LOG.parent.mkdir(exist_ok=True)
    with open(PRIORITY_LOG, 'a') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def main():
    if len(sys.argv) < 2:
        print("🎯 V6.1 优先级评分系统")
        print("用法：python3 priority_scorer.py <任务描述>")
        print()
        print("示例:")
        print("  python3 priority_scorer.py '发布技能到 ClawHub'")
        print("  python3 priority_scorer.py '修复测试脚本'")
        return
    
    task = " ".join(sys.argv[1:])
    
    bv = rate_business_value(task)
    kg = rate_knowledge_gap(task)
    lc = rate_learning_cost(task)
    score = calculate_priority(bv, kg, lc)
    level = get_priority_level(score)
    
    print(f"🎯 优先级评分")
    print(f"任务：{task}")
    print()
    print(f"业务价值：{bv}/5")
    print(f"知识缺口：{kg}/5")
    print(f"学习成本：{lc}/5 (1=最低)")
    print()
    print(f"优先级分数：{score:.2f}")
    print(f"优先级等级：{level}")
    print()
    
    log_priority(task, bv, kg, lc, score)
    print(f"✅ 评分已记录到：{PRIORITY_LOG}")

if __name__ == "__main__":
    main()
