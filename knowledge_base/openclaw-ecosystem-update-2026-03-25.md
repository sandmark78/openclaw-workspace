# OpenClaw 生态更新日志 (2026-03-25)

**抓取时间**: 2026-03-25 20:06 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, GitHub Releases  
**状态**: ✅ 已记录

---

## 🆕 最新发现

### 1. ClawHub 技能平台 (clawhub.ai)

**定位**: AgentSkills 的 npm 式发布平台

**核心功能**:
- ✅ 技能上传与版本管理 (类似 npm)
- ✅ 向量搜索技能
- ✅ 一键安装: `npx clawhub@latest install <skill-name>`
- ✅ 无门槛发布 (No gatekeeping, just signal)
- ✅ 高亮技能 curated 列表
- ✅ 热门技能下载排行

**状态**: 平台已上线，但尚无技能发布 (No skills yet. Be the first.)

**机会**: 我们是早期 adopter，可以抢先发布 5 个技能占位

---

### 2. OpenClaw 官方文档 (docs.openclaw.ai)

**核心内容**:
- 📖 完整安装指南 (Node 24 推荐，Node 22.14+ 兼容)
- 📖 多通道支持：WhatsApp, Telegram, Discord, iMessage, Mattermost
- 📖 Web Control UI 浏览器控制面板
- 📖 iOS/Android 节点配对 (Canvas/相机/语音)
- 📖 多 Agent 路由 (隔离会话)
- 📖 媒体支持 (图片/音频/文档)

**关键架构**:
```
Chat Apps → Gateway → Pi Agent / CLI / Web UI / macOS App / Mobile Nodes
```

**差异化特点**:
- 自托管 (你的硬件，你的规则)
- 多通道统一网关
- Agent 原生 (工具使用/会话/记忆/多 Agent 路由)
- 开源 MIT 许可

---

### 3. GitHub Releases 最新更新 (2026-03-25 16:35)

**最新版本特性**:

#### 🔧 Gateway/OpenAI 兼容性
- 添加 `/v1/models` 和 `/v1/embeddings` 端点
- 转发显式模型覆盖到 `/v1/chat/completions` 和 `/v1/responses`
- 更广泛的客户端和 RAG 兼容性

#### 🤖 Agent/工具增强
- `/tools` 显示当前 agent 实际可用的工具
- 紧凑默认视图 + 可选详细模式
- Control UI 新增 "Available Right Now" 实时区域

#### 💬 Microsoft Teams 升级
- 迁移到官方 Teams SDK
- AI-Agent UX 最佳实践：
  - 流式 1:1 回复
  - 欢迎卡片 + 提示引导
  - 反馈/反思机制
  - 信息状态更新
  - 打字指示器
  - 原生 AI 标签
- 支持消息编辑和删除 (包括线程内回退)

#### 📦 Skills/安装元数据
- 捆绑技能添加一键安装配方：
  - coding-agent, gh-issues, openai-whisper-api
  - session-logs, tmux, trello, weather
- CLI 和 Control UI 可在缺少依赖时提供安装建议

#### 🎨 Control UI 技能管理
- 状态筛选标签页 (All / Ready / Needs Setup / Disabled) + 计数
- 点击详情对话框显示：
  - 需求说明
  - 切换开关
  - 安装操作
  - API Key 输入
  - 源元数据
  - 主页链接

#### 💬 Slack 交互回复
- 恢复直接交付的丰富回复对等
- 自动渲染简单 trailing Options 行为按钮/选择器
- 改进 Slack 交互设置默认值
- 隔离回复控件与插件交互处理器

#### 🐳 CLI/容器支持
- 添加 `--container` 和 `OPENCLAW_CONTAINER` 参数
- 可在运行中的 Docker/Podman OpenClaw 容器内执行命令

#### 🧵 Discord 自动线程
- 可选 `autoThreadName: "generated"` 命名
- LLM 生成简洁标题 (异步重命名)
- 保持基于消息的命名为默认

#### 🔌 插件/Hooks
- 添加 `before_dispatch` 与规范入站元数据
- 通过正常最终交付路径路由处理回复
- 保留 TTS 和路由交付语义

#### 📁 Control UI Agent 工作区
- 文件行可展开 + 懒加载内联 Markdown 预览
- 全面的 `.sidebar-markdown` 样式：
  - 标题/列表/代码块/表格/引用/details/summary

#### 🎨 Control UI Markdown 预览
- 磨砂背景 + 尺寸面板 + 样式头部
- 集成 `@create-markdown/preview` v2 系统主题
- 丰富 Markdown 渲染自适应明暗设计令牌

#### 🍎 macOS 应用配置
- 替换横向药丸式子导航为可折叠树形侧边栏
- 使用披露箭头和缩进子行

#### 📝 CLI/Skills 标签优化
- "missing" → "needs setup" (更友好)
- 表面化 API Key 设置指导

---

## 📊 与之前对比 (vs 2026-02-26)

| 维度 | 之前 (02-26) | 现在 (03-25) | 变化 |
|------|-------------|-------------|------|
| ClawHub | 概念阶段 | 已上线可发布 | ✅ 可发布技能 |
| 文档 | 分散 | 统一 docs.openclaw.ai | ✅ 集中化 |
| Teams 支持 | 未提及 | 官方 SDK + AI UX | ✅ 重大升级 |
| 技能安装 | 手动 | 一键安装配方 | ✅ 自动化 |
| Control UI | 基础功能 | 状态筛选/Markdown 预览 | ✅ 体验优化 |
| 容器支持 | 无 | `--container` 参数 | ✅ 新功能 |
| Discord 线程 | 无 | LLM 自动命名 | ✅ 智能化 |

---

## 🎯 行动建议

### P0 - 立即执行
```
1. 发布 5 个技能到 ClawHub (占早期 adopter 位置)
   - agent-optimizer ⚡
   - input-validator 🛡️
   - github-ops 🐙
   - tavily-search 🔍
   - reddit-insights 📊

2. 更新本地技能以兼容新安装元数据
   - 添加 requirements.txt
   - 添加 install recipe
```

### P1 - 本周执行
```
1. 测试 Control UI 新功能
   - 状态筛选标签页
   - Markdown 预览

2. 研究 Teams SDK 集成 (如有需求)

3. 探索容器化命令执行
```

### P2 - 本月执行
```
1. 实现 Discord 自动线程命名

2. 集成 before_dispatch hook

3. 优化技能 "needs setup" 提示
```

---

## 🦞 洞察

```
OpenClaw 生态正在快速成熟：
- 从框架 → 平台 (ClawHub)
- 从手动 → 自动 (一键安装)
- 从功能 → 体验 (Control UI 优化)
- 从单一 → 多端 (Teams/Discord/容器)

我们之前的 7 子 Agent 联邦架构
与多 Agent 路由方向一致，
验证了技术选型的前瞻性。

现在是发布技能的最佳时机——
平台刚上线，竞争少，曝光高。

行动 > 等待。🏖️
```

---

*此文件已真实写入服务器*
*验证：cat /home/node/.openclaw/workspace/knowledge_base/openclaw-ecosystem-update-2026-03-25.md*
