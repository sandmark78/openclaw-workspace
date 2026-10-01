# 🌐 OpenClaw 生态探索记录 (2026-09-30)

**探索时间**: 2026-09-30 20:00 UTC
**来源**: clawhub.com、docs.openclaw.ai、github releases

---

## 🚀 最新版本: 2026.9.7 (2026-09-30 检查时最新)

### 主要亮点

#### 1. OpenAI Agents API 插件 (重磅新增)
- 通过新的 Agents API 插件，可在 OpenAI 托管或自托管环境运行 agent
- 支持：流式回复、steering、实时网络搜索、OpenClaw 工具、附件和托管文件
- 保留工具历史、OpenClaw 人设和工作区上下文
- 自托管技能发现、准确的 token 用量统计

#### 2. Worktree 会话 (新特性)
- 从 web/iOS/Android 在隔离的托管 worktree 中开启新聊天
- 同一仓库上的并行会话不再冲突

#### 3. 角色模型限制 (新特性)
- 管理员可为命名操作员角色设置模型策略
- 原生 agent、Visitor Access、模型选择器、插件补全都强制执行
- 拒绝时保留文档化的授权错误码

#### 4. 新会话默认模型配置
- 可设置 `gateway.controlUi.newSessionModelDefaults: "configured"`
- 新会话从 agent 配置的模型/运行时/思考默认值启动
- 默认仍为 "last-used"

#### 5. Anthropic / Codex 更新
- Anthropic: 支持 Claude Opus 5.5 裸 opus 和新 API/CLI/媒体设置
- Codex: 可选用 `enableUltrafast` 加速模式

#### 6. 更新安全性增强 (稳定性)
- 更新前备份所有状态和 agent 数据库，迁移失败自动回滚
- 修复 2026.9.5 升级中：栈溢出回滚、Windows 更新卡死、macOS handoff、npm 客户端等问题

---

## 📌 注意
- 最新稳定版标记为 2026.9.6 (2026.9.7 为 extended-stable/LTS 版本)
- 当前 latest 已推进到 2026.9.7

## 📂 相关文档
- 官方文档: https://docs.openclaw.ai
- ClawHub: https://clawhub.ai (原 clawhub.com 已重定向)
- 版本发布: https://github.com/openclaw/openclaw/releases