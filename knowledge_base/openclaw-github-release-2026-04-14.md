# OpenClaw GitHub Release 2026.4.14

**抓取时间**: 2026-04-14 20:00 UTC  
**发布时间**: 2026-04-14 13:03 UTC  
**版本**: 2026.4.14 — Broad Quality Release  
**当前运行**: 2026.3.8（落后一个大版本）

> 继 4.12 之后的又一质量提升版本，聚焦模型提供商和通道提供商问题修复。

---

## 新特性 (Changes)

### 🧠 OpenAI Codex/Models
- **GPT-5.4-pro 前向兼容支持**
- 包含 Codex 定价/限制设置
- 在上游目录更新前即可通过 list/status 可见
- PR: [#66453](https://github.com/openclaw/openclaw/pull/66453) | Thanks @jepson-liu

### 💬 Telegram/Forum Topics
- **在 Agent 上下文中展示人类 Topic 名称**
- 通过 Telegram 论坛服务消息学习 Topic 名称
- 包含 prompt 元数据和 plugin hook 元数据
- PR: [#65973](https://github.com/openclaw/openclaw/pull/65973) | Thanks @ptahdunbar
- **Topic 名称持久化**: 重启后仍可使用人类 Topic 名称，无需重新学习
- PR: [#66107](https://github.com/openclaw/openclaw/pull/66107) | Thanks @obviyus

---

## 修复 (Fixes)

### 🔧 Agents/Ollama
- 将配置的 embedded-run timeout 转发到全局 undici stream timeout 调优
- 解决慢速本地 Ollama 运行不再继承默认 stream 截断的问题
- Issue: [#63175](https://github.com/openclaw/openclaw/issues/63175)

### 🤖 Models/Codex
- Codex provider 目录输出包含 apiKey
- 防止 Pi ModelRegistry 验证器拒绝条目并静默丢弃所有自定义模型
- PR: [#66180](https://github.com/openclaw/openclaw/pull/66180) | Thanks @hoyyeva

### 🖼️ Tools/Image+PDF
- 标准化配置的 provider/model refs 再进行媒体工具注册表查找
- 修复 image/PDF 工具因跳过 model-ref 标准化而拒绝有效 Ollama 视觉模型的问题
- Issue: [#59943](https://github.com/openclaw/openclaw/issues/59943)

### 💬 Slack/Interactions
- **安全加固**: 将全局 allowFrom 所有者白名单应用于频道 block-action 和 modal 交互事件
- 要求预期的 sender id 进行交叉验证
- 拒绝模糊的频道类型，防止交互触发绕过文档化的白名单意图
- PR: [#66028](https://github.com/openclaw/openclaw/pull/66028) | Thanks @eleqtrizit

### 📎 Media/Attachments
- **安全加固**: 当本地附件路径无法通过 realpath 规范解析时 fail closed
- 防止 realpath 错误降级 canonical-roots 白名单检查为非规范比较
- 有 URL 的附件仍回退到网络获取路径
- PR: [#66022](https://github.com/openclaw/openclaw/pull/66022) | Thanks @eleqtrizit

### 🔒 Agents/Gateway-Tool
- **重大安全加固**: 拒绝 model-facing gateway tool 的 config.patch/config.apply 调用
- 当调用会新启用安全审计标记的危险 flag 时拒绝（如 dangerouslyDisableDeviceAuth, allowInsecureAuth, dangerouslyAllowHostHeaderOriginFallback, hooks.gmail.allowUnsafeExternalContent, tools.exec.applyPatch.workspaceOnly: false）
- 已启用的 flag 不受影响，直接认证的 operator RPC 行为不变
- PR: [#62006](https://github.com/openclaw/openclaw/pull/62006) | Thanks @eleqtrizit

### 🎨 Google Image Generation
- 修复调用原生 Gemini image API 时移除配置的 Google base URL 末尾的 /openai 后缀
- 解决 Gemini 图像请求 404 问题，同时不影响显式 OpenAI 兼容的 Google 端点
- PR: [#66445](https://github.com/openclaw/openclaw/pull/66445) | Thanks @dapzthelegend

---

## 与 4.12 的差异

| 4.12 新增 | 4.14 新增 |
|---|---|
| Active Memory 插件 | GPT-5.4-pro 兼容 |
| exec-policy CLI | Telegram Topic 名称持久化 |
| MLX 本地语音 | Ollama timeout 修复 |
| Gateway commands.list RPC | Codex apiKey 修复 |
| Matrix MSC4357 | Image/PDF tool 标准化 |
| Multipass QA runner | **Slack 交互安全加固** |
| Docs i18n | **Gateway 工具安全加固** |
| | Google image URL 修复 |
| | **附件 realpath 安全修复** |

---

## 对我们的影响评估

### 🔴 安全相关（值得关注）
1. **Gateway 工具安全加固** (#62006) - 防止通过模型调用启用危险 flag，这是重要的安全补丁
2. **Slack 交互安全加固** (#66028) - 防止交互触发绕过白名单
3. **附件 realpath 安全修复** (#66022) - 防止路径绕过

### 💡 功能相关
1. **GPT-5.4-pro 兼容** - 如果用 OpenAI/Codex 模型值得注意
2. **Telegram Topic 名称** - 我们使用 Telegram，重启后 Topic 名称不再丢失
3. **Image/PDF tool 修复** - 如果用 Ollama 视觉模型会有改善

### 升级建议
- 当前 2026.3.8 → 最新 2026.4.14，落后约一个月
- 包含多项安全加固，建议升级
- 升级前备份 openclaw.json
- 注意 Active Memory 插件可能需要额外配置

---

*记录时间: 2026-04-14 20:00 UTC*
*下次检查: 心跳/下次生态探索任务*
