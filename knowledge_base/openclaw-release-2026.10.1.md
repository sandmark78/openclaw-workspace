# OpenClaw 2026.10.1 预发布版本

**发现时间**: 2026-10-07 20:00 UTC  
**状态**: Pre-release (预发布)  
**类型**: Gateway-only extended-stable (相当于 LTS)

---

## 重要更新摘要

### 1. Sessions 和 Memory 改进
- 跨注册表变更保留使用记录
- 远程工作区的 worker 附件传递
- 防止排队取消和转录别名阻塞活动轮次
- 嵌入缓存批量迁移 + 超大行报告

### 2. 回复和媒体
- 恢复本地视频内联播放
- 被拒绝的媒体链接替换为有用错误
- Telegram 进度更新不再显示预览卡片
- 修复 reasoning 启用时的纯语音回复

### 3. 更新和 Doctor
- 改进 serving-verdict 恢复指导
- 只读托管配置的修复仍然有效
- 移除重复的配置/备份/元数据/pnpm-root 探测
- 成功清理报告为进度而不破坏 JSON 输出
- 仍在启动的 Gateway 视为警告

### 4. Windows 工作区和浏览器启动
- 修复空和嵌套 Windows worktree 创建
- 改进 Linux Chromium 发现
- ARM64 上自动启动 Playwright Chromium

### 5. Cloud Workers 和 Crabbox
- 显示真正的 cloud-worker 故障
- 强制 Linux leases
- worker-bundle 下载与 bootstrap 重叠
- 防止慢读取或不支持的后端导致 worker 中断

### 6. Plugins, Codex, 和 MCP
- 保留 Bun 包导入捕获
- 减少 prerelease 元数据请求
- 防止过期的远程执行审批污染认证配置
- 恢复节点策略钩子
- 同步 MCP 表单/文件/上下文
- 后台技能审查通过 Workshop proposals 路由

### 7. 新增功能
- 添加 inactive-foundation 支持 incognito actor memory 和 Codex history routing
- 现有 agents 迁移到本地 Claws
- 减少 Sessions-board 和 state-path 开销

### 8. 即将弃用 (重要)
大量 SDK API 弃用警告，涉及：
- session-manager-sync-persistence → 使用 Async 后缀方法
- workspace-mutation-guard-callback → 使用 SQL-free guard.assertHost
- 多个 plugin SDK 兼容性别名移除
- media-legacy-projection → 使用有序媒体事实

---

## 升级建议

**当前状态**: 预发布版本，建议等正式版再升级  
**关注点**: 
1. Telegram 媒体播放修复（对我们有用）
2. Session/Memory 稳定性改进
3. 大量 SDK 弃用 → 如果用了插件需要关注

---

*来源: https://github.com/openclaw/openclaw/releases*
