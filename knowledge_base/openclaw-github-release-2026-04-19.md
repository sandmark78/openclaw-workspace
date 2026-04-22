# OpenClaw GitHub Release 2026.4.19-beta.1 & beta.2

**抓取时间**: 2026-04-19 20:05 UTC  
**发布时间**: 2026-04-19 02:15 UTC (beta.1) & 06:27 UTC (beta.2)  
**版本**: 预发布版本（Pre-release）  
**当前运行**: 2026.3.8（落后 2 个大版本）  
**最新正式版**: 2026.4.15（2026-04-16 发布）

---

## 2026.4.19-beta.2（最新，今天发布）

### 修复 (Fixes)

#### 🤖 Agents/openai-completions — 上下文用量显示修复
- **stream_options.include_usage**: 流式请求始终发送此参数，让本地/自定义 OpenAI 兼容后端报告真实上下文用量，不再显示 0%
- PR: [#68746](https://github.com/openclaw/openclaw/pull/68746) | Thanks @kagura-agent

#### 🤖 Agents/nested lanes — 嵌套 Agent 隔离
- **按目标会话限定嵌套 Agent 工作范围**，一个会话中长时间运行的嵌套 Agent 不再阻塞 Gateway 中其他不相关会话
- 解决 head-of-line blocking 问题
- PR: [#67785](https://github.com/openclaw/openclaw/pull/67785) | Thanks @stainlu

#### 📊 Agents/status — Token 用量持久化
- **保留向前传递的 session token 总计**，当提供商不提供用量元数据时，/status 和 openclaw sessions 命令继续显示最后已知的上下文用量，而非回退到 unknown/0%
- PR: [#67695](https://github.com/openclaw/openclaw/pull/67695) | Thanks @stainlu

#### 🔧 Install/update — 升级兼容性
- **保持遗留升级验证与 QA Lab runtime shim 兼容**，从旧全局安装升级到 beta 时不再在 npm 成功安装包后失败

---

## npm 版本时间线（截至 2026-04-19）

| 版本 | 发布时间 | 类型 |
|------|----------|------|
| 2026.4.15 | 2026-04-16 22:11 UTC | ✅ 最新正式版 |
| 2026.4.19-beta.1 | 2026-04-19 02:15 UTC | ⚠️ 预发布 |
| 2026.4.19-beta.2 | 2026-04-19 06:27 UTC | ⚠️ 预发布（最新） |

---

## 📊 ClawHub 生态数据（2026-04-19）

- **域名**: clawhub.com → clawhub.ai（重定向）
- **Stats**: 52.7k tools / 180k users / 12M downloads / 4.8 avg rating
- **定位**: AI agent 技能的版本化注册表（类似 npm for skills）

---

## 与上次跟踪对比

上次跟踪 (2026-04-15-16) 后的变化:
- ✅ 新增 2026.4.19-beta.1 + beta.2（均为今天发布）
- ✅ 聚焦 Agent 层修复：OpenAI 兼容后端、嵌套 Agent 隔离、Token 用量显示
- ❌ ClawHub 无显著变化
- ❌ docs.openclaw.ai 无显著变化
