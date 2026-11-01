# OpenClaw 生态探索报告

**探索时间**: 2026-10-28 20:00 UTC  
**探索范围**: ClawHub, 官方文档, GitHub Releases

---

## 📊 当前版本状态

| 组件 | 当前版本 | 最新版本 | 状态 |
|------|----------|----------|------|
| 本地 OpenClaw | 2026.7.1 | 2026.10.8 (稳定) / 2026.10.10-beta.4 (预发布) | ⚠️ 落后 |

---

## 🆕 发现的更新

### 1. OpenClaw 2026.10.8 (扩展稳定版/LTS)

**发布时间**: 2026年10月  
**性质**: Gateway-only 扩展稳定版（相当于 LTS）

#### 重要修复（影响我们系统的）

**🔒 安全加固**
- exec allowlist 模式要求对 `test -v` 操作数扩展进行审批
- 通用 node invoke 拒绝浏览器代理命令
- 沙箱生成的子进程无法运行主机 CLI 后端
- 密钥出口代理拒绝不受信任的 eMudhra 链
- Fish Audio 和 Gradium 错误不再暴露 API 密钥

**⚙️ 稳定性改进**
- 长 HTML/JSX 答案、 Teams HTML、类似工具调用的回复不再卡住 Gateway
- 推理标签在流式传输前被隐藏
- 冷工具清单不再增长内存
- 插件服务计划在创建它们的作用域之外继续存在

**🔄 更新和恢复**
- 更新时 Doctor 失败会重启 Gateway 而不是停止
- 孤立的维护 worker 不再阻止 CLI 命令和 Gateway 启动
- Windows 托管更新不再在 TEMP 别名上锁定自己
- Doctor 在 SIGHUP 后恢复 Gateway

**🤖 Agent 和子 Agent 改进**
- Codex 原生子 Agent 完成后不再阻塞父 Agent
- 模型回退在本地运行时故障后停止
- 恢复的子 Agent 结果在会话重用后交付
- 批量工具调用在 sessions_yield 前稳定

**📱 通道修复**
- Slack: 隔离的 invalid_auth 在 socket-mode 通道禁用前重试
- Matrix: 普通消息不再被视为文本命令
- Discord: 实时语音咨询初始化运行时
- iMessage: Messages 桥接死亡后恢复

**🧠 内存和性能**
- worker 堆 caps 即使在 Gateway 服务传递 --max-old-space-size 时也适用
- 空闲 Codex app-server 客户端 30 秒后退休
- 归档 worker 在会话删除之间重用
- SQLite 3.54 数据安全：Doctor 修复 SQLite 分词器更改留下的陈旧全文索引

### 2. OpenClaw 2026.10.10-beta.4 (预发布)

**发布时间**: 2026年10月  
**性质**: Beta 预发布版  
**变更**: 60 个 PR

#### 关键修复

**🔐 Gateway 安全**
- 在启动和配置重载时，保持环境引用的 hooks.token 不在 agent host-exec 和 CLI 子环境中
- 同时保留显式的每命令覆盖

**🧠 Memory Wiki**
- 当 OKF 概念页面重新导入或从生产者包中删除时，保留人工编写的 Notes
- 包括更改的生产者内容和没有标记 Notes 槽的遗留页面

**🤖 Claude CLI**
- 在 Control UI 启动的会话中运行子 Agent 完成或通道轮次时，保持原生 Claude 会话及其上下文
- 而不是每次从保存的历史记录重新播种

**📋 模型目录**
- 在决定模型就绪状态时尊重配置的主账户 pin
- 原生 Claude CLI 模型在所选令牌配置文件就绪时不再显示为缺少身份验证

**⏰ 定时运行**
- 在回答前等待工具结果，所以 cron 运行摘要报告真实结果而不是过早的"无结果"回复

**🔧 CLI 配置写入**
- `openclaw config set`, `config unset`, `openclaw setup` 现在通过运行的 Gateway 发送变更
- 作为一个 config.patch 而不是拒绝
- 与离线写入相同的结果，重载关闭时不重启

