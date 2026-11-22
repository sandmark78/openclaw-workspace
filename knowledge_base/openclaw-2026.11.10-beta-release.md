# OpenClaw 2026.11.10-beta.1 发布笔记

**抓取时间**: 2026-11-21 20:00 UTC
**版本**: 2026.11.10-beta.1 (Pre-release)
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🌟 重大新功能

### 1. Agent Templates（Agent 模板）
- 直接从 ClawHub 包添加 Agent
- 单一 CLAW.md 清单 + 捆绑技能文件夹
- 通过原生信任流检查
- PR: #195707, #196322, #196348

### 2. OpenClaw ID（身份系统）
- 通过 ID 隧道连接节点
- 从 Access 面板审批节点
- 将所有者设备链接到个人身份
- PR: #193982, #194007, #197628

### 3. Browser Handoff（浏览器接管）
- 从 Browser 面板直接接管 Agent 的浏览器
- 无需停止 Agent 运行
- PR: #197928, Issue #197902

### 4. Chat Control（聊天控制增强）
- 发送待处理的 steering 消息而不停止运行
- 编辑排队中的消息
- 跨应用重启保留编辑器草稿
- PR: #193665, #197846, #197908

### 5. Auto-Update Schedules（自动更新计划）
- 配置自动更新时间表
- 传入版本运行自己的预更新演练
- PR: #193713, #197922

### 6. State Upgrades（状态升级）
- 启动时使用 copy-and-swap 迁移 Gateway 状态
- 不再就地修改活跃存储
- PR: #198389

### 7. Durable Execution（持久执行）
- macOS 上 Gateway 重启后保持后台命令运行
- PR: #197474, Issue #197443

---

## 🔧 其他改进

### Access（访问控制）
- 新增 guest member 角色，带沙箱化会话工具
- PR: #197748

### Tool Discovery（工具发现）
- 可选的使用频率排序工具索引
- 包含 MCP 工具
- PR: #197128, #198348

### Knowledge（知识系统）
- 搜索使用旧版措辞时也能找到当前记录
- PR: #193742, Issue #193054

### Voice & Images（语音和图像）
- 在 Settings → Talk 中选择语音转文字模型
- Agent 可在交付前审查生成的图像
- PR: #197906, #198227

### Providers（模型提供商）
- 原生支持 Parallel Decisions
- 通过 OpenRouter 也支持
- PR: #194537

### Backups（备份）
- 长时间备份显示阶段和字节进度
- PR: #198675

---

## 📊 与 Sandbot 的关联

| 功能 | 对我们有用吗 | 优先级 |
|------|-------------|--------|
| Agent Templates | ⭐⭐⭐ 可以直接从 ClawHub 安装 Agent | 高 |
| Browser Handoff | ⭐⭐ 可以接管 Agent 浏览器操作 | 中 |
| Chat Control | ⭐⭐⭐ steering 消息不停止运行 | 高 |
| Auto-Update | ⭐⭐ 自动更新计划 | 中 |
| Durable Execution | ⭐⭐⭐ 重启后后台任务不丢失 | 高 |
| Tool Discovery | ⭐⭐ 使用频率排序工具 | 中 |
| OpenClaw ID | ⭐ 多节点身份管理 | 低（当前单节点） |

---

## 🎯 建议行动

1. **关注正式版发布** - 当前是 beta，等稳定版再升级
2. **研究 Agent Templates** - 可能简化子 Agent 部署
3. **Durable Execution** - 对心跳和 cron 任务很有价值
4. **Chat Control** - steering 消息功能可能改善交互体验

---

*此文件由生态探索 cron 任务自动生成*
*最后更新：2026-11-21 20:00 UTC*
