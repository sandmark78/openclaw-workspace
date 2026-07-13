# OpenClaw 生态探索更新 - 2026-06-12

**探索时间**: 2026-06-12 20:00 UTC
**触发**: 定时生态探索 Cron

---

## 🚨 关键发现：版本落后

| 项目 | 值 |
|------|-----|
| **当前安装版本** | 2026.3.8 |
| **npm 最新版本** | 2026.6.6 |
| **落后跨度** | ~3 个月（2.8 个版本号） |
| **建议** | 升级到最新版本以获取安全修复和新功能 |

---

## 📦 ClawHub 变化

| 项目 | 旧状态 | 新状态 |
|------|--------|--------|
| **域名** | clawhub.com | → **clawhub.ai** |
| **技能总数** | - | 52,700+ |
| **用户数** | - | 180,000+ |
| **总下载** | - | 12,000,000+ |
| **平均评分** | - | 4.8/5 |
| **导航结构** | 简单 | Skills / Plugins / Audits / Publishers |

---

## 📝 Docs 新变化 (docs.openclaw.ai)

### 安装方式更新
- 新增一键安装脚本：`curl -fsSL https://openclaw.ai/install.sh | bash`
- Windows PowerShell 安装脚本：`iwr -useb https://openclaw.ai/install.ps1 | iex`

### 系统要求变化
- **Node.js**: Node 24 推荐（之前 Node 22）
- Node 22.19+ 仍支持

### 新特性（文档提及）
- **macOS 桌面 Hub 应用**（Native Windows/macOS app）
- **iOS & Android 节点**：Canvas、摄像头、语音工作流
- **自定义 Control UI 挂载**：支持自定义 dashboard 构建
- **环境变量系统**：OPENCLAW_HOME / OPENCLAW_STATE_DIR / OPENCLAW_CONFIG_PATH

---

## 🔒 GitHub 最新 Release 亮点 (2026-06-12 发布)

### 安全边界大幅收紧
- 转录、沙箱绑定、主机环境继承强化
- MCP stdio 安全增强
- Codex HTTP 访问控制
- 原生搜索策略
- 提升的发送者检查
- 已删除 Agent 的 ACP 绕过修复
- 回环工具安全
- Discord 审核和 Teams 群组动作
- exec 审批超时后失败关闭

### Telegram 投递改进
- 账号级别主题路由到正确的 Agent
- 流式文本在工具调用中存活
- /compact 在通用入口上工作
- 回调处理使用具体 API
- 草稿分块共享
- 持久调度去重移入 SDK
- 未授权 DM 文本不进缓存和提示上下文

### iMessage 恢复和投递
- 始终在线的入站重启
- 持久 echo 标记
- 块流式传输
- 空闲审批发现
- 加固的出站传输

### 浏览器和 MCP 连接
- 现有会话 CDP 支持
- 发现的 WebSocket 验证
- 默认 profile cdpUrl 处理
- 更安全的浏览器输出边界
- Streamable HTTP 回环传输
- 修正的 OAuth/SSE 授权处理

---

## 📊 生态统计

- ClawHub: 52.7k 工具 / 180k 用户 / 12M 下载 / 4.8 评分
- GitHub Repo: github.com/openclaw/openclaw (正确的仓库路径)
- ClawHub GitHub: github.com/openclaw/clawhub
