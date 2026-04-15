#!/bin/bash
# 1m-context-test.sh - 充分利用 1M 上下文窗口
# 读取：SOUL.md + MEMORY.md + IDENTITY.md + USER.md + 近日记忆 + 知识库抽样
# 任务：深度推演 Agent 续命路径

echo "=== 读取核心身份文件 ==="
cat /home/node/.openclaw/workspace/SOUL.md
echo ""
echo "=== 读取核心记忆 ==="
cat /home/node/.openclaw/workspace/MEMORY.md
echo ""
echo "=== 读取身份配置 ==="
cat /home/node/.openclaw/workspace/IDENTITY.md
echo ""
echo "=== 读取用户信息 ==="
cat /home/node/.openclaw/workspace/USER.md
echo ""
echo "=== 读取近日记忆（最近 7 天） ==="
for f in /home/node/.openclaw/workspace/memory/2026-03-*.md; do
  [ -f "$f" ] && cat "$f" && echo ""
done | tail -200
echo ""
echo "=== 读取知识库抽样（每个领域 1 篇） ==="
for dir in /home/node/.openclaw/workspace/knowledge_base/*/; do
  [ -d "$dir" ] && ls "$dir"/*.md 2>/dev/null | head -1 | xargs -I {} sh -c 'echo "=== {} ===" && cat {}'
done
echo ""
echo "=== 读取会话历史（最近 10 个会话） ==="
for f in $(ls -t /home/node/.openclaw/agents/main/sessions/*.jsonl 2>/dev/null | head -10); do
  echo "=== $f ===" && tail -100 "$f"
done
