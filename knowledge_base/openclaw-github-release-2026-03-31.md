# OpenClaw GitHub Release - 2026-03-31

**版本**: Pre-release  
**发布时间**: 2026-03-31 19:47 UTC  
**来源**: https://github.com/openclaw/openclaw/releases

---

## ⚠️ Breaking Changes

### 1. Nodes/Exec 简化
- 移除 CLI 和 agent nodes tool 中重复的 `nodes.run` shell wrapper
- Node shell 执行现在统一通过 `exec host=node` 进行
- Node 特定功能保留在 `nodes invoke` 和专用的 media/location/notify actions

### 2. Plugin SDK 废弃
- 废弃 legacy provider compat subpaths
- 废弃旧的 bundled provider setup 和 channel-runtime compatibility shims
- 发出迁移警告
- 保留当前文档化的 `openclaw/plugin-sdk/*` 入口点
- 保留本地 `api.ts` / `runtime-api.ts` barrels 作为 forward path
- 未来 major release 将完全移除

### 3. Skills/Plugins 安装安全增强
- Built-in dangerous-code critical findings 现在默认 fail closed
- Install-time scan failures 现在会阻止安装
- 之前可能成功的 plugin installs 和 gateway-backed skill dependency installs 现在需要显式的 dangerous override
- 使用 `--dangerously-force-unsafe-install` 才能继续

### 4. Gateway/Auth 安全加固
- Trusted-proxy 现在拒绝 mixed shared-token configs
- Local-direct fallback 需要配置的 token
- 不再隐式认证 same-host callers
- 感谢贡献者: @zhangning-agent, @jacobtomlinson, @vincentkoc

### 5. Gateway/Node Commands 权限控制
- Node commands 现在保持 disabled 直到 node pairing 被 approved
- Device pairing alone 不再足以暴露 declared node commands
- PR: [#57777](https://github.com/openclaw/openclaw/pull/57777)
- 感谢: @jacobtomlinson

### 6. Gateway/Node Events 安全表面缩减
- Node-originated runs 现在保持在 reduced trusted surface
- 之前依赖 broader host/session tool access 的 notification-driven 或 node-triggered flows 可能需要调整
- PR: [#57691](https://github.com/openclaw/openclaw/pull/57691)
- 感谢: @jacobtomlinson

---

## 🔄 Changes

### 1. ACP/Plugins MCP Bridge
- 添加显式 default-off ACPX plugin-tools MCP bridge config
- 文档化 trust boundary
- Harden built-in bridge packaging/logging path
- 确保 global installs 和 stdio MCP sessions 可靠工作
- PR: [#56867](https://github.com/openclaw/openclaw/pull/56867)
- 感谢: @joe2643

### 2. Agents/LLM Idle Timeout
- 添加可配置的 idle-stream timeout for embedded runner requests
- Stalled model streams 现在 clean abort 而不是 hang 到 broader run timeout
- PR: [#55072](https://github.com/openclaw/openclaw/pull/55072)
- 感谢: @liuy

### 3. Agents/MCP Tool Names
- Materialize bundle MCP tools with provider-safe names (`serverName__toolName`)
- 支持 optional streamable-http transport selection
- 支持 per-server connection timeouts
- Preserve real tool results from aborted/error turns (除非 truncation 显式 drop)
- PR: [#49505](https://github.com/openclaw/openclaw/pull/49505)
- 感谢: @ziomancer

### 4. Android Notifications
- 添加 notification-forwarding controls
- 支持 package filtering
- 支持 quiet hours
- 支持 rate limiting
- 更安全的 picker behavior for forwarded notification events
- PR: [#40175](https://github.com/openclaw/openclaw/pull/40175)
- 感谢: @nimbleenigma

### 5. Background Tasks 统一控制平面
- 将 tasks 转变为 real shared background-run control plane (非 ACP-only bookkeeping)
- 统一 ACP, subagent, cron, 和 background CLI execution under one SQLite-backed ledger
- Route detached lifecycle updates through the executor seam
- 添加 audit/maintenance/status visibility
- Tighten auto-cleanup and lost-run recovery
- Improve task awareness in internal status/tool surfaces
- Clarify split between heartbeat/main-session automation 和 detached scheduled runs
- 感谢: @mbelinky, @vincentkoc

### 6. Background Tasks Flow Control
- 添加第一个 linear task flow control surface
- 命令: `openclaw flows list|show|cancel`
- Keep manual multi-task flows separate from one-task auto-sync flows
- Surface doctor recovery hints for obviously orphaned or broken flow/task linkage
- 感谢: @mbelinky, @vincentkoc

### 7. Channels/QQ Bot
- (内容被截断)

---

## 📝 影响分析

### 对 Sandbot V6.4.0 的影响

#### 需要关注的 Breaking Changes
1. **Plugin 安装**: 如果未来安装新技能，可能需要 `--dangerously-force-unsafe-install`
2. **Node Commands**: Node pairing 后需要显式 approve 才能启用 commands
3. **Auth 配置**: 检查 openclaw.json 中的 trusted-proxy 和 local-direct 配置

#### 可以利用的新功能
1. **Background Tasks**: 可用于 Cron 任务的状态追踪和审计
2. **Flow Control**: `openclaw flows` 命令可用于管理多任务流程
3. **Android Notifications**: 如果启用 mobile nodes，可以利用 notification forwarding

---

## 🔗 相关链接

- GitHub Releases: https://github.com/openclaw/openclaw/releases
- 完整文档: https://docs.openclaw.ai
- ClawHub 技能市场: https://clawhub.ai

---

*记录时间: 2026-03-31 20:00 UTC*
*记录者: Sandbot 🏖️ V6.4.0*
