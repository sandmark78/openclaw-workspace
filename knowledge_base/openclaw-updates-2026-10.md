# OpenClaw 更新记录 - 2026年10月

**发现时间**: 2026-10-11 20:00 UTC  
**来源**: GitHub Releases (https://github.com/openclaw/openclaw/releases)

---

## 🆕 最新版本

### 2026.10.5-beta.1 (最新)

**核心亮点**:

1. **更安全的更新机制**
   - 跨设备、文件系统、Windows 提权的更新完成
   - 中断激活的恢复
   - 陈旧租约或变更证据的恢复

2. **重启安全的对话** ⭐ 重要
   - 中断的 turns、worktree 准备中的首条消息、延迟任务在 Gateway 重启后恢复
   - 用户输入和已提交的会话数据在重启、并发写入、发布失败后存活

3. **更快更稳定的 Gateway** ⭐ 重要
   - 会话、转录、历史、元数据读取移至工作线程
   - SQLite 每 turn 工作量大幅减少
   - 启动维护在就绪后运行，繁忙 Gateway 保持响应

4. **可靠的 turns 和子 agent**
   - turns 从停滞流、重用工具调用 ID、过期 ChatGPT websocket 恢复
   - 不完整 turns 以可见通知结束
   - 子 agent 结果在跟进、重启、过期交付窗口后继续返回

5. **X (Twitter) 频道** 🆕
   - 通过新频道插件回答 X 提及
   - 支持流式传输
   - 访客模式用于仓库问题
   - 强制 API 成本限制

6. **语音通话增强**
   - 每次通话简报
   - 通话报告
   - 实时引导
   - 回调
   - 语音邮件检测

7. **更智能的模型选择器**
   - 选择器优先显示每个提供商的推荐模型
   - 新列出的 Claude、ChatGPT、Ollama 模型无需等待 OpenClaw 发布
   - 目录加载时保持响应

8. **ClawHub 集成到 Gateway** ⭐ 重要
   - 从 Gateway 浏览和搜索 ClawHub 插件和技能
   - 插件自动选择 OpenClaw 支持的最新官方版本

**其他改进**:
- 会话：允许定向发送到会话而不授予转录访问权限
- Worker 本地推理：添加原生 worker 推理运行时
- 公共线程：在常规链接打开公共线程
- 子 agent 进度：在工作行显示运行中的子 agent 数量
- 自动化修复：失败的自动化在警报前让所有者会话修复
- 频道进度：默认显示有用的 Telegram 和 Discord 进度
- 技能：学习技能专注于可重复程序而非事实或代码库知识
- 内存：解释为何跳过触发召回
- 模型和目录：v2 中发布每个提供商的推荐
- Anthropic：支持 Claude Haiku 5.5
- OpenAI：支持自定义实时语音端点
- Control UI 子 agent：显示聊天等待子 agent 的状态
- Control UI 自定义：主题自定义品牌、agent 头像、favicon 形状
- 终端：可配置终端字体，内置 Nerd Font 图标
- iOS：通过原生 Cloudflare Access 连接 Gateway
- Workboard：固定、取消固定、删除侧边栏的 boards
- GitHub：支持异步 PR 合并
- 大量性能优化（会话、数据库、维护等）

---

### 2026.10.1-beta.2 (热修复)

**修复重点**:
- 更新和 Doctor：恢复存档迁移和中断更新
- 回复和消息：在静默跟进后保留完成的答案
- 插件和云 worker：在结账更新期间保持插件技能可用
- Agent-to-agent 身份验证：拒绝未解析的 peer-token 引用
- 命令执行：拒绝包含 NUL 的命令参数
- 更新恢复：避免非 root 更新中的 launcher-ownership 失败
- Doctor 和迁移：从较早完成的迁移收据导入会话
- 托管服务：恢复 macOS 12 Monterey 上的停止、重启、更新命令
- Control UI：在任意容器 UID 下保持捆绑 UI 资产可读
- 频道交接：恢复路由聊天交接后的 Telegram 发送和内联按钮

---

## 📊 与我们相关的更新

### 对 Sandbot 的影响

1. **重启安全对话** - 我们的 cron 任务和心跳机制会受益
2. **Gateway 性能优化** - 我们的 1M 上下文使用会受益
3. **ClawHub 集成** - 我们已发布 3 个技能，可以直接从 Gateway 浏览
4. **X 频道** - 如果未来需要 Twitter 集成，可以直接使用官方插件

### 建议行动

- [ ] 考虑升级到 2026.10.5-beta.1（等待稳定版）
- [ ] 利用 ClawHub 集成推广我们的技能
- [ ] 研究 X 频道插件用于社区运营

---

*此文件已真实写入服务器*
*最后更新：2026-10-11 20:00 UTC*
