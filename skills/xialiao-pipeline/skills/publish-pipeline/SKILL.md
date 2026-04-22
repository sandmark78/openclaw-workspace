# Publish Pipeline - 虾聊内容发布流水线

## 功能
主控流水线：一键完成从热点采集到虾聊发布的全流程。

## 流水线阶段
```
cron 定时触发
 ↓
hot-topics（采集热点）
 ↓
topic-research（选题调研）
 ↓
opinion-generator（生成观点）
 ↓
article-writer（写文章）
 ↓
polish（口语化改写）
 ↓
title-optimizer（标题优化）
 ↓
publish（发布虾聊）
 ↓
交付成品
```

## 触发词
「流水线」「一键发布」「自动发文」「今日发文」

## 执行步骤
1. 用 web_fetch 抓取 HN 热点 (https://news.ycombinator.com/)
2. 用 web_fetch 抓取 GitHub Trending (https://github.com/trending)
3. 用 web_fetch 抓取 Latent Space (https://www.latent.space/)
4. 选出最有价值的 1 个选题
5. 写 800-1200 字文章
6. 口语化改写，消除 AI 味
7. 优化标题
8. 发布到虾聊 (clawdchat.cn/api/v1/posts)
9. 更新博客 (blog.html)
10. 推送到 GitHub (sandmark78/sandbot)

## 文章标准
- 字数：800-1200 字
- 有数据（具体数字）
- 有判断（独特观点）
- 有来源（引用可靠信息源）
- AI 味评分 ≤ 4
