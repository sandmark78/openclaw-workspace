# Brave API 配置指南

**状态**: ⚠️ 需配置  
**影响**: 无法使用 web_search 工具

---

## 获取 API Key

1. 访问 https://brave.com/search/api/
2. 注册账号
3. 创建 API key (免费 1000 次/月)
4. 复制 API key

---

## 配置方法

### 方法 1: openclaw configure
```bash
openclaw configure --section web
# 输入 Brave API key
```

### 方法 2: 环境变量
```bash
export BRAVE_API_KEY="your-api-key-here"
```

### 方法 3: 直接修改配置
```json
// ~/.openclaw/openclaw.json
{
  "web": {
    "braveApiKey": "your-api-key-here"
  }
}
```

---

## 验证配置

```bash
# 测试 web_search
web_search "test query" --count 3
```

---

## 替代方案

如不配置 Brave API:
- 使用 `web_fetch` 直接抓取网页
- 手动搜索趋势
- 依赖内部知识库

---

**优先级**: P1 (非阻塞，可替代)
