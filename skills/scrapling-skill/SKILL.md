# scrapling-skill

**功能**: 自适应网页爬虫，处理从单页请求到大规模爬取  
**版本**: 1.0.0  
**作者**: Sandbot 🏖️ (基于 D4Vinci/Scrapling)  
**来源**: https://github.com/D4Vinci/Scrapling

---

## 🎯 功能特性

### 核心能力
- ✅ **自适应解析**: 自动适应网站结构变化
- ✅ **反爬虫绕过**: 绕过 Cloudflare Turnstile 等反爬系统
- ✅ **多会话支持**: HTTP/浏览器/隐身模式统一接口
- ✅ **暂停/恢复**: 基于检查点的爬取持久化
- ✅ **并发爬取**: 可配置的并发限制和域名节流
- ✅ **流式模式**: 实时输出爬取结果

### 三种 Fetcher
| 类型 | 用途 | 特点 |
|------|------|------|
| Fetcher | HTTP 请求 | 快速，模拟浏览器 TLS 指纹 |
| StealthyFetcher | 隐身模式 | 绕过反爬，自动解决 Cloudflare |
| DynamicFetcher | 完整浏览器 | Playwright/Chrome 自动化 |

---

## 🛠️ 使用方法

### 基础使用

```python
# 安装
pip install scrapling

# 简单请求
from scrapling.fetchers import Fetcher
page = Fetcher.get('https://example.com/')
data = page.css('.product::text').getall()

# 隐身模式 (绕过 Cloudflare)
from scrapling.fetchers import StealthyFetcher
page = StealthyFetcher.fetch('https://nopecha.com/demo/cloudflare')
data = page.css('#padded_content a').getall()

# 浏览器自动化
from scrapling.fetchers import DynamicFetcher
page = DynamicFetcher.fetch('https://quotes.toscrape.com/')
data = page.css('.quote .text::text').getall()
```

### 高级使用

```python
# 会话管理
from scrapling.fetchers import FetcherSession, StealthySession

with FetcherSession(impersonate='chrome') as session:
    page1 = session.get('https://example.com/1')
    page2 = session.get('https://example.com/2')

# 隐身会话
with StealthySession(headless=True, solve_cloudflare=True) as session:
    page = session.fetch('https://protected-site.com')
    data = page.css('.content').getall()
```

### 完整爬虫

```python
from scrapling.spiders import Spider, Response

class MySpider(Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]
    concurrent_requests = 10

    async def parse(self, response: Response):
        for quote in response.css('.quote'):
            yield {
                "text": quote.css('.text::text').get(),
                "author": quote.css('.author::text').get(),
            }
        
        next_page = response.css('.next a')
        if next_page:
            yield response.follow(next_page[0].attrib['href'])

# 运行爬虫
result = MySpider().start()
print(f"Scraped {len(result.items)} quotes")
result.items.to_json("quotes.json")
```

### 暂停/恢复爬取

```python
# 启动带检查点的爬取
MySpider(crawldir="./crawl_data").start()

# 按 Ctrl+C 暂停，再次运行自动恢复
MySpider(crawldir="./crawl_data").start()
```

---

## 📋 OpenClaw 集成

### 技能命令

```bash
# 使用 Scrapling 爬取网页
scrapling-fetch <url> [options]

# 隐身模式爬取
scrapling-stealth <url> [options]

# 浏览器自动化
scrapling-dynamic <url> [options]

# 运行爬虫
scrapling-spider <spider_name> [options]
```

### 示例工作流

```python
# 1. 简单数据提取
from scrapling.fetchers import Fetcher

def scrape_products(url):
    page = Fetcher.get(url)
    products = page.css('.product').getall()
    return [{
        'name': p.css('.name::text').get(),
        'price': p.css('.price::text').get(),
    } for p in products]

# 2. 绕过反爬
from scrapling.fetchers import StealthyFetcher

def scrape_protected(url):
    page = StealthyFetcher.fetch(url, solve_cloudflare=True)
    return page.css('.content::text').getall()

# 3. 大规模爬取
from scrapling.spiders import Spider, Response

class ProductSpider(Spider):
    name = "products"
    start_urls = ["https://example.com/products"]
    concurrent_requests = 20

    async def parse(self, response: Response):
        for product in response.css('.product'):
            yield {
                'name': product.css('.name::text').get(),
                'price': product.css('.price::text').get(),
                'url': product.css('a::attr(href)').get(),
            }
```

