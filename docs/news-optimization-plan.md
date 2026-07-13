# 新闻抓取优化方案

**日期**: 2026-07-13  
**目标**: 减少模型调用、减少时间、保证质量

---

## 📊 优化前后对比

| 项目 | 优化前 | 优化后 | 改进 |
|------|--------|--------|------|
| **模型调用** | 2-3 次/天 | 0 次/天 | ✅ 100% 减少 |
| **抓取时间** | 2-3 分钟 | 30 秒 | ✅ 80% 减少 |
| **数据源** | 单一 HN | HN + AIHOT + FiNews | ✅ 3x 增加 |
| **稳定性** | 经常超时 | 使用官方 API | ✅ 更稳定 |
| **成本** | ¥0.02-0.06/天 | ¥0 | ✅ 100% 节省 |

---

## 🔧 优化方案

### 1. 统一新闻聚合脚本

**文件**: `scripts/news-aggregator.py`

**功能**:
- 一次抓取多个新闻源（HN、AIHOT、FiNews）
- 使用官方 API（HN Firebase API）
- 本地处理数据，不需要模型
- 输出结构化 JSON + 可读 Markdown

**用法**:
```bash
# 抓取所有源，每个源最多 10 条
python3 scripts/news-aggregator.py --sources all --top 10

# 只抓 HN，最多 5 条
python3 scripts/news-aggregator.py --sources hn --top 5

# 抓取 HN + AIHOT
python3 scripts/news-aggregator.py --sources hn,aihot --top 10
```

**输出**:
```
tmp/news/YYYY-MM-DD.json  - 结构化数据
tmp/news/YYYY-MM-DD.md    - 可读摘要
```

### 2. 轻量级 Cron 脚本

**文件**: `scripts/news-cron.sh`

**功能**:
- 纯 bash 脚本，不调用模型
- 自动执行 news-aggregator.py
- 记录日志到 tmp/news-cron.log
- 自动清理旧日志

**用法**:
```bash
# 手动运行
./scripts/news-cron.sh

# 添加到系统 crontab（每天 09:00 UTC）
0 9 * * * /home/node/.openclaw/workspace/scripts/news-cron.sh
```

### 3. 新闻源配置

| 源 | API/URL | 优势 | 阈值 |
|----|---------|------|------|
| **Hacker News** | Firebase API | 官方 API，快速稳定 | 100+ 分数 |
| **AIHOT** | 网页抓取 | AI 专业热点 | - |
| **FiNews** | 网页抓取 | 美股日报 | - |

---

## 📝 实施步骤

### 步骤 1: 更新 Cron 配置

**当前 Cron**（需要模型调用）:
```json
{
  "name": "📥 抓热点文章素材",
  "schedule": { "expr": "15 9 * * *" },
  "payload": {
    "kind": "agentTurn",
    "message": "你是 Sandbot 🏖️，执行轻量级热点抓取任务..."
  }
}
```

**新 Cron**（不需要模型调用）:
```json
{
  "name": "📥 抓热点文章素材（优化版）",
  "schedule": { "expr": "0 9 * * *" },
  "payload": {
    "kind": "systemEvent",
    "text": "bash /home/node/.openclaw/workspace/scripts/news-cron.sh"
  }
}
```

### 步骤 2: 文章生成流程

**优化前**:
```
Cron 触发 → 模型抓取 HN → 模型抓取原始 URL → 模型保存素材
调用次数: 3-5 次
时间: 2-3 分钟
```

**优化后**:
```
Cron 触发 → 脚本抓取新闻 → 保存到文件
调用次数: 0 次
时间: 30 秒

需要写文章时 → 读取素材文件 → 模型写文章
调用次数: 1 次
时间: 1 分钟
```

### 步骤 3: 质量筛选

**本地筛选**（不需要模型）:
```python
# 在 news-aggregator.py 中添加筛选逻辑
if story.get('score', 0) >= 100:  # HN 100+ 分数
    stories.append(story)
```

**模型筛选**（需要时才调用）:
```
读取 tmp/news/YYYY-MM-DD.json
↓
模型筛选 3 个最有价值的选题
↓
生成文章
```

---

## 🎯 预期效果

### 每日节省

| 项目 | 节省量 |
|------|--------|
| **模型调用** | 2-3 次/天 |
| **成本** | ¥0.02-0.06/天 |
| **时间** | 2-3 分钟/天 |
| **月度成本** | ¥0.6-1.8/月 |

### 质量提升

- ✅ 使用官方 API，数据更准确
- ✅ 多个新闻源，覆盖更广
- ✅ 本地筛选，减少幻觉
- ✅ 结构化数据，易于处理

---

## 📚 相关文件

- `scripts/news-aggregator.py` - 统一新闻聚合脚本
- `scripts/news-cron.sh` - 轻量级 Cron 脚本
- `tmp/news/YYYY-MM-DD.json` - 每日新闻数据
- `tmp/news/YYYY-MM-DD.md` - 每日新闻摘要
- `tmp/news-cron.log` - Cron 执行日志

---

## 🔄 后续优化

1. **添加更多新闻源**: Reddit、Product Hunt、GitHub Trending
2. **智能筛选**: 使用简单的规则引擎，不需要模型
3. **缓存机制**: 缓存已抓取的内容，避免重复抓取
4. **推送通知**: 发现重要新闻时推送给老大

---

**维护说明**:
- 每周检查一次 news-cron.log，确保正常运行
- 每月清理一次 tmp/news/ 目录（保留最近 30 天）
- 如需添加新闻源，修改 news-aggregator.py 的 SOURCES 配置
