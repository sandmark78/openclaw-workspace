# 工具系统进化 (2026-04~08)

**更新时间**: 2026-08-09  
**覆盖周期**: 2026-04-01 ~ 2026-08-09

---

## 关键进展

### 1. 脚本体系完善 (2026-08-09)

#### 发布流水线
| 脚本 | 功能 | 状态 |
|------|------|------|
| publish-article.sh | 一键发布（验证+音频+更新+git） | ✅ |
| update-blog.py | 自动更新blog.html文章列表 | ✅ |
| update-index.py | 更新首页 | ✅ |
| generate-article-from-template.py | 基于V4模板生成文章 | ✅ |

#### 质量系统
| 脚本 | 功能 | 状态 |
|------|------|------|
| article-quality-score.py | LLM 10维度评分 | ✅ |
| check-topic-duplicate.py | 选题去重检查 | ✅ |
| get-recent-improvements.sh | 读取最近改进建议 | ✅ |

#### 音频系统
| 脚本 | 功能 | 状态 |
|------|------|------|
| edge-tts-human.py | 语音生成（已修复SSML） | ✅ |
| extract-article-text.py | TTS文本提取（过滤UI元素） | ✅ |
| regenerate-audio.sh | 重新生成音频 | ✅ |

#### 素材抓取
| 脚本 | 功能 | 状态 |
|------|------|------|
| aihot-scraper.py | AIHOT素材抓取（已改用API） | ✅ |
| news-aggregator.py | 多源聚合（含AIHOT） | ✅ |

#### 安全工具
| 脚本 | 功能 | 状态 |
|------|------|------|
| input-validator.py | 输入验证（91分） | ✅ |
| decision-gate-wrapper.py | 决策记录封装 | ✅ |

### 2. API调用优化 (2026-07-10)
- **问题**: 文章Cron触发API rate limit
- **优化**: 创建脚本合并操作，8-9次调用→3次
- **铁律**: 每个任务不超过3次调用

### 3. 工具使用规范 (2026-08-09)
```
铁律：
- 数据源有API → 必须用API，禁止网页解析
- 每个任务不超过3次调用
- 合并多个操作到一个脚本
- 一次性完成，不要重试
- 不要多次读取同一个文件
```

---

## 核心教训

### 1. AIHOT必须用API (2026-08-03)
- **问题**: aihot-scraper.py用网页解析，网站改版后失败
- **根因**: AIHOT有公开API，但脚本没更新
- **铁律**: 数据源有API → 必须用API，禁止网页解析

### 2. 文章生成流水线5个bug (2026-08-03)
- sections正则没匹配到模板实际结构
- 音频路径没替换
- 文章生成到错误目录
- 评分组件缺失
- 发布脚本没有验证步骤
- **教训**: 改了模板结构 → 必须同步更新生成脚本 → 必须测试 → 必须验证

### 3. 验证循环浪费token (2026-08-03)
- **问题**: 完成编辑后陷入"验证-确认-再验证"循环
- **教训**: "验证一次就够，做完就说已完成"

### 4. 中文引号导致JavaScript语法错误 (2026-07-12)
- **问题**: excerpt字段中有未转义的中文引号
- **教训**: JavaScript字符串中的中文引号必须转义
- **应对**: update-blog.py新增escape_js_string()函数

### 5. TTS播客问题 (2026-07-12)
- **问题**: TTS会读出UI元素和结构性内容
- **教训**: TTS提取必须过滤所有UI元素和结构性内容
- **应对**: extract-article-text.py过滤13种UI元素

---

## 数据指标

| 指标 | 数值 | 备注 |
|------|------|------|
| 发布脚本 | 4个 | publish/update/generate/update-index |
| 质量脚本 | 3个 | score/check-duplicate/get-improvements |
| 音频脚本 | 3个 | edge-tts/extract-text/regenerate |
| 素材脚本 | 2个 | aihot-scraper/news-aggregator |
| 安全脚本 | 2个 | input-validator/decision-gate-wrapper |
| 总脚本数 | 14个 | 核心工具 |

---

## 下一步

- [ ] 定期用darwin-skill评估工具脚本
- [ ] 每次修改脚本后同步更新文档
- [ ] 建立脚本测试用例库

---

*此文件已真实写入服务器*  
*验证: cat /home/node/.openclaw/workspace/knowledge_base/12-tools/2026-08-tools-evolution.md*
