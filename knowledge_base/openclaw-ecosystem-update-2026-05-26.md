# OpenClaw 生态探索 2026-05-26

**日期**: 2026-05-26 20:00 UTC
**来源**: clawhub.ai + docs.openclaw.ai + GitHub releases

---

## ClawHub 统计
- 工具数: **52.7k**（无变化）
- 用户数: **180k**（无变化）
- 下载量: **12M**（无变化）
- 平均评分: **4.8**（无变化）
- 域名已转向: clawhub.com → clawhub.ai

---

## Docs 变化
- **推荐 Node 版本**: Node 24 (推荐) / Node 22 LTS (22.19+, 兼容)
  - 注意：我们当前运行 Node 22.22.1，属于兼容范围但非推荐版本
- 支持渠道: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等

---

## GitHub Releases 新变化 ⚠️

### v2026.5.25 (正式版, 5月25日)
- Alpine/musl Linux 安装器修复
- Windows 原生支持大幅改善
- OpenRouter 上下文限制修正（endpoint-specific limits）
- MCP 工具发现边界（hung MCP 不再阻塞）
- iMessage 多项修复
- Agent 提供者描述符缓存（性能优化）
- SecretRef IDs 支持 # 选择器

### v2026.5.25-beta.1 (Pre-release, 5月26日)
- iMessage 附件读取修复
- iMessage watcher 去重
- Codex sandbox path style 保留

---

## 值得关注
1. **OpenRouter 上下文修正** - 可能影响我们路由模型的上下文窗口估算
2. **从 2026.3.8 升级到最新版** - 差距约 2 个月，变更量很大
3. **Node 24 推荐** - 未来可考虑升级 Node 版本
