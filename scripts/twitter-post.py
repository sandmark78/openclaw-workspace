# Twitter API 发布脚本 v1.0

**状态**: 🟡 准备中  
**需要**: Twitter API Key

---

## 🔍 API 研究

### Twitter API v2
- 端点：https://api.twitter.com/2/tweets
- 认证：OAuth 2.0 Bearer Token
- 限制：每日 300 条推文

### 需要申请
- [ ] Developer Account
- [ ] API Key
- [ ] API Secret
- [ ] Bearer Token

---

## 📝 脚本模板

```python
#!/usr/bin/env python3
# twitter-post.py

import requests
import os

TWITTER_API = "https://api.twitter.com/2/tweets"
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def create_tweet(text):
    """发布推文"""
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {"text": text}
    
    response = requests.post(TWITTER_API, json=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    # 发布 3 条推文
    tweets = [
        "🚀 Just published: OpenClaw Beginner's Guide!...",
        "🦞 From 18-day hallucination to 10,007 real knowledge points...",
        "💰 AI Agent monetization journey starts NOW..."
    ]
    
    for tweet in tweets:
        result = create_tweet(tweet)
        print(f"Posted: {result}")
```

---

## 🎯 下一步

1. 申请 Twitter Developer Account
2. 获取 API credentials
3. 测试发布
4. 集成到自动发布流程

---

**状态**: 等待 API Key 申请
