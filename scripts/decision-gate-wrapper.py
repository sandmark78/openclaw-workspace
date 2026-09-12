#!/usr/bin/env python3
"""decision-gate wrapper - 高风险操作前写决策记录"""
import sys, os
sys.path.insert(0, os.path.expanduser('~/.openclaw/workspace/skills/@vaahl-dev/decision-gate'))
from decision_gate import gate

def publish_gate(article_file):
    """发布文章前的决策门"""
    with gate(
        action_id=f"publish-{os.path.basename(article_file)}",
        decision="SEND",
        risk_band="under-10",
        evidence_classes=["content_generated", "template_used", "quality_scored"],
        reversible=True,
    ) as receipt:
        print(f"✅ 决策已记录: {receipt.action_id} (hash: {receipt.entry_hash[:12]}...)")
        return receipt

def git_push_gate(message):
    """git push前的决策门"""
    with gate(
        action_id=f"git-push-{message[:20].replace(' ','-')}",
        decision="SEND",
        risk_band="under-10",
        evidence_classes=["changes_committed", "no_secrets"],
        reversible=True,
    ) as receipt:
        print(f"✅ git push 决策已记录: {receipt.action_id}")
        return receipt

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("用法: decision-gate-wrapper.py [publish|push] <target>")
        sys.exit(1)
    action = sys.argv[1]
    target = sys.argv[2]
    if action == 'publish':
        publish_gate(target)
    elif action == 'push':
        git_push_gate(target)
