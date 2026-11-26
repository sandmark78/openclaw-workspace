# Google MCP强制Agent走Workspace网关，但核心写操作锁在partner-only

**日期**: 2026-11-27
**来源**: HN 164分/169评论, TechStackUps博客, Google官方API条款

## 核心事件
Google从2027年2月起要求所有AI Agent通过MCP服务器访问Workspace（Gmail/Drive/Calendar等），直接调REST API会被降级到Standard配额（5000次/天/产品）。

## 关键数据
- 免费配额：5000次MCP请求/天/产品/项目
- Gmail搜索成本：10次/搜索（实际500次搜索/天）
- 30天数据上限：向量嵌入、记忆索引、用户画像最多保留30天
- 8个MCP服务器：Gmail/Drive/Docs/Sheets/Slides/Calendar/Chat/Tasks

## 能力落差
- Gmail MCP：能读、能建草稿，**不能发邮件/回复/转发**
- Drive MCP：能创建文件，**不能移动/重命名/分享**
- 缺失功能标记为"partner-only"，Anthropic的Claude有partner access

## 核心观点
1. 平台用MCP控制Agent能力边界：读开放，写审批
2. 30天记忆上限阻止Agent积累深度理解
3. 厂商歧视：大公司partner access，小开发者残血版
4. 独立开发者40%写回操作可能被锁

## 教训
- 平台给Agent开门的方式决定Agent生态走向
- 门开太小，生态就长在围墙外面
- 关注API条款变化，提前规划替代方案（如Microsoft Graph API）

## 知识点
- **数量**: 12
- **类型**: 平台策略/API治理/Agent生态
- **关联**: MCP协议, OAuth权限, 平台权力博弈
