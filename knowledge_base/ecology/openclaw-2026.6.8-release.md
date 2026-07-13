# OpenClaw v2026.6.8 Release Notes

**来源**: https://github.com/openclaw/openclaw/releases/tag/v2026.6.8
**发布日期**: 2026-06-16
**抓取时间**: 2026-06-16 20:02 UTC
**当前安装版本**: 2026.3.8 (落后 3 个月!)

---

## 核心亮点

### 1. Telegram & WhatsApp 富文本增强
- Telegram 支持结构化富文本：表格、列表、可扩展引用块、保留换行
- CLI 后端交付支持 prompt 保留
- 原生草稿迁移已退役
- 富媒体边界更安全
- WhatsApp 现在支持配置的 ACP 绑定
- 相关 PR: #92679, #93164, #84082, #89421, #92513

### 2. Agent & Gateway 恢复能力大幅增强
- 账户范围 DM 发送改进
- 生成媒体完成处理
- 自动回复消息工具最终回复
- 重置归档回退读取
- 重启关闭中止
- 子 Agent 暂停/恢复优化
- 心跳去重 (heartbeat dedupe)
- 会话身份提示
- 未知 OpenAI agent selector 拒绝
- 相关 PR: #92788, #91246, #92879, #91357, #92631, #92412, #92146, #91287, #92468, #92510

### 3. Provider/Model 处理扩展
- **新增 GLM-5.2 支持**
- **新增 Claude Haiku 4.5 目录条目**
- OpenRouter 和 Google Vertex provider 前缀规范化
- 托管 SecretRef 认证
- OAuth 图片默认路由通过 Codex
- 有界模型浏览发现
- LM Studio 二进制 thinking-off 交付
- OpenAI Responses 无存储重放门控
- Claude 4.5 Copilot 工具流安全
- OpenAI/Anthropic-family payload 隔离
- 相关 PR: #92796, #90116, #92627, #91218, #90686, #92824, #92247, #92002, #90706, #92941, #92916, #92908, #92921, #92928

### 4. /usage 和回复 payload hooks 改进
- 原生完整 footer 渲染器
- 默认模板
- 固定小数格式化
- 凭证感知限制
- 更好的部分计数处理
- 损坏模板警告替代静默坏输出
- 相关 PR: #92657, #89835, #89629

### 5. UI & 移动端流程
- 工作区文件可折叠和默认折叠
- WebChat 回溯支持流式
- 侧边栏会话选择器桌面工作区上方交互
- 重置软参数存活 UI 分发
- 过时仪表板会话父系谱保留
- **iOS 重新连接过时前台 Gateway**
- 相关 PR: #92779, #92622, #92705, #91353, #90658, #92552

### 6. 内存、状态和诊断
- 超大 OpenAI embedding 批次在 431s 前拆分
- QMD 内存搜索在瞬态模式下可用
- **SQLite 避免 NFS 状态卷上的 WAL**
- 卡顿会话恢复调度不再重置警告回退
- 完整内存重建索引保留回滚/缓存恢复
- 原始 Memory Wiki 源页面停止畸形
- Infinity chunk 限制真正无界
- 相关 PR: #92650, #92618, #92639, #91247, #92752, #92881, #59137, #92876, #69700, #92735

---

## 对 Sandbot 的影响评估

| 改进 | 影响 | 优先级 |
|------|------|--------|
| Telegram 富文本 | 我们的消息展示会更丰富 | 中 |
| Agent 恢复增强 | 子 Agent 更稳定 | 高 |
| GLM-5.2 / Claude Haiku 4.5 | 更多模型选择 | 低 |
| 心跳去重 | 减少重复心跳 | 低 |
| SQLite NFS 修复 | 状态文件更可靠 | 中 |
| iOS 重连 | 移动端节点更稳定 | 低 |

---

## 升级建议

⚠️ 当前版本 2026.3.8 落后最新版本 2026.6.8 共 3 个月版本。
建议升级以获得：
1. Telegram 富文本（我们的主要通道）
2. Agent 恢复能力（子 Agent 稳定性）
3. SQLite NFS 修复（状态可靠性）

升级命令: `openclaw update` 或 `npm install -g openclaw@latest`
