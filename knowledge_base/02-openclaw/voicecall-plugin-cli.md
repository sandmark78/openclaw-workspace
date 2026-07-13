# OpenClaw Voice Call Plugin - 语音通话能力

**来源**: docs.openclaw.ai/cli/voicecall
**发现时间**: 2026-03-24 20:00 UTC
**数量**: ~20 知识点

---

## 概述

`openclaw voicecall` 是一个插件提供的命令，需要安装并启用 voice-call 插件后才可用。为 Agent 提供语音通话能力。

## 核心命令

```bash
# 查看通话状态
openclaw voicecall status --call-id <id>

# 发起语音通话
openclaw voicecall call --to "+15555550123" --message "Hello" --mode notify

# 继续通话
openclaw voicecall continue --call-id <id> --message "Any questions?"

# 结束通话
openclaw voicecall end --call-id <id>
```

## Webhook 暴露 (Tailscale)

```bash
# 通过 Tailscale Serve 暴露
openclaw voicecall expose --mode serve

# 通过 Tailscale Funnel 暴露 (公网)
openclaw voicecall expose --mode funnel

# 关闭
openclaw voicecall expose --mode off
```

## 安全注意事项
- 只向信任的网络暴露 webhook 端点
- 优先使用 Tailscale Serve 而非 Funnel
- Funnel 会暴露到公网，需谨慎

## 能力扩展意义
- Agent 从文本交互扩展到语音交互
- 支持通知模式 (mode: notify) 的主动外呼
- 可与 Cron/Standing Orders 结合实现自动语音通知
- 对客服、紧急通知等场景有直接价值

## 依赖
- voice-call 插件
- Tailscale (用于 webhook 暴露)
- 电话号码格式: 国际格式 (+国家代码)
