# OpenClaw 生态探索 - 2026-04-06

## 🆕 重大发现：OpenClaw v2026.4.5 发布 (2026-04-06)

**来源**: https://github.com/openclaw/openclaw/releases/tag/v2026.4.5
**发布者**: steipete (Peter Steinberger)
**反应**: 156 reactions, 103 contributors mentioned
**下载**: macOS DMG 3685次, ZIP 5882次

### ⚠️ Breaking Changes
- 移除了多个遗留配置别名 (talk.voiceId, talk.apiKey, agents.*.sandbox.perSession 等)
- 提供了 `openclaw doctor --fix` 迁移支持

### 🔥 重要新功能

#### 1. 内置视频生成工具 (`video_generate`)
- 支持 xAI (grok-imagine-video), 阿里模型工坊 Wan, Runway
- Agent 可直接生成视频并在回复中返回

#### 2. 内置音乐生成工具 (`music_generate`)
- 支持 Google Lyria, MiniMax, ComfyUI workflow
- 异步任务追踪 + 完成后自动发送

#### 3. 新增模型提供商
- **Qwen** (通义千问 - 原生支持)
- **Fireworks AI**
- **StepFun**
- MiniMax TTS/Search
- Ollama Web Search
- ComfyUI 本地工作流插件

#### 4. Control UI 多语言支持
- 简体中文 ✅, 繁体中文, 日语, 韩语
- 葡萄牙语, 德语, 西班牙语, 法语
- 土耳其语, 印尼语, 波兰语, 乌克兰语

#### 5. Memory Dreaming (实验性)
- 自动短期记忆提升为长期记忆
- `/dreaming` 命令, Dreams UI
- 三阶段: light, deep, REM
- Dream Diary 界面

#### 6. ClawHub 集成到 Control UI
- 可直接在 Skills 面板搜索/查看/安装 ClawHub 技能

#### 7. Lobster 插件内置运行
- 不再需要外部 CLI，减少传输开销

#### 8. 提示缓存大幅改进
- 跨传输 fallback, 工具排序确定性
- 系统提示指纹标准化
- `openclaw status --verbose` 缓存诊断

### 🔒 安全修复 (重要)
- 限制性插件工具白名单保护
- `/allowlist` 需要 owner 权限
- 阻止浏览器 SSRF 重定向绕过
- Claude CLI 安全隔离 (清除继承的配置环境变量)
- 设备配对安全加固

### 📱 通道修复
- **Telegram**: 模型选择器修复, 语音转写恢复, 推理预览修复
- **Discord**: 代理/webhook 流量修复, 图片生成修复
- **WhatsApp**: 流控和看门狗超时修复
- **Matrix**: 加密恢复改进, DM 会话作用域
- **MS Teams**: 图片下载和回复线程修复

### 🏗️ 架构改进
- ACPX 运行时直接嵌入 (移除外部 ACP CLI)
- Amazon Bedrock Mantle 支持
- 结构化计划更新和执行事件

## 📊 ClawHub 状态
- 网站正常: clawhub.com (重定向到 clawhub.ai)
- 定位: "A versioned registry for AI agent skills"
- 新增 Plugins 页面 (除了 Skills)
- 安装: `npx clawhub@latest install <skill_name>`

## 📚 文档站状态
- docs.openclaw.ai 正常运行
- 最新文档更新: 2026-04-05 ~ 2026-04-06
- 已支持多语言 (含波兰语等)
- 使用 gpt-5.4 模型生成翻译

## 🔄 上一版本
- v2026.4.2 (2026-04-02)

---
*探索时间: 2026-04-06 20:00 UTC*
