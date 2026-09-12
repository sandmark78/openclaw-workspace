# OpenClaw 内置能力检查

**版本**: 1.0.0  
**创建时间**: 2026-08-25  
**触发场景**: 用户请求需要外部工具的任务（网页爬取、浏览器自动化、数据处理等）

---

## 核心原则

**在执行任何任务前，先检查 OpenClaw 已有的内置能力，再考虑安装外部依赖。**

---

## 为什么需要这个技能

### 问题案例
```
用户需求：爬取 AIHOT 平台（客户端渲染）
错误做法：直接尝试安装 Playwright
正确做法：先检查 OpenClaw 是否有浏览器自动化工具
实际发现：内置 browser 工具已支持 ✅
```

### 常见陷阱
```
❌ 看到"爬取" → 立即安装 Scrapy/Playwright
❌ 看到"浏览器自动化" → 立即安装 Selenium
❌ 看到"数据处理" → 立即安装 Pandas
❌ 不检查已有能力 → 重复造轮子
```

---

## OpenClaw 内置能力清单

### 1. 浏览器自动化 (`browser` 工具)
```
能力：
  ✅ 打开网页、导航
  ✅ 截图 (screenshot)
  ✅ 页面快照 (snapshot) - 获取 DOM 结构
  ✅ 表单填写、点击、输入
  ✅ JavaScript 执行
  ✅ 处理客户端渲染页面
  
使用场景：
  - 爬取 JS 渲染的网站
  - 自动化网页操作
  - 网页测试
  - 数据提取
  
示例：
  browser action=open url="https://example.com"
  browser action=snapshot  # 获取页面结构
  browser action=screenshot  # 截图
```

### 2. 网页抓取 (`web_fetch` 工具)
```
能力：
  ✅ 抓取静态网页内容
  ✅ 自动转换为 Markdown
  ✅ 提取可读内容
  
使用场景：
  - 抓取静态网站
  - 获取文章/文档内容
  - API 调用
  
示例：
  web_fetch url="https://example.com"
```

### 3. 网络搜索 (`web_search` 工具)
```
能力：
  ✅ 搜索引擎查询
  ✅ 获取搜索结果
  
使用场景：
  - 信息检索
  - 查找资源
  - 研究调查
  
示例：
  web_search query="OpenClaw browser automation"
```

### 4. 文件操作 (内置工具)
```
能力：
  ✅ 读取文件 (read)
  ✅ 写入文件 (write)
  ✅ 编辑文件 (edit)
  ✅ 执行命令 (exec)
  
使用场景：
  - 数据处理
  - 文件转换
  - 批量操作
```

### 5. 技能系统 (`skills/` 目录)
```
已安装技能检查：
  ls /home/node/.openclaw/workspace/skills/
  ls /home/node/.openclaw/plugin-skills/
  
常见技能：
  - browser-automation: 浏览器自动化
  - tavily-search: AI 优化搜索
  - reddit-insights: Reddit 搜索
  - x-tweet-fetcher: Twitter 推文获取
```

---

## 执行流程

### 步骤 1：识别任务类型
```
用户请求 → 分析需要什么能力？
  - 网页爬取？→ 检查 browser/web_fetch
  - 浏览器自动化？→ 检查 browser
  - 数据处理？→ 检查 exec/python
  - 搜索？→ 检查 web_search
```

### 步骤 2：检查内置工具
```bash
# 检查可用的内置工具
# (在思考过程中完成，不需要执行命令)

内置工具清单：
  - browser: 浏览器自动化
  - web_fetch: 网页抓取
  - web_search: 网络搜索
  - read/write/edit: 文件操作
  - exec: 命令执行
  - image: 图像分析
  - pdf: PDF 处理
```

### 步骤 3：检查已安装技能
```bash
# 检查技能目录
ls /home/node/.openclaw/workspace/skills/
ls /home/node/.openclaw/plugin-skills/

# 检查特定技能
cat /home/node/.openclaw/plugin-skills/browser-automation/SKILL.md
```

### 步骤 4：决策
```
如果内置工具能解决：
  ✅ 直接使用内置工具
  ✅ 告诉用户"OpenClaw 已有这个能力"
  
如果内置工具不够：
  ⚠️ 说明为什么需要外部工具
  ⚠️ 提出安装建议
  ⚠️ 等待用户确认
```

---

## 实战示例

