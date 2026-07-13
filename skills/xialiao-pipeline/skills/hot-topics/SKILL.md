# Hot Topics - 热点选题采集

## 功能
从 HN、GitHub Trending、Latent Space 等前沿信息源采集当日热点选题。

## 输出
10-15 个选题，每个包含：
- 标题
- 来源
- 热度（分数/评论数）
- 为什么值得写（独特角度）

## 触发词
「采集热点」「找选题」「今日热点」

## 执行步骤
1. 用 web_fetch 抓取 https://news.ycombinator.com/
2. 用 web_fetch 抓取 https://github.com/trending
3. 用 web_fetch 抓取 https://www.latent.space/
4. 提取 Top 10-15 热点
5. 为每个热点写一个"为什么值得写"的独特角度
6. 输出结构化选题列表
