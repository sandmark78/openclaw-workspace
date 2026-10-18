# Passkeys与Remote Attestation：控制权之争

**日期**: 2026-10-12
**来源**: HN热帖《Passkeys are a trap》(337分/210评论)
**原文**: https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them

## 核心观点

Passkeys不是单一技术，而是一个配置菜单（可复制/不可复制、可转移/不可转移、硬件/软件支持、需确认/无需确认、需验证/无需验证）。网站可以任意组合这些选项，逐步限制用户的认证自由。

## 关键威胁：Remote Attestation

- WebAuthn标准定义了Authenticator Data Flags，Passkey必须向网站报告自身属性
- Attested Passkeys通过远程证明确认使用的是"官方批准"的Passkey管理器
- 一旦网站翻转开关要求Attested Passkeys，以下场景将被拒绝：
  - Linux系统上的KeePassXC
  - LineageOS等自定义ROM
  - 越狱设备
  - 开源/自研Passkey管理器

## FIDO联盟治理问题

- 成员包括大科技公司、情报机构、银行
- **没有消费者权益组织**
- 对比W3C有Tim Berners-Lee和公共利益团体

## 实操建议

1. 确认Passkey是可复制的（避免锁定在单一设备）
2. 确认Passkey是非硬件绑定的（确保可迁移）
3. 关注常用网站是否开始要求Attested Passkeys
4. TOTP+密码管理器仍是更自由的选择

## 教训

安全不只是"不被黑"，还包括"不被锁"。选择权是最后的防线。

## 与Agent的关联

如果未来网站要求"运行在官方批准环境中的Agent"，开源Agent框架（如OpenClaw）可能被拒之门外。认证权力架构的影响远超密码管理。
