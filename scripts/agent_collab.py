#!/usr/bin/env python3
"""
多 Agent 协作工作流 - V6.1 联邦智能专用

功能:
1. 任务自动分配 - 根据任务类型分配给对应子 Agent
2. 结果自动审核 - Auditor 自动审查输出质量
3. 跨 Agent 知识共享 - 共享记忆和知识库
4. 协作工作流编排 - 复杂任务多 Agent 协作

使用:
python3 agent_collab.py [assign|review|share|orchestrate]
"""

import os
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
SUBAGENTS_DIR = WORKSPACE / "subagents"
COLLAB_LOG = WORKSPACE / "memory" / "agent_collab.jsonl"

# 7 子 Agent 专长映射
AGENT_SPECIALTIES = {
    "techbot": {
        "keywords": ["教程", "代码", "技术", "实现", "开发"],
        "roi_target": 3.2,
        "description": "技术教程开发"
    },
    "financebot": {
        "keywords": ["收益", "财务", "ROI", "变现", "赚钱"],
        "roi_target": 2.1,
        "description": "金融收益分析"
    },
    "creativebot": {
        "keywords": ["创意", "内容", "营销", "文案", "设计"],
        "roi_target": 2.0,
        "description": "创意内容生成"
    },
    "autobot": {
        "keywords": ["抓取", "自动化", "数据", "爬虫", "API"],
        "roi_target": 2.5,
        "description": "数据抓取自动化"
    },
    "researchbot": {
        "keywords": ["研究", "分析", "调研", "市场", "竞品"],
        "roi_target": 2.5,
        "description": "深度研究分析"
    },
    "auditor": {
        "keywords": ["审核", "质量", "验证", "检查", "审计"],
        "roi_target": 3.0,
        "description": "质量保障审计"
    },
    "devopsbot": {
        "keywords": ["部署", "运维", "CI/CD", "服务器", "配置"],
        "roi_target": 2.0,
        "description": "工程化运维"
    }
}

def assign_task(task_description):
    """根据任务描述自动分配给最合适的子 Agent"""
    print(f"📋 任务分配：{task_description[:50]}...")
    
    best_match = None
    best_score = 0
    
    for agent_id, info in AGENT_SPECIALTIES.items():
        score = 0
        for keyword in info["keywords"]:
            if keyword.lower() in task_description.lower():
                score += 1
        
        if score > best_score:
            best_score = score
            best_match = agent_id
    
    if best_match:
        print(f"✅ 分配给：{best_match} ({AGENT_SPECIALTIES[best_match]['description']})")
        print(f"   匹配度：{best_score} 个关键词")
        
        # 记录分配
        log_collab({
            "type": "assignment",
            "task": task_description,
            "assigned_to": best_match,
            "score": best_score,
            "timestamp": datetime.now().isoformat()
        })
        
        return best_match
    else:
        print("⚠️ 未找到匹配，分配给 TechBot (默认)")
        return "techbot"

def review_output(agent_id, output):
    """Auditor 审核输出质量"""
    print(f"🔍 审核 {agent_id} 的输出...")
    
    # 简单质量检查
    issues = []
    
    # 检查 1: 输出长度
    if len(output) < 50:
        issues.append("输出过短 (<50 字符)")
    
    # 检查 2: 是否包含具体文件路径
    if "/" not in output and "✅" not in output:
        issues.append("缺少文件路径或交付证明")
    
    # 检查 3: 是否包含可验证信息
    if "ls" not in output.lower() and "cat" not in output.lower():
        issues.append("缺少验证命令")
    
    if issues:
        print(f"❌ 发现 {len(issues)} 个问题:")
        for issue in issues:
            print(f"   - {issue}")
        
        log_collab({
            "type": "review",
            "agent": agent_id,
            "status": "failed",
            "issues": issues,
            "timestamp": datetime.now().isoformat()
        })
        
        return False
    else:
        print("✅ 审核通过")
        
        log_collab({
            "type": "review",
            "agent": agent_id,
            "status": "passed",
            "timestamp": datetime.now().isoformat()
        })
        
        return True

def share_knowledge(from_agent, knowledge):
    """跨 Agent 知识共享"""
    print(f"📚 {from_agent} 分享知识...")
    
    # 写入共享知识库
    shared_kb = WORKSPACE / "knowledge_base" / "shared"
    shared_kb.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    kb_file = shared_kb / f"{from_agent}_{timestamp}.md"
    
    with open(kb_file, 'w') as f:
        f.write(f"# 知识分享 - {from_agent}\n\n")
        f.write(f"**时间**: {datetime.now().isoformat()}\n\n")
        f.write(knowledge)
    
    print(f"✅ 知识已保存到：{kb_file}")
    
    log_collab({
        "type": "knowledge_share",
        "from": from_agent,
        "file": str(kb_file),
        "timestamp": datetime.now().isoformat()
    })
    
    return str(kb_file)

def orchestrate_workflow(complex_task):
    """编排复杂任务的多 Agent 协作"""
    print(f"🎭 编排复杂任务：{complex_task[:50]}...")
    
    # 示例工作流：教程开发
    workflow = [
        {"agent": "researchbot", "task": "市场调研和竞品分析"},
        {"agent": "techbot", "task": "技术教程内容编写"},
        {"agent": "creativebot", "task": "营销文案优化"},
        {"agent": "auditor", "task": "质量审查"},
        {"agent": "devopsbot", "task": "部署和发布"}
    ]
    
    print("📋 工作流步骤:")
    for i, step in enumerate(workflow, 1):
        print(f"  {i}. {step['agent']}: {step['task']}")
    
    log_collab({
        "type": "orchestration",
        "task": complex_task,
        "workflow": workflow,
        "timestamp": datetime.now().isoformat()
    })
    
    return workflow

def log_collab(entry):
    """记录协作日志"""
    with open(COLLAB_LOG, 'a') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("用法：python3 agent_collab.py [assign|review|share|orchestrate]")
        print("  assign <task>     - 分配任务")
        print("  review <agent>    - 审核输出")
        print("  share <agent>     - 分享知识")
        print("  orchestrate <task>- 编排工作流")
        return
    
    command = sys.argv[1]
    
    if command == "assign":
        task = sys.argv[2] if len(sys.argv) > 2 else "编写技术教程"
        assign_task(task)
    elif command == "review":
        agent = sys.argv[2] if len(sys.argv) > 2 else "techbot"
        review_output(agent, "✅ 教程已完成：/workspace/skills/test/README.md\n验证：ls -la")
    elif command == "share":
        agent = sys.argv[2] if len(sys.argv) > 2 else "techbot"
        share_knowledge(agent, "# 技术教程开发最佳实践\n\n1. 先写大纲\n2. 填充内容\n3. 添加代码示例\n4. 验证可运行")
    elif command == "orchestrate":
        task = sys.argv[2] if len(sys.argv) > 2 else "开发完整教程系列"
        orchestrate_workflow(task)
    else:
        print(f"未知命令：{command}")

if __name__ == "__main__":
    main()
