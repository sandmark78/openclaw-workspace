# OpenClaw 生态探索 - 2026-06-13

**探索时间**: 2026-06-13 20:00 UTC
**来源**: clawhub.ai / docs.openclaw.ai / GitHub Releases
**状态**: 🆕 有新版本

---

## 变更摘要

| 来源 | 状态 | 详情 |
|------|------|------|
| ClawHub.ai | 📭 无变化 | 52.7k 工具 / 180k 用户 / 12M 下载 / 4.8 评分 |
| docs.openclaw.ai | 📭 无变化 | 文档内容未更新 |
| GitHub Releases | 🆕 **新版本** | 预发布 2026.6.7 (2026-06-13) ← **今天新发布** |

---

## GitHub Release 2026.6.7 要点 (Pre-release, 2026-06-13)

### 1. 频道交付增强
- Slack/Telegram 交付更紧密：同频道 Slack 最终消息保留在转录中
- Telegram 可扩展 blockquotes 和 spooled replay 存活交付
- 静默助手回复保持静默
- 进度草稿启动失败会被报告
- 频道操作结果页面可增量获取

### 2. 提供商和模型处理更健壮
- **Kimi K2.7 Code 上线** 🆕
- Kimi 原生 tool-call IDs 和 replayed reasoning_content 修复
- Mistral 跳过不可读的 tool schema
- Fireworks catalog 参数从 manifests 获取
- DeepSeek 保持配置的静态传输
- 提供商 fallbacks 正确解析
- Anthropic thinking replay 修复
- Anthropic Vertex 停止重新标记传输预算缓存控制

### 3. 安全边界加固
- **Feishu 不再泄露 prompt-preface 运行时上下文到回复中** 🔒
- WebSocket 载荷处理加固
- CLI-backed /btw fallback fail-closed
- 本地 setup trust 加固
- Skill Workshop symlink 写入在回滚元数据写入前被门控和验证

### 4. Agent/Memory/Codex/Cron 修复
- 无效插件模型 catalog 隔离
- QMD 启动失败存活 fallback 错误
- Codex memory prompts 保持注册
- 源消息工具回复不再阻止 agent 进度
- 结构化不支持的模型错误分类
- heartbeat/cron 终端状态保留
- Linux 服务更新干净交接
- cron 状态报告 SQLite store 路径

---

## 当前运行版本提醒

- **运行版本**: OpenClaw 2026.3.8
- **最新正式版**: 2026.6.5
- **最新预发布**: **2026.6.7** 🆕 (2026-06-13)
- **落后**: 约 3 个月

---

## 建议

预发布 2026.6.7 包含重要的 Feishu 安全修复（不再泄露上下文）和多个模型提供商修复。建议关注正式版发布后考虑升级。
