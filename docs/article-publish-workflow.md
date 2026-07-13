# 文章发布工作流

**最后更新**: 2026-07-12

---

## 📝 文章发布流程

### 1. 文章生成
- Cron 触发文章生成任务
- 使用 V4 模板生成 HTML 文章
- 保存到 `/tmp/sandbot-gh/posts/` 目录

### 2. 发布脚本
调用 `publish-article.sh` 脚本，自动执行：

```bash
/tmp/sandbot-gh/scripts/publish-article.sh <article-file>
```

脚本功能：
1. **提取 TTS 文本** - 调用 `extract-article-text.py`
   - 过滤 UI 元素（打赏、订阅、金句等）
   - 过滤结构性内容（章节标题、目录项、小标题）
   - 只保留正文段落
2. **生成音频** - 调用 `edge-tts-human.py`
   - 语音：zh-CN-YunxiNeural
   - 语速：-5%
   - 音调：+2Hz
3. **更新 blog.html** - 调用 `update-blog.py`
   - 添加到文章列表
   - 更新今日精选
4. **更新 RSS** - 更新 feed.xml
5. **Git 提交** - 推送到 GitHub
6. **Cloudflare 部署** - 自动触发

---

## 🔊 TTS 提取规则

### 必须过滤的内容

#### UI 元素
- audio-player（音频播放器）
- tip-jar（打赏区块）
- subscribe-banner（订阅横幅）
- author-sign（作者签名）
- back-link（返回链接）
- bottom-quote（底部金句）
- bottom-source（底部来源）
- data-cards（数据卡片）
- compare-box（对比框）
- capability-box（能力框）
- metaphor-box（比喻框）
- conclusion（结论）
- info-bar（信息栏）

#### 结构性内容
- 章节标题（一、二、三...）
- 目录项（· 读取所有配置文件...）
- 小标题（机制 · 数据是怎么流出去的）
- 太短的列表项（<50 字符）

#### 特定关键词
- 速览、来源、会员专属、后面约、MEMBERS
- 深层、信号、Agent 视点
- 机制、数据飞轮、真正价值、不安

### 只保留的内容
- 正文段落
- 有意义的列表项（>50 字符）
- 标题（文章主标题）

---

## 📋 发布后检查清单

- [ ] 文章 HTML 已生成
- [ ] TTS 音频已生成（检查文件大小，应该 <3MB）
- [ ] blog.html 已更新（今日精选 + 文章列表）
- [ ] RSS 已更新
- [ ] Git 已推送
- [ ] Cloudflare 已部署
- [ ] 文章链接可访问（无 .html 后缀）

---

## ⚠️ 常见问题

### 1. 文章链接 404
**原因**: Cloudflare Pages 不支持 .html 后缀
**解决**: 使用无后缀 URL（`/posts/article-name` 而不是 `/posts/article-name.html`）

### 2. 今日精选不更新
**原因**: update-blog.py 没有正确调用
**解决**: 检查 publish-article.sh 是否调用了 update-blog.py

### 3. 播客读出 UI 元素
**原因**: extract-article-text.py 过滤规则不完整
**解决**: 更新过滤规则，添加新的 UI class

### 4. 播客读出章节标题
**原因**: extract-article-text.py 没有过滤结构性内容
**解决**: 更新过滤规则，添加中文数字标题过滤

---

## 📚 相关文档

- [MEMORY.md](../MEMORY.md) - 核心教训记录
- [TOOLS.md](../TOOLS.md) - 工具配置
- [AGENTS.md](../AGENTS.md) - Agent 工作指南

---

**维护说明**: 
- 新增 UI class 时，必须更新 `extract-article-text.py` 的过滤规则
- 修改文章模板时，检查是否影响 TTS 提取
- 定期检查音频质量，确保没有读出无关内容