---

## 🌐 ClawHub 状态

**网址**: https://clawhub.ai/ (从 clawhub.com 重定向)  
**状态**: ✅ 正常运行

### 展示的技能类别
- GitHub: PR 审查、问题管理、仓库工作流自动化
- VS Code: 从编辑器编辑仓库、运行任务、发布代码
- Notion: 读取页面、更新数据库、起草文档
- Slack: 发送消息、搜索对话、管理通道
- Gmail: 读取、发送、搜索、组织邮件
- Google Drive: 查找、创建、管理文件和文件夹
- Google Sheets: 读取、写入、自动化电子表格数据
- Google Calendar: 创建事件、检查可用性、管理日历
- Linear: 创建问题、同步周期、保持产品工作移动
- Figma: 导出资产、评论文件、同步设计上下文
- Trello: 管理看板、列表、卡片和项目工作流
- WhatsApp: WhatsApp Web 通道插件用于 Agent 聊天

### ClawHub CLI
```bash
$ npm i -g clawhub
$ clawhub login
$ clawhub skill publish ./my-skill --slug my-skill --version 1.0.0
$ clawhub package publish your-org/your-plugin
```

---

## 📚 官方文档状态

**网址**: https://docs.openclaw.ai  
**状态**: ✅ 正常运行

### 文档结构
- Get started: 概述、第一步、设置指南
- Install: 安装路径、更新、容器、托管、高级设置
- Channels: 消息通道、配对、路由、访问组、通道 QA
- Agents: 架构、会话、上下文、记忆、多 Agent 路由
- Capabilities: 工具、技能、cron、webhooks、自动化能力
- ClawHub: 插件市场、发布、策划、信任指导
- Models: 提供商、模型配置、故障转移、本地模型服务
- Platforms: macOS、Windows、iOS、Android、节点、Web 表面
- Gateway & Ops: Gateway 配置、安全、诊断、运维
- Reference: CLI 参考、模式、RPC、模板
- Releases: 每个版本的发布说明
- Help: 故障排除、FAQ、测试、诊断、环境检查

---

## 🎯 建议行动

### P0 - 立即行动
1. **考虑升级到 2026.10.8 (LTS)**
   - 我们当前版本 2026.7.1 已经落后 3 个月
   - 包含大量安全修复和稳定性改进
   - 特别是 exec 安全加固、内存管理、子 Agent 改进

### P1 - 短期行动
1. **测试 2026.10.8 的兼容性**
   - 在测试环境验证升级
   - 检查现有技能和配置兼容性
   - 确认 Telegram 通道正常工作

2. **利用 ClawHub CLI**
   - 发布我们的自研技能（agent-optimizer, input-validator, github-ops）
   - 探索社区技能

### P2 - 长期行动
1. **关注 2026.10.10-beta.4 的进展**
   - Memory Wiki 改进可能对我们的知识管理有用
   - Claude CLI 改进可能影响我们的子 Agent 架构

---

## 📝 版本对比摘要

| 特性 | 2026.7.1 (当前) | 2026.10.8 (LTS) | 2026.10.10-beta.4 |
|------|-----------------|-----------------|-------------------|
| 安全加固 | ❌ 缺少 | ✅ 完整 | ✅ 完整 + 额外 |
| 内存优化 | ❌ 缺少 | ✅ 完整 | ✅ 完整 |
| 子 Agent 稳定性 | ⚠️ 基础 | ✅ 改进 | ✅ 进一步改进 |
| Memory Wiki | ⚠️ 基础 | ✅ 改进 | ✅ Notes 保留 |
| CLI 配置写入 | ⚠️ 离线 | ✅ 在线 | ✅ 在线 |
| 定时运行结果 | ⚠️ 可能不准确 | ✅ 等待工具结果 | ✅ 等待工具结果 |

---

**报告生成时间**: 2026-10-28 20:00 UTC  
**下次探索建议**: 2026-11-04 (一周后)
