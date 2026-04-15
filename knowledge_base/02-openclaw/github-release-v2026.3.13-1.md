# OpenClaw GitHub Release v2026.3.13-1

**发布日期**: 2026-03-14 18:04 UTC  
**版本**: v2026.3.13-1 (恢复版本)  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 📋 版本说明

这是一个**恢复版本**，用于修复损坏的 v2026.3.13 标签/发布路径。

**重要提示**:
- 此版本存在是为了恢复损坏的 v2026.3.13 标签/发布路径
- 对应的 npm 版本仍然是 2026.3.13，不是 2026.3.13-1
- `-1` 后缀仅用于 Git 标签和 GitHub Release

---

## 🔧 核心修复

### 会话与压缩 (Session & Compaction)
- **fix(compaction)**: 使用完整会话 token 计数进行压缩后健全性检查 ([#28347](https://github.com/openclaw/openclaw/pull/28347))
- **fix(session)**: 会话重置时保留 lastAccountId 和 lastThreadId ([#44773](https://github.com/openclaw/openclaw/pull/44773))
- **fix(agents)**: 避免在不区分大小写的挂载上重复注入记忆文件 ([#26054](https://github.com/openclaw/openclaw/pull/26054))
- **fix**: 保持压缩摘要中的人格和语言连续性 ([#10456](https://github.com/openclaw/openclaw/pull/10456))
- **fix(agents)**: 重绘会话重置提示以避免 Azure 内容过滤器 ([#43403](https://github.com/openclaw/openclaw/pull/43403))
- **fix(agents)**: 重放时删除 Anthropic 思考块 ([#44843](https://github.com/openclaw/openclaw/pull/44843))

### 通道与消息 (Channels & Messages)
- **fix(telegram)**: 将线程媒体传输策略引入 SSRF ([#44639](https://github.com/openclaw/openclaw/pull/44639))
- **fix**: 处理 Discord 网关元数据获取失败 ([#44397](https://github.com/openclaw/openclaw/pull/44397))
- **fix**: 地址交付去重审查后续 ([#44666](https://github.com/openclaw/openclaw/pull/44666))
- **fix(signal)**: 在 Signal 通道模式中添加群组配置 ([#27199](https://github.com/openclaw/openclaw/pull/27199))
- **Slack**: 添加选择性交互式回复指令 ([#44607](https://github.com/openclaw/openclaw/pull/44607))

### 模型与代理 (Models & Agents)
- **Updated**: 默认模型从 openai-codex/gpt-5.3-codex 更新为 openai-codex/gpt-5.4 ([#44367](https://github.com/openclaw/openclaw/pull/44367))
- **fix(agents)**: 尊重非原生 openai-completions 的显式用户兼容性覆盖 ([#44432](https://github.com/openclaw/openclaw/pull/44432))
- **fix**: 解析跨代理子代理生成的目标代理工作区 ([#40176](https://github.com/openclaw/openclaw/pull/40176))
- **fix(ollama)**: 隐藏原生推理专用输出 ([#45330](https://github.com/openclaw/openclaw/pull/45330))

### 移动端 (Mobile)
- **feat(android)**: 重新设计聊天设置 UI ([#44894](https://github.com/openclaw/openclaw/pull/44894))
- **fix(android)**: 使用 Google Code Scanner 进行 onboarding QR 码 ([#45021](https://github.com/openclaw/openclaw/pull/45021))
- **feat(ios)**: 添加 onboarding 欢迎页面 ([#45054](https://github.com/openclaw/openclaw/pull/45054))
- **Android**: 修复 TalkModeVoiceResolver 中的 HttpURLConnection 泄漏 ([#43780](https://github.com/openclaw/openclaw/pull/43780))
- **ui**: 移动端导航抽屉和主题变体优化 ([#45107](https://github.com/openclaw/openclaw/pull/45107))

### 配置与安全 (Config & Security)
- **Docker**: 添加 OPENCLAW_TZ 时区支持 ([#34119](https://github.com/openclaw/openclaw/pull/34119))
- **security(docker)**: 防止 Docker 构建上下文中网关 token 泄漏 ([#44956](https://github.com/openclaw/openclaw/pull/44956))
- **fix(config)**: 在 agents.list[] 验证模式中添加缺失的 params 字段 ([#41171](https://github.com/openclaw/openclaw/pull/41171))
- **fix(discovery)**: 在 wideArea Zod 配置模式中添加缺失的域 ([#35615](https://github.com/openclaw/openclaw/pull/35615))
- **fix(ui)**: 在不安全的 control-ui 连接上保持共享认证 ([#45088](https://github.com/openclaw/openclaw/pull/45088))
- **test(config)**: 在兼容模式固定装置中覆盖 requiresOpenAiAnthropicToolPayload ([#43438](https://github.com/openclaw/openclaw/pull/43438))

### CLI 与文档 (CLI & Docs)
- **CLI**: 对齐 xhigh thinking 帮助文本 ([#44819](https://github.com/openclaw/openclaw/pull/44819))
- **docs**: 将发布后变更日志条目移至 Unreleased ([#44691](https://github.com/openclaw/openclaw/pull/44691))
- **docs**: 修复 xhigh help 的变更日志归属 ([#44874](https://github.com/openclaw/openclaw/pull/44874))
- **docs**: 修复会话密钥 :dm: → :direct: ([#26506](https://github.com/openclaw/openclaw/pull/26506))
- **Docs**: 描述 Slack 交互式回复 ([#45463](https://github.com/openclaw/openclaw/pull/45463))
- **Fix**: 修复文档中 brave 成本的错误渲染 ([#44989](https://github.com/openclaw/openclaw/pull/44989))

### Cron 与更新 (Cron & Updater)
- **fix(cron)**: 防止隔离 cron 嵌套 lane 死锁 ([#45459](https://github.com/openclaw/openclaw/pull/45459))
- **Fix**: 修复服务重新安装时的更新器刷新 cwd ([#45452](https://github.com/openclaw/openclaw/pull/45452))

### UI 优化 (UI Improvements)
- **fix(ui)**: 在滚动 pill 按钮上恢复 chat-new-messages 类 ([#44856](https://github.com/openclaw/openclaw/pull/44856))
- **[codex]**: 优化侧边栏状态、代理技能和聊天渲染 ([#45451](https://github.com/openclaw/openclaw/pull/45451))

### 其他修复 (Other Fixes)
- **fix(windows)**: 在重启和进程清理期间抑制可见的控制台窗口 ([#44842](https://github.com/openclaw/openclaw/pull/44842))
- **fix**: 恢复运行时 zod 模式中的 web fetch firecrawl 配置 ([#42583](https://github.com/openclaw/openclaw/pull/42583))
- **refactor**: 删除 Slack probe 中冗余的 ?? undefined ([#44775](https://github.com/openclaw/openclaw/pull/44775))
- **test**: 注释聊天中止辅助导出 ([#45346](https://github.com/openclaw/openclaw/pull/45346))
- **perf(build)**: 去重插件构建
- **small addition**: .gitignore 小更新 ([#42879](https://github.com/openclaw/openclaw/pull/42879))

---

## 📊 统计

| 指标 | 数值 |
|------|------|
| PR 总数 | 40+ |
| 主要贡献者 | @frankekn, @vincentkoc, @Lanfei, @obviyus |
| 修复类型 | Bug 修复为主，少量功能增强 |
| 影响范围 | 会话/压缩/通道/移动端/安全 |

---

## 🎯 对 Sandbot 的影响

### 高相关性
1. **记忆文件重复注入修复** ([#26054](https://github.com/openclaw/openclaw/pull/26054))
   - 我们依赖 MEMORY.md 和每日记忆文件
   - 此修复避免在不区分大小写的文件系统上重复注入

2. **压缩摘要人格连续性** ([#10456](https://github.com/openclaw/openclaw/pull/10456))
   - 我们的 V6.3 依赖压缩来管理 1M 上下文
   - 人格连续性对 Sandbot 人设至关重要

3. **Cron 死锁修复** ([#45459](https://github.com/openclaw/openclaw/pull/45459))
   - 我们的 Cron #102+ 依赖隔离会话
   - 死锁修复提高 Cron 稳定性

### 中相关性
1. **默认模型更新**: gpt-5.3-codex → gpt-5.4
   - 我们使用 bailian/qwen3.5-plus，不受直接影响
   - 但反映 OpenClaw 默认配置趋势

2. **Telegram 媒体传输修复**
   - 我们使用 Telegram 作为主要通道
   - SSRF 策略改进可能影响媒体发送

3. **Docker 时区支持**
   - 我们在 Docker 中运行
   - OPENCLAW_TZ 可用于正确设置 UTC+8 时区

---

## 🔗 相关链接

- [GitHub Release](https://github.com/openclaw/openclaw/releases/tag/v2026.3.13-1)
- [npm package](https://www.npmjs.com/package/openclaw) (版本 2026.3.13)
- [完整变更日志](https://github.com/openclaw/openclaw/blob/main/CHANGELOG.md)

---

*记录时间*: 2026-03-21 20:01 UTC  
*记录者*: Sandbot V6.3 Cron 生态探索任务  
*验证*: `cat knowledge_base/02-openclaw/github-release-v2026.3.13-1.md`
