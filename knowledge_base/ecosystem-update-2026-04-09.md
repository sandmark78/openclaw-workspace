# OpenClaw 生态探索 - 2026-04-09 20:00 UTC

## 🆕 重大发现：OpenClaw v2026.4.9 已发布

**当前安装版本**: 2026.3.8
**最新可用版本**: 2026.4.9 (2026-04-09 02:41 UTC)
**版本差距**: 11 个版本跨度 (4.1 → 4.9)
**来源**: https://github.com/openclaw/openclaw/releases

---

## v2026.4.9 更新内容 (2026-04-09)

### 🧠 Memory/Dreaming 重大改进
- **Grounded REM backfill lane**: 历史 REM harness --path 支持
- **Diary commit/reset flows**: 日记提交/重置流
- **Durable fact extraction**: 更干净的持久事实提取
- **Live short-term promotion**: 短期记忆提升到长期记忆集成
- **Structured diary view**: 结构化日记视图 + 时间线导航
- **Backfill/reset controls**: 回溯/重置控制
- **Traceable dreaming summaries**: 可追溯的梦境摘要
- **Grounded Scene lane**: 带提升提示的 Scene lane + 安全清除动作

### 🧪 QA/Lab
- **Character-vibes evaluation reports**: 角色风格评估报告
- **Model selection + parallel runs**: 模型选择 + 并行运行
- **Live QA 对比候选行为**: 更快的 QA 测试

### 🔌 Plugins/Provider-Auth
- **providerAuthAliases**: 提供商变体可共享环境变量、认证配置文件
- **Config-backed auth**: 配置支持的认证
- **API-key onboarding choices**: API 密钥引导选择

### 📱 iOS
- **CalVer 版本固定**: apps/ios/version.json 明确 CalVer 版本
- **TestFlight iteration**: 同一短版本保持 TestFlight 迭代
- **pnpm ios:version:pin**: 文档化的版本发布流程

### 🛡️ 安全修复 (重要！)
1. **Browser SSRF**: 交互后重新运行 blocked-destination 安全检查 (#63226)
2. **dotenv 安全**: 阻止不可信 workspace .env 的运行时控制环境变量 (#62660, #62663)
3. **Node exec 事件**: 标记远程节点 exec 事件为不可信并清理输出 (#62659)
4. **Onboarding auth**: 防止不可信插件与内置提供商 auth-choice 冲突 (#62368)
5. **依赖升级**: basic-ftp 5.2.1 (CRLF 命令注入修复) + Hono 升级

### 🐛 Bug 修复
- **Android 配对**: 清除过期 setup-code，QR 扫描后引导新会话 (#63199)
- **Matrix 网关**: 等待同步就绪再标记启动成功 (#62779)
- **Slack 媒体**: 保留 files.slack.com 重定向的 bearer auth (#62960)

---

## 📊 版本发布节奏 (2026-04)
| 版本 | 发布日期 | 备注 |
|------|----------|------|
| 2026.4.1 | 2026-04-01 | 月初版本 |
| 2026.4.2 | 2026-04-02 | 日更新 |
| 2026.4.5 | 2026-04-06 | 大版本 (视频/音乐生成) |
| 2026.4.7 | 2026-04-08 | 日更新 |
| 2026.4.8 | 2026-04-08 | 日更新 |
| **2026.4.9** | **2026-04-09** | **Memory Dreaming 大改进 + 安全修复** |

---

## 📌 建议行动
1. **⚠️ 强烈建议升级** - 当前 2026.3.8 落后 11 个版本
2. **安全修复紧急** - SSRF、dotenv 注入、exec 事件清理都是严重安全修复
3. **Memory Dreaming** - 新功能的完整实现值得升级体验
4. **升级命令**: `npm update -g openclaw` 或重新运行 install 脚本

---

## ClawHub
- 域名: clawhub.ai (原 clawhub.com 重定向)
- 状态: 正常，无重大变化
- 技能浏览功能正常工作

## Docs
- 文档结构稳定
- 新增内容: Memory Dreaming 相关文档可能在更新中

---

*生成时间: 2026-04-09 20:01 UTC*
*下次探索: 自动 cron 任务*
