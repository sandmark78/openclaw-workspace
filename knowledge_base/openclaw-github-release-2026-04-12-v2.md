# OpenClaw GitHub Release 2026.4.12 (Broad Quality Release)

**抓取时间**: 2026-04-13 20:00 UTC  
**发布时间**: 2026-04-13 12:35 UTC  
**版本**: 2026.4.12 — Broad Quality Release  
**当前运行**: 2026.3.8（落后一个大版本）

> ⚠️ 此版本内容与之前记录的 4月11日 pre-release **完全不同**，已从 pre-release 阶段升级为大规模质量提升 release。

---

## 新特性 (Changes)

### 🧠 Memory/Active Memory (全新！⭐)
- **新 Active Memory 插件**: 为主回复前增加专用记忆子 Agent
- 自动从偏好、上下文和历史中提取相关信息
- 无需用户手动说"记住这个"或"搜索记忆"
- 支持 configurable message/recent/full context modes
- 支持 /verbose 实时检查
- 高级 prompt/thinking 覆盖调优
- 可选 transcript 持久化用于调试
- PR: [#63286](https://github.com/openclaw/openclaw/pull/63286) | Thanks @Takhoffman

### 🔐 QA/lab
- Convex 支持的 Telegram 凭证池租赁
- `openclaw qa credentials admin` 命令
- Broker 设置文档
- PR: [#65596](https://github.com/openclaw/openclaw/pull/65596) | Thanks @joshavant

### 🗣️ macOS/Talk
- 实验性本地 MLX 语音 provider
- 显式 provider 选择
- 本地语音回放 + 中断处理
- system-voice fallback
- PR: [#63539](https://github.com/openclaw/openclaw/pull/63539) | Thanks @ImLukeF

### 🔧 CLI/exec policy (全新)
- `openclaw exec-policy` 命令 (show/preset/set)
- 同步 tools.exec.* 配置与本地 exec 审批文件
- Node-host 拒绝加固
- Rollback 安全性
- 冲突检测
- PR: [#64050](https://github.com/openclaw/openclaw/pull/64050)

### 🌐 Gateway
- **commands.list RPC**: 远程客户端可发现 runtime-native/text/skill/plugin 命令
- 感知 surface 的命名 + 序列化参数元数据
- **Split startup/runtime seams**: 生命周期排序、重载状态、关闭行为更易维护
- PR: [#62656](https://github.com/openclaw/openclaw/pull/62656) | Thanks @samzong
- PR: [#63975](https://github.com/openclaw/openclaw/pull/63975) | Thanks @gumadeiras

### 🤖 Models/Providers
- 每 provider 的 `models.providers.*.request.allowPrivateNetwork`
- 允许受信任的自托管 OpenAI 兼容端点
- WebSocket 管理器在传输覆盖变更时刷新缓存
- PR: [#63671](https://github.com/openclaw/openclaw/pull/63671) | Thanks @qas

### 🧪 QA/Testing
- `--runner multipass` lane for openclaw qa suite
- 可在一次性 Linux VM 内运行 repo-backed QA 场景
- PR: [#63426](https://github.com/openclaw/openclaw/pull/63426) | Thanks @shakkernerd

### 📚 Docs i18n
- 块化文档翻译
- 拒绝截断的标记输出
- 避免歧义 body-only wrapper unwrapping
- 从终止的 Pi 翻译会话中恢复
- PR: [#62969](https://github.com/openclaw/openclaw/pull/62969), [#63808](https://github.com/openclaw/openclaw/pull/63808) | Thanks @hxy91819

### 🎨 Control UI/Dreaming
- 简化 Scene 和 Diary 界面
- 保留未知 phase 状态用于部分状态载荷
- 稳定 waiting-entry 最近排序
- PR: [#64035](https://github.com/openclaw/openclaw/pull/64035) | Thanks @davemorin

### 💬 Matrix/Partial Streaming
- MSC4357 live markers 用于草稿预览发送和编辑
- 支持 Matrix 客户端的实时/打字机动画
- PR: [#63513](https://github.com/openclaw/openclaw/pull/63513) | Thanks @TigerInYourDream

### 📱 QA/Telegram
- 实时 QA Telegram lane 用于私人群 bot-to-bot 检查
- Artifact 处理加固
- 原生 Telegram 命令回复线程保留
- PR: [#64303](https://github.com/openclaw/openclaw/pull/64303)

---

## 与之前记录的关键差异

| 之前记录 (4月11日 pre-release) | 当前 (4月13日 12:35 UTC) |
|---|---|
| Dreaming Wiki Import | **Active Memory 全新插件** |
| Control UI 媒体气泡 | **exec-policy CLI 命令** |
| 视频生成工具 | **MLX 本地语音** |
| 飞书评论增强 | **Gateway commands.list RPC** |
| Teams 反应支持 | **Private network allow** |
| 插件 manifest | **Multipass QA runner** |
| Ollama 缓存 | **Matrix MSC4357 live markers** |

---

## 对我们的影响评估

### 直接相关 ⭐
1. **Active Memory 插件** - 可能替代我们自建的 memory_search 工作流，值得研究
2. **Telegram session 修复** (之前记录中的 #64869) - topic-scoped session 初始化修复
3. **exec-policy 命令** - 可以更安全地管理 exec 权限

### 值得关注
- **commands.list RPC** - 可用于发现可用命令
- **Docs i18n** - 中文文档可能改善

### 升级建议
- 当前运行 2026.3.8，建议升级到 2026.4.12
- 升级前备份配置 (openclaw.json)
- 重点关注 Active Memory 是否可以与现有 memory 系统配合使用

---

*记录时间: 2026-04-13 20:00 UTC*
*下次检查: 心跳/下次生态探索任务*
