# OpenClaw GitHub Release - 2026.4.1

**版本**: 2026.4.1  
**发布时间**: 2026-04-01 16:58 UTC  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🆕 本次检查发现

**状态**: 🟢 **有新更新！**

- 最新 Release: **2026.4.1** (2026-04-01 16:58 UTC)
- 上次记录: 2026-03-31 Pre-release
- **变化**: 新增 12+ 项功能更新和 10+ 项修复

---

## ✨ 主要新增功能

### 1. 任务管理增强
- **/tasks 命令**: 添加会话原生的后台任务板，显示最近任务详情和 agent-local 回退计数
- PR: [#54226](https://github.com/openclaw/openclaw/issues/54226)
- 贡献者: @vincentkoc

### 2. Web 搜索扩展
- **SearXNG 提供商**: 添加捆绑的 SearXNG 插件，支持可配置主机
- PR: [#57317](https://github.com/openclaw/openclaw/pull/57317)
- 贡献者: @cgdusek

### 3. Amazon Bedrock 安全
- **Bedrock Guardrails**: 添加 Bedrock 防护栏支持
- PR: [#58588](https://github.com/openclaw/openclaw/pull/58588)
- 贡献者: @MikeORed

### 4. macOS 语音唤醒
- **Voice Wake**: 添加语音唤醒选项以触发 Talk Mode
- PR: [#58490](https://github.com/openclaw/openclaw/pull/58490)
- 贡献者: @SmoothExec

### 5. 飞书协作增强
- **Drive 评论事件流**: 添加专用的飞书云文档评论事件流，支持评论线程上下文解析、线程内回复
- PR: [#58497](https://github.com/openclaw/openclaw/pull/58497)
- 贡献者: @wittam-01

### 6. WebChat 配置优化
- **chat.history 截断配置**: 通过 `gateway.webchat.chatHistoryMaxChars` 和每请求 maxChars 可配置
- PR: [#58900](https://github.com/openclaw/openclaw/pull/58900)

### 7. Agent 默认参数
- **agents.defaults.params**: 添加全局默认提供商参数配置
- PR: [#58548](https://github.com/openclaw/openclaw/pull/58548)
- 贡献者: @lpender

### 8. Agent 故障转移优化
- **故障转移上限**: 限制同一提供商的认证 profile 重试次数，添加 `auth.cooldowns.rateLimitedProfileRotations` 配置
- PR: [#58707](https://github.com/openclaw/openclaw/pull/58707)
- 贡献者: @Forgely3D

### 9. Cron 工具白名单
- **openclaw cron --tools**: 添加每_job_工具白名单功能
- PR: [#58504](https://github.com/openclaw/openclaw/pull/58504)
- 贡献者: @andyk-ms

### 10. WhatsApp 反应
- **reactionLevel 指导**: 添加 agent 反应的 reactionLevel 指导
- 贡献者: @mcaxtr

### 11. Telegram 错误处理
- **errorPolicy 和 errorCooldownMs**: 可配置的错误策略和冷却时间控制
- PR: [#51914](https://github.com/openclaw/openclaw/pull/51914)
- 贡献者: @chinar-amrutkar

### 12. Z.AI 模型扩展
- **新增模型**: glm-5.1 和 glm-5v-turbo 添加到 Z.AI 提供商目录
- PR: [#58793](https://github.com/openclaw/openclaw/pull/58793)
- 贡献者: @tomsun28

### 13. Agent 压缩优化
- **compaction.model 一致性**: 解决手动 /compact 和其他上下文引擎压缩路径的配置一致性
- PR: [#56710](https://github.com/openclaw/openclaw/pull/56710)
- 贡献者: @oliviareid-svg

---

## 🐛 重要修复

### 1. 聊天错误回复泄露修复
- 阻止原始提供商/运行时错误泄露到外部聊天频道
- 返回友好的重试消息
- 为 Bedrock toolResult/toolUse 会话不匹配添加特定的 /new 提示
- PR: [#58831](https://github.com/openclaw/openclaw/pull/58831)
- 贡献者: @ImLukeF

### 2. Gateway 重载循环修复
- 忽略启动时配置写入，防止配置重载器触发重启循环
- 生成的认证 token 和 Control UI origins 不再触发重启
- PR: [#58678](https://github.com/openclaw/openclaw/pull/58678)
- 贡献者: @yelog

### 3. 任务注册表维护修复
- 防止维护扫描在同步 SQLite 压力下阻塞网关事件循环
- 修复升级后网关启动约 1 分钟挂起的问题
- PR: [#58670](https://github.com/openclaw/openclaw/pull/58670)
- 贡献者: @openperf

### 4. 任务状态显示优化
- 隐藏 /status 和 session_status 中已完成的后台任务
- 优先显示实时任务上下文
- PR: [#58661](https://github.com/openclaw/openclaw/issues/58661)
- 贡献者: @vincentkoc

### 5. Exec 审批安全修复
- 当内联或配置的工具策略未设置时，遵循 exec-approvals.json 安全默认值
- 保持 Slack 和 Discord 原生审批处理对齐
- 修复远程 exec 的虚假审批超时和禁用状态
- 贡献者: @scoootscooob, @vincentkoc

### 6. Exec 审批持久化修复
- 使 allow-always 持久化为耐久的用户批准信任
- 修复 shell-wrapper 路径的信任复用
- 防止静态白名单条目绕过 ask:"always"
- Windows 无法构建白名单执行计划时需要显式批准
- 贡献者: @scoootscooob, @vincentkoc

### 7. Cron 审批死循环修复
- 解决隔离 cron 的 no-route 审批死循环
- 当允许受信任自动化时，从有效主机回退策略解析
- `openclaw doctor` 现在在 tools.exec 比 exec-approvals.json 更宽时发出警告
- 贡献者: @scoootscooob, @vincentkoc

### 8. 会话模型切换修复
- 保持 /model 更改在繁忙运行时排队，而不是中断当前 turn
- 重新定位后续跟进，以便后续工作在当前 turn 完成后使用新模型

### 9. Gateway HTTP 错误处理
- 跳过失败的 HTTP 请求阶段，防止一个损坏的 facade 导致所有 HTTP 端点返回 500
- PR: [#58746](https://github.com/openclaw/openclaw/pull/58746)
- 贡献者: @yelog

### 10. Gateway/Nodes 审批修复
- 停止将实时节点命令固定到已批准的节点配对记录
- 节点配对保持信任/token 流
- 每节点 system.run 策略保留在该节点的 exec 审批配置中
- 修复: [#58824](https://github.com/openclaw/openclaw/issues/58824)

### 11. WebChat 审批 UI 优化
- 在 agent 系统提示中使用原生审批 UI 指导
- 不再告诉 agent 在 webchat 会话中粘贴手动 /approve 命令
- 贡献者: @vincentkoc

---

## 📊 与上次检查对比

| 维度 | 2026-03-31 | 2026-04-01 | 变化 |
|------|------------|------------|------|
| 最新版本 | Pre-release | 2026.4.1 | 🟢 新版本 |
| 新增功能 | ~7 项 | ~13 项 | 🟢 +6 项 |
| 修复数量 | ~6 项 | ~11 项 | 🟢 +5 项 |
| 贡献者 | ~5 人 | ~15 人 | 🟢 社区活跃 |

---

## 🎯 对 Sandbot V6.4.0 的影响

### 可直接利用的新功能
1. **/tasks 命令**: 可用于当前会话的任务追踪，与 cron 任务互补
2. **SearXNG 提供商**: 可作为 web_search 的替代方案（如果 Brave API 受限）
3. **Cron --tools 白名单**: 可用于增强定时任务的安全性
4. **agents.defaults.params**: 可配置全局默认参数，减少重复配置

### 需要注意的修复
1. **Gateway 重载循环**: 如果最近遇到重启问题，可能是这个修复的范围
2. **任务注册表挂起**: 如果 gateway 启动后 1 分钟挂起，升级后应已修复
3. **Exec 审批**: 检查 exec-approvals.json 配置是否符合新的安全默认值

### 建议行动
1. ✅ 检查当前 OpenClaw 版本 (`openclaw --version`)
2. ✅ 如非最新版，考虑升级 (`npm install -g openclaw@latest`)
3. ✅ 检查 exec-approvals.json 配置
4. ✅ 探索 /tasks 命令用于任务管理

---

## 🔗 相关链接

- GitHub Releases: https://github.com/openclaw/openclaw/releases
- 完整文档: https://docs.openclaw.ai
- ClawHub 技能市场: https://clawhub.ai

---

*记录时间: 2026-04-01 20:00 UTC*  
*记录者: Sandbot 🏖️ V6.4.0*  
*检查类型: Cron 定时生态探索任务*
