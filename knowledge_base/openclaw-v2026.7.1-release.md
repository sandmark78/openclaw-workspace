# OpenClaw v2026.7.1 发布记录

**发现时间**: 2026-07-26 20:00 UTC  
**当前版本**: v2026.3.8  
**最新版本**: v2026.7.1  
**发布日期**: 2026-07-13  
**贡献**: 3,063 次提交，532 位贡献者  
**Release URL**: https://github.com/openclaw/openclaw/releases/tag/v2026.7.1  
**完整说明**: https://docs.openclaw.ai/releases/2026.7.1

---

## 主要更新

### 🎨 Control UI 大改版
- 对话管理更便捷，支持并排工作
- 实时 Tasks、更清晰的聊天控制
- 更好的用量和成本视图
- 文件、下载、配对、审批、Gateway 健康状态整合

### 🚀 安装引导优化
- 引导式设置，从安装到首次聊天更流畅
- 保存前检查连接
- 中断后保留之前的选择

### 📱 官方 App 更新
- iOS/iPadOS、Android、macOS 全面升级
- 设置、导航、聊天、语音、权限、本地化
- 文件、定时任务、离线阅读、排队发送
- 连接恢复、原生会话控制

### 🤖 模型和提供商扩展
- **GPT-5.6** 兼容性改进（OpenAI + Codex 路由）
- **腾讯混元 Hy3** 完整设置路径
- **Meta Muse Spark 1.1** 支持
- Claude、Ollama、ClawRouter、LongCat 等扩展

### 💻 Codex 和编程 Agent
- `openclaw attach` 给 Claude Code 临时会话访问
- Codex 委派和原生子 Agent 更可靠
- Copilot 更多提供商选择
- 长时间运行的会话和目标更易恢复

### 💬 渠道更新
- **Telegram**: 实时进度、照片文档、话题、命令、重试、账户路由
- **Slack**: 线程、卡片、进度、身份、反应、去重
- **Discord**: 回复、附件、语音会话、进度、重连、多账户
- **Apple Messages**: 回复、输入、媒体、路由、设置引导

### ⚙️ Gateway 改进
- **崩溃循环修复**: 反复失败的 Gateway 不再无限重启，提供稳定修复路径
- 定时任务：仅在变化时唤醒
- 远程浏览器控制：已登录标签页可远程配对
- 工作区终端：Web/iOS/Android 可用

### 🔒 安全增强
- 密码和 token 不再出现在更多日志中
- 设备配对更清晰
- 不安全的下载/文件/网络请求更早被阻止

---

## ⚠️ 升级建议

当前 v2026.3.8 → v2026.7.1 跨度较大，建议：
1. 先在测试环境验证
2. 备份 openclaw.json 配置
3. 关注 Telegram 渠道兼容性
4. 检查现有技能是否兼容
