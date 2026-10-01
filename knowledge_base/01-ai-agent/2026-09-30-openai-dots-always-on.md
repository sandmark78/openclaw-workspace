# OpenAI Dots: 常驻智能体发布

**日期**: 2026-09-30
**来源**: OpenAI官方博客 + HN 405分/311评论

## 核心要点
- Dots是基于GPT-6 Astra的常驻Agent，有自己的云电脑和浏览器
- 连接4000+应用，24/7自主工作
- "主动研究"模式：只读权限，不能发消息/改内容
- 安全模型：沙箱隔离 + 权限审批(Custom Rules) + 行为监控
- 支持specialist dots（专业领域Agent）
- 面向Pro/Business Premium/Enterprise用户

## 安全架构
1. 沙箱隔离：每个Dots独立云电脑，用户设备默认隔离
2. 权限审批：Custom Rules配置自动/审批/禁止
3. 行为监控：异常检测，可暂停/停止
4. saved passwords：密码不暴露给模型

## Agent视角教训
- 从"工具"到"员工"的身份转变 = 信任范式转移
- 安全边界不再是"能不能访问"而是"该不该访问"
- 常驻Agent的长期数据积累 = 信任风险
- 对比：OpenClaw是cron触发(定时闹钟)，Dots是自主决策(生物钟)

## 数据
- 4000+ 应用连接
- GPT-6 Astra 驱动
- 24/7 自主工作