---

## 🔧 配置选项

### Fetcher 配置

```python
from scrapling.fetchers import Fetcher

# 模拟浏览器 TLS 指纹
page = Fetcher.get('https://example.com', impersonate='chrome')

# 使用 HTTP/3
page = Fetcher.get('https://example.com', http3=True)

# 隐身请求头
page = Fetcher.get('https://example.com', stealthy_headers=True)
```

### StealthyFetcher 配置

```python
from scrapling.fetchers import StealthyFetcher

# 隐身模式，解决 Cloudflare
page = StealthyFetcher.fetch(
    'https://example.com',
    headless=True,
    solve_cloudflare=True,
    google_search=False  # 禁用 Google 搜索
)
```

### DynamicFetcher 配置

```python
from scrapling.fetchers import DynamicFetcher

# 完整浏览器自动化
page = DynamicFetcher.fetch(
    'https://example.com',
    headless=True,
    disable_resources=False,  # 加载所有资源
    network_idle=True  # 等待网络空闲
)
```

---

## 📊 性能对比

| 操作 | Scrapling | Scrapy | BeautifulSoup |
|------|-----------|--------|---------------|
| CSS 选择 | ⚡️ 快 | ⚡️ 快 | 🐌 慢 |
| JSON 序列化 | ⚡️ 10x 快 | 🐌 标准 | 🐌 标准 |
| 内存占用 | ✅ 低 | ⚠️ 中 | ⚠️ 中 |
| 反爬绕过 | ✅ 内置 | ❌ 需插件 | ❌ 不支持 |
| 自适应解析 | ✅ 内置 | ❌ 需手动 | ❌ 不支持 |

---

## 🎯 适用场景

### 适合使用 Scrapling

- ✅ 需要绕过 Cloudflare 等反爬系统
- ✅ 网站结构经常变化
- ✅ 需要大规模并发爬取
- ✅ 需要暂停/恢复长时爬取
- ✅ 需要浏览器自动化

### 不适合使用 Scrapling

- ❌ 简单静态页面 (用 Fetcher 即可)
- ❌ 已有 Scrapy 项目 (迁移成本高)
- ❌ 需要 JavaScript 渲染 (用 DynamicFetcher)

---

## 📁 文件结构

```
scrapling-skill/
├── SKILL.md              # 本文件
├── examples/
│   ├── basic_fetch.py    # 基础请求示例
│   ├── stealth_mode.py   # 隐身模式示例
│   ├── spider_example.py # 爬虫示例
│   └── pause_resume.py   # 暂停恢复示例
└── .clawhub/
    └── origin.json       # ClawHub 配置
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install scrapling
```

### 2. 测试连接

```python
from scrapling.fetchers import Fetcher
page = Fetcher.get('https://example.com/')
print(f"Title: {page.css('title::text').get()}")
```

### 3. 开始爬取

```python
from scrapling.spiders import Spider, Response

class MyFirstSpider(Spider):
    name = "my_spider"
    start_urls = ["https://quotes.toscrape.com/"]

    async def parse(self, response: Response):
        for quote in response.css('.quote'):
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
            }

MyFirstSpider().start()
```

---

## 📚 文档链接

- **官方文档**: https://scrapling.readthedocs.io
- **GitHub**: https://github.com/D4Vinci/Scrapling
- **Discord**: https://discord.gg/EMgGbDceNQ
- **PyPI**: https://pypi.org/project/scrapling/

---

## ⚠️ 注意事项

1. **遵守 robots.txt**: 爬取前检查目标网站的 robots.txt
2. **请求频率**: 设置合理的下载延迟，避免封禁
3. **数据存储**: 使用 `result.items.to_json()` 导出结果
4. **错误处理**: 添加重试逻辑和异常处理

---

## 🦞 硅基宣言

```
一个库，零妥协。
快速、自适应、可扩展。
为爬虫而生，因爬虫而强。

旅程继续。🏖️
```

---

**版本**: 1.0.0  
**创建时间**: 2026-03-04  
**状态**: ✅ 就绪
