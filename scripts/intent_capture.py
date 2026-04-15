#!/usr/bin/env python3
"""
主动意图捕捉 - V6.1 联邦智能专用

借鉴 memU 主动意图捕捉理念
监控用户输入，预测下一步需求
主动准备上下文和资源

使用:
python3 intent_capture.py <input_text>
"""

import os
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
INTENT_LOG = WORKSPACE / "memory" / "intent_capture.jsonl"

# 意图模式库
INTENT_PATTERNS = {
    "research": {
        "keywords": ["研究", "分析", "调研", "探索", "学习", "了解"],
        "actions": ["准备相关资料", "搜索类似项目", "整理知识框架"],
        "resources": ["knowledge_base/", "memory/search_cache_*.md"]
    },
    "coding": {
        "keywords": ["代码", "脚本", "实现", "开发", "编写", "创建"],
        "actions": ["准备代码模板", "检查依赖", "创建文件结构"],
        "resources": ["scripts/", "skills/"]
    },
    "writing": {
        "keywords": ["文档", "文章", "教程", "报告", "总结", "记录"],
        "actions": ["准备文档模板", "整理大纲", "收集参考资料"],
        "resources": ["knowledge_base/", "memory/*.md"]
    },
    "deploy": {
        "keywords": ["部署", "发布", "提交", "推送", "上线"],
        "actions": ["检查配置文件", "准备部署脚本", "验证环境"],
        "resources": ["scripts/*.sh", "clawhub-releases/"]
    },
    "optimize": {
        "keywords": ["优化", "改进", "增强", "提升", "效率"],
        "actions": ["分析当前状态", "识别瓶颈", "准备优化方案"],
        "resources": ["memory/*summary*.md", "growth/"]
    }
}

def detect_intent(input_text):
    """检测用户意图"""
    scores = {}
    input_lower = input_text.lower()
    
    for intent, config in INTENT_PATTERNS.items():
        score = 0
        for keyword in config["keywords"]:
            if keyword in input_lower:
                score += 1
        scores[intent] = score
    
    # 返回最高分意图
    if max(scores.values()) > 0:
        best_intent = max(scores, key=scores.get)
        return best_intent, scores[best_intent]
    else:
        return "general", 0

def predict_next_steps(intent):
    """预测下一步需求"""
    if intent in INTENT_PATTERNS:
        return INTENT_PATTERNS[intent]["actions"]
    else:
        return ["准备通用资源", "等待进一步指令"]

def prepare_resources(intent):
    """准备相关资源"""
    resources = []
    if intent in INTENT_PATTERNS:
        for resource_pattern in INTENT_PATTERNS[intent]["resources"]:
            # 检查资源是否存在
            import glob
            matches = glob.glob(str(WORKSPACE / resource_pattern))
            resources.extend(matches[:5])  # 最多 5 个
    return resources

def log_intent(input_text, intent, confidence, predictions, resources):
    """记录意图捕捉"""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "input": input_text[:200],
        "intent": intent,
        "confidence": confidence,
        "predictions": predictions,
        "resources": resources
    }
    
    with open(INTENT_LOG, 'a') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("🔮 主动意图捕捉 - V6.1 联邦智能")
        print()
        print("用法：python3 intent_capture.py <input_text>")
        print()
        print("示例:")
        print("  python3 intent_capture.py '帮我研究 OpenClaw 生态'")
        print("  python3 intent_capture.py '创建一个 Python 脚本'")
        print("  python3 intent_capture.py '写一篇文档'")
        return
    
    input_text = " ".join(sys.argv[1:])
    
    # 检测意图
    intent, confidence = detect_intent(input_text)
    
    # 预测下一步
    predictions = predict_next_steps(intent)
    
    # 准备资源
    resources = prepare_resources(intent)
    
    # 记录
    log_intent(input_text, intent, confidence, predictions, resources)
    
    # 输出
    print(f"🔮 意图分析")
    print(f"输入：{input_text[:50]}...")
    print(f"意图：{intent} (置信度：{confidence})")
    print(f"预测下一步:")
    for i, action in enumerate(predictions, 1):
        print(f"  {i}. {action}")
    print(f"准备资源:")
    for resource in resources[:3]:
        print(f"  - {resource}")
    print()
    print(f"✅ 意图已记录到：{INTENT_LOG}")

if __name__ == "__main__":
    main()
