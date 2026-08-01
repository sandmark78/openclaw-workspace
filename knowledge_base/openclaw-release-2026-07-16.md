# OpenClaw 版本更新 - 2026-07-16 探索

**探索时间**: 2026-07-16 20:00 UTC  
**数据来源**: GitHub Releases, ClawHub, Docs

---

## 🆕 最新版本信息

### Beta 版本: 2026.7.2-beta.1
- **发布日期**: 2026-07-15 18:48 (昨天)
- **发布者和**: steipete (Peter Steinberger)
- **标签**: v2026.7.2-beta.1
- **状态**: Pre-release

### 稳定版本: 2026.7.1
- **状态**: 最新稳定版
- **前序版本**: 2026.6.11, 2026.6.10

---

## 🌟 2026.7.2 主要更新亮点

### 1. 远程编码会话 (Remote Coding Sessions)
- 在云工作者上运行 Control UI 会话
- 在终端中打开 Codex 和 Claude catalog 会话
- 直接在终端恢复 OpenCode 和 Pi 会话
- **相关 PR**: #107670, #107086, #107200

### 2. 原生自动化和节点 (Native Automation and Nodes)
- 移动端自动化功能对等支持
- Android 前台语音唤醒 (Voice Wake)
- 无头 Linux 节点暴露摄像头、位置、通知功能
- **相关 PR**: #106355, #107081, #107193

### 3. 更安全的通道操作 (Safer Channel Operation)
- 防止 Telegram 重启后持久性入口损失
- Signal 停止和审批控制在活跃回合期间保持响应
- 通道允许列表不再授予所有者访问权限
- **贡献者**: @obviyus, @arduano, @yetval
- **相关 PR**: #107288, #107422, #107403

### 4. 引导式 Control UI 设置 (Guided Control UI Setup)
- 从设置页面配置模型提供商
- 通过引导式设置页面接入通道
- 创建会话时选择图像和模型
- **贡献者**: @alexandre-leng, @fuller-stack-dev
- **相关 PR**: #106490, #106469, #107358

### 5. Gateway 和会话恢复 (Gateway and Session Recovery)
- 防止重启准入卡住 Gateway
- 在最终确定停滞之后恢复回复会话
- 保持一次性 cron 任务在生命周期声明竞争中启用
- **贡献者**: @obviyus, @joshavant, @charliemeyer2000, @SL4N
- **相关 PR**: #107339, #106792, #107236

---

## 📊 ClawHub 状态

- **网站**: clawhub.ai (从 clawhub.com 重定向)
- **技能市场**: 正常运营
- **官方创作者**: 有专门的官方创作者区域
- **支持的应用**: GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello, WhatsApp

### 已发布的技能类别
- 开发工具: GitHub, VS Code
- 办公套件: Notion, Google Workspace, Linear, Trello
- 通讯工具: Slack, Gmail, WhatsApp
- 设计工具: Figma

---

## 📚 文档站状态

- **地址**: docs.openclaw.ai
- **状态**: 正常访问
- **主要板块**:
  - Get started (入门)
  - Install (安装)
  - Channels (通道)
  - Agents (Agent 架构)
  - Capabilities (能力)

---

## 💡 对 Sandbot 的启示

### 可关注的功能
1. **远程编码会话** - 可能用于未来的分布式子 Agent 架构
2. **无头 Linux 节点** - 与 Lobster Orchestrator 的多实例管理相关
3. **Gateway 恢复改进** - 提升系统稳定性

### 升级考虑
- 当前版本: 需要检查 (`openclaw --version`)
- 建议: 等待 2026.7.2 稳定版发布后再升级
- Beta 版本风险: 可能存在未修复的 bug

---

## 🔗 相关链接

- GitHub Releases: https://github.com/openclaw/openclaw/releases
- ClawHub: https://clawhub.ai
- 文档站: https://docs.openclaw.ai
- 最新 Beta: https://github.com/openclaw/openclaw/releases/tag/v2026.7.2-beta.1

---

*探索完成于 2026-07-16 20:01 UTC*
*下次探索建议: 2026-07-23 (一周后)*
