# OpenClaw 生态探索记录 — 2026-06-20

**检查时间**: 2026-06-20 20:00 UTC
**检查范围**: ClawHub、docs.openclaw.ai、GitHub Releases

---

## 🔴 有新发现！

### 1. GitHub Releases — 新版本 v2026.6.9-beta.1

**发布日期**: 2026-06-19 05:52 UTC（昨天，pre-release）

相比上次记录（2026.5.19-beta），相隔约 3 周的大版本更新。

#### 核心亮点

**① Telegram 交付大幅增强（🎯 与我们直接相关！）**
- 现在发送富 HTML，保留 rich markdown 和 sticker 路径
- 更忠实地渲染进度草稿和命令输出
- mentions 和 spooled handlers 保持在正确的投递路径上
- 涉及 PR: #93286, #93164, #93124, #93364, #93130, #93088, #93281

**② Agent 恢复更可靠**
- 重试、终端结果、compaction 后的 usage 保留
- 会话历史修复和 reply reconciliation
- 被中断或部分完成的轮次更可能到达可见的最终结果
- 涉及 PR: #92191, #93073, #93228, #93084, #93469, #93291, #90943

**③ Codex 集成增强**
- 自动插件审批、GPT-5.3 Spark OAuth 路由
- 远程节点 exec 作为动态工具
- 更可靠的 app-server teardown 和终端结果

**④ 独立官方 Provider 插件**
- 外部 provider 包成为一等 npm 发布
- 外部安装的 channel 插件在 Gateway 启动时自动发现
- StepFun 仅限 npm 安装（ClawHub 包名不可用）

**⑤ Web 和原生客户端增强**
- Control UI 新增 session workspace rail 和扩展健康状态
- iOS 新增 Watch controls
- Android 显示聊天上下文

**⑥ 搜索和技能改进**
- Codex Hosted Search 可用
- ClawHub 技能安装保留已验证的来源出处

#### 安全修复
- 调试/配置输出中脱敏 secret
- 阻止内部 HTTP 会话覆盖
- 审计开放 DM 工具暴露
- 保留插件写入权限检查

#### 存储修复
- 避免网络文件系统上 SQLite WAL 问题
- 清理 reindex artifacts
- 设置状态移出 workspace dot-directories
- default-agent auth profiles 导入 SQLite

### 2. ClawHub 平台（无重大变化）

- 域名：clawhub.com → clawhub.ai
- 热门技能：GitHub、VS Code、Notion、Slack、Gmail、Google Drive/Sheets/Calendar、Linear、Figma、Trello、WhatsApp 插件
- CLI 发布流程不变

### 3. docs.openclaw.ai（结构稳定）

- 标准文档首页，Node 24 推荐 / Node 22 LTS (22.19+) 兼容
- 支持的通道：Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等

---

## 📊 版本对比

| 项目 | 本次 (6/19) | 上次 (5/19) | 变化 |
|------|-------------|-------------|------|
| 最新 npm 版本 | **v2026.6.9-beta.1** | v2026.5.19 | ⬆️ 新版本 |
| ClawHub 结构 | 稳定 | 稳定 | 无变化 |
| Docs | 稳定 | 稳定 | 无变化 |

---

## 🎯 对我们最相关的变更

1. **Telegram 富交付增强** — 我们正使用 Telegram 通道，这意味着更好的消息格式、markdown 渲染和进度草稿显示
2. **Agent 恢复可靠性** — 减少中断/超时后丢失上下文的概率
3. **Provider 插件独立化** — 未来更新 provider 可能更灵活

---

*下次检查: 2026-06-21 20:00 UTC*
