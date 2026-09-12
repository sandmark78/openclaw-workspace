# OpenClaw 2026.9.2 发布记录

**抓取时间**: 2026-09-07 20:00 UTC
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🆕 2026.9.2 版本亮点

### 1. 更快更流畅的聊天体验
- 长 transcript 和磁盘处理时，聊天/仪表盘/会话交互保持响应
- 直接仪表盘查找、减少冷加载工作
- 持久化历史读取移至 Gateway 事件循环外
- 相关 PR: #136862, #138094, #138669, #138888, #138860, #138894

### 2. 可靠的升级和恢复
- 自动更新时保留活跃设置、启用的技能、默认 agent 所有权
- Git 更新后恢复 Gateway 重启
- 报告结果并提供可操作的恢复指导
- 相关 Issue: #138760
- 贡献者: @fuller-stack-dev, @jason-allen-oneal

### 3. GPT-6 Astra 支持 ⭐
- 模型选择: `openai/gpt-6-astra`
- 需要 OpenAI API key 或符合条件的 ChatGPT/Codex 账户
- 支持文本和图像输入
- 支持 Responses tool calls
- 支持推理控制 (reasoning controls)
- 相关 Issue: #137549

### 4. 回复在重启后存活
- Gateway 重启后恢复活跃、排队和委托的回复
- 防止一个已完成的回复丢弃另一个的恢复标记
- 保持 continuation instructions 通过压缩和重试

---

## 📊 ClawHub 热门技能 (2026-09-07 快照)

| 技能 | 作者 | 热度 |
|------|------|------|
| instagram-scraper | apidojo-io | 293 |
| tiktok-scraper | apidojo-io | 290 |
| google-maps-api | fetcher-sh | 219 |
| planning-with-files | othmanadi | 207 |
| youtube-api | fetcher-sh | 207 |
| remotion-best-practices | am-will | 201 |
| wisdom-accountability-coach | mikecourt | 171 |
| self-improving-agent | pskoett | 152 |
| iran-chem-database | orionshaowswmw | 143 |

新增/值得关注的:
- seedance-2-5-reference-to-video (genmedia-labs) - 参考引导的 1080p 视频生成
- ai-image-generation (genmedia-labs) - 11+ AI 模型图像生成
- reddit-automation (flowkit-labs) - Reddit 自动化

---

## 💡 对我们的意义

1. **GPT-6 Astra**: 如果老大想用，需要 OpenAI API key，目前我们用 bailian/qwen3.7-plus
2. **升级可靠性**: 自动更新保留设置和技能，对我们有用
3. **重启恢复**: 回复不丢失，提升用户体验
4. **planning-with-files 技能**: 值得研究，可能改进我们的任务管理
