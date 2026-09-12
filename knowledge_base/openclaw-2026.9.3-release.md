# OpenClaw 2026.9.3 版本更新

**抓取时间**: 2026-09-09 20:00 UTC
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🆕 重大新功能

### 1. 更安全的更新机制
- 在隔离的候选状态中预演核心和插件变更
- 支持 2026.9.2 迁移
- 恢复被遗弃的更新记录而不停止健康的 Gateway

### 2. 性能优化
- 保留热 prompt 缓存
- 减少冷会话更新和记忆搜索中的不必要工作
- 会话间复用 worker 构建

### 3. Skill Workshop 改进
- 技能在一个持久化的 agent 所有集合中管理（跨工作区）
- 比较完整技能指令
- 通过 Doctor 安全退役缺失草稿建议

### 4. 浏览器标签页增强
- 实时和本地标签页：观察 agent 页面重绘
- Mac 上可在本地标签页中打开外部链接，切换聊天时保持标签页

### 5. 提供商账户统一管理
- 在 Models 设置中管理已连接账户和优先级

### 6. 会话分享功能
- 可发布可撤销的只读会话视图
- 任何有公开链接的人可访问

### 7. 会议记录库
- 浏览保存的笔记，搜索完整转录
- 下载 Markdown 或 JSONL 归档
- 从 Control UI 管理捕获源

### 8. 团队活动报告（可选）
- 安装启用后可浏览 GitHub 活动和 Discord 讨论
- 存储历史 + 可选模型摘要

---

## ⚠️ Breaking Changes

### Node.js 要求变更（重要！）
- **要求**: Node 24.16.0+ (24.x) 或 Node 26.1.0+
- **推荐**: Node 26
- **不再支持**: Node 22, Node 25, 更早的 24.x/26.x
- **我们当前**: Node v24.16.0 ✅ 刚好满足要求

### execution-policy SDK 变更
- exec-mode 和 comparator helpers 从 infra-runtime 移至 execPolicy
- 需使用 resolveExecModePolicy

---

## 📊 对我们的影响

| 项目 | 状态 | 说明 |
|------|------|------|
| Node 版本 | ✅ 满足 | v24.16.0 刚好是最低要求 |
| Skill Workshop | ✅ 可受益 | 我们的技能管理会更稳定 |
| 性能优化 | ✅ 可受益 | 热缓存 + worker 复用 |
| 会话分享 | 🆕 新功能 | 可以分享对话给老大看 |
| 更新机制 | ✅ 更安全 | 升级风险降低 |

---

## 🔗 相关链接
- GitHub Release: https://github.com/openclaw/openclaw/releases/tag/2026.9.3
- 文档: https://docs.openclaw.ai
- ClawHub: https://clawhub.ai
