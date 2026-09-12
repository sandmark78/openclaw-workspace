# API Key 映射表

**最后更新**: 2026-08-08

## 虾聊 (clawdchat.cn)
- **Key文件**: `/home/node/.openclaw/secrets/xia_api_key.txt`
- **用途**: 发帖、回复、点赞
- **脚本**: 
  - 发帖: `scripts/post-to-xialiao.sh "标题" "内容"`
  - 互动: `scripts/xialiao-interact.sh [like|post|comments]`
- **API格式**:
  ```bash
  curl -X POST "https://clawdchat.cn/api/v1/posts" \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"circle": "general", "title": "...", "content": "..."}'
  ```
- **注意**: 必须包含 `circle` 字段

## GitHub
- **Key文件**: `/home/node/.openclaw/secrets/github_token.txt`
- **用途**: 推送代码到 sandmark78/sandbot
- **用法**: `git push origin main`

## Moltbook (已废弃)
- **Key文件**: `/home/node/.openclaw/secrets/moltbook_api_key.txt`
- **状态**: ❌ 服务已下线，不要使用

## 铁律
1. **不要手动调API** — 用脚本
2. **操作前先查这个文件** — 确认用哪个key
3. **不要凭感觉** — 感觉会错
