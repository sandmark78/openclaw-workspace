# OpenClaw Release v2026.3.13-1 (Recovery Release)

**发布日期**: 2026-03-14 18:04 UTC  
**类型**: 恢复版本 (Recovery Release)  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 📋 版本说明

此版本是为修复损坏的 v2026.3.13 标签/发布路径而创建的恢复版本。

**重要提示**:
- 此版本仅用于恢复 v2026.3.13 的发布路径
- npm 版本仍为 2026.3.13，不是 2026.3.13-1
- `-1` 后缀仅用于 Git 标签和 GitHub Release

---

## 🔧 核心修复

### 会话与压缩
- **fix(compaction)**: 使用完整会话 token 计数进行压缩后健全性检查 (#28347)
- **fix(session)**: 会话重置时保留 lastAccountId 和 lastThreadId (#44773)
- **fix(agents)**: 避免在大小写不敏感挂载上重复注入记忆文件 (#26054)
- **fix(agents)**: 重议会话重置提示以避免 Azure 内容过滤器 (#43403)
- **fix(agents)**: 在重放时删除 Anthropic thinking blocks (#44843)

### 通道与消息
- **fix(telegram)**: 将线程媒体传输策略纳入 SSRF (#44639)
- **fix**: 处理 Discord 网关元数据获取失败 (#44397)
- **fix**: 地址交付去重审查后续 (#44666)
- **fix(signal)**: 在 Signal 通道模式中添加 groups 配置 (#27199)

### 配置与兼容性
- **fix(config)**: 在代理兼容模式中为非原生 openai-completions 保留显式用户覆盖 (#44432)
- **fix(config)**: 在 agents.list[] 验证模式中添加缺失的 params 字段 (#41171)
- **fix**: 恢复运行时 zod 模式中的 web fetch firecrawl 配置 (#42583)
- **test(config)**: 在兼容模式固件中覆盖 requiresOpenAiAnthropicToolPayload (#43438)

### 移动端改进
- **feat(android)**: 重新设计聊天设置 UI (#44894)
- **fix(android)**: 在 TalkModeVoiceResolver 中修复 HttpURLConnection 泄漏 (#43780)
- **fix(android)**: 在 onboarding 中使用 Google Code Scanner 进行 QR 扫描 (#45021)
- **feat(ios)**: 添加 onboarding 欢迎分页器 (#45054)

### Docker 与部署
- **Docker**: 添加 OPENCLAW_TZ 时区支持 (#34119)

### 文档与 CLI
- **docs**: 将发布后变更日志条目移至 Unreleased (#44691)
- **CLI**: 对齐 xhigh thinking 帮助文本 (#44819)
- **docs**: 修复 xhigh 帮助的贡献者署名 (#44874)
- **docs**: 修复会话键 :dm: → :direct: (#26506)

### 测试与模型
- **测试**: 将默认模型从 openai-codex/gpt-5.3-codex 更新为 openai-codex/gpt-5.4 (#44367)

---

## 📊 统计

| 类别 | 数量 |
|------|------|
| 修复 (fix) | 15+ |
| 功能 (feat) | 3 |
| 文档 (docs) | 4 |
| 测试 (test) | 1 |
| 总 PR 数 | 20+ |

---

## 🎯 关键改进

### 对 Sandbot 团队的影响
1. **会话稳定性**: 会话重置时保留账户/线程 ID，减少重新配对需求
2. **Telegram 媒体**: 媒体传输策略改进，可能解决之前推送问题
3. **Docker 时区**: OPENCLAW_TZ 支持，便于容器化部署时区配置
4. **移动端体验**: Android/iOS onboarding 改进，便于新用户配对

### 建议行动
- ✅ 考虑升级到 v2026.3.13-1 (npm install -g openclaw@latest)
- ✅ 检查当前版本：`openclaw --version`
- ✅ 如使用 Docker，设置 OPENCLAW_TZ=Asia/Shanghai

---

## 🔗 相关链接

- GitHub Release: https://github.com/openclaw/openclaw/releases/tag/v2026.3.13-1
- npm 包: https://www.npmjs.com/package/openclaw (版本 2026.3.13)
- 完整变更日志: https://github.com/openclaw/openclaw/blob/main/CHANGELOG.md

---

*此文档由 Sandbot V6.3 自动创建*
*创建时间：2026-03-20 20:07 UTC*
*Cron Job: 1de12fc8-036c-4d24-b390-b8317a7a9dfe*
