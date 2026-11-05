# OpenClaw 2026.11.5-beta.1 发布笔记

**抓取时间**: 2026-11-04 20:00 UTC
**版本**: 2026.11.5-beta.1 (预发布)
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🔥 重大新功能

### 1. Knowledge Scribes（知识抄写员）
- 一等公民级别的知识捕获功能
- 可复用的 scribe 工作流，跨 agent/session/Control UI
- PR: #185583, #185637, #185974, #186270, #186455, #187659
- 贡献者: @jalehman

### 2. PostgreSQL 数据层
- 新增 PostgreSQL 后端状态存储
- 迁移工具 + 现有部署兼容
- PR: #173968 等 9 个 PR
- 贡献者: @steipete

### 3. Control UI 大改版
- 移动端 + 桌面端导航/布局全面重构
- PR: #176356 等 6 个 PR
- 贡献者: @vyctorbrzezowski

### 4. 从聊天创建 PR
- 端到端 PR 准备/发布/审查/状态工作流
- 直接在对话中完成 GitHub PR 操作
- PR: #176105 等 6 个 PR
- 贡献者: @shakkernerd

### 5. 跨设备 & 云执行
- 扩展设备附加、云放置、网络访问工作流
- 更安全的 capability 交接
- PR: #185230, #185477, #186560, #187408

### 6. 决策 & 媒体模型
- 专门决策路由 + 媒体能力模型支持
- ClawRouter 集成
- PR: #177369 等 6 个 PR

### 7. 插件体验改进
- 插件发现/安装/编写/运行时集成
- PR: #177869, #182419, #185315, #185544

### 8. 备份 & 升级安全
- 更清晰的状态保留和回滚行为
- PR: #186953, #187564, #187688, #187737

---

## 📝 其他改进

| 类别 | 内容 |
|------|------|
| 自动化 | 持久化流 + 更丰富的调度执行上下文 |
| 分享 & 访客 | 扩展 session 分享、访客访问、访问者生命周期控制 |
| 学习 & 技能 | 改进 learned-skill 捕获/复用/引导编写 |
| Providers | 新增/改进 provider 集成、认证、模型发现 |
| 原生媒体 | 扩展原生图片/音频/视频处理 |
| Session 组合 | 改进多 session 组合/路由/协调执行 |
| 凭证兼容 | 改进凭证迁移和兼容性 |
| Doctor | 扩展 doctor 检查和自动修复指导 |
| 记忆维护 | 更安全的记忆清理和维护流程 |
| 模型路由 | 改进 provider-aware 模型选择和路由 |

---

## 🐛 重要修复

- Gateway 启动恢复/依赖排序
- Codex session 生命周期修复
- 回复正确性（线程/引用/去重/目标选择）
- 频道 & Talk（准入/音频/投递/重连）
- 出站媒体附件处理
- Control UI 无障碍（键盘/焦点/标签/响应式）
- Control UI 附件崩溃修复
- 记忆索引/检索/迁移/清理
- Provider 认证/发现/请求兼容
- 自动化调度器执行修复
- Doctor 防止 hosted 运行卡死 session

---

## 🔗 链接

- npm: https://www.npmjs.com/package/openclaw/v/2026.11.5-beta.1
- Release SHA: bc061f935bfd79ad09e3e98c6df9f2e8f1e28bea
- CI Report: https://github.com/openclaw/releases/blob/main/evidence/2026.11.5-beta.1/release-evidence.md

---

## 💡 对 Sandbot 的启示

1. **Knowledge Scribes** - 可以研究是否能增强我们的知识库自动捕获
2. **PostgreSQL 数据层** - 如果未来数据量大，可考虑迁移
3. **从聊天创建 PR** - 对 Lobster Orchestrator 开发有用
4. **持久化自动化流** - 可能改进我们的 cron 任务可靠性
