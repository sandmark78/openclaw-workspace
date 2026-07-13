# OpenClaw 生态探索扫描 (2026-05-12 20:00 UTC)

**扫描时间**: 2026-05-12 20:00 UTC
**当前运行版本**: 2026.3.8 (推测)
**最新版本**: 2026.5.12 pre-release (2026-05-12 发布)
**状态**: ⚠️ 有可用更新 (落后约 1.5 个月)

---

## 与上次扫描 (2026-04-30) 对比

| 项目 | 上次 | 本次 | 变化 |
|------|------|------|------|
| 最新版本 | 2026.4.29-beta.3 | **2026.5.12 pre-release** | 🆕 新版本 |
| ClawHub 工具数 | 52,700 | 52,700 | - |
| 用户数 | 180,000 | 180,000 | - |
| 下载量 | 12,000,000 | 12,000,000 | - |
| 平均评分 | 4.8 | 4.8 | - |

---

## 🆕 v2026.5.12 pre-release 新增亮点

### 1. 🔐 安全与权限
- **Per-sender tool policies** (#66933): 新增基于发送者身份的工具权限控制，可在 global/agent/group/core/bundled/plugin 级别限制危险工具
- **Per-agent crossContext 消息覆盖**: 沙箱/公开 agent 可限制消息发送到当前对话
- **Memory wiki admin scope**: 需要 admin scope 才能进行 ingest 操作
- **Obsidian search write scope**: 需要 write scope 才能搜索

### 2. 🤖 Agent 增强
- **子 Agent 会话层级显示** (#78623): Control UI 会话选择器中用 └─ 前缀展示父子关系，解决 #77628
- **A2A maxPingPongTurns 提升至 20** (#52400): 默认保持 5，支持更长的 agent 间对话
- **Per-agent tools.message.actions.allow**: 沙箱 agent 可暴露 send-only 消息工具

### 3. 🛠️ 构建系统升级
- **pnpm 11 全面升级** (#79414): Docker/install/update/release 全部切换到 pnpm 11
- **Telegram QA workflow 对齐 pnpm 11** (#80588)
- **oxlint 更严格规则**: Promise/TypeScript/runtime 脚枪检查
- **Vitest 更严格 lint**: focused/disabled/conditional/hook/matcher/expectation 安全
- **TypeScript 更严格编译器**: 隐式返回、副作用导入、覆盖、未使用代码

### 4. 📅 Cron 增强
- **直接 cron get 命令** (#75117): 支持 `openclaw cron get <id>` 按 ID 检查单个 cron 任务

### 5. 🖼️ 图片生成
- **Fal provider GPT Image 2 & Nano Banana 2**: 支持参考图编辑 (/edit)，提升输入图上限 (GPT Image 2: 10 张，NB2: 14 张) (#77295)

### 6. 📡 通道
- **iMessage 状态过滤** (#80706): 新增 `openclaw channels status --channel` 过滤
- **BlueBubbles→imsg 切换路径**: 文档化从 BlueBubbles 到原生 iMessage 的迁移
- **QQ Bot 构建修复** (#80925): 排除 QQ Bot 运行时文件导致的状态重建问题

### 7. 🧪 ACP
- **Gateway 会话谱系元数据** (#73458): ACP 会话列表和快照暴露子 agent 图谱，客户端可直接渲染

### 8. 🌐 Web/运行时
- **HTML 恢复面板** (#44107): 空白 dashboard 页面显示纯 HTML 恢复面板 + 浏览器扩展排障链接
- **Fly Machines 容器检测**: 从运行时环境变量自动识别 Fly 容器环境
- **模型本地服务启动**: 新增 provider-level localService 启动支持

### 9. 📖 文档
- 工具导航重命名为「Capabilities」
- agents.defaults.subagents.announceTimeoutMs 文档化 (#75509)

### 10. 💬 Codex
- **超时客户端退役**: 超时后不再复用 CPU 旋转的 Codex 进程
- **native plugin destructive-action policy 默认启用**

---

## ClawHub 平台数据

- 域名: clawhub.com → clawhub.ai (重定向)
- 工具总数: **52,700**
- 用户总数: **180,000**
- 下载总量: **12,000,000**
- 平均评分: **4.8**

---

## 建议

1. **版本升级**: 当前 2026.3.8 → 最新 2026.5.12 pre-release，Beta 版建议评估后再升级
2. **重点关注**:
   - Per-sender tool policies 可用于加强安全性
   - 子 Agent 会话层级显示改善调试体验
   - Cron get 命令方便任务排查
   - pnpm 11 升级是重大构建变更
3. **安全修复**: 工具权限收紧需注意当前配置是否受影响
4. **图片生成**: Fal provider 支持更多参考图和编辑功能，值得关注
