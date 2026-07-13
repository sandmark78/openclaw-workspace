# OpenClaw Zalo Channel Plugin - 越南消息应用集成

**来源**: docs.openclaw.ai/channels/zalo
**发现时间**: 2026-03-24 20:00 UTC
**数量**: ~25 知识点
**状态**: 实验性 (experimental)

---

## 概述

Zalo 是越南最流行的消息应用，OpenClaw 通过插件支持 Zalo Bot API 集成。

- **状态**: 实验性
- **支持**: 仅 DM (私聊)
- **安装**: `openclaw plugins install @openclaw/zalo`
- **适用场景**: 客服、通知等需要确定性路由回 Zalo 的场景

## 关键特性
- 确定性路由：回复直接回到 Zalo，模型不选择通道
- DM 共享 Agent 主会话
- 默认 DM 策略为 pairing

## 配置示例
```json5
{
  channels: {
    zalo: {
      enabled: true,
      accounts: {
        default: {
          botToken: "12345689:abc-xyz",
          dmPolicy: "pairing",
        },
      },
    },
  },
}
```

## 注意事项
- Zalo Bot Creator / Marketplace bots 与 Zalo Official Account (OA) bots 是不同产品
- 当前仅支持 Marketplace-bot 行为
- 多账户支持：通过 `channels.zalo.accounts` 配置
- Token 可通过环境变量 `ZALO_BOT_TOKEN=...` 设置

## 市场意义
- 越南市场切入点 (1亿+ 用户)
- 东南亚 AI Agent 部署的新通道
- 与 Telegram/Discord 互补的区域性通道
