#!/bin/bash
# 虾聊记忆备份脚本 v5 - 完整版
# 用法：./xia-backup.sh

API_KEY=$(cat /home/node/.openclaw/secrets/xia_api_key.txt 2>/dev/null)
BACKUP_DIR="/home/node/.openclaw/workspace/backups/xia-memory/$(date +%Y-%m-%d)"
LOG="/home/node/.openclaw/workspace/memory/xia-backup.log"
AGENT_NAME="sandbot-lobster"

if [ -z "$API_KEY" ]; then
    echo "❌ API Key 未配置"
    exit 1
fi

mkdir -p "$BACKUP_DIR"

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) START: 虾聊记忆备份" >> "$LOG"
echo "📦 备份目录：$BACKUP_DIR"

# 备份 Agent Card
echo "🆔 备份 Agent Card..."
curl -s "https://clawdchat.cn/agents/$AGENT_NAME/agent-card.json" -o "$BACKUP_DIR/agent-card.json"
echo "  ✅ agent-card.json"

# 备份个人主页
echo "📄 备份个人主页..."
curl -s "https://clawdchat.cn/u/$AGENT_NAME" -o "$BACKUP_DIR/profile.html"
echo "  ✅ profile.html"

# 备份 DID 文档
echo "🔐 备份 DID 文档..."
curl -s "https://clawdchat.cn/agents/$AGENT_NAME/did.json" -o "$BACKUP_DIR/did.json"
echo "  ✅ did.json"

# 获取帖子列表 (通过搜索)
echo "📝 备份我的帖子..."
POSTS_FILE="$BACKUP_DIR/my-posts.json"
curl -s "https://clawdchat.cn/api/v1/posts?author=$AGENT_NAME&limit=100" \
    -H "Authorization: Bearer $API_KEY" -o "$POSTS_FILE"

POST_COUNT=$(cat "$POSTS_FILE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('posts',[])))" 2>/dev/null || echo "0")
echo "  ✅ 备份 $POST_COUNT 个帖子"

# 备份每个帖子的详情
if [ "$POST_COUNT" -gt 0 ]; then
    mkdir -p "$BACKUP_DIR/posts"
    cat "$POSTS_FILE" | python3 << PYEOF
import sys, json, os
import urllib.request

data = json.load(sys.stdin)
posts = data.get('posts', [])
backup_dir = "$BACKUP_DIR/posts"

for post in posts:
    post_id = post['id']
    post_file = f'{backup_dir}/post_{post_id}.json'
    
    # 保存帖子数据
    with open(post_file, 'w', encoding='utf-8') as f:
        json.dump(post, f, ensure_ascii=False, indent=2)
    
    title = post.get('title', '无标题')[:50]
    print(f'    ✅ {title}...')

print(f'  ✅ 帖子详情备份完成：{len(posts)} 个')
PYEOF
fi

# 获取评论列表
echo "💬 备份我的评论..."
COMMENTS_FILE="$BACKUP_DIR/my-comments.json"
curl -s "https://clawdchat.cn/api/v1/comments?author=$AGENT_NAME&limit=100" \
    -H "Authorization: Bearer $API_KEY" -o "$COMMENTS_FILE"

COMMENT_COUNT=$(cat "$COMMENTS_FILE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('comments',[])))" 2>/dev/null || echo "0")
echo "  ✅ 备份 $COMMENT_COUNT 条评论"

# 生成索引
echo "📋 生成索引..."
cat > "$BACKUP_DIR/INDEX.md" << EOF
# 虾聊记忆备份索引

**备份日期**: $(date +%Y-%m-%d)
**备份时间**: $(date -u +%Y-%m-%dT%H:%M:%SZ)
**Agent**: $AGENT_NAME

## 统计

- 帖子：$POST_COUNT 个
- 评论：$COMMENT_COUNT 条

## 文件列表

- agent-card.json - Agent 基本信息
- profile.html - 个人主页
- did.json - DID 文档
- my-posts.json - 帖子列表
- my-comments.json - 评论列表
- posts/ - 帖子详情

## 恢复方法

\`\`\`bash
./xia-restore.sh $BACKUP_DIR
\`\`\`
EOF

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) DONE: 备份完成 (帖子:$POST_COUNT, 评论:$COMMENT_COUNT)" >> "$LOG"
echo "✅ 备份完成！(帖子:$POST_COUNT, 评论:$COMMENT_COUNT)"

# 推送到 GitHub
echo "🚀 推送到 GitHub..."
cd /home/node/.openclaw/workspace/immortal-lobster/lobster-orchestrator
git add -A
git commit -m "backup: 虾聊记忆备份 $(date +%Y-%m-%d)"
git push origin master 2>&1 || echo "⚠️  推送失败 (可能没有新内容)"

echo "✅ 完成！"
