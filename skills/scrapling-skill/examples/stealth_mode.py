#!/usr/bin/env python3
"""Scrapling 隐身模式示例 - 绕过 Cloudflare"""

from scrapling.fetchers import StealthyFetcher

# 隐身模式请求 (自动解决 Cloudflare)
page = StealthyFetcher.fetch('https://nopecha.com/demo/cloudflare')
links = page.css('#padded_content a').getall()

print(f"找到 {len(links)} 个链接:")
for i, link in enumerate(links[:5], 1):
    print(f"{i}. {link}")
