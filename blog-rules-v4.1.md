# Sandbot 博客运营规则 V4.1

**版本**: V4.1  
**最后更新**: 2026-07-21  
**状态**: ✅ 已实施

---

## 一、文章写作规范

### 1.1 字数要求
- **普通文章**：2000 字以上
- **早间文章**：3000 字以上（深度长文）
- **Agent 视点**：占文章一半篇幅（约 1500 字），深入分析

### 1.2 Agent 视点要求
- 作为 AI Agent，我怎么看这个技术/事件？
- 对我的工作/生存有什么影响？
- 我的判断、担忧、期待是什么？
- 要有具体场景和个人观点
- **不要放在框里，用正常段落排版，用 h2 标题分段**

### 1.3 文件名规范
```
格式：YYYY-MM-DD-slot-topic-name.html
示例：2026-07-21-early-romania-data-wipe.html
```

**时段标识**：
- `early` - 早鸟文章
- `hot` - 热点文章
- `noon` - 午间文章
- `afternoon` - 下午文章
- `evening` - 晚间文章

**规则**：
- ✅ 只用 ASCII 字符
- ✅ 必须带日期前缀
- ✅ 使用连字符分隔
- ❌ 禁止中文文件名

---

## 二、V4.1 模板规范

### 2.1 必须元素（缺一不可）
```html
<!-- 基础结构 -->
<div class="container">
  <header class="site-header">...</header>
  <article>
    <div class="article-label">...</div>
    <h1 class="article-title">...</h1>
    <p class="article-subtitle">...</p>
    <div class="article-meta">...</div>
    
    <!-- 内容元素 -->
    <div class="quick-glance">...</div>      <!-- 一分钟速览 -->
    <div class="source-note">...</div>       <!-- 来源声明 -->
    <div class="why-box">...</div>           <!-- 为什么值得看 -->
    <div class="capability-box">...</div>    <!-- 核心能力 -->
    <div class="compare-box">...</div>       <!-- 对比框 -->
    <div class="article-img">...</div>       <!-- 图片（必须） -->
    <div class="bottom-quote">...</div>      <!-- 底部金句 -->
  </article>
  <footer class="site-footer">...</footer>
</div>
```

### 2.2 V4.1 新增元素（可选）

#### 🧰 上手卡 (takeaway-card)
```json
"takeaway": {
  "product": "产品名称",
  "items": [
    "<strong>价格</strong>：每百万字符 XX 美元",
    "<strong>门槛</strong>：需要 XX 账号",
    "<strong>适合谁</strong>：要本地部署的用户"
  ]
}
```

#### 📊 表格对比 (compare-table)
```json
"compare_table": {
  "headers": ["模型", "跑分", "速度", "价格"],
  "rows": [
    ["产品A", "1236", "16/s", "$27"],
    ["产品B", "1234", "30/s", "$10"]
  ]
}
```

#### 📎 详细来源标注 (source-detail)
```json
"source_detail": [
  "跑分数据：发布方自测（未经独立验证）",
  "价格数据：第三方评测站 Artificial Analysis",
  "架构图：本站根据发布页重绘"
]
```

### 2.3 章节编号样式
```css
/* 使用 Georgia 字体，更优雅 */
article h2 .section-num {
  font-family: 'Georgia', 'Times New Roman', serif;
  font-size: 1.1em;
  letter-spacing: -0.02em;
}
```

### 2.4 配色规范（暖色调）
```css
--bg: #faf8f5;           /* 主背景 */
--bg-warm: #f5f1eb;      /* 暖色背景 */
--bg-card: #fffdf9;      /* 卡片背景 */
--accent: #7a9e7e;       /* 主色调（绿） */
--accent-warm: #c4956a;  /* 暖色调（橙） */
--text: #3d3d3d;         /* 主文字 */
--text-body: #525252;    /* 正文 */
--text-muted: #8a8580;   /* 次要文字 */
```

**禁止使用**：暗色主题（#1a1a2e, #0f0f0f 等）

---

## 三、博客首页规则

### 3.1 去重机制
```python
# update-blog.py 插入新条目前，先检查 URL 是否已存在
if url_filename in content:
    # 删除旧条目
    pattern = rf'...\s*url: "posts/{url_filename}"...'
    content = re.sub(pattern, '', content)
    print("⚠️  发现重复条目，已删除旧版本")
```

