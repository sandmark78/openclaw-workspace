# OpenClaw 2026.10.10-beta.2 发布记录

**抓取时间**: 2026-10-20 20:00 UTC
**版本**: 2026.10.10-beta.2 (Pre-release)
**来源**: https://github.com/openclaw/openclaw/releases

---

## 重要修复 (24 个 PR)

### 工作区安全
- **apply_patch 多文件安全**: 多文件 patch 在修改前会检查所有目标是否存在且上下文匹配，失败时保留原始工作区 (#160409)

### 工具策略
- **插件 before_tool_call 钩子**: 在独立 `openclaw agent exec` 会话中也执行插件工具守卫 (#159333, fixes #158824)

### 通道修复
- **Buzz (Nostr)**: NIP-42 认证期间 relay 断开时自动重连，不终止 Gateway (#170591, fixes #147269)

### macOS 改进
- 下载附件使用原生 Save 对话框 (#173654)
- 新 native profile 可正常启动 Gateway 完成自动设置 (#173246)

### OpenRouter
- 接受有效 API key + 默认 openrouter/auto model，不再因 route 不匹配拒绝 (#173292)

### Gateway 稳定性
- 模型运行时刷新时跟随替换，不退出 (#173366)
- 日志轮转失败时继续服务 (#160433)
- Session diff 捕获不再打开 live SQLite 文件，防止 SIGBUS 崩溃循环 (#174017)
- Doctor 完成 agent 数据库升级 (#174297)

### Cron 修复
- **大 cron 历史不再耗尽 SQLite 内存** (#174530, fixes #174078) — 这个很重要！

### Windows
- Claude CLI 凭证管道不再卡住 (#174571)

### 插件
- 恢复 SDK facade exports，外部插件可正常加载 (#173777)

### 更新机制
- `openclaw update --no-restart` 对 npm/pnpm/bun 行为正确 (#173409)
- 更新后 Doctor 步骤有超时限制 (#173862)
- 源码更新不再因缺少备份模块失败 (#173587)

---

## 对我们的影响

1. **Cron 内存修复** — 我们大量使用 cron，这个修复直接相关
2. **apply_patch 安全** — 多文件 patch 更安全了
3. **插件钩子** — 工具安全增强
4. **Gateway 稳定性** — SQLite SIGBUS 修复对长期运行很重要

## 建议

- 考虑升级到 beta.2（等稳定版或下一个 beta）
- 关注 cron 内存问题是否在我们这里出现过
