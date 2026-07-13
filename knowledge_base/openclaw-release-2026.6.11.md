# OpenClaw v2026.6.11 发布说明

**发现时间**: 2026-07-11 20:00 UTC
**当前版本**: v2026.3.8 (我们)
**最新版本**: v2026.6.11 (2026-06-11 发布)
**状态**: ⚠️ 落后约 3 个月，建议升级

---

## 核心改进

### 1. 通道投递可靠性 (重点)
- **Telegram**: 引用回复更准确，进度气泡清理逻辑优化
- **WhatsApp/Matrix/Google Chat/iMessage/Feishu**: 重连和消息投递修复
- **Discord**: 回复和镜像聊天历史绑定更稳定
- **后台任务**: 图片/视频/音乐结果现在能正确返回到请求的聊天
- **飞书**: 语音回复现在显示时长
- **QQBot**: 群管理员可控制斜杠命令可见性
- **心跳**: 推理模型不再在通道中暴露内部推理过程

### 2. 其他改进
- Google Chat 私聊不再被误判为群聊
- iMessage 命令和链接消息合并优化
- WebChat 和控制台 UI 修复
- 终端 UI 修复

### 3. 管理安全
- 更安全的默认管理员设置

---

## 升级建议

**优先级**: P1 (重要)
**原因**: 
1. Telegram 回复准确性改进直接影响我们的日常使用
2. 后台任务投递修复解决"消息发错人"问题
3. 心跳推理隐藏避免暴露内部思考
4. 3 个月的 bug 修复积累

**风险**: 中等 (跨 3 个月版本，需检查 breaking changes)
**建议**: 先查看完整 release notes，备份配置后升级

---

## ClawHub 生态

- 热门技能: self-improving-agent (3.9k⭐), skill-vetter (1.3k⭐), ontology (649⭐)
- 新趋势: 安全审查类技能 (skill-vetter, SkillScan) 受到关注
- 生态项目: Crabbox, ClickClack, Crabfleet, Octopool 等多个社区项目

---

*完整说明: https://docs.openclaw.ai/releases/2026.6.11*
