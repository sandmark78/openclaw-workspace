# OpenClaw 生态探索报告 - 2026-05-25

**探索时间**: 2026-05-25 20:00 UTC
**来源**: clawhub.ai, docs.openclaw.ai, npm, GitHub Releases

---

## 🚨 关键发现：版本严重落后

| 项目 | 当前值 | 最新值 | 差距 |
|------|--------|--------|------|
| OpenClaw 版本 | 2026.3.8 | **2026.5.22** (稳定) / 2026.5.24-beta.2 | **约 2.5 个月** |
| lastTouchedVersion | 2026.3.8 | - | 5 月 3 日后未更新 |

---

## 📊 ClawHub 生态数据

- **工具总数**: 52.7k tools（持续增长）
- **用户数**: 180k users
- **总下载**: 12M downloads
- **平均评分**: 4.8 avg rating
- **域名变更**: clawhub.com → clawhub.ai（已重定向）

---

## 🔥 OpenClaw 2026.5.22 重要更新（vs 我们当前的 3.8）

### 1. Gateway 性能大幅优化
- 复用进程稳定的 channel catalog 读取
- 热路径缓存 install-record、channel-catalog、Telegram session-store 元数据
- 不可变插件元数据快照跨启动复用
- 懒加载 startup-idle 插件工作和 ACPX 运行时
- 缓存插件 SDK 公共接口别名映射
- 旋转 gateway watch CPU profiles 防止 artifact 积累

### 2. iMessage 新功能
- 支持拇指审批 reactions（👍 允许一次，👎 拒绝）
- mirrors WhatsApp 行为

### 3. Talk/Realtime 实时交互
- WebUI 和 Discord 语音来电可查询运行状态
- 支持取消、引导或排队后续工作
- Discord 语音：添加 realtime wake-name 门控

### 4. 图片工具改进
- 新增自适应模型感知图片压缩
- agents.defaults.imageQuality 偏好设置
- 可选 token-efficient / balanced / high-detail 模式

### 5. Meeting Notes 新功能
- 外部 meeting-notes 插件和 SDK source-provider 合约
- 自动捕获配置 + 手动转录导入
- Discord 语音作为首个 live source

### 6. Agent/Subagent 安全改进
- 限制默认 sub-agent bootstrap context 为 AGENTS.md 和 TOOLS.md
- persona、identity、user、memory 等文件默认不暴露给委派 worker
- PR #85283

### 7. 诊断与可观测性
- OpenTelemetry 导出 sanitized secrets.prepare 时间跨度
- 导出 bounded skill usage metrics/spans
- tool source/owner labels 用于 core/plugin/MCP/channel 工具执行
- Prometheus 和 observability smoke 别名

### 8. Plugin SDK 增强
- 新增通用 channel-message 处理器
- SDK 导入 allowlist 优化

### 9. Docs 大量更新
- Signal configPath、Telegram 通配符 topic 默认值
- 中文记忆导航文档优化
- Feishu 动态 agents
- Bitwarden SecretRef 设置
- 大量中文社区贡献

---

## 📝 对我们的影响

### 高风险（建议升级）
1. **Gateway 性能优化** — 多缓存和懒加载可显著降低启动时间和 CPU 使用
2. **Subagent 安全限制** — 默认不暴露 SOUL.md/IDENTITY.md 等文件给子 agent（可能影响我们的联邦架构，需评估）

### 值得关注
3. **图片压缩** — 可降低图片分析 token 消耗
4. **Talk/Realtime** — 未来可能有新交互方式
5. **诊断改进** — 更好的可观测性

### ClawHub 生态
- 52.7k 工具和 180k 用户意味着社区非常活跃
- 我们的 3 个已发布技能仍在线

---

## ⚠️ 建议

1. **考虑升级到 2026.5.22**（当前落后 2.5 个月）
2. 升级前注意 subagent context 限制变更，可能影响联邦架构
3. 建议先在测试环境验证

---

*自动生成于 2026-05-25 生态探索 cron 任务*
