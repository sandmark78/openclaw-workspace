# 生态扫描报告 - 2026-06-14

**扫描时间**: 2026-06-14 20:00 UTC  
**执行者**: Sandbot 🏖️ (cron 任务)

---

## 📊 当前状态 vs 最新版本

| 组件 | 当前版本 | 最新版本 | 差距 |
|------|----------|----------|------|
| OpenClaw | 2026.3.8 | **2026.6.8** (pre-release) | ⚠️ 落后 ~3个月 |
| ClawHub | - | 52.7k tools / 180k users | 持续增长 |

---

## 🦞 ClawHub 动态

- **域名变更**: clawhub.com → **clawhub.ai** (自动重定向)
- **规模**: 52.7k 工具 | 180k 用户 | 12M 下载 | 4.8 平均评分
- **定位**: "Tools built by thousands, ready in one search."
- **三大板块**: Skills (Agent skill bundles) / Plugins (Gateway plugins) / Publishers (People and orgs)

---

## 📖 docs.openclaw.ai 更新

- **推荐 Node 版本**: Node 24 (推荐)，Node 22 LTS (22.19+) 兼容
- **支持通道**: Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo, 等
- **核心能力**:
  - 多通道网关 (单 Gateway 服务所有通道)
  - 插件通道 (Matrix, Nostr, Twitch, Zalo 等)
  - 多 Agent 路由 (隔离 session)
  - Web 控制面板
  - 移动端节点 (iOS/Android Canvas/相机/语音)

---

## 🚀 GitHub Releases - 2026.6.8 亮点 (2026-06-13)

### 1. Telegram & WhatsApp 增强
- Telegram 可发送结构化富文本 (表格、列表、可扩展引用)
- 保留 prompt 的 CLI 后端交付
- 更安全的富媒体边界
- WhatsApp 现在尊重配置的 ACP 绑定

### 2. Agent/Gateway 恢复优化
- 账户范围 DM 发送改进
- 生成媒体补全优化
- 自动回复消息工具最终回复
- 心跳去重 (heartbeat dedupe)
- Session 身份提示优化
- 未知 OpenAI Agent 选择器拒绝

### 3. 新模型/提供商支持
- **GLM-5.2** 支持
- **Claude Haiku 4.5** 目录条目
- OpenRouter 和 Google Vertex 提供商前缀规范化
- LM Studio 二进制 thinking-off 交付
- Claude 4.5 Copilot 工具流安全

### 4. /usage 和回复钩子
- 原生完整 footer 渲染器
- 凭证感知限制
- 更好的部分计数处理

### 5. UI 和移动端
- 工作区文件可折叠
- WebChat 回滚支持流式传输
- 侧边栏 session 选择器交互优化
- iOS 重新连接过时前台网关

### 6. 内存/诊断
- 过大 OpenAI 嵌入批次自动分割
- QMD 内存搜索在瞬态模式下可用
- SQLite 避免 NFS 状态卷上的 WAL
- 完整内存重新索引保留回滚/缓存恢复

---

## ⚠️ 行动建议

1. **P0**: 考虑升级到 2026.6.8 (有重大 Telegram 增强和恢复优化)
2. **P1**: 关注 ClawHub 技能生态增长 (52.7k 工具)
3. **P2**: 检查新模型 GLM-5.2 是否适合我们

---

*下次扫描建议: 2026-06-21*
