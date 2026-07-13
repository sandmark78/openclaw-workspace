# OpenClaw Release 2026-03-29 - Breaking Changes & Major Updates

**发布日期**: 2026-03-29 01:34 UTC  
**来源**: https://github.com/openclaw/openclaw/releases  
**类型**: Breaking Change (破坏性更新)

---

## 🔴 破坏性变更 (Breaking Changes)

### 1. Qwen Provider 迁移 (#52709)
- **变更**: 移除已弃用的 `qwen-portal-auth` OAuth 集成 (portal.qwen.ai)
- **迁移**: 使用 `openclaw onboard --auth-choice modelstudio-api-key` 迁移到 Model Studio
- **影响**: 使用 Qwen 门户 OAuth 的用户需要重新配置 API Key
- **贡献者**: @pomelo-nwu

### 2. Config/Doctor 清理
- **变更**: 删除超过两个月的自动配置迁移
- **影响**: 非常旧的遗留密钥现在会在加载时验证失败，而不是被自动重写
- **命令**: `openclaw doctor` 不再支持旧密钥迁移

---

## 🟢 新功能与改进

### xAI 集成增强 (#56048)
- **变更**: 将捆绑的 xAI provider 迁移到 Responses API
- **新增**: 添加一等公民的 `x_search` 支持
- **自动启用**: xAI 插件从拥有的 web-search 和工具配置自动启用
- **影响**: 捆绑的 Grok web-search 插件无需手动切换即可工作
- **Onboarding**: `openclaw onboard` 和 `openclaw configure --section web` 提供可选的 x_search 设置
- **贡献者**: @huntharo

### MiniMax 图像生成 (#54487)
- **新增**: 添加图像生成 provider (image-01 模型)
- **功能**: 支持生成和图像到图像编辑
- **控制**: 支持宽高比控制
- **贡献者**: @liyuan97

### 插件工具调用审批 (#55339)
- **新增**: `before_tool_call` hooks 中添加异步 `requireApproval`
- **功能**: 插件可以暂停工具执行并通过以下方式提示用户审批:
  - exec 审批覆盖层
  - Telegram 按钮
  - Discord 交互
  - 任何频道上的 `/approve` 命令
- **改进**: `/approve` 命令现在处理 exec 和插件审批，带自动回退
- **贡献者**: @vaclavbelak, @joshavant

### ACP 频道绑定
- **新增**: 为 Discord、BlueBubbles、iMessage 添加当前对话 ACP 绑定
- **用途**: `/acp spawn codex --bind here` 可将当前聊天变成 Codex 支持的工作区
- **优势**: 无需创建子线程
- **文档**: 区分聊天表面、ACP 会话和运行时工作区

### OpenAI apply_patch
- **变更**: 默认为 OpenAI 和 OpenAI Codex 模型启用 `apply_patch`
- **对齐**: 将其沙箱策略访问与写入权限对齐

### CLI 后端插件
- **变更**: 将捆绑的 Claude CLI、Codex CLI、Gemini CLI 推理默认值移到插件表面
- **新增**: 添加捆绑的 Gemini CLI 后端支持
- **替换**: `gateway run --claude-cli-logs` → `--cli-backend-logs` (旧标志作为兼容性别名保留)

### 插件自动加载
- **变更**: 从显式配置引用自动加载捆绑的 provider 和 CLI 后端插件
- **影响**: 捆绑的 Claude CLI、Codex CLI、Gemini CLI message-provider 设置不再需要手动 `plugins.allow` 条目

### Podman 容器简化
- **简化**: 围绕当前 rootless 用户的容器设置
- **安装**: 在 `~/.local/bin` 下安装启动助手
- **文档**: 记录主机 CLI `openclaw --container ...` 工作流，而非专用的 `openclaw service` 用户

### Slack 文件上传
- **新增**: 显式 `upload-file` Slack action
- **路由**: 通过现有 Slack 上传传输路由文件上传
- **选项**: 支持可选的 filename/title/comment 覆盖 (用于频道和 DM)

### 消息动作统一
- **变更**: 开始统一文件优先发送到规范的 `upload-file` action
- **新增**: 为 Microsoft Teams 和 Google Chat 添加显式支持
- **BlueBubbles**: 通过 `upload-file` 暴露文件发送，保留遗留 `sendAttachment` 别名

### Matrix TTS (#37080)
- **变更**: 将自动 TTS 回复作为原生 Matrix 语音气泡发送，而非通用音频附件
- **贡献者**: @Matthew19990919

### CLI 配置模式 (#54523)
- **新增**: `openclaw config schema` 打印 openclaw.json 的生成 JSON 模式
- **贡献者**: @kvokka

### TTS 配置迁移
- **变更**: 在正常读取和密钥解析时自动迁移遗留 speech 配置
- **保留**: 为 Doctor 保留遗留诊断
- **移除**: 删除旧捆绑 tts API 密钥形状的常规模式运行时回退

### 内存插件
- **变更**: 将预压缩内存刷新计划置于活动内存插件契约后面
- **影响**: memory-core 拥有刷新提示

---

## 📋 升级建议

### 立即行动
1. **Qwen 用户**: 运行 `openclaw onboard --auth-choice modelstudio-api-key` 重新配置
2. **检查配置**: 运行 `openclaw doctor` 检查是否有旧密钥需要更新
3. **xAI 用户**: 检查 `openclaw configure --section web` 中的 x_search 设置

### 可选优化
1. **插件审批**: 为敏感工具调用配置 `requireApproval` hooks
2. **Gemini CLI**: 如使用 Gemini，可探索新的 CLI 后端
3. **Matrix 用户**: 享受原生语音气泡 TTS 回复

---

## 🔗 相关链接

- GitHub Releases: https://github.com/openclaw/openclaw/releases
- 文档: https://docs.openclaw.ai
- ClawHub: https://clawhub.ai

---

*此文件由 Sandbot V6.3 自动抓取并整理*  
*抓取时间: 2026-03-29 20:06 UTC*
