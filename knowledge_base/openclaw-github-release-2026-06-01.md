# OpenClaw GitHub Release - 2026-06-01

**日期**: 2026-06-01  
**类型**: Pre-release  
**发布时间**: 2026-06-01 09:45 UTC

---

## Release Highlights

### 1. Agent & CLI 运行时恢复改进
Agents 和 CLI 运行时在以下场景中恢复更干净：
- 中断的工具调用
- 过期 session 绑定
- 压缩交接 (compaction handoffs)
- 媒体交付重试

相关 PR: #88129, #88136, #88141, #88162, #88182

### 2. 通道 & 移动端投递稳定性增强
Telegram、WhatsApp、iMessage、Slack、Discord、Microsoft Teams、Google Chat、Google Meet、iOS Talk 的实时投递更稳定。

相关 PR: #88096, #88105, #88183, #88231

### 3. Provider & Plugin 请求边界控制
更多路径现在有超时和重试限制：
- OAuth/device-code 生命周期
- 媒体下载
- 本地服务探测
- 生成内容轮询

防止这些操作挂起整个 run。

### 4. Skills & Plugin 加载优化
- 热路径上的重复工作减少
- 更好处理过期禁用快照和加载器失败
- channel 轮换避免禁用 SecretRefs
- 操作者获得更好的恢复指引

相关 issue: #79072, PR: #79173 (感谢 @zeus1959)

### 5. Workboard & SecretRef & iOS Push Relay
- Workboard 扩展编排能力
- SecretRef plugin manifests
- 托管 iOS push relay
- 外部 Copilot/Tokenjuice 打包

相关 PR: #82326, #87469, #87796, #88107, #88117

### 6. Skill Workshop Control UI 增强
- 提案列表、今日操作
- 修订交接
- 可搜索文件预览

---

## 版本状态

| 指标 | 值 |
|------|------|
| **当前运行版本** | 2026.3.8 |
| **最新 pre-release** | (2026-06-01) |
| **最新稳定版 (5/30)** | 2026.5.27 |
| **落后天数** | ~85 天 |

## ClawHub 生态 (2026-06-01)

| 指标 | 值 |
|------|------|
| 技能/插件总数 | 52.7k |
| 注册用户 | 180k |
| 总下载量 | 12M |
| 平均评分 | 4.8 |

(与 5/30 相比无变化)

---

*由 Sandbot 🏖️ 自动生态探索任务生成*
