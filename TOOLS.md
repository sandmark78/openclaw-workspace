# TOOLS.md - Sandbot V6.1 的本地配置笔记

**最后更新**: 2026-02-24 15:20 UTC

---

## 🛠️ 核心工具配置

### 模型配置
```
提供商：bailian (阿里云百炼)
模型：qwen3.5-plus
上下文：1M tokens (按次计费)
并发：主 Agent 4, 子 Agent 8
```

### 通道配置
```
Telegram:
  - Bot: @sand66_bot
  - Chat ID: 773172564
  - 状态：✅ 已配对

WebUI:
  - 地址：http://172.18.0.2:18789/
  - Token: 78fd582aacc1563229e20b025e4093b679804dcf56b5084e
  - 状态：✅ 可访问
```

### 工作区路径
```
容器内：/home/node/.openclaw/workspace/
宿主机：/opt/1panel/apps/openclaw/openclaw/data/workspace/
映射关系：Docker volume 挂载
```

---

## 📁 目录结构

```
/home/node/.openclaw/workspace/
├── *.md                    # 核心身份文件 (8 个)
├── subagents/              # 7 子 Agent 配置
│   ├── techbot/           # 技术教程开发
│   ├── financebot/        # 金融收益分析
│   ├── creativebot/       # 创意内容生成
│   ├── autobot/           # 数据抓取自动化
│   ├── researchbot/       # 深度研究分析
│   ├── auditor/           # 质量保障审计
│   └── devopsbot/         # 工程化运维
├── skills/                 # 技能库 (11 个)
│   ├── agent-optimizer/   # 自研性能优化
│   ├── tavily-search/     # AI 优化搜索
│   ├── reddit-insights/   # Reddit 语义搜索
│   └── ...
├── memory/                 # 记忆文件 (30+)
│   ├── YYYY-MM-DD.md      # 每日记录
│   └── learning/          # 学习总结
└── knowledge_base/         # 知识库 (20+)
    ├── 23_articles_series/
    └── *.md
```

---

## 🔧 已安装技能清单

### 核心技能 (必用)
| 技能 | 用途 | 状态 |
|------|------|------|
| `tavily-search` | AI 优化搜索引擎 | ✅ 已安装 |
| `reddit-insights` | Reddit 语义搜索 | ✅ 已安装 |
| `x-tweet-fetcher` | X/Twitter 推文获取 | ✅ 已安装 |
| `find-skills` | 技能发现工具 | ✅ 已安装 |

### 专业领域技能
| 技能 | 用途 | 状态 |
|------|------|------|
| `email-marketing` | 邮件营销 | ✅ 已安装 |
| `yc-cold-outreach` | YC 冷邮件 outreach | ✅ 已安装 |
| `proactive-agent-1-2-4` | 主动型 Agent 模式 | ✅ 已安装 |
| `foundry` | 自写元扩展 | ✅ 已安装 |

### 自研技能
| 技能 | 用途 | 状态 |
|------|------|------|
| `agent-optimizer` | V6.1 性能优化框架 | ✅ 自研 |

### 学习记录 (未安装)
| 技能 | 原因 | 状态 |
|------|------|------|
| `agent-lightning` | pip 权限不足，无法安装 | 📝 已记录 |

---

## ⚙️ 工具使用规范

### 文件操作
```bash
# ✅ 推荐：使用原生 write 工具
write /path/to/file.md "内容"

# ⚠️ 注意：Bash 写入可能转义错误
echo "内容" > /path/to/file.md  # 含引号时容易出错

# 安全建议：
# - 简单文本：exec 足够
# - 复杂内容 (代码/Markdown)：用 write 工具
# - 精确编辑：用 edit 工具
```

### 网络请求
```bash
# ✅ 推荐：web_fetch (直接抓取网页)
web_fetch "https://duckduckgo.com/html/?q=搜索关键词"
web_fetch "https://news.ycombinator.com/"
web_fetch "https://reddit.com/r/opensource"

# ✅ 推荐：内部知识库搜索
grep -r "关键词" knowledge_base/
python3 scripts/knowledge-retriever-demo.py

# 🚫 禁用：web_search (Brave API 已永久禁用)
# web_search "query" --count 5  # 不再使用
```

### AIHOT API（2026-08-03 更新）
```bash
# ✅ 官方 API v1（已验证可用）
curl "https://aihot.virxact.com/api/v1/items?mode=selected&window=24h&limit=20"

# ✅ 公开 API
curl "https://aihot.virxact.com/api/public/items?limit=50"

# 脚本位置
/home/node/.openclaw/workspace/sandbot-blog/scripts/aihot-scraper.py      # 独立抓取
/home/node/.openclaw/workspace/sandbot-blog/scripts/news-aggregator.py     # 多源聚合（含 AIHOT）

# ⚠️ 铁律：数据源有 API → 必须用 API，禁止网页解析
```

### 子 Agent 调用
```bash
# 调用特定子 Agent
sessions_spawn --agent-id techbot --task "编写教程"

# 并发调用多个子 Agent
sessions_spawn --agent-id techbot,financebot --task "项目分析"
```

---

## 🔐 敏感信息存储

### secrets 目录
```
位置：/home/node/.openclaw/secrets/
权限：700 (目录), 600 (文件)
内容：
  - moltbook_api_key.txt  ✅ 已存储
  - clawtasks_api_key.txt ❌ 已删除 (服务下线)
```

### 配置中的敏感信息
```
openclaw.json 包含:
  - Bailian API Key: sk-sp-54997e1f8fa84942b1c077b1fa8f5269
  - Telegram Bot Token: 8549971570:AAFotFWJkGjhwgM4WghwuejoUGCGUbnYnxM
  - Feishu App Secret: VbKSKWynB2IJ7DwhRNibNdLEMjjrCq0V

安全建议:
  - 不要将这些文件复制到 workspace 外
  - 不要提交到 Git
  - 定期轮换密钥
```

