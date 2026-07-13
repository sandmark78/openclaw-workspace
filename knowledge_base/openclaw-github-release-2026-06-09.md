# OpenClaw GitHub Release 2026.6.5（2026-06-09 正式发布）

**发布日期**: 2026-06-09 18:13 UTC
**版本**: 2026.6.5（June 2026 floor）
**类型**: 正式发布（从 2026-06-05 预发布升级）
**来源**: https://github.com/openclaw/openclaw/releases

---

## 📌 版本说明

这是 2026.6.5 的正式发布版，相比 06-05 预发布增加了大量 Changes 和 Fixes 条目，并正式切换到 **YYYY.M.PATCH 月度补丁编号系统**。

---

## 🔥 相比 06-05 预发布的新增内容

### 1. Auth & Plugin 状态持久化 (新) ⬆️
- Auth profiles 现在存储在 SQLite 中（更耐久）
- 官方 npm 插件安装记录保留可信 pin
- pre-release fallback 完整性检查避免携带过时的 integrity
- PR: #89102, #88585

### 2. Agent/Tool/Provider 循环更严格 (新) ⬆️
- MCP lease timestamps 更严格管理
- prompt-cache tool names 防护
- 本地 tool catalog 更紧凑
- 不可读 dynamic tools 被隔离
- owner-only HTTP tools 安全检查
- 减少隐藏重试和不安全暴露
- PR: #91124, #91233, #90022, #90261

### 3. macOS Node 模式修复 (新) ⬆️
- macOS node 不再从健康的直接 Gateway 会话静默自 reconnect
- 减少 companion app 意外的 session 轮换
- PR: #90668, #90815（贡献者: @vrurg）

### 4. 升级和服务路径更安全 (新) ⬆️
- cron legacy JSON stores 在 doctor preflight 时迁移
- service env 占位符不再遮蔽 state-dir secrets
- WhatsApp 启动等待有上限
- 禁用的 WhatsApp 账号在 config reload 时自动清理
- PR: #90072, #90208, #90277, #90488, #90486, #87951, #87965

### 5. ClawHub Skills GitHub 仓库安装 (新) ⬆️
- 通过 resolved install API 安装 GitHub 仓库支持的 ClawHub skills
- 下载 pinned GitHub commit
- 保留 install-policy 检查
- 安装成功后报告 telemetry
- PR: #90478（贡献者: @Patrick-Erichsen）

### 6. Skills 文件系统优化 (新)
- 避免每个 skill 文件一个 filesystem watcher
- 防止大型 skill 树耗尽 watcher 限制

### 7. Google Chat 原生 Approval 卡片 (新)
- Google Chat 审批使用平台原生卡片，替代通用消息流

### 8. 移动端改进 (新)
- Android: provider/model 屏幕更清晰展示 expiring/unavailable/unresolved/attention 状态
- Android: 新增主题模式选择
- iOS: settings 和 Talk tabs 保留诊断、gateway rows、附件标签、fallback copy

### 9. Memory QMD 搜索 (新)
- QMD 搜索支持新的 rerank toggle
- memory adapter 状态使用 resolved default model identity 检查

### 10. 发布流程变更 (新)
- **正式切换到 YYYY.M.PATCH 月度补丁编号系统**
- 保持过渡前标签兼容
- June 2026 floor 锁定在 2026.6.5
- session-metadata SQLite 迁移从 beta 推迟（保持现有 JSON-backed 路径）

---

## 📋 与 06-05 预发布相同的内容（已记录）

- QQBot 推理内容过滤 (#89913, #90132)
- MCP 工具结果强制转换 (#90710, #90728)
- Anthropic 扩展思维会话恢复 (#90667, #90697)
- Parallel 内置 web_search 提供商 (#85158)
- Google Vertex ADC 修复 (#90506, #90609, #90717, #90816)
- Matrix 语音笔记改进 (#78016, #90415)

---

## 📊 版本对比

| 项目 | 值 |
|------|------|
| **当前运行版本** | OpenClaw 2026.3.8 |
| **最新正式版** | 2026.6.5 (2026-06-09) ⬆️ **NEW** |
| **落后版本** | 3 个月度版本 (3.8 → 6.5) |

---

## 📝 行动建议

⚠️ 2026.6.5 是正式发布版（不再是 pre-release），新增了大量修复和改进。特别是：
- **Auth 持久化到 SQLite**: 更可靠的认证状态
- **MCP lease 管理**: 更安全的工具循环
- **升级路径安全改进**: cron 迁移、WhatsApp 清理等
- **ClawHub Skills GitHub 安装**: 技能安装更可靠

建议老大考虑升级到 2026.6.5。

---

*自动生成于 2026-06-09 20:07 UTC*
