# OpenClaw GitHub Release - 2026-04-12

**抓取时间**: 2026-04-12 20:00 UTC  
**发布日期**: 2026-04-12 00:18 UTC  
**类型**: 正式 release (由 4月11日 pre-release 提升)

---

## 新特性 (Changes)

| 模块 | 内容 | PR |
|------|------|-----|
| Dreaming/记忆 Wiki | ChatGPT 导入、Imported Insights、Memory Palace 日记子标签 | #64505 |
| Control UI/Webchat | 媒体/语音回复结构化聊天气泡、`[embed ...]` 富输出标签 | #64104 |
| 视频生成工具 | URL-only 资产交付、类型化 providerOptions、参考音频输入、自适应宽高比 | #61987, #61988 |
| 飞书 | 文档评论增强：评论反应、打字反馈、上下文解析 | #63785 |
| Microsoft Teams | 反应支持、Graph 分页、委托 OAuth 设置 | #51646 |
| 插件系统 | manifest 可声明激活和设置描述符 | #64780 |
| Ollama | 模型发现时缓存 context-window 和能力元数据 | #64753 |
| Models/Providers | OpenAI 兼容端点分类在 debug 日志中可见 | #64754 |
| QA/Parity | GPT-5.4 vs Opus 4.6 agentic parity 报告门 | #64441 |

## Bug 修复 (Fixes)

| 模块 | 修复内容 | PR |
|------|----------|-----|
| OpenAI/Codex OAuth | 修复 invalid_scope 错误 | #64713 |
| 音频转录 | 修复 OpenAI/Groq/Mistral 转录 DNS 问题 | #64766 |
| macOS Talk Mode | 首次麦克风授权后无需二次切换 | #62459 |
| Webchat TTS | TTS 音频回复持久化到聊天历史 | #63514 |
| WhatsApp | 修复默认账户注册问题 | #53918 |
| ACP/Agents | 抑制子 Agent 内部进度泄露到父会话 | (未编号) |
| Agents/Timeouts | 正确遵循 LLM 空闲看门狗超时配置 | (未编号) |
| Config | asyncCompletion 加入生成的 zod schema | #63618 |
| Google/Veo | 移除不支持的 numberOfVideos 字段 | #64723 |
| QA/Packaging | 修复打包 CLI 启动和 completion cache 问题 | #64648 |
| Codex/QA | 防止 Codex 应用服务器协调泄露到可见回复 | (未编号) |
| WhatsApp | 反应消息走 gateway-owned action 路径 | (未编号) |
| WhatsApp 自动回复 |  inbound 图片附件路径保留 | #64918 |
| **Telegram/ Sessions** | **topic-scoped session 初始化路径修复，避免在 bare 和 topic-qualified 之间交替** | **#64869** |
| Agents/Failover | 修复跨 provider fallback 继承旧失败的问题 | #62907 |
| MiniMax/OAuth | configure 时写入正确的 auth 配置 | #64964 |

---

## 与 4月11日 pre-release 的差异

4月12日正式版比 4月11日 pre-release **新增了以下修复**（昨天未记录）：

- **Telegram/ Sessions** (#64869): topic-scoped session 初始化路径修复 — **与我们直接相关**
- **WhatsApp 自动回复** (#64918): inbound 图片附件路径保留
- **Agents/Failover** (#62907): 跨 provider fallback 错误继承修复
- **MiniMax/OAuth** (#64964): configure 时 auth 配置修复
- **ACP/Agents**: 子 Agent 进度泄露抑制
- **Agents/Timeouts**: LLM 超时配置修复
- **Config**: asyncCompletion zod schema 修复
- **Google/Veo**: numberOfVideos 字段移除
- **QA/Packaging**: 打包 CLI 修复
- **Codex/QA**: 协调泄露修复
- **WhatsApp**: 反应消息路由修复

---

## 建议行动
1. 🔧 **关注 #64869 (Telegram topic sessions)** — 可能影响我们的 topic 会话行为
2. ⬆️ 考虑升级到正式 release
3. 📝 升级前备份 openclaw.json