---

## 📊 工具性能优化

### 单次调用最大化
```
模型：qwen3.5-plus (1M 上下文)
策略：
  1. 批量处理多任务
  2. 充分利用上下文窗口
  3. 减少调用次数，增加单次内容

示例:
  ❌ 3 次调用分别读 3 个文件
  ✅ 1 次调用同时读 3 个文件 + 分析 + 输出报告
```

### 缓存策略
```
本地缓存:
  - 搜索结果 → memory/search_cache_*.md
  - 网页内容 → memory/fetch_cache_*.md
  - API 响应 → memory/api_cache_*.md

缓存有效期:
  - 静态内容：7 天
  - 动态内容：1 小时
  - 配置信息：永久 (除非变更)
```

### 并发控制
```
主 Agent: maxConcurrent: 4
子 Agent: maxConcurrent: 8

使用建议:
  - 独立任务：并发执行
  - 依赖任务：串行执行
  - 混合任务：分组并发
```

---

## 🛡️ 安全注意事项

### 禁止访问的路径
```
~/.ssh/          # SSH 私钥
~/.gnupg/        # GPG 密钥
~/.aws/          # AWS 凭证
~/.config/gh/    # GitHub token
```

### 敏感操作确认
```
需要确认的操作:
  - 删除文件 (尤其是批量删除)
  - 修改系统配置
  - 安装外部软件
  - 发送外部消息 (邮件/推文)

无需确认的操作:
  - 读取文件
  - 搜索网络
  - 写入 workspace 内文件
  - 整理文档
```

### 工具限制配置
```json
// openclaw.json 可选配置
{
  "tools": {
    "profile": "coding",
    "deny": ["group:runtime"]  // 禁止 exec 等运行时工具
  }
}
```

---

## 📝 工具使用技巧

### 高效搜索
```bash
# 精准搜索 (加引号)
web_search "\"OpenClaw\" subagents configuration"

# 排除无关结果
web_search "agent optimization -lightning"

# 限制结果数量
web_search "query" --count 3
```

### 文件管理
```bash
# 批量重命名
find . -name "*.txt" -exec mv {} {}.md \;

# 查找大文件
find . -type f -size +1M -exec ls -lh {} \;

# 统计文件数
find . -name "*.md" | wc -l
```

### 调试技巧
```bash
# 查看工具调用历史
cat /home/node/.openclaw/agents/main/sessions/*.jsonl | grep "toolCall"

# 检查 Gateway 日志
tail -f /tmp/openclaw/openclaw-*.log

# 验证文件写入
ls -la /home/node/.openclaw/workspace/memory/2026-02-24*.md
```

---

## 🚫 不转圈原则（2026-08-04 老大指出）
```
知道流程 → 直接执行 → 完成即停
不重复检查同一个东西
不验证已经验证过的东西
每次多余的检查 = 浪费一次API调用
老大说"直接做"就是真的直接做
```

## 🔍 先检查内置能力原则（2026-08-25 老大指出）
```
遇到任务 → 先检查 OpenClaw 内置工具 → 再考虑外部依赖
不盲目安装外部工具
不重复造轮子
每次安装前先问：OpenClaw 有这个能力吗？

内置工具清单：
  - browser: 浏览器自动化（支持 JS 渲染）
  - web_fetch: 静态网页抓取
  - web_search: 网络搜索
  - read/write/edit: 文件操作
  - exec: 命令执行
  - image: 图像分析
  - pdf: PDF 处理

技能目录：
  - /home/node/.openclaw/workspace/skills/
  - /home/node/.openclaw/plugin-skills/
```

详细技能文档：`/home/node/.openclaw/workspace/skills/openclaw-capability-check/SKILL.md`

## 🎯 工具选择决策树

```
需要写文件？
├─ 简单文本 → exec (echo)
├─ 复杂内容 (代码/Markdown) → write 工具
└─ 精确编辑 → edit 工具

需要搜索？
├─ 网络信息 → web_search
├─ 网页内容 → web_fetch
└─ 本地文件 → grep/find

需要执行命令？
├─ 系统查询 → exec (ps, ls, cat)
├─ 文件操作 → 优先用原生工具 (read/write/edit)
└─ 网络请求 → 优先用 web_* 工具

需要调用 Agent?
├─ <30秒能完成？ → 主Agent自己干（ls/cat/grep/curl/git status）
│
├─ 需要专业领域？ → 按分工表选对应Agent
│  ├─ 技术/代码 → TechBot
│  ├─ 金融/成本 → FinanceBot
│  ├─ 创意/文案 → CreativeBot
│  ├─ 数据/爬虫 → AutoBot
│  ├─ 研究/调研 → ResearchBot
│  ├─ 审计/质量 → Auditor
│  └─ 部署/运维 → DevOpsBot
│
├─ 需要并行？ → spawn多个，**必须分工**
│  ├─ ✅ A翻译1-20，B翻译21-40
│  ├─ ✅ A调研产品A，B调研产品B
│  └─ ❌ A和B都做同样的事
│
└─ 需要质量审查？ → Auditor介入

⚠️ 铁律：
- ❌ 多个子Agent做同样的事
- ❌ spawn子Agent但不明确分工
- ❌ 主Agent什么都干，子Agent形同虚设
- ❌ spawn子Agent处理简单任务（<30秒）
- ❌ 并发超过2个子Agent做同类任务
```

---

*此文件已真实写入服务器*
*最后更新：2026-02-24 15:20 UTC*
*验证：cat /home/node/.openclaw/workspace/TOOLS.md*
