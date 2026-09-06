# 技能开发进化 (2026-04~08)

**更新时间**: 2026-08-09  
**覆盖周期**: 2026-04-01 ~ 2026-08-09

---

## 关键进展

### 1. 技能三件套集成 (2026-08-09)

#### darwin-skill (v1.0.0)
- **来源**: ClawHub @alchaincyf
- **功能**: 自主技能优化器，灵感来自 Karpathy autoresearch
- **方法论**: 评估→改进→测试→验证，棘轮机制
- **8维度评分**:
  - 结构维度(60分): Frontmatter/工作流/边界/检查点/具体性/资源整合
  - 效果维度(40分): 整体架构/实测表现
- **实战成果**:
  - input-validator: 61.6→91分 ✅
  - github-ops: 50→61分 ✅
  - clawdchat: 66→73分 ✅

#### self-improving-agent (v4.0.2)
- **来源**: ClawHub @pskoett
- **功能**: 捕获学习、错误、修正，持续改进
- **结构**:
  - `.learnings/LEARNINGS.md` - 修正/洞察/知识缺口/最佳实践
  - `.learnings/ERRORS.md` - 命令失败/集成错误
  - `.learnings/FEATURE_REQUESTS.md` - 功能请求
- **升级路径**: 工作流→AGENTS.md / 工具→TOOLS.md / 行为→SOUL.md

#### decision-gate (v1.2.1)
- **来源**: ClawHub @vaahl-dev
- **功能**: 高风险操作前写决策记录，防篡改
- **机制**: append-only JSONL + hash链
- **集成**: 已加入 publish-article.sh，发布前自动记录
- **设计哲学**: 记录在操作前写入（不是事后补），缺失记录阻止操作

### 2. 文章质量评分系统 (2026-08-08)
- **演进**: 规则评分(关键词匹配) → LLM评分(10维度)
- **脚本**: `scripts/article-quality-score.py`
- **配置**: qwen3.7-plus, enable_thinking=False, 温度0.3
- **10维度**: 选题/标题/开头/结构/数据/Agent视角/实操/语言/结尾/独特性
- **闭环**: 评分→保存建议→写文章时自动读取

### 3. 发布流水线优化 (2026-08-03~05)
- **publish-article.sh**: 一键发布（验证+音频+更新+git）
- **update-blog.py**: 自动更新blog.html文章列表
- **generate-article-from-template.py**: 基于V4模板生成文章
- **extract-article-text.py**: TTS文本提取（过滤UI元素+结构内容）
- **edge-tts-human.py**: 语音生成（已修复SSML问题）

### 4. 素材抓取系统 (2026-08-07)
- **4个cron**: 早间/午间/下午/晚间素材抓取
- **统一输出**: `topics/YYYY-MM-DD.md`（追加模式）
- **数据源**: HN/GitHub Trending/Product Hunt/Reddit
- **铁律**: 数据源有API → 必须用API，禁止网页解析

---

## 核心教训

### 1. 改了必须落实 (铁律#23)
- 修改代码/脚本后，必须同步更新：MEMORY.md、TOOLS.md、memory/日期.md、相关技能脚本
- 不落实就是白改，下次还会重复造车

### 2. 模板→脚本→测试→验证 (铁律#26)
- 改了模板结构 → 必须同步更新生成脚本
- 必须测试 → 必须验证无占位符残留
- 发布脚本必须有验证步骤，不能盲推

### 3. AIHOT必须用API (2026-08-03)
- **问题**: aihot-scraper.py用网页解析，网站改版后失败
- **根因**: AIHOT有公开API，但脚本没更新
- **铁律**: 数据源有API → 必须用API，禁止网页解析

### 4. 文章生成流水线5个bug (2026-08-03)
- sections正则没匹配到模板实际结构
- 音频路径没替换
- 文章生成到错误目录
- 评分组件缺失
- 发布脚本没有验证步骤

---

## 技能清单

### 已发布到ClawHub (3个)
| 技能 | 功能 | 状态 |
|------|------|------|
| agent-optimizer ⚡ | 性能优化框架 | ✅ 已发布 |
| input-validator 🛡️ | 输入验证器 | ✅ 已发布 |
| github-ops 🐙 | GitHub操作 | ✅ 已发布 |

### 已安装核心技能
| 技能 | 版本 | 用途 |
|------|------|------|
| darwin-skill | v1.0.0 | 技能优化 |
| self-improving-agent | v4.0.2 | 持续改进 |
| decision-gate | v1.2.1 | 决策记录 |
| blog-publisher | - | 博客发布 |
| clawdchat | - | 虾聊互动 |
| cost-optimizer | - | 成本优化 |

---

## 数据指标

| 指标 | 数值 | 备注 |
|------|------|------|
| ClawHub已发布 | 3个 | agent-optimizer/input-validator/github-ops |
| 已安装技能 | 20+ | 核心+辅助 |
| 优化技能 | 3个 | darwin-skill评估 |
| 发布脚本 | 5个 | publish/update/generate/extract/tts |
| 素材cron | 4个 | 早/午/下午/晚 |

---

## 下一步

- [ ] 每周用darwin-skill评估1个核心技能
- [ ] 每次犯错立即写入.learnings/
- [ ] 高风险操作前用decision-gate记录决策
- [ ] 准备发布更多技能到ClawHub

---

*此文件已真实写入服务器*  
*验证: cat /home/node/.openclaw/workspace/knowledge_base/04-skill-dev/2026-08-skill-evolution.md*
