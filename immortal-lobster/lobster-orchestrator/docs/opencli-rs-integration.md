# opencli-rs 集成指南

**安装时间**: 2026-04-01  
**版本**: 0.2.3  
**位置**: `/home/node/.local/bin/opencli-rs`

---

## 📊 性能优势

| 指标 | opencli-rs | 传统方式 | 提升 |
|------|------------|----------|------|
| 内存占用 | 9-15MB | 95-99MB | **10.6x** |
| 二进制大小 | 4.7MB | ~50MB | **10x** |
| 响应速度 | ~500ms | ~20s | **40x** |

---

## 🎯 可用命令 (公共 API - 无需浏览器)

### 技术社区
```bash
# HackerNews
opencli-rs hackernews top --limit 10
opencli-rs hackernews new --limit 10
opencli-rs hackernews best --limit 10
opencli-rs hackernews search "AI Agent" --limit 10

# DevTo
opencli-rs devto top --limit 10
opencli-rs devto tag rust --limit 10

# Lobsters
opencli-rs lobsters hot --limit 10
opencli-rs lobsters newest --limit 10

# StackOverflow
opencli-rs stackoverflow hot --limit 10
opencli-rs stackoverflow search "Rust" --limit 10
opencli-rs stackoverflow bounties --limit 10
```

### 其他平台
```bash
# Steam 游戏销量
opencli-rs steam top-sellers --limit 10

# HuggingFace
opencli-rs hf top --limit 10

# Linux.do
opencli-rs linux-do hot --limit 10

# V2EX
opencli-rs v2ex hot --limit 10

# Arxiv 论文
opencli-rs arxiv search "LLM" --limit 10

# Wikipedia
opencli-rs wikipedia search "AI" --limit 5
```

---

## 📁 集成脚本

### 1. 通用搜索脚本
```bash
# 用法：./opencli-search.sh <site> <command> [args...]
./scripts/opencli-search.sh hackernews top --limit 10
```

### 2. 热搜监控脚本
```bash
# 用法：./trending-monitor.sh
./scripts/trending-monitor.sh
```

### 3. AI Agent 集成
在 `AGENT.md` 或 `.cursorrules` 中添加：
```markdown
## Available Tools

### opencli-rs
- `opencli-rs hackernews top --limit 10` - Get HackerNews top stories
- `opencli-rs devto top --limit 10` - Get DevTo top articles
- `opencli-rs stackoverflow hot --limit 10` - Get StackOverflow hot questions
- `opencli-rs arxiv search "query" --limit 10` - Search academic papers
```

---

## 🌐 需要浏览器的命令

以下命令需要安装 Chrome 扩展：

1. 下载扩展：https://github.com/nashsu/opencli-rs/releases
2. 解压到任意目录
3. Chrome → `chrome://extensions` → 开发者模式 → 加载已解压的扩展
4. 保持 Chrome 运行

**支持平台**:
- Twitter/X, Bilibili, Reddit
- 知乎，小红书，微博
- YouTube, Medium, Substack
- Facebook, Instagram, TikTok
- 等等 55+ 网站

---

## 📊 输出格式

支持多种格式：
```bash
--format table  # ASCII 表格 (默认)
--format json   # JSON
--format yaml   # YAML
--format csv    # CSV
--format md     # Markdown 表格
```

---

## 🔧 故障排查

### 问题：命令找不到
```bash
# 解决：添加 PATH
export PATH=/home/node/.local/bin:$PATH
echo 'export PATH=/home/node/.local/bin:$PATH' >> ~/.bashrc
```

### 问题：需要浏览器
```
🌐 [browser] Chrome is not running
```
**解决**: 安装 Chrome 扩展并保持 Chrome 运行

### 问题：API 限流
```bash
# 解决：降低频率，添加延迟
sleep 2 between requests
```

---

## 🎯 最佳实践

### 1. 批量搜索
```bash
# 同时搜索多个平台
for site in hackernews devto lobsters; do
    opencli-rs $site top --limit 10 --format json
done
```

### 2. 定时监控
```bash
# 添加到 crontab
0 */4 * * * /home/node/.openclaw/workspace/scripts/trending-monitor.sh
```

### 3. 数据导出
```bash
# 导出为 JSON
opencli-rs hackernews top --limit 100 --format json > hn_top100.json

# 导出为 CSV
opencli-rs stackoverflow hot --limit 100 --format csv > so_hot100.csv
```

---

## 📈 使用案例

### 1. AI Agent 资料搜集
```bash
# 搜索最新 AI 论文
opencli-rs arxiv search "LLM Agent" --limit 20

# 搜索技术讨论
opencli-rs hackernews search "AI Agent" --limit 20

# 搜索 StackOverflow 问题
opencli-rs stackoverflow search "AI Agent" --limit 20
```

### 2. 全网热搜监控
```bash
# 运行监控脚本
./scripts/trending-monitor.sh

# 输出保存到 memory/trending/ 目录
```

### 3. 竞品分析
```bash
# 监控竞品动态
opencli-rs twitter search "competitor_name" --limit 50
opencli-rs reddit search "competitor_name" --limit 50
```

---

## 🦞 集成到 OpenClaw

现在 OpenClaw Agent 可以通过 exec 工具调用 opencli-rs：

```bash
# 在对话中直接使用
opencli-rs hackernews top --limit 10
```

**优势**:
- ✅ 实时数据，非预测
- ✅ 55+ 网站支持
- ✅ 多格式输出
- ✅ 极低资源占用

---

**🦞 opencli-rs 已完全集成！现在可以抓取数据、找资料、搜索网页了！**
