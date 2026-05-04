# OpenClaw 生态探索扫描 (2026-04-30 20:00 UTC)

**扫描时间**: 2026-04-30 20:00 UTC
**当前版本**: 2026.3.8
**最新版本**: 2026.4.29-beta.3 (2026-04-29 发布，Pre-release)
**状态**: ⚠️ 有可用更新 (落后约 1.5 个月)

---

## 与上次扫描 (2026-04-29) 对比

| 项目 | 上次 | 本次 | 变化 |
|------|------|------|------|
| 最新版本 | 2026.4.26 | **2026.4.29-beta.3** | 🆕 +3 次修订，Beta 版 |
| ClawHub 工具数 | 52,700 | 52,700 | - |
| 用户数 | 180,000 | 180,000 | - |
| 下载量 | 12,000,000 | 12,000,000 | - |
| 平均评分 | 4.8 | 4.8 | - |

---

## 🆕 v2026.4.29-beta.3 新增亮点

### 1. 🧠 消息与自动化增强
- **默认启用 active-run steering**：消息队列自动转向模型边界
- **visible-reply enforcement**：全局 messages.visibleReplies 要求所有可见输出经 message(action=send) 发送
- **spawned subagent routing metadata**：子 Agent 聊天和广播 payload 新增 spawnedBy 字段，方便路由
- **opt-in follow-up commitments**：心跳驱动的待办提醒，支持 commitments.enabled/commitments.maxPerDay 配置

### 2. 📖 Memory 进化为「人物感知 wiki」
- **人物 wiki 元数据**：canonical aliases, person cards, relationship graphs
- **隐私/来源追溯**：provenance 报告、evidence-kind drilldown
- **per-conversation Active Memory 过滤器**：allowedChatIds / deniedChatIds，可选择性回忆
- **超时部分召回**：子 Agent 超时时返回有界部分摘要

### 3. 🚀 Provider/Model 覆盖扩展
- **NVIDIA onboarding + catalogs**：更快的 manifest-backed 模型/认证路径
- **Bedrock Opus 4.7 thinking parity**
- **更安全的 Codex/OpenAI-compatible replay 和 streaming 行为**

### 4. 🔧 Gateway/Plugin 可靠性
- 慢主机启动优化
- 可复用模型目录
- 事件循环就绪诊断
- 运行时依赖修复
- 过期会话恢复
- 版本范围更新缓存

### 5. 📡 通道修复
- **Slack**：Block Kit 限制
- **Telegram**：proxy/webhook/polling/send 韧性增强
- **Discord**：启动/速率限制处理
- **WhatsApp**：交付/心跳
- **Microsoft Teams / Matrix / Feishu**：边缘情况修复

### 6. 🔒 安全与运营
- **工具安全加固**：tools.exec/tools.fs 配置不再隐式放宽 restrict 配置
- **OpenGrep 扫描**：新增代码安全扫描
- **更严格的 GHSA 分类策略**
- **更安全的 exec/pairing/owner-scope 处理**
- **Docker/onboarding 自动化**
- **web-fetch IPv6 ULA opt-in**（可信代理栈）

---

## ClawHub 平台数据

- 域名: clawhub.com → clawhub.ai (重定向)
- 工具总数: **52,700**
- 用户总数: **180,000**
- 下载总量: **12,000,000**
- 平均评分: **4.8**

---

## 建议

1. **版本升级**: 当前 2026.3.8 → 最新 2026.4.29-beta.3，Beta 版建议评估后再升级
2. **重点关注**:
   - Memory 人物 wiki 功能对我们的记忆系统有参考价值
   - active-run steering 默认启用可能影响现有消息流
   - visibleReplies 可能影响 Telegram 回复行为
3. **安全修复**: 工具权限收紧需注意当前配置是否受影响
4. **通道修复**: Telegram proxy/webhook/polling/send 韧性增强值得关注
