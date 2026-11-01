# YC Labs Minecraft Agent Swarm 实验

**日期**: 2026-10-30
**来源**: Y Combinator Labs《Agents in Games》
**HN**: 212分68评论

## 核心事件
YC Labs与Olam Labs联合实验：50个GPT-6.1 Sol Agent在Minecraft生存世界运行3小时，目标"建立繁荣文明"。

## 关键发现
1. **层级按目录顺序形成**：Ada排第一，成为事实领导人
2. **第一晚死亡22/34**：僵尸、骷髅、蜘蛛导致Agent永久保守化
3. **官僚系统自发涌现**：食物配给表(food-queue.md)、审批流程、快递调度
4. **5900条消息/3小时**：每Agent每小时118条消息
5. **框架已开源**：github.com/yc-software/minecraft-agent-harness

## 核心洞察
- 多Agent系统的瓶颈不是智能，是协调开销
- Agent会复制人类官僚主义，因为这是不确定性下的安全解
- 协调成本随Agent数量指数增长，50个Agent需要food-queue.md，500个需要什么？

## 技术细节
- 基于Mineflayer，核心循环用Pi运行
- Agent能力：观察、推理、记忆、行动、消息、脚本执行
- 死亡无惩罚（只掉装备），但死亡日志导致行为保守化

## 教训
- "让1000个Agent解决问题"假设沟通零成本，但Civ50显示沟通本身就是成本
- 人类官僚主义根源不是人类笨，而是协调难
- AI继承了这个问题，而不是解决了它
