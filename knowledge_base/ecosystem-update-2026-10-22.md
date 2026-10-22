# 生态探索更新 2026-10-22

**检查时间**: 2026-10-22 20:00 UTC

---

## 🟢 发现新变化

### GitHub Releases — 🆕 v2026.10.6 稳定版发布

| 项目 | 状态 |
|------|------|
| 最新稳定版 | **v2026.10.6** (2026-10-22 发布) |
| 最新 Beta | 2026.10.10-beta.3 |
| 当前安装版本 | 2026.7.1 |
| 版本差距 | **约 3 个月** |
| 本次 PR 数量 | **293 个 PR** |

### v2026.10.6 主要更新亮点

#### 🔴 安全关键 — Node 运行时升级
- **必须升级 Node**: 要求 Node 24.22.1+ (24线) 或 26.12.1+ (26线)
- 原因: 2026年10月 Node.js 安全发布，拒绝被入侵证书密钥签名的 TLS 链
- Docker 镜像已附带 Node 24.22.1
- `openclaw update` 会在旧 Node 上拒绝安装并给出恢复指引
- 源码构建固定 pnpm 12.15.0

#### 🛡️ 更安全的更新和恢复
- 包交换拒绝不安全的 service 状态
- Windows/macOS 包管理器更新可从平台特定故障恢复
- 冻结的 Gateway 启动 owner 可被清理

#### 💾 数据保护迁移和备份
- Doctor 和迁移路径拒绝畸形/有损的 workspace 导入
- 保留畸形 Notes bytes
- 拒绝不安全的非 UTF-8 wiki 重写
- 保留深层嵌套 SQLite 备份
- 恢复检查失败时保留 staging 证据

#### 🔄 跨重启可靠投递
- 排队 turns、监视的子任务结果、死信投递、流式回复在恢复后不丢失/不重复
- 不再产生误报的"缺失回答"通知

#### 🤖 Provider 和模型弹性
- GPT-5.6 tool turns 修复
- OpenRouter DeepSeek tool calls 修复
- LM Studio 溢出恢复
- 并行 OpenAI reasoning 设置
- 模型 retry/fallback 预算行为一致

#### 📱 Windows 和移动端稳定性
- Windows fresh state stores、Proxy 环境、Anthropic 凭证不再阻塞启动
- iOS Talk 和聊天连接从首次回复/超时故障中恢复

#### 🔧 Agent 和工具调用恢复
- 未完成工具现在可见超时
- 上下文溢出在 steered tool 结果后压缩
- 畸形调用在早期拒绝后继续
- 大 patch hunks 避免参数限制崩溃
- 停止的 yielded 任务保持停止

#### 💬 通道投递正确性
- WhatsApp 重试和贴纸
- Telegram 相册和双栈回复
- Slack relay 恢复
- Discord 语音通话回复不再丢失/重复消息

#### ⚙️ Worker 和 worktree 恢复
- 主机重启后回收 worker 容量
- 部分克隆 worktree 修复缺失对象
- 子任务结果和 exec-wake 证据在 Gateway 重启后存活

### ClawHub
- 与昨日一致，无新变化
- 域名 clawhub.ai，官方集成技能持续可用

### docs.openclaw.ai
- 与昨日一致，无新变化

---

## ⚠️ 建议

1. **安全升级**: v2026.10.6 包含 Node.js 安全补丁，建议优先升级
2. **升级路径**: `openclaw gateway update` (需先确认 Node 版本 ≥ 24.22.1)
3. **当前版本**: 2026.7.1 落后最新稳定版约 3 个月

---

## 📊 对比上次 (2026-10-21)

| 项目 | 昨天 | 今天 | 变化 |
|------|------|------|------|
| 最新稳定版 | v2026.10.5 | **v2026.10.6** | 🆕 +1 版本 |
| 当前安装版 | 2026.7.1 | 2026.7.1 | 未变 |
| PR 数量 | - | 293 | 大型更新 |
| 安全补丁 | 无 | Node TLS 证书 | 🔴 重要 |
