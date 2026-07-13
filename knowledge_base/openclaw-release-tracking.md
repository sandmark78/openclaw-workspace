# OpenClaw 版本更新跟踪

**最后更新**: 2026-04-19 20:05 UTC
**当前运行版本**: 2026.3.8
**最新正式版**: 2026.4.15 (2026-04-16，已由 pre-release 转正)
**最新 beta**: 2026.4.19-beta.2 (2026-04-19 06:27 UTC，今天发布)

---

## 📌 v2026.4.14 (最新正式 Release)

发布日期：2026-04-14
重点：GPT-5 家族支持 + 渠道提供商改进 + 核心性能重构

### 新功能
- **OpenAI Codex**: 支持 gpt-5.4-pro（前瞻性兼容，含定价/限制/可见性）(#66453)
- **Telegram/forum topics**: 从 Telegram 论坛服务消息中学习人类可读的 topic 名称，展示在 agent 上下文中 (#65973)

### 修复
- **Agents/Ollama**: 修复 Ollama 本地模型慢运行时超时问题 (#63175)
- **Models/Codex**: 修复 apiKey 在 codex 提供者目录中缺失导致自定义模型被丢弃的问题 (#66180)
- **Tools/image+pdf**: 修复 Ollama 视觉模型被错误拒绝的问题 (#59943)
- **Slack/interactions**: 修复交互事件绕过 allowFrom 白名单的安全漏洞

---

## 📌 v2026.4.15 (最新正式 Release，2026-04-16 由 pre-release 转正)

发布日期：2026-04-16 21:50 UTC（latest release 确认）

### 新功能
- **Control UI/Overview**: 新增 Model Auth 状态卡片，显示 OAuth token 健康度和提供商限速压力 (#66211)
- **Memory/LanceDB**: 支持云存储，memory index 可跑在远程对象存储上 (#63502)
- **GitHub Copilot/memory search**: 新增 Copilot embedding provider 用于 memory search (#61718)
- **Agents/local models**: 新增 `experimental.localModelLean: true`，为弱本地模型去除重量级工具以减小 prompt 体积 (#66495)
- **Packaging/plugins**: 插件依赖本地化，减小发布体积 (#67099)

### 修复
- **Security/approvals**: 在 exec 审批 prompt 中脱敏密钥 (#64790)
- **CLI/configure**: 修复配置写入后 stale-hash 竞争问题 (#66528)
- **CLI/update**: 修复 npm 升级后残留 chunk 导致升级失败 (#66959)
- **Onboarding/CLI**: 修复全局 CLI 安装时在 onboarding 中的频道选择崩溃 (#66736)
- **Memory-core/QMD memory_get**: 限制 memory_get 只能读取标准记忆文件路径，防止被用作通用文件读取 (#66026)

---

## 📌 v2026.4.19-beta.2（最新 Beta，2026-04-19 今天发布）

发布日期：2026-04-19
重点：Agent 层修复（OpenAI 兼容后端 / 嵌套隔离 / Token 用量）

### 修复
- **Agents/openai-completions**: stream_options.include_usage 始终发送，自定义 OpenAI 兼容后端可报告真实上下文用量 (#68746)
- **Agents/nested lanes**: 嵌套 Agent 按目标会话隔离，解决 head-of-line blocking (#67785)
- **Agents/status**: 保留 session token 总计，提供商无用量元数据时仍显示最后已知值 (#67695)
- **Install/update**: 遗留升级验证与 QA Lab runtime shim 兼容

---

## 📌 ClawHub 生态
- 域名已转向 clawhub.ai
- 定位：AI agent 技能的版本化注册表（类似 npm）
- 安装方式：`npx clawhub@latest install <skill>`
- 有 Staff Picks 和 Popular skills 分类

## 📌 待升级检查
- [ ] 从 2026.3.8 → 2026.4.15 升级影响评估
- [ ] 关注 2026.4.19-beta.2 转正时间（嵌套 Agent 隔离 + Token 用量修复值得关注）
- [ ] Telegram forum topics 特性对我们 (@sand66_bot) 的影响
- [ ] gpt-5.4-pro 支持对我们模型配置的影响
- [ ] Claude Opus 4.7 作为默认 image understanding 模型的影响
- [ ] Gemini TTS 集成（新增语音回复能力）
