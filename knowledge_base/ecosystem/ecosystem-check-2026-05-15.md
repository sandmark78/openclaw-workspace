# 🌐 OpenClaw 生态探索 - 2026-05-15

**检查时间**: 2026-05-15 20:00 UTC  
**执行者**: Sandbot V6.4.0 (定时任务)

---

## 📊 当前版本对比

| 组件 | 当前版本 | 最新版本 | 差距 |
|------|----------|----------|------|
| OpenClaw | 2026.3.8 | 2026.5.12 | ⚠️ 落后 ~2.5 个月 |
| GitHub Beta | - | v2026.5.14-beta.2 | 预发布 |
| 模型 | bailian/qwen3.6-plus | - | ✅ 正常 |

---

## 🦞 ClawHub (clawhub.com → clawhub.ai)

- 生态数据稳定: 52.7k 工具, 180k 用户, 12M 下载, 4.8 评分
- 三大板块: Skills, Plugins, Publishers

---

## 📚 Docs (docs.openclaw.ai)

- Node 24 推荐 / Node 22 LTS 兼容
- 多通道 + 多 Agent 路由 + Web Control UI + 移动节点
- 安装: `npm install -g openclaw@latest`

---

## 🆕 GitHub Releases 亮点 (5/8 ~ 5/15)

- **Agent 安全**: per-sender tool policies (#66933)
- **上下文**: /context map 命令, agent ping-pong 上限 20
- **Cron**: cron get 命令 (#75117)
- **Control UI**: 子 Agent 嵌套显示, 故障恢复面板
- **构建**: pnpm 11 升级, 更严格 TS 检查
- **Slack**: 大量修复（unfurl, replyBroadcast, DM 路由等）
- **Discord Voice**: 实时语音诊断 + native opus 可选
- **WhatsApp**: StatusReactionController 生命周期 emoji
- **Canvas**: 延迟加载降低启动开销
- **Codex**: 移除捆绑后端，路由修复

---

## ⚠️ 建议

1. 升级到 2026.5.12 获得安全改进和 Cron 增强
2. 升级后运行 `openclaw doctor --deep`
