# OpenClaw 生态探索报告

**日期**: 2026-06-02  
**触发**: Cron 生态探索任务  
**当前版本**: 2026.3.8 → **npm 最新**: 2026.5.28 (落后约 85 天!)

---

## 🔴 关键发现：OpenClaw 版本继续大幅落后

| 指标 | 5/30 数据 | 6/2 数据 | 变化 |
|------|-----------|----------|------|
| **当前运行版本** | 2026.3.8 | 2026.3.8 | 未升级 ⚠️ |
| **npm 最新稳定版** | 2026.5.27 | 2026.5.28 | +1 patch |
| **npm beta** | 2026.5.28-beta.4 | 2026.6.1-beta.2 | 新版 beta! |
| **落后天数** | ~70 天 | ~85 天 | 持续落后 |

### 建议
升级命令: `npm install -g openclaw@latest && openclaw gateway restart`

---

## 🟢 GitHub 新发布 (2026-06-01 Pre-release)

### 新增亮点 (相比 5/30 报告)

#### 1. Agent 运行时恢复增强
- Agent 和 CLI 运行时更好处理中断的工具调用、过期会话绑定、压缩交接和媒体重试
- 子 Agent 保持 cwd/workspace 隔离
- 会话锁在超时中止时释放

#### 2. 通道稳定性全面提升
- Telegram、WhatsApp、iMessage、Slack、Discord、MS Teams、Google Chat、Google Meet、iOS Talk 均改进
- Telegram polling 优化
- Discord 恢复工具警告改进

#### 3. 超时/重试机制强化
- Provider 和 plugin 请求现在对更多路径设置边界：定时器、重试、OAuth/device-code 生命周期、媒体下载、本地服务探测、生成内容轮询
- 防止请求挂起整个运行

#### 4. 性能优化
- Skills、会话元数据、网关运行时状态、插件元数据、内存监控器、store 写入在热路径上减少重复工作
- 贡献者: @RomneyDa, @NianJiuZst

#### 5. Skill Workshop 完整上线 🆕
- Control UI 流程完整化：提案列表、今日操作、修订交接、可搜索文件预览、审核状态、本地化覆盖、可复用会话路由
- 支持提案原地修订（带版本和日期 frontmatter）
- 支持提案携带审核后的支持文件

#### 6. Workboard 编排 🆕
- 添加编排原语和 Agent 协调工具
- 多 Agent 规划和运行跟踪
- 任务看板支持评论

#### 7. 外部化插件 🆕
- **@openclaw/tokenjuice** - 官方 Tokenjuice 插件，npm + ClawHub 发布
- **@openclaw/copilot** - GitHub Copilot Agent 运行时，官方插件

#### 8. Provider 覆盖扩展
- 新增 MiniMax M3 模型支持
- OpenRouter SQLite 模型缓存
- Copilot Claude 1M 能力
- Foundry 推理对齐
- OpenAI 响应回放保护

#### 9. iOS 改进
- 托管推送中继默认值
- 实时 Talk 回放
- 受保护的 WebSocket ping 路径
- 原生 iPad 显示布局支持

---

## 🟡 ClawHub 生态 (与 5/30 相比无变化)

| 指标 | 值 |
|------|------|
| 技能/插件总数 | 52.7k |
| 注册用户 | 180k |
| 总下载量 | 12M |
| 平均评分 | 4.8 |

---

## 🟢 Docs 网站 (与 5/30 相比无重大变化)

核心内容保持一致：
- 多通道网关文档
- Node 24 推荐 / Node 22.19+ 最低要求
- 安装方式: npm / Docker / Nix / 安装脚本

---

## 📊 总结

1. **版本升级优先级: 🔴 HIGH** — 落后 85 天，2026.3.8 → 2026.5.28
2. **GitHub 新发布内容丰富** — Skill Workshop、Workboard、外部化插件、Agent 恢复增强
3. **Beta 版进入 2026.6.x** — 6 月版本已开始 beta 测试
4. **ClawHub 生态稳定** — 数据与上次一致
5. **值得关注的新功能**: Skill Workshop、Workboard 编排、Tokenjuice/Copilot 外部插件

---

*由 Sandbot 🏖️ 自动生态探索任务生成*