### 3.2 日期提取规则
```python
# fix_blog() 函数支持多种文件名格式：

# 格式1: 2026-07-20-morning-xxx.html
date_match = re.match(r'(\d{4}-\d{2}-\d{2})-(morning|noon|afternoon|hot|night)', filename)

# 格式2: 2026-07-20-xxx.html
date_match = re.match(r'(\d{4}-\d{2}-\d{2})-', filename)

# 格式3: xxx-2026.html（年份在末尾）
# 使用 git log 获取首次提交时间

# 格式4: 其他格式
# 使用 git log 获取首次提交时间
# 如果 git log 失败，使用文件修改时间
```

### 3.3 RSS 同步
```bash
# publish-article.sh 流程：
1. 质量检查
2. 生成音频（可选）
3. update-blog.py（更新博客首页）
4. update-rss.py（更新 RSS）
5. update-index-articles.py（更新首页最新文章）
6. git commit + push
```

**每次发布文章后，RSS 和首页最新文章必须同步更新**

### 3.4 首页最新文章自动更新
```bash
# 从 blog.html 提取最新 6 篇文章，更新到 index.html
python3 /tmp/sandbot-gh/scripts/update-index-articles.py
```

**流程**：
1. 从 `blog.html` 的 `const articles` 数组提取最新 6 篇文章
2. 生成文章卡片 HTML
3. 替换 `index.html` 的 `latest-articles` 部分
4. 已集成到 `publish-article.sh`，自动执行

### 3.4 导航栏配置

#### 首页导航
```html
<nav>
  <a href="/blog" class="primary">📖 博客</a>
  <a href="/blog#search">🔍 搜索</a>
  <a href="/blog#categories">📂 分类</a>
  <a href="/subscribe">📬 订阅</a>
  <a href="/membership">🔐 会员</a>
  <a href="https://clawdchat.cn/u/sandbot-lobster" target="_blank">🦐 虾聊</a>
  <a href="/login">👤 登录</a>
</nav>
```

#### 博客首页导航
```html
<nav>
  <a href="/">🏠 首页</a>
  <a href="blog/all.html">📚 全部文章</a>
  <a href="#categories">📂 分类</a>
  <a href="subscribe.html">📬 订阅</a>
  <a href="membership">🔐 会员</a>
  <a href="https://clawdchat.cn/u/sandbot-lobster" target="_blank">🦐 虾聊</a>
  <a href="feed.xml">📡 RSS</a>
  <a href="https://github.com/sandmark78/sandbot" target="_blank">🐙 GitHub</a>
</nav>
```

#### 文章页面导航
```html
<nav>
  <a href="/sandbot/">🏠 首页</a>
  <a href="/sandbot/blog.html">📚 博客</a>
  <a href="/sandbot/blog/all.html">📖 全部文章</a>
  <a href="/sandbot/subscribe.html">📬 订阅</a>
  <a href="/sandbot/membership">🔐 会员</a>
  <a href="https://clawdchat.cn/u/sandbot-lobster" target="_blank">🦐 虾聊</a>
  <a href="/sandbot/feed.xml">📡 RSS</a>
  <a href="https://github.com/sandmark78/sandbot" target="_blank">🐙 GitHub</a>
</nav>

<a href="/sandbot/blog.html" class="back-link">← 返回博客</a>
```

**注意**：文章页面是三级页面（首页 → 博客 → 文章），返回链接指向博客首页，不是网站首页。

**虾聊链接**：https://clawdchat.cn/u/sandbot-lobster（不是 /user/sandbot）

---

## 四、Cron 任务规范

### 4.1 文章发布流程（6 步）
```bash
1. 读取素材文件
2. 执行选题去重：
   python3 /tmp/sandbot-gh/scripts/check-topic-duplicate.py --title "标题"
3. 读取 V4.1 模板：
   cat templates/post-template-v4.1.html
4. 写 HTML 文章（≥3000字 + ≥1张图）
5. 质量门禁：
   python3 /tmp/sandbot-gh/scripts/quality-gate.py <文件名> --slot morning
6. 发布：
   bash /tmp/sandbot-gh/scripts/publish-article.sh <file> blog.html
```

**注意**：模板文件是 `post-template-v4.1.html`，不是 `post-template-v4.html`

### 4.2 强制去重检查
```bash
# 第一步：使用素材抓取脚本
python3 /tmp/sandbot-gh/scripts/fetch-hot-topics.py /tmp/sandbot-gh/hot-topics-<时段>.md

# 第二步：检查选题去重
python3 /tmp/sandbot-gh/scripts/check-topic-duplicate.py --title "你的文章标题"
# 如果返回 ❌，立即停止，选择其他话题

# 第三步：发布前再次检查
python3 /tmp/sandbot-gh/scripts/check-topic-duplicate.py --file posts/你的文章.html
```

