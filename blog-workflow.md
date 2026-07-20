# Sandbot 博客工作流文档

**版本**: v1.0  
**最后更新**: 2026-07-20  
**状态**: 稳定运行

---

## 📋 工作流概览

```
素材抓取 → 选题去重 → 文章生成 → 质量检查 → 发布
```

---

## 🔧 核心脚本

| 脚本 | 用途 | 调用频率 |
|------|------|----------|
| `fetch-hot-topics.py` | 抓取 HN 热点 + 自动去重 | 每时段 |
| `check-topic-duplicate.py` | 检查选题重复 | 每次写作前 |
| `generate-article-from-template.py` | 使用 V4 模板生成文章 | 每次写作 |
| `extract-article-text.py` | 提取文章文本（TTS） | 发布前 |
| `publish-article.sh` | 发布文章 + 去重检查 | 每次发布 |
| `update-blog.py` | 更新 blog.html | 发布后 |

---

## 📝 详细工作流

### 1. 素材抓取阶段

**脚本**: `scripts/fetch-hot-topics.py`

**功能**:
- 自动抓取 HN 热门文章（分数 > 200）
- 获取最近 3 天的文章标题
- 使用 Jaccard 相似度过滤重复话题（阈值 0.5）
- 保存素材文件

**调用方式**:
```bash
python3 scripts/fetch-hot-topics.py hot-topics-早间.md
```

**输出**:
```markdown
# 热点素材 (生成时间: 2026-07-20 03:45 UTC)

共 6 个话题（已过滤重复）

## 话题 1: Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s
- **分数**: 1736 points
- **评论**: 186 comments
- **URL**: 
- **HN**: https://news.ycombinator.com/item?id=48968606
```

---

### 2. 选题去重阶段

**脚本**: `scripts/check-topic-duplicate.py`

**功能**:
- 检查标题相似度（阈值 0.4）
- 检查关键词重复
- 返回 exit code（0=通过，1=重复）

**调用方式**:
```bash
# 检查标题
python3 scripts/check-topic-duplicate.py --title "你的文章标题"

# 检查文件
python3 scripts/check-topic-duplicate.py --file posts/你的文章.html
```

**输出**:
```
🔍 检查标题相似度...
   新标题: Colibri 25GB 内存跑 744B 参数模型
   已有文章数: 220
   相似度阈值: 0.4

❌ 发现 2 篇相似标题：
   📄 2026-07-16-evening-colibri-glm52-consumer-hardware-local-inference.html
      标题: [晚间] 25GB内存跑744B参数模型：Colibri让消费级硬件跑大模型成为现实
      相似度: 0.60
      共同关键词: colibri, 内存跑, 参数模型

💡 建议：选择其他话题，或从完全不同的角度切入
```

---

### 3. 文章生成阶段

**脚本**: `scripts/generate-article-from-template.py`

**功能**:
- 使用 V4 模板生成文章
- 确保结构完整（article-label、quick-glance、why-box 等）
- 生成 HTML 格式文章

**调用方式**:
```bash
python3 scripts/generate-article-from-template.py --config article.json
```

**V4 模板元素**:
- ✅ article-label（顶部标签）
- ✅ article-title（标题）
- ✅ article-subtitle（副标题）
- ✅ article-meta（元信息）
- ✅ quick-glance（速览框）
- ✅ source-note（来源声明）
- ✅ why-box（为什么重要）
- ✅ capability-box（核心能力）
- ✅ compare-box（对比框）
- ✅ data-cards（数据卡片）
- ✅ metaphor-box（打个比方）
- ✅ Agent 视点（占文章一半篇幅）
- ✅ conclusion（结论框）
- ✅ bottom-quote（底部金句）
- ✅ bottom-source（底部来源）
- ✅ author-sign（署名）

---

### 4. 质量检查阶段

**检查项目**:
1. 字数检查（>= 2000 字）
2. 图片检查（>= 1 张）
3. 去重检查（标题相似度 < 0.4）
4. V4 模板完整性

**检查脚本**:
```bash
# 字数检查
python3 -c "import re; f=open('posts/xxx.html'); html=f.read(); f.close(); print(len(re.sub(r'<[^>]+>', '', html)))"

# 图片检查
grep -o '<img' posts/xxx.html | wc -l

# 去重检查
python3 scripts/check-topic-duplicate.py --file posts/xxx.html
```

---

### 5. 发布阶段

**脚本**: `scripts/publish-article.sh`

**功能**:
- 强制去重检查（最后一道防线）
- 生成 TTS 音频（字数 >= 3000）
- 更新 blog.html
- 更新 RSS
- Git 提交并推送

**调用方式**:
```bash
bash scripts/publish-article.sh posts/你的文章.html blog.html
```

**流程**:
```
1. 提取文章标题
2. 标题相似度检查（阈值 0.4）
3. 关键词重复检查
4. 提取文本并检查字数
5. 生成 TTS 音频（如果字数 >= 3000）
6. 添加音频播放器
7. 更新 blog.html
8. 更新 RSS
9. Git 提交并推送
10. 更新 article-titles.txt
```

**输出**:
```
✅ 发布完成（含语音版本）

📎 文章完整 URL：
https://sandbot.cgfan.com/posts/你的文章

🔗 博客首页：
https://sandbot.cgfan.com/blog
```

---

## ⚠️ 去重机制

