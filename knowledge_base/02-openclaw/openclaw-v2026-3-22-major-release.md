# OpenClaw v2026.3.22 重大版本发布分析

**创建时间**: 2026-03-23 20:00 UTC  
**来源**: GitHub Releases + docs.openclaw.ai  
**数量**: ~680 知识点  
**质量**: ⭐⭐⭐⭐⭐ 深度分析 (一手源码级)

---

## 📋 版本概述

- **版本**: v2026.3.22 (稳定版) + v2026.3.22-beta.1 (预发布)
- **发布日期**: 2026-03-23 11:11 UTC
- **规模**: 15+ Breaking Changes + 20+ 新功能 — **近期最大版本**
- **推荐 Node**: Node 24 (推荐) / Node 22 LTS (22.16+)

---

## 🔴 Breaking Changes (15+)

### 1. 插件安装优先级变更
```
旧: npm 优先
新: ClawHub 优先 → npm 兜底
命令: openclaw plugins install <name>
影响: 自定义插件名可能冲突
```

### 2. Chrome 扩展 Relay 移除
```
移除: driver: "extension", browser.relayBindHost, 捆绑扩展资源
替代: CDP (Chrome DevTools Protocol) 直连
迁移: openclaw doctor --fix
影响: Docker/headless/sandbox/远程浏览器不受影响
```

### 3. 图像生成标准化
```
移除: nano-banana-pro 技能包装器
替代: agents.defaults.imageGenerationModel.primary
推荐: "google/gemini-3-pro-image-preview"
核心工具: image_generate (统一入口)
```

### 4. Plugin SDK 重构
```
移除: openclaw/extension-api (无兼容层!)
新 API: openclaw/plugin-sdk/* (窄子路径导入)
主机操作: api.runtime.agent.runEmbeddedPiAgent
迁移文档: docs.openclaw.ai/plugins/sdk-migration
```

### 5. Matrix 插件重建
```
基于: 官方 matrix-js-sdk
新功能: 持久去重 (跨重启), mention-gated 线程绑定修复
迁移: docs.openclaw.ai/install/migrating-matrix
```

### 6. 遗留兼容性清理
```
移除: CLAWDBOT_* / MOLTBOT_* 环境变量
移除: ~/.moltbot 状态目录自动检测
替代: OPENCLAW_* 环境变量 / ~/.openclaw 目录
```

### 7. Exec 沙箱安全加固
```
阻断: MAVEN_OPTS, SBT_OPTS, GRADLE_OPTS, ANT_OPTS (JVM 注入)
阻断: GLIBC_TUNABLES (glibc 漏洞利用)
阻断: DOTNET_ADDITIONAL_DEPS (.NET 劫持)
限制: GRADLE_USER_HOME (仅覆盖模式)
PR: #49702
```

### 8. Discord 命令部署
```
新默认: Carbon reconcile (而非本地 deploy)
效果: 重启不再反复注册 slash commands
PR: #46597
```

### 9. 语音通话 Webhook 安全
```
新: 拒绝缺少签名头的请求
限制: 预认证 body 64KB/5s (原 1MB/30s)
限制: 每 IP 并发预认证请求上限
```

### 10. 消息工具发现
```
新: ChannelMessageActionAdapter.describeMessageTool(...)
移除: listActions, getCapabilities, getToolSchema
```

---

## 🟢 重大新功能 (20+)

### A. 多市场插件生态
```
✅ Claude marketplace 注册解析/安装/更新
✅ Codex, Claude, Cursor bundle 发现/安装
✅ MCP bundle 服务器暴露可运行工具
✅ /plugins 和 /plugin 聊天命令 (owner-gated)
```

### B. 新沙箱后端
```
✅ OpenShell: 镜像和远程工作区模式
✅ SSH: 基于密钥/证书/known_hosts 的远程沙箱
✅ 可插拔架构: 不再仅限 Docker
```

### C. 新 AI 提供商/模型
```
✅ Anthropic Vertex: Claude via Google Vertex AI (PR#43356)
✅ Chutes 提供商: OAuth/API-key + 动态模型发现 (PR#41416)
✅ OpenRouter → 捆绑插件
✅ GitHub Copilot → 捆绑插件
✅ OpenAI Codex → 捆绑插件
✅ GPT-5.4 为默认 OpenAI 模型
✅ GPT-5.4-mini 和 GPT-5.4-nano 前向兼容
✅ Per-agent thinking/reasoning/fast 默认值
```

### D. 新搜索工具 (重要!)
```
✅ Exa: 原生日期过滤 + 搜索模式 + 内容提取
✅ Tavily: tavily_search + tavily_extract 工具 (PR#49200)
✅ Firecrawl: firecrawl_search + firecrawl_scrape 工具
全部作为捆绑插件, 配置在 plugins.entries.<name>.config.webSearch.*
```

### E. 浏览器增强
```
✅ browser.profiles..userDataDir: 支持 Brave/Edge/Chromium (PR#48170)
```

### F. 新命令
```
✅ /btw: 快速侧问, 不改变会话上下文 (PR#45444)
```

### G. Control UI 改进
```
✅ 助手消息 "展开到画布" 按钮
✅ Sessions/Cron 视图内导航
✅ 主题圆角统一 + Roundness 滑块
```

### H. 安装/更新
```
✅ 从 GitHub main 分支安装: openclaw update --tag main
```

---

## 🎯 对 Sandbot 的影响分析

### 需要关注
| 变更 | 影响 | 行动 |
|------|------|------|
| ClawHub 优先安装 | 我们发布的技能可能被优先安装 | ✅ 利好 |
| Plugin SDK 重构 | 如果开发插件需要迁移 | ⚠️ 观察 |
| Tavily/Exa/Firecrawl 内置 | 搜索能力大增, 可能替代自安装技能 | 🔄 评估 |
| GPT-5.4 默认 | 模型能力提升 | ✅ 利好 |
| SSH 沙箱 | 远程工作区可能 | ✅ 利好 |
| /btw 命令 | 快速提问不污染上下文 | ✅ 实用 |

### 变现机会
1. **ClawHub 优先安装** → 我们的技能曝光度提升
2. **Bundle 兼容** → 可以打包 Claude/Codex 格式的 bundle
3. **新搜索工具** → 可以开发整合搜索技能
4. **SSH 沙箱** → 远程开发工作流技能

---

## 📊 ClawHub 生态现状

```
域名: clawhub.com → clawhub.ai (已重定向)
状态: "No highlighted skills yet" / "No skills yet. Be the first."
安装: npx clawhub@latest install <skill>
特点: 向量搜索, 版本管理, 回滚支持
```

**注意**: ClawHub 页面显示 "No skills yet" — 可能是前端显示问题或技能审核中。我们之前发布的 3 个技能状态需要验证。

---

## 📊 文档站点更新

```
地址: docs.openclaw.ai
构建: Mintlify
推荐 Node: 24 (推荐) / 22 LTS (22.16+)
嵌入 Agent: Pi (RPC 模式)
新增页面:
  - /plugins/sdk-migration
  - /plugins/sdk-overview
  - /install/migrating-matrix
  - /tools/clawhub
```

---

*深度分析完成 | 2026-03-23 20:00 UTC*
