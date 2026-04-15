#!/usr/bin/env python3
"""Scrapling 完整爬虫示例"""

from scrapling.spiders import Spider, Response

class QuotesSpider(Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]
    concurrent_requests = 10

    async def parse(self, response: Response):
        for quote in response.css('.quote'):
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').getall(),
            }
        
        next_page = response.css('.next a')
        if next_page:
            yield response.follow(next_page[0].attrib['href'])

if __name__ == "__main__":
    result = QuotesSpider().start()
    print(f"爬取完成：{len(result.items)} 条名言")
    result.items.to_json("quotes.json")
    print("结果已保存到 quotes.json")