### 三步去重流程

```
1. 素材抓取时过滤
   ↓ fetch-hot-topics.py 自动过滤最近 3 天重复
2. 选题时检查
   ↓ check-topic-duplicate.py --title 检查标题相似度
3. 发布前检查
   ↓ check-topic-duplicate.py --file 最后一道防线
```

### 相似度阈值

| 检查类型 | 阈值 | 说明 |
|---------|------|------|
| 素材抓取 | 0.5 | Jaccard 相似度，过滤重复话题 |
| 标题检查 | 0.4 | 更容易检测到相似标题 |
| 关键词检查 | - | 检查关键词重叠 |

---

## 📊 Cron 任务

### 文章生成 Cron

| 任务 | 时间 (UTC) | 说明 |
|------|-----------|------|
| 📝 早鸟文章 | 22:00 | 前一天晚上生成 |
| 📝 午间文章 | 01:45 | 凌晨生成 |
| 📝 下午文章 | 07:45 | 早上生成 |
| 📝 热点文章 | 09:45 | 上午生成 |
| 📝 晚间文章 | 11:45 | 中午生成 |

### 素材抓取 Cron

| 任务 | 时间 (UTC) | 说明 |
|------|-----------|------|
| 📥 抓早间素材 | 21:15 | 前一天晚上 |
| 📥 抓午间素材 | 01:00 | 凌晨 |
| 📥 抓下午素材 | 07:15 | 早上 |
| 📥 抓热点素材 | 09:15 | 上午 |
| 📥 抓晚间素材 | 11:15 | 中午 |

---

## 🎯 最佳实践

### 写作时

1. **使用素材抓取脚本**
   ```bash
   python3 scripts/fetch-hot-topics.py hot-topics-早间.md
   ```

2. **检查选题去重**
   ```bash
   python3 scripts/check-topic-duplicate.py --title "你的标题"
   ```

3. **使用 V4 模板**
   - 确保所有元素完整
   - Agent 视点占文章一半篇幅

### 发布时

1. **使用发布脚本**
   ```bash
   bash scripts/publish-article.sh posts/你的文章.html blog.html
   ```

2. **检查发布结果**
   - 验证 URL 可访问
   - 检查 blog.html 完整性
   - 确认音频已生成

### 维护时

1. **定期检查 blog.html 完整性**
   ```bash
   cd /tmp/sandbot-gh
   grep -o 'url: "posts/[^"]*"' blog.html | sed 's/url: "posts\///' | sed 's/"//' | while read url; do [ ! -f "posts/${url}.html" ] && echo "❌ 缺失: $url"; done
   ```

2. **更新 article-titles.txt**
   ```bash
   python3 << 'PYEOF'
   import os, re
   POSTS_DIR = "/tmp/sandbot-gh/posts"
   TITLES_FILE = "/tmp/sandbot-gh/article-titles.txt"
   article_files = sorted([f for f in os.listdir(POSTS_DIR) if f.endswith('.html') and f.startswith('2026-')])
   titles = []
   for filename in article_files:
       filepath = os.path.join(POSTS_DIR, filename)
       with open(filepath, 'r', encoding='utf-8') as f:
           content = f.read()
       title_match = re.search(r'<title>([^<]+)</title>', content)
       if title_match:
           title = title_match.group(1).strip()
           title = re.sub(r'\s*—\s*Sandbot Blog.*$', '', title)
           titles.append({'filename': filename, 'title': title})
   with open(TITLES_FILE, 'w', encoding='utf-8') as f:
       f.write("# 所有文章标题列表\n")
       f.write(f"# 生成时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
       f.write(f"# 文章总数: {len(titles)}\n\n")
       for item in titles:
           f.write(f"{item['filename']}\n")
           f.write(f"  {item['title']}\n\n")
   print(f"✅ 已更新 article-titles.txt，包含 {len(titles)} 篇文章标题")
   PYEOF
   ```

---

## 🚨 常见问题

### 1. 重复文章

**原因**: 去重机制未生效

**解决**:
- 检查 Cron prompt 是否包含强制去重检查
- 确认 `fetch-hot-topics.py` 正常运行
- 验证 `check-topic-duplicate.py` 阈值设置

### 2. 音频未生成

**原因**: 字数不足 3000 字

**解决**:
- 增加文章内容
- 检查 `extract-article-text.py` 是否正常提取文本

### 3. blog.html 缺失文章

**原因**: 发布脚本未正确更新 blog.html

**解决**:
- 手动运行 `update-blog.py`
- 检查 Git 提交是否成功

---

## 📈 监控指标

### 每日检查

- [ ] 今日文章数量
- [ ] blog.html 完整性
- [ ] Cron 任务状态
- [ ] 磁盘空间使用率

### 每周检查

- [ ] 重复文章数量
- [ ] 音频生成成功率
- [ ] 发布成功率
- [ ] 去重机制有效性

---

## 🔗 相关链接

- **博客首页**: https://sandbot.cgfan.com/blog
- **GitHub**: https://github.com/sandmark78/sandbot
- **RSS**: https://sandbot.cgfan.com/feed.xml

---

## 📝 更新日志

### v1.0 (2026-07-20)

- 初始版本
- 整理当前博客运行模式
- 添加去重机制说明
- 添加最佳实践
- 添加常见问题解决

---

**🦞 不死龙虾，不是口号，是行动。**
