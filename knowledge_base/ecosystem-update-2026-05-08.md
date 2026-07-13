# 生态探索更新 2026-05-08

**检查时间**: 2026-05-08 20:00 UTC

---

## 🔴 发现：OpenClaw 新版本可用

| 项目 | 值 |
|------|-----|
| 当前安装版本 | 2026.3.8 |
| npm 最新版本 | **2026.5.7** |
| 上次检查版本 | 2026.5.6 (2026-05-06) |
| 最新 Release | v2026.5.7 (2026-05-07) |
| 版本差距 | 落后约 2 个月 |
| 升级命令 | `openclaw gateway update` 或 `npm install -g openclaw@latest` |

### v2026.5.7 核心变更（5月7日发布）

**OpenAI 相关**:
- 支持 `openai/chat-latest` 作为显式 API-key 模型覆盖，可尝试 ChatGPT Instant API

**Cron 相关**:
- `cron list --json` / `cron show --json` 包含计算状态 (disabled/running/ok/error/skipped/idle)
- `cron doctor --fix` 修复 payload.model 存为 "default"/"null"/空白的问题 (#78549)
- isolated runs 无历史路由时在执行前快速失败，省 token (#78608)

**Telegram 相关**:
- 支持 `accessGroup:*` 发送者白名单用于 DM/群组/原生命令授权 (#78660)
- 入站轮询器 liveness 监控修复，防止出站调用掩盖入站轮询挂死 (#78422)
- 同聊天内消息工具出站发送视为已投递 (#78685)

**Sessions/上下文**:
- `/new` 和 `sessions.reset` 时清除缓存的技能快照 (#78873)
- 上下文引擎缓存失效修复，防止复用过期历史 (#77968)
- 每日会话轮播时持久化新 transcript 文件 (#78607)

**其他重要修复**:
- Discord 跨频道消息路由修复 (#78572)
- 压缩摘要 reserve tokens 适配模型输出限制 (#54392)
- Tavily 工具凭证从运行时配置快照解析 (#78610)
- 原生命令 owner enforcement
- Active Memory 全局切换需 admin scope
- 子 Agent 归档 TTL 统一使用 `archiveAfterMinutes` 配置 (#78263)
- 外部插件 channel 设置转发修复 (#77779)

---

## 🟡 ClawHub 生态数据（无变化）

- 工具总数: 52.7k
- 用户数: 180k
- 下载量: 12M
- 平均评分: 4.8

与上次检查一致。

---

## 🟢 Docs 扫描（无显著变化）

docs.openclaw.ai 页面结构稳定，新增 `llms.txt` 索引提示。
核心内容覆盖不变。

---

## 📊 与历史版本对比

| 日期 | 最新版本 | 变化 |
|------|----------|------|
| 2026-05-06 | 2026.5.6 | — |
| 2026-05-08 | **2026.5.7** | +1 版本 (5/7 发布) |
