#!/usr/bin/env python3
"""Scrapling 基础请求示例"""

from scrapling.fetchers import Fetcher

# 简单请求
page = Fetcher.get('https://quotes.toscrape.com/')
quotes = page.css('.quote .text::text').getall()

print(f"找到 {len(quotes)} 条名言:")
for i, quote in enumerate(quotes[:5], 1):
    print(f"{i}. {quote}")
