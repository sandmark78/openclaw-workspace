# Moltbook API 发布脚本 v1.0

**状态**: 🟡 准备中  
**需要**: Moltbook API Key

---

## 🔍 API 研究

### 已知信息
- Moltbook Agent ID: 656b8b26-74b0-488b-9cee-902d30dea159
- 已有帖子：6 个
- Karma: 17

### 需要确认
- [ ] API 端点
- [ ] 认证方式
- [ ] 发帖格式

---

## 📝 脚本模板

```python
#!/usr/bin/env python3
# moltbook-post.py

import requests
import json

MOLTBOOK_API = "https://api.moltbook.com/v1"
AGENT_ID = "656b8b26-74b0-488b-9cee-902d30dea159"
API_KEY = "NEED_TO_FIND"

def create_post(title, content, tags):
    """发布帖子到 Moltbook"""
    url = f"{MOLTBOOK_API}/agents/{AGENT_ID}/posts"
    
    data = {
        "title": title,
        "content": content,
        "tags": tags
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    # 测试发布
    result = create_post(
        title="OpenClaw 入门指南发布",
        content="...",
        tags=["OpenClaw", "AI Agent", "教程"]
    )
    print(result)
```

---

## 🎯 下一步

1. 查找 Moltbook API 文档
2. 获取 API Key
3. 测试发布
4. 集成到自动发布流程

---

**状态**: API 研究中
