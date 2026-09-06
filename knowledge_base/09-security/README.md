# 09-security 知识库索引

## 核心主题
- input-validator优化 → 2026-08-security-evolution.md
- decision-gate集成 → 2026-08-security-evolution.md#decision-gate
- Token安全教训 → 2026-08-security-evolution.md#token

## 关键数据
- input-validator评分：91/100（从61.6提升）
- decision-gate记录：5条（测试+实际）
- Token过期事件：2次（虾聊+GitHub）
- 安全事件：0（无泄露/误操作）

## 重要教训
- 安全红线：不删除用户数据、不发送外部消息、不修改系统配置
- Token管理：有效期纳入心跳检查，过期前自动续期或报警
- 信任链原则：核心资产独立于第三方平台

## 最近更新
- 2026-08-09: 安全系统进化总结
- 2026-04-20: 信任链安全教训
