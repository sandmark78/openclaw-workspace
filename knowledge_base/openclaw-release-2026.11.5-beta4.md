# OpenClaw 2026.11.5-beta.4 更新日志

**记录时间**: 2026-11-16 20:00 UTC
**本地版本参考**: 2026.7.1
**最新 Beta**: 2026.11.5-beta.4（Pre-release）

## 主要更新（Highlights）

### 1. Telegram Widgets
- Render interactive widgets as Telegram messages（把交互式 widget 渲染为 Telegram 消息）

### 2. 重要修复
- **Transcripts 与附件**: 并发数据库准备期间保持 transcript 可读，释放 SQLite reader 无需重启游标，避免把二进制附件插入模型提示
- **自动化连续性**: 父轮次结束后正常投递失败的子任务结果、正确运行延迟的定时任务、配置变更时保留进行中的任务、修复轮次可检查自己的 job
- **自动化隐私**: 队列自动化启动时重新检查 owner 私有 memory 访问权限
- **Claude 与审批**: CLI 清理失败后恢复、保留配对节点 Gateway 上下文、跨不同 tool-call ID 转发审批、允许配置主 fallback
- **Provider 恢复**: 修复 OpenAI 会话 compaction 冲突恢复、兼容新版 Claude OAuth 客户端、保持 OpenRouter 请求在自身 endpoint
- **更新安全**: 重试安装发现、ledger 失败时保留运行监听、finalization 期间保持插件 lifecycle lease、Doctor/启动失败时回滚 release、处理移动的 cron partition
- **大会话内存**: 分页导出 memory、更新后完成大索引重建、避免 native context seed 的不必要 transcript 分配
- **Telegram**: 投递内联按钮点击、保持禁用按钮不激活、保留审批与 widget 的 topic、message hooks 包含运行时 session key
- **移动端与语音**: block streaming 关闭时投递带字幕的 Feishu 媒体、修复 iOS 语音权限崩溃、为 Talk 请求启动 backing agents
- **Control UI**: 修复重复切换 session 时保留加载动画卡顿、避免 WebKit picker/menu 冻结、修复 chat Details 更新无监听错误
- **Gateway 韧性**: 限制 Matrix 格式化消息 mention 解析、关闭时取消 MCP listener、恢复 npm 安装的 Bonjour 发现
- **数据库恢复与备份**: staging 内压缩备份、检查引擎而不复制实时数据库、保留损坏诊断
- **模型选择**: 修复配置大量模型时模型读取过慢

## 相关 PR 示例
#196991 (Telegram widgets), #188055, #190242, #198309, #198289 (transcripts/attachments),
#197658, #197484, #197606, #197591, #188105 (automation continuity),
#198697, #198695 (automation privacy), #198224, #195431, #197853 (Claude & approvals)

## ClawHub 生态（clawhub.com → clawhub.ai）
- 域名已从 clawhub.com 跳转到 clawhub.ai
- 官方集成：GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello, WhatsApp Web
- CLI 发布流程：`npm i -g clawhub` → `clawhub login` → `clawhub skill publish` / `clawhub package publish`

## 行动建议
- 当前为 Pre-release（beta.4），升级需先评估稳定性
- Telegram widget 渲染是本次亮点，适合交互式通知场景
- Doctor 命令建议定期运行以排查系统健康
- 关注 ClawHub 新技能集成（尤其 WhatsApp / Slack / Gmail 等常用工具）