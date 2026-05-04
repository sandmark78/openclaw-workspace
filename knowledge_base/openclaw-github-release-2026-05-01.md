# OpenClaw GitHub Release 2026.4.29

**抓取时间**: 2026-05-01 20:01 UTC  
**发布时间**: 2026-04-30 21:01 UTC  
**版本**: 最新正式版 (Latest)  
**发布者**: steipete (Peter Steinberger)  
**Tag**: v2026.4.29  
**上次记录版本**: 2026.4.26 (2026-04-28 记录)

---

## 2026.4.29 亮点

### 🧠 记忆系统升级
- **People-aware wiki**: 记忆进化为人员感知的 wiki，带 provenance 视图
- **Active Memory 过滤**: 每对话独立 Active Memory 过滤器
- **Partial recall**: 超时后部分回忆
- **Bounded REM preview**: 有界 REM 预览诊断

### ⚡ 自动化与 Agent 路由
- **Active-run steering**: 默认启用主动运行引导
- **Visible-reply enforcement**: 可见回复强制执行
- **Subagent routing metadata**: 子 Agent 路由元数据
- **Heartbeat follow-up commitments**: 心跳交付提醒的可选后续承诺

### 🌐 提供商/模型覆盖扩展
- **NVIDIA**: 新增 onboarding/catalogs + 更快的 manifest-backed model/auth 路径
- **Bedrock Opus 4.7**: 完整 thinking parity
- **Codex/OpenAI-compatible**: 更安全的 replay 和 streaming 行为

### 🔧 Gateway & 插件可靠性
- 慢主机启动优化
- 可复用 model catalogs
- 事件循环就绪诊断
- 运行时依赖修复
- 过期会话恢复
- 版本级更新缓存

### 📡 频道修复
- **Slack**: Block Kit 限制修复
- **Telegram**: 代理/webhook/polling/send 弹性增强
- **Discord**: 启动/限速处理优化
- **WhatsApp**: 投递/存活改善
- **Teams/Matrix/Feishu**: 边界情况修复

### 🔒 安全与运维
- **OpenGrep**: 新增安全扫描
- **GHSA triage**: 更精准的安全策略
- **Exec/pairing/owner-scope**: 更安全的处理
- **Docker/onboarding**: 自动化增强
- **web-fetch IPv6 ULA**: 可信代理栈可选支持

### 🔧 工具安全强化
- 配置的工具段 (tools.exec, tools.fs) 不再隐式放宽限制配置文件 (messaging, minimal)
- 限制配置文件下需要这些工具的用户必须显式添加 alsoAllow 条目

---

## 与上次记录 (v2026.4.26) 对比

| 类别 | 变化 |
|------|------|
| 版本号 | v2026.4.26 → **v2026.4.29** (+3 小版本) |
| 记忆 | 无 → People-aware wiki + Active Memory 过滤 |
| Agent | sessions_spawn 修复 → Active-run steering + 子 Agent 路由元数据 |
| 提供商 | 无新增 → NVIDIA + Bedrock Opus 4.7 |
| 安全 | 无 → OpenGrep 扫描 + GHSA triage + 工具段安全 |
| 频道 | 基础修复 → 全渠道弹性增强 (Slack/Telegram/Discord/WhatsApp/Teams/Matrix/Feishu) |

---

## ClawHub 统计 (2026-05-01)

| 指标 | 数值 | 与上次对比 |
|------|------|-----------|
| 工具总数 | 52.7k | ↔ 持平 |
| 用户数 | 180k | ↔ 持平 |
| 下载量 | 12M | ↔ 持平 |
| 平均评分 | 4.8 | ↔ 持平 |

---

## 对我们的影响

### 值得关注
1. **Memory wiki 升级**: 人员感知 + provenance 视图，可能对我们记忆系统有参考价值
2. **Active-run steering**: 默认启用，可能影响我们的 cron 和心跳行为
3. **NVIDIA 支持**: 新增模型提供商选项
4. **Telegram 弹性增强**: 我们的主要通道，proxy/webhook/polling/send 都做了优化
5. **工具安全强化**: exec/fs 工具段不再隐式放宽，注意检查配置

### 当前运行版本
⚠️ 容器内运行版本未知，建议确认是否已自动更新

---

*此文件由生态探索 cron 自动生成*
*下次探索：下一个 cron 周期*
