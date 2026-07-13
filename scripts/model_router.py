#!/usr/bin/env python3
"""
模型路由器 - V6.1 联邦智能专用

借鉴 ClawRouter 成本优化理念
不替换现有模型配置，添加智能路由层

根据任务复杂度选择模型:
- SIMPLE: qwen3.5-turbo (便宜)
- MEDIUM: qwen3.5-plus (默认)
- COMPLEX: qwen-max (高质量)

使用:
python3 model_router.py <task_description>
"""

import os
import sys
import json
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
ROUTER_LOG = WORKSPACE / "memory" / "model_router.jsonl"

# 模型配置
MODELS = {
    "turbo": {
        "name": "qwen3.5-turbo",
        "cost_per_million": 0.5,  # 假设价格
        "best_for": ["简单问答", "文本处理", "日常对话"],
        "context_window": 32000
    },
    "plus": {
        "name": "qwen3.5-plus",
        "cost_per_million": 2.0,
        "best_for": ["代码生成", "复杂分析", "多步骤任务"],
        "context_window": 1000000
    },
    "max": {
        "name": "qwen-max",
        "cost_per_million": 10.0,
        "best_for": ["深度研究", "创意写作", "关键决策"],
        "context_window": 1000000
    }
}

# 任务复杂度关键词
COMPLEXITY_KEYWORDS = {
    "simple": ["问候", "简单", "查询", "查看", "列表", "统计"],
    "medium": ["分析", "编写", "创建", "修改", "优化", "调试"],
    "complex": ["研究", "设计", "架构", "策略", "深度", "完整"]
}

def assess_complexity(task_description):
    """评估任务复杂度"""
    score = 0
    task_lower = task_description.lower()
    
    for level, keywords in COMPLEXITY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in task_lower:
                if level == "simple":
                    score += 1
                elif level == "medium":
                    score += 2
                elif level == "complex":
                    score += 3
    
    # 根据分数判断复杂度
    if score <= 2:
        return "turbo"
    elif score <= 5:
        return "plus"
    else:
        return "max"

def select_model(task_description, budget_constraint=None):
    """
    选择最合适的模型
    
    Args:
        task_description: 任务描述
        budget_constraint: 预算限制 (可选)
    
    Returns:
        dict: 选中的模型配置
    """
    # 评估复杂度
    model_tier = assess_complexity(task_description)
    
    # 考虑预算限制
    if budget_constraint == "eco":
        return MODELS["turbo"]
    elif budget_constraint == "premium":
        return MODELS["max"]
    else:
        return MODELS[model_tier]

def log_routing(task, selected_model, cost_estimate):
    """记录路由决策"""
    entry = {
        "task": task,
        "selected_model": selected_model["name"],
        "cost_estimate": cost_estimate,
        "timestamp": __import__('datetime').datetime.now().isoformat()
    }
    
    with open(ROUTER_LOG, 'a') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def show_stats():
    """显示路由统计"""
    if not ROUTER_LOG.exists():
        print("📊 暂无路由记录")
        return
    
    with open(ROUTER_LOG, 'r') as f:
        logs = [json.loads(line) for line in f]
    
    # 统计
    model_counts = {}
    total_cost = 0
    
    for log in logs:
        model = log["selected_model"]
        model_counts[model] = model_counts.get(model, 0) + 1
        total_cost += log.get("cost_estimate", 0)
    
    print("📊 路由统计")
    print("=" * 50)
    print(f"总调用次数：{len(logs)}")
    print(f"预估总成本：${total_cost:.2f}")
    print()
    print("模型分布:")
    for model, count in model_counts.items():
        percentage = (count / len(logs)) * 100
        print(f"  {model}: {count} 次 ({percentage:.1f}%)")
    
    # 成本对比
    if logs:
        avg_cost = total_cost / len(logs)
        print(f"\n平均每次成本：${avg_cost:.4f}")
        print(f"相比全部使用 max 模型：节省 ${(10.0 - avg_cost) * len(logs):.2f}")

def main():
    if len(sys.argv) < 2:
        print("🤖 模型路由器 - V6.1 联邦智能")
        print()
        print("用法：python3 model_router.py [command] [args]")
        print()
        print("命令:")
        print("  route <task>     - 路由任务到合适模型")
        print("  stats            - 显示路由统计")
        print("  models           - 显示可用模型")
        print("  test <task>      - 测试路由决策")
        print()
        print("示例:")
        print("  python3 model_router.py route '编写一个简单脚本'")
        print("  python3 model_router.py test '深度研究 OpenClaw 生态'")
        return
    
    command = sys.argv[1]
    
    if command == "route":
        task = sys.argv[2] if len(sys.argv) > 2 else "默认任务"
        budget = sys.argv[3] if len(sys.argv) > 3 else None
        
        model = select_model(task, budget)
        print(f"✅ 任务：{task[:50]}...")
        print(f"🎯 选择模型：{model['name']}")
        print(f"💰 预估成本：${model['cost_per_million']}/M tokens")
        print(f"📝 适用场景：{', '.join(model['best_for'])}")
        
        log_routing(task, model, model['cost_per_million'] * 0.001)  # 假设 1K tokens
        
    elif command == "stats":
        show_stats()
        
    elif command == "models":
        print("📦 可用模型")
        print("=" * 50)
        for tier, config in MODELS.items():
            print(f"\n{tier.upper()}: {config['name']}")
            print(f"  成本：${config['cost_per_million']}/M tokens")
            print(f"  上下文：{config['context_window']:,} tokens")
            print(f"  适用：{', '.join(config['best_for'])}")
    
    elif command == "test":
        task = sys.argv[2] if len(sys.argv) > 2 else "测试任务"
        
        print(f"🧪 测试任务：{task}")
        print()
        
        # 显示不同预算下的选择
        for budget in [None, "eco", "premium"]:
            model = select_model(task, budget)
            budget_label = budget if budget else "auto"
            print(f"{budget_label:8} → {model['name']} (${model['cost_per_million']}/M)")
    
    else:
        print(f"❌ 未知命令：{command}")

if __name__ == "__main__":
    main()
