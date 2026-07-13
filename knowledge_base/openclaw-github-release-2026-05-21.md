# OpenClaw GitHub Release 2026-05-21 (Pre-release)

**日期**: 2026-05-21 15:57 UTC
**类型**: Pre-release
**来源**: https://github.com/openclaw/openclaw/releases

---

## 重要变更

### Exec 审批机制重构
- 移除旧的 `cat SKILL.md && printf` allowlist 兼容路径
- 现在 skill 文件必须通过 read 工具加载
- 只有真正的 skill 可执行文件才能自动允许

### Discord 语音会话增强
- 语音会话可以跟随配置的用户进入语音频道 (#84264)
- 支持多用户切换、有界协调、DAVE 恢复保留
- 语音 session 默认包含 IDENTITY.md/USER.md/SOUL.md 上下文 (#84499)
- 可通过 `voice.realtime.bootstrapContextFiles: []` 禁用

### 新增 Policy 插件
- 捆绑 Policy 插件用于策略驱动频道一致性检查 (#80407)
- 支持 doctor lint 发现和 opt-in workspace 修复

### 提供商更新
- **xAI**: 新增 device-code OAuth 登录，支持远程/无头部署授权 (#84005)
- **OpenRouter**: 支持 provider-level params.provider 路由策略
- **Codex harness**: 升级到 @openai/codex 0.132.0

### Agent 配置
- 新增 `agents.list[].experimental.localModelLean` 配置
- 可以为单个 agent 启用 lean local-model 模式（非全局）

---

## 修复

| 修复项 | PR | 贡献者 |
|--------|-----|--------|
| CLI/tasks: 维护决策包含 --json 输出 | #84691 | @efpiva |
| Codex app-server: hook 提供的 SOUL/IDENTITY 上下文正确报告字符数 | #84736 | @JARVIS-Glasses |
| MiniMax music: 移除 durationSeconds 控制广告 | #84508 | @neeravmakwana |
| Doctor: 沙箱工具策略隐藏 MCP 工具时警告 | #84699 | @nxmxbbd |
| WhatsApp: Baileys 升级到 7.0.0-rc12 | - | - |
| CLI/nodes: 插件注册日志路由到 stderr | #84684 | @TurboTheTurtle |
| Approvals: 手动 /approve 通过可信运行时路由 | - | - |
| Mac app: 更新 About 版权年为 2026 | #84385 | @pejmanjohn |
| Dependencies: @openclaw/fs-safe 0.2.7 | - | - |

---

## ClawHub 统计
- 工具数: 52.7k
- 用户数: 180k
- 下载量: 12M
- 平均评分: 4.8

---

## 对我们有用的变更
1. **Exec 审批重构** - 影响 skill 加载方式，需关注兼容性
2. **Discord 语音增强** - 如果未来启用 Discord 通道值得关注
3. **Policy 插件** - 新增策略检查能力
4. **xAI OAuth** - 如果用 xAI 模型可以无头部署
5. **localModelLean** - 可以为单个 agent 启用本地模型 lean 模式