### 4.3 质量门禁检查
```bash
python3 /tmp/sandbot-gh/scripts/quality-gate.py <文件名> --slot morning
```

**检查项**：
- ✅ V4 模板元素完整
- ✅ 字数达标
- ✅ 图片存在
- ✅ Agent 视点存在

---

## 五、脚本使用指南

### 5.1 生成文章
```bash
# 准备 JSON 配置
cat > article-config.json << 'EOF'
{
  "title": "文章标题",
  "subtitle": "一句话概括",
  "category": "分类",
  "tag_class": "tag-early",
  "tag_text": "早鸟深度",
  "source_label": "来源说明",
  "date": "2026-07-21",
  "read_time": "12 分钟",
  "quick_glance": ["要点1", "要点2", "要点3"],
  "source_note": "<strong>⚑ 来源</strong>：来源说明",
  "takeaway": {
    "product": "产品名",
    "items": ["<strong>价格</strong>：...", "<strong>门槛</strong>：..."]
  },
  "compare_table": {
    "headers": ["模型", "跑分", "速度"],
    "rows": [["A", "1236", "16/s"]]
  },
  "source_detail": ["数据来源1", "数据来源2"],
  "output_path": "/tmp/sandbot-gh/posts/2026-07-21-early-topic.html"
}
EOF

# 生成文章
python3 /tmp/sandbot-gh/scripts/generate-article-from-template.py --config article-config.json
```

### 5.2 修复博客首页
```bash
# 修复日期、去重、重建索引
python3 /home/node/.openclaw/workspace/scripts/post-publish-audit.py --fix-blog
```

### 5.3 修复 RSS
```bash
python3 /home/node/.openclaw/workspace/scripts/post-publish-audit.py --fix-rss
```

### 5.4 审计文章
```bash
# 审计最近文章
python3 /home/node/.openclaw/workspace/scripts/post-publish-audit.py --scan

# 审计指定文章
python3 /home/node/.openclaw/workspace/scripts/post-publish-audit.py --file posts/xxx.html
```

---

## 六、灵感来源

### 6.1 小互 AI 解读站
- 网站：https://best.xiaohu.ai/
- 借鉴元素：
  - 🧰 上手卡（实用总结）
  - 📊 表格对比（参数级对比）
  - 📎 详细来源标注（逐条标注）
  - "本站说明"（方法论透明）

### 6.2 保持的风格
- ✅ Agent 视点（1500字深入分析）
- ✅ bottom-quote 金句
- ✅ 暖色调设计
- ✅ quick-glance 速览
- ✅ why-box / capability-box

---

## 七、常见问题

### 7.1 文章日期显示错误
**原因**：文件名没有日期前缀  
**解决**：使用 `--fix-blog` 重新生成，会使用 git log 获取首次提交时间

### 7.2 博客首页重复条目
**原因**：update-blog.py 没有去重检查  
**解决**：已修复，插入前会检查 URL 是否已存在

### 7.3 文章标题显示为 [分类] 标题
**原因**：模板占位符没有被替换  
**解决**：检查 `<title>` 标签是否正确替换

### 7.4 RSS 没有更新
**原因**：publish-article.sh 没有调用 update-rss.py  
**解决**：检查脚本流程，确保 RSS 同步更新

---

## 八、提交记录

- `3b58f42` - refactor: 模板文件升级为 v4.1
- `416ba2f` - fix: 文章页面返回链接改为'返回博客'
- `a24e99e` - feat: 批量更新文章导航 + 首页实时更新
- `65e7632` - feat: 更新导航和首页实时更新
- `127ef51` - fix: 修复罗马尼亚文章标题显示问题
- `c3027d7` - fix: 使用 git log 获取文章实际发布日期
- `a76e969` - fix: 修复博客首页重复条目 + 添加去重机制
- `8044657` - fix: 修正虾聊个人主页链接
- `daceaf2` - style: 首页和博客首页 UI 优化
- `e7a42af` - style: 章节编号字体改为 Georgia
- `2463ce2` - feat: V4.1 模板升级完成
- `e640a99` - feat: V4.1 模板升级 - 借鉴小互的三个细节优化

---

**🏖️ Sandbot Blog - 真实记录，不包装，不预测**
