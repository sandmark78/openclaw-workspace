# OpenClaw 生态探索记录 2026-06-05

**抓取时间**: 2026-06-05 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, GitHub Releases

---

## 📊 ClawHub 平台数据

- **域名**: clawhub.com → 重定向到 clawhub.ai
- **工具总数**: 52.7k
- **用户数**: 180k
- **总下载**: 12M
- **平均评分**: 4.8
- **三大板块**: Skills (技能包)、Plugins (网关插件)、Publishers (构建者和组织)

---

## 🆚 版本差距

| 项目 | 值 |
|------|------|
| **当前运行版本** | OpenClaw 2026.3.8 |
| **最新预发布** | 2026.6.2 (2026-06-03) |
| **最新稳定版** | 2026.5.30 (2026-05-30) |
| **落后版本** | 3 个大版本！(3.8 → 5.30 → 6.2) |

---

## 🔥 2026.6.2 预发布亮点 (2026-06-03)

1. **插件/技能安装策略革新**: 用 operator install policy 替换了旧的 dangerous-code scanner，更清晰的 doctor/CLI/ClawHub/排障界面
2. **通道交付安全增强**: Telegram、Feishu、Discord、WhatsApp 在重复转录镜像、Telegram 管理员回写、流式最终预览、审批允许列表、轮询修饰符等方面更安全
3. **UI 全面改进**: Chat、Control UI、Skill Workshop、Workboard、Android 伴侣、WebChat 流式文本保留、ACK 计时、Workboard 键盘移动、对话框无障碍、懒加载使用视图
4. **安全/策略/配置恢复**: 拒绝损坏的 shell 快照、不支持的策略键、不安全的 exec 审批预检查环境、格式错误的脚本限制、可疑的网关启动配置

---

## 🔥 2026.5.30 稳定版亮点 (2026-05-30)

1. **Agent/Codex 运行时恢复更稳定**: 子 agent cwd/workspace 分离、hook 上下文保持 prompt-local、会话锁超时释放、Codex 失败不再破坏共享运行时
2. **通道交付和会话身份更安全**: Matrix 房间 ID、iMessage 反应/审批、Slack 最终回复、Discord 恢复工具警告、WhatsApp 配置文件认证根、Telegram 轮询、Microsoft Teams 服务 URL 信任检查

---

## 📝 行动建议

⚠️ 当前版本 2026.3.8 落后较远，建议老大考虑升级到 2026.5.30（稳定版）。主要收益：
- 通道交付安全性大幅提升（直接影响 Telegram）
- Agent 运行时稳定性增强
- 插件安装策略革新

---

*自动生成，下次生态探索将对比此快照*
