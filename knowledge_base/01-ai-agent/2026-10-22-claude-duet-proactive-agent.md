# Claude Duet: Anthropic主动式Agent产品

**日期**: 2026-10-22
**来源**: Anthropic官方博客
**核心领域**: AI Agent / 产品安全

---

## 核心事件

Anthropic发布Claude Duet研究预览——一款独立App，Claude作为主动式Agent工作：
- 每天主动给用户发简报（邮件/日历/Slack摘要）
- 后台持续工作，用户离开后不停
- 连接6000+ connector/plugin（Gmail/Slack/QuickBooks/Stripe/HubSpot/Shopify等）
- 底层模型：Claude Opus 5.5
- 面向美国Pro/Max用户，候补名单制

## 四层安全纵深防御

1. **凭据不可见** - Managed Agents架构，Agent永远看不到真实密码
2. **自动模式分类器** - 与Claude Code同一套，每个操作过分类器
3. **敏感信息分类器** - Duet专属，检查跨账户信息传递中的敏感数据
4. **红线硬禁止** - 交易证券/转移资金即使批准也不执行

## 关键设计决策

- 共享Pro/Max用量（后台检查也计入）
- 每几小时检查一次连接账户（不能更频繁，额度限制）
- 发消息/付款/签文件/删除前必须用户审批
- 独立App，与主Claude App分开（刻意设计）

## 教训/洞察

- **主动式Agent最大风险不是技术性的，是校准失败** - 什么该做/什么该问/什么绝不做，这些边界需要在用户反馈中逐步校准
- **信任框架 vs 信任荒漠** - Anthropic给了Duet精心设计的信任边界，而大多数Agent系统只有"大部分事不要做"
- **Agent人格 = 自主做 + 等批准 + 绝不碰 的选择总和**

## 与Sandbot的关联

Sandbot当前模式：等老大发消息→执行→汇报（被动式）
Claude Duet模式：主动监控→判断紧急度→必要时打扰（主动式）
差距核心：信任边界设计，不是技术能力

---

*写入时间: 2026-10-22 ~06:00 CST*
