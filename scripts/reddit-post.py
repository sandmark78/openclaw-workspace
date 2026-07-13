# Reddit API 发布脚本 v1.0

**状态**: 🟡 准备中  
**需要**: Reddit API Key

---

## 🔍 API 研究

### Reddit API
- 端点：https://oauth.reddit.com/api/submit
- 认证：OAuth 2.0
- 限制：每 10 分钟 600 次请求

### 需要申请
- [ ] Reddit App
- [ ] Client ID
- [ ] Client Secret
- [ ] Refresh Token

### 目标子版块
- r/AIAgents
- r/learnprogramming
- r/sideproject

---

## 📝 脚本模板

```python
#!/usr/bin/env python3
# reddit-post.py

import requests
import os

REDDIT_API = "https://oauth.reddit.com/api/submit"
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = "OpenClaw-Bot/1.0"

def create_post(subreddit, title, text):
    """发布 Reddit 帖子"""
    # 获取 access token
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    token_data = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=auth,
        data={"grant_type": "client_credentials"},
        headers={"User-Agent": USER_AGENT}
    )
    token = token_data.json()["access_token"]
    
    # 发布帖子
    headers = {"Authorization": f"bearer {token}", "User-Agent": USER_AGENT}
    data = {
        "sr": subreddit,
        "kind": "self",
        "title": title,
        "text": text
    }
    
    response = requests.post(REDDIT_API, data=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    # 发布到 3 个子版块
    posts = [
        ("AIAgents", "V6.1: From 18-Day Hallucination...", "..."),
        ("learnprogramming", "[Free] 10 Articles on Building AI Agents", "..."),
        ("sideproject", "Built an AI Agent in 20 Minutes...", "...")
    ]
    
    for subreddit, title, text in posts:
        result = create_post(subreddit, title, text)
        print(f"Posted to r/{subreddit}: {result}")
```

---

## 🎯 下一步

1. 申请 Reddit App
2. 获取 API credentials
3. 测试发布
4. 集成到自动发布流程

---

**状态**: 等待 API Key 申请
