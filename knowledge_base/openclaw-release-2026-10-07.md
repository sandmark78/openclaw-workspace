# OpenClaw 2026.10.7 版本发布记录

**抓取时间**: 2026-10-25 20:00 UTC  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🎯 核心亮点

### 1. 会话恢复安全性增强 (Replay-safe session recovery)
- 中断的会话保留恢复来源和未完成的工具结果
- 停止的对话在接受下一条消息前清理终端恢复残留
- 被拒绝的 Claude CLI 草稿不会出现在最终回复中
- 大批量子任务完成保持在请求者上下文内
- Codex 预览在上下文刷新后不再阻塞回复

### 2. 更新激活和恢复更安全
- 验证后的激活在后续维护或账本错误时保持成功
- 中断的包更新安全恢复
- 激活后 Doctor 等待有界
- 过期收据不能否决有效修复
- Windows 深度或 8.3 状态路径不再中止 onboarding 或迁移

### 3. 数据库和工作连续性
- 维护拒绝保留 peer readers 和 borrowers
- 不兼容的保留 agent 数据库保持隔离
- 空转录删除跳过不必要的归档物化
- Bun admission deadlines 保持线程本地
- worker 关闭在 inventory 退休后完成

### 4. 备份和状态持久性
- 快照保留支持的旧版 exec-approval 策略
- 中断的 R2 验证和恢复安全恢复
- 配置观察在截断写入期间保留最后已知良好快照
- 失败的多文件补丁保留早期文件
- Memory Wiki 重新导入保留人工编写的笔记

### 5. 操作者控制连续性
- 原生计算机控制在会话过期后恢复
- 迟附加的 GitHub 操作者可以发布 PR
- 同步节点输出不重复为完成唤醒
- cron 公告保留 CLI 聊天
- 历史维护在有效载荷前读取身份

### 6. 提供商和插件连续性
- 模型刷新、配置账户准备、GPT-5.6 工具轮次
- OpenRouter onboarding
- 增量插件加载
- 更快的外部 TypeScript 插件启动
- 保留当前状态而不是拒绝有效设置或丢弃提供商

### 7. 托管集成可靠性
- 保存的 Linux Gateway 仪表板在重启时保留配对
- 慢速 macOS Talk 运行保留回复
- 应用升级汇聚官方插件
- Copilot 设置正确验证 SDK 支持的 agent
- Claude CLI 缓存前缀在子完成后保持稳定
- 密码提示不再阻止无头浏览器点击

### 8. 跨平台应用管理升级
- 原生状态修复、恢复快照、Gateway 运行时准入
- 升级后服务恢复在不丢失 agent 访问的情况下汇聚
- 支持 macOS 和 Windows

---

## 🆕 新功能

### Google 模型支持
- **新增 Gemini 4 Argon 支持** (PR #171852)

---

## 🐛 修复

1. **更新指导**: 避免在缺少包管理器时提供无关的数据库修复建议，成功更新后删除过时警告
2. **macOS onboarding**: 允许新配置文件启动 Gateway 并完成自动设置
3. **Gateway 日志**: 防止删除或过期的临时日志目录在日期翻转时将 Gateway 卡在满 CPU
4. **Control UI 队列状态**: 在队列命令消耗后清除 slash-steer 芯片

---

## 📊 统计

- **PR 总数**: 70 个唯一 PR (49 个在范围内 + 21 个保留的仅种子 PR)
- **主要贡献者**: RomneyDa, wangmiao0668000666, shanselman, dor-sr, brucemccurdy 等

---

## 🔗 相关链接

- 完整发布说明: https://github.com/openclaw/openclaw/releases
- 最新提交: [5c4a797](https://github.com/openclaw/openclaw/commit/5c4a797362e0d9c94ce82ed0b6be2c9827ad9c45)

---

*此文件由生态探索 cron 任务自动创建*