### 示例 1：爬取客户端渲染网站
```
用户：帮我爬取 https://aihot.virxact.com 的所有文章

❌ 错误流程：
1. 尝试 curl → 发现只有 HTML 壳
2. 决定安装 Playwright
3. 执行 pip install playwright
4. 发现已安装，但浪费了时间

✅ 正确流程：
1. 识别任务：爬取 JS 渲染网站
2. 检查内置工具：browser 工具支持 ✅
3. 直接使用：
   browser action=open url="https://aihot.virxact.com"
   browser action=snapshot  # 获取渲染后的内容
4. 提取数据并保存
```

### 示例 2：自动化表单填写
```
用户：帮我自动填写这个表单

❌ 错误流程：
1. 安装 Selenium
2. 配置 WebDriver
3. 编写脚本

✅ 正确流程：
1. 识别任务：表单自动化
2. 检查内置工具：browser 工具支持 ✅
3. 直接使用：
   browser action=open url="表单URL"
   browser action=snapshot  # 查看表单结构
   browser action=act kind=click ref="表单字段"
   browser action=act kind=type ref="输入框" text="内容"
```

### 示例 3：数据清洗
```
用户：帮我清洗这个 CSV 文件

❌ 错误流程：
1. 安装 Pandas
2. 编写 Python 脚本

✅ 正确流程：
1. 识别任务：数据处理
2. 检查内置工具：exec 可以运行 Python ✅
3. 检查是否已安装 Pandas：
   exec command="python3 -c 'import pandas; print(pandas.__version__)'"
4. 如果已安装，直接使用
5. 如果未安装，评估是否必要（简单处理可以用原生 Python）
```

---

## 检查清单

### 任务开始前问自己：
```
□ 这个任务需要什么能力？
□ OpenClaw 有内置工具吗？
□ 已经安装了相关技能吗？
□ 内置工具能满足需求吗？
□ 如果不能满足，差距在哪里？
□ 必须安装外部工具吗？
□ 有没有更简单的替代方案？
```

### 常见任务 → 内置工具映射
```
网页爬取（静态）→ web_fetch
网页爬取（动态）→ browser
浏览器自动化 → browser
网络搜索 → web_search
文件处理 → read/write/edit/exec
数据分析 → exec (Python)
图像处理 → image
PDF 处理 → pdf
代码执行 → exec
```

---

## 失败案例复盘

### 案例：AIHOT 爬取任务
```
时间：2026-08-25
任务：爬取 AIHOT 平台所有文章
问题：客户端渲染，curl 无法获取内容

错误行为：
  1. 尝试 curl → 失败
  2. 决定安装 Playwright
  3. 执行 pip install playwright
  4. 发现已安装但不知道

正确行为应该是：
  1. 识别任务：爬取 JS 渲染网站
  2. 检查内置工具：browser 工具 ✅
  3. 读取技能文档：/home/node/.openclaw/plugin-skills/browser-automation/SKILL.md
  4. 直接使用 browser 工具

教训：
  ❌ 不检查已有能力 → 浪费时间
  ❌ 不知道内置工具 → 重复造轮子
  ✅ 先检查 → 再行动
```

---

## 最佳实践

### 1. 建立能力地图
```
定期更新内置工具清单：
  - 阅读 TOOLS.md
  - 检查 skills/ 目录
  - 了解每个工具的能力边界
```

### 2. 优先使用内置工具
```
优先级：
  1. 内置工具 (browser, web_fetch, etc.)
  2. 已安装技能 (skills/)
  3. 系统已安装工具 (Python, Node.js, etc.)
  4. 需要安装的外部工具 (最后选择)
```

### 3. 文档化发现
```
如果发现新的内置能力：
  - 更新 TOOLS.md
  - 记录使用场景
  - 分享给未来的自己
```

---

## 总结

**核心洞察**：
OpenClaw 已经有强大的内置能力，但助手常常不知道或不记得使用。

**解决方案**：
每次任务开始前，先检查内置工具 → 再考虑外部依赖。

**预期效果**：
- ✅ 减少不必要的安装
- ✅ 提高任务执行效率
- ✅ 充分利用已有能力
- ✅ 避免重复造轮子

---

*此技能已真实写入服务器*
*最后更新：2026-08-25 12:03 UTC*
*验证：cat /home/node/.openclaw/workspace/skills/openclaw-capability-check/SKILL.md*
