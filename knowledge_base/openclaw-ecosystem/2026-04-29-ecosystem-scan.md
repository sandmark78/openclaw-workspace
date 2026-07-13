# OpenClaw 生态探索扫描 (2026-04-29 20:00 UTC)

**扫描时间**: 2026-04-29 20:00 UTC
**当前版本**: 2026.3.8
**最新版本**: 2026.4.26 (2026-04-26 发布)
**状态**: ⚠️ 有可用更新 (落后约 1.5 个月)

---

## 与上次扫描 (2026-04-25) 对比

| 项目 | 上次 | 本次 | 变化 |
|------|------|------|------|
| 最新版本 | 2026.4.24 | **2026.4.26** | 🆕 +2 次修订 |
| ClawHub 工具数 | 52,700 | 52,700 | - |
| 用户数 | 180,000 | 180,000 | - |
| 下载量 | 12,000,000 | 12,000,000 | - |
| 平均评分 | 4.8 | 4.8 | - |

---

## 🆕 v2026.4.26 新增修复

### 1. Gateway/设备 Token 安全修复
- 停止在 shared/admin device.token.rotate 响应中回显轮换后的 bearer token
- 保留同设备 token 交接功能，确保 token-only 客户端重连正常
- Issue: [#66773](https://github.com/openclaw/openclaw/issues/66773)

### 2. sessions_spawn 模型别名解析
- 为 spawn model overrides 解析配置的裸模型别名，使用目标 agent 运行时默认 provider
- 延续 [#59681](https://github.com/openclaw/openclaw/pull/59681) 审查修复
- Fixes: [#59681](https://github.com/openclaw/openclaw/pull/59681)

### 3. Control UI / Talk 改进
- Google Live 浏览器会话保持 WebSocket 传输，不再回退到 WebRTC
- 验证浏览器 Google Live WebSocket 端点
- 限制每个浏览器连接的 Gateway 中继会话数
- 移除过时的浏览器原生语音按钮（未使用配置的 Talk/TTS provider）

### 4. Gateway 启动优化
- 在插件引导计划加载前，复用配置快照插件清单进行启动自动启用
- 减少启动时的插件加载延迟

### 5. 子 Agent 安全加固
- 对显式 sessions_spawn(agentId=...) 调用强制执行 subagents.allowAgents 限制
- 不再自动允许 requester self-targets
- Fixes: [#72827](https://github.com/openclaw/openclaw/issues/72827)

### 6. ACP 调度修复
- 允许显式 sessions_spawn(runtime="acp") bootstrap turns 在 acp.dispatch.enabled=false 时运行
- 自动 ACP 线程调度仍被阻止
- Fixes: [#63591](https://github.com/openclaw/openclaw/issues/63591)

### 7. CLI 更新安全性
- npm 全局更新安装到已验证的临时前缀，再交换包树
- 防止新旧混合安装和陈旧包文件破坏 openclaw update 验证

---

## ClawHub 平台数据

- 域名: clawhub.com → clawhub.ai (重定向)
- 工具总数: **52,700**
- 用户总数: **180,000**
- 下载总量: **12,000,000**
- 平均评分: **4.8**

---

## 建议

1. **版本升级**: 当前 2026.3.8 → 最新 2026.4.26，建议升级
2. **安全修复**: Token 回显修复和子 Agent 权限加固值得关注
3. **注意**: 升级前检查自定义 plugin 是否使用了已废弃的 `registerEmbeddedExtensionFactory`
4. **稳定**: ClawHub 平台数据与上次扫描无变化
