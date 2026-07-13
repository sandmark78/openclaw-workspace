# 生态探索记录 2026-05-10

## 检查时间
2026-05-10 20:00 UTC

## 当前安装版本
**OpenClaw 2026.3.8**

## 最新版本
- **npm latest**: 2026.5.7
- **GitHub 最新**: 2026.5.9-rc (2026-05-10 pre-release，今天刚发！)

## ⚠️ 版本差距：落后约 2 个月（2026.3.8 → 2026.5.x）

---

## 自上次检查 (2026-04-20) 以来的新变化

### 1. ClawHub 平台（无显著变化）
- 工具数：52,700+ / 用户：180,000+ / 下载：12M+ / 评分：4.8
- 域名仍为 clawhub.ai（从 clawhub.com 重定向）

### 2. OpenClaw Pre-release 2026.5.9-rc (2026-05-10 今天发布！)

#### 新功能
- **QA/Mantis**: Telegram 自动化 PR 证据（Convex 凭证 + Crabbox 转录 + GIF 预览）
- **QA/Mantis**: Telegram 桌面场景构建器（VNC 截图/视频记录）
- **Discord/Voice**: 实时语音诊断（说话者轮次、回放重置、打断检测、音频截断分析）
- **Talk**: 新增 talk.realtime.instructions，操作者可追加实时语音风格指令
- **Discord/Voice**: 默认纯 JS opusscript 解码器，避免原生 addon 编译
- **Gateway/Skills**: 新增可选私有技能压缩包安装路径（skills.install.allowUploadedArchives）

#### 依赖更新
- ACPX @agentclientprotocol/claude-agent-acp 0.33.1
- Codex ACP 0.14.0、Baileys 7.0.0-rc10
- Google GenAI 2.0.1、OpenAI 6.37.0、AWS SDK 3.1045.0
- Kysely 0.29.0、tsdown 0.22.0

#### 重要修复
- **Telegram**: 修复 Agent  scoped 媒体根目录传递问题
- **ACPX**: 修复嵌入式 ACP 后端启动探针，解决 gateway ready 信号过早问题 (#79596)
- **OpenAI 兼容模型**: 清理历史中过时 assistant reasoning 字段，防止 Qwen 后续轮次拒绝/卡顿 (#46637)
- **OpenAI 兼容模型**: 新增 compat.strictMessageKeys，严格模式下剥离工具/元数据键 (#50374)
- **Gateway**: SIGUSR1 重启后从磁盘重新读取配置，防止使用陈旧快照 (#79947)
- **Cron**: 隔离 self-cleanup 运行可检查自身 job 历史 (#80019)
- **CLI/config**: config set/patch 值等于运行时时也能持久化 (#79856)
- **Control UI**: 修复 PWA 和 favicon 在 SPA 路由下 404 (#80072)
- **Telegram**: 修复无回复 DM 静默回复变可见的问题 (#78188)
- **Telegram**: 修复 managed select 按钮回调处理顺序 (#79816)
- **xAI**: 暴露 /think low|medium|high 给 Grok 推理模型 (#79210)
- **Anthropic**: 添加 claude-haiku-4-5 到默认 allowlist

#### 改进
- **CLI/onboarding**: 改进终端流程引导，解释下一个有用命令
- **Agents/Codex**: 移除 Codex 动态工具配置，固定 workspace/edit/patch/exec/plan 工具
- **Voice/Ollama**: 遵守 routed voice agent tools.allow 空 allowlist
- **Agents**: LLM 空闲看门狗在 provider stream setup 期间也生效
- **Discord**: 修复模型选择器加载前交互超时

---

## 与我们相关的重点修复
1. **#46637 OpenAI 兼容模型 reasoning 字段清理** → 我们用的是 bailian/qwen，可能受益于 reasoning 字段处理
2. **#79947 Gateway SIGUSR1 重启配置刷新** → 我们常用 gateway restart
3. **#79596 ACPX 启动探针** → 如果未来用 ACP 会话
4. **#80019 Cron self-inspection** → 我们的定时任务可能受益

---

## 建议
1. **强烈建议升级到 2026.5.x**（落后 2 个月，大量修复和功能）
2. 升级前务必备份 openclaw.json 和 workspace
3. 关注 Telegram 相关修复（#78188, #79816）— 我们的主通道
