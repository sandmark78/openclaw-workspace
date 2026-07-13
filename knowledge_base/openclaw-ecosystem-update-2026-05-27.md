# OpenClaw 生态探索 2026-05-27

**日期**: 2026-05-27 20:00 UTC
**来源**: clawhub.ai + docs.openclaw.ai + GitHub releases + npm registry

---

## ClawHub 统计 (clawhub.ai)
- 工具数: **52.7k**（与 5/26 无变化）
- 用户数: **180k**（无变化）
- 下载量: **12M**（无变化）
- 平均评分: **4.8**（无变化）

---

## Docs 变化 (docs.openclaw.ai)
- 推荐 Node 24 / 兼容 Node 22 LTS (22.19+)
- 我们当前运行 Node 22.22.1，兼容但非推荐
- 支持渠道: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等

---

## ⚠️ 重大变化：GitHub Releases

### GitHub 仓库迁移
- 旧地址: `github.com/nicepkg/openclaw` (404)
- 新地址: `github.com/openclaw/openclaw` ✅

### 版本差距 ⚠️
- **我们当前**: 2026.3.8 (约 2 个月旧)
- **npm latest**: 2026.5.26
- **GitHub 最新 release**: 2026.5.27 (今天发布!)

### v2026.5.27 (2026-05-27 最新发布) 核心变更:

#### 性能优化
- Gateway 启动跳过重复的 plugin/channel/session 扫描
- 回复路径分离用户发送与后续慢操作
- 缓存插件元数据、通道解析、session/auth 热路径
- 减少高负载下运行时/session 缓存抖动

#### 核心新功能
- **Transcripts**: 转录支持的会议摘要、source-provider chunks、CLI/TUI 回放
- **Reaction Approvals**: Signal/iMessage/WhatsApp 支持拇指审批反应（无需 /approve 命令）
- **Named Auth Profiles**: 命名模型登录配置，支持 Hermes/OpenCode/Codex 凭证迁移
- **OpenTelemetry LLM spans**: 可观测性增强
- **Activity Tab**: 控制 UI 新增临时 Activity 标签页

#### 渠道改进
- **Telegram**: 保留 typing/progress 上下文和论坛主题
- **iMessage**: 附件根处理、远程媒体暂存、重复源处理、拇指审批
- **WhatsApp**: 恢复群组/媒体行为、拇指审批
- **Discord**: 改进语音播放和模型选择、字母桶选择器（>25 模型时）
- **Signal**: 拇指审批反应

#### Voice/Talk
- 实时 Talk 运行可从 Web UI/Discord 语音检查、引导、取消
- 共享实时 turn-context 追踪
- Android/iOS 移动 Talk 模式改进
- iOS: 直接实时语音会话、紧凑工具栏、波形反馈

#### 安全
- Browser snapshot 读取遵循 SSRF 策略
- system-event 文本不能伪造嵌套 prompt 标记
- 抓取文件文本包装为外部内容
- ClickClack 入站发送者白名单在 agent 调度前运行
- 过期设备 token 拒绝
- 序列化工具调用文本从回复中清除
- 记忆存储工具拒绝 prompt-like 文本
- auth 速率限制默认启用

#### 移动端
- Android: 新增 pair-new-gateway 动作
- iOS: Talk 模式改进（直接实时语音会话）
- 离线语音/gateway 恢复

#### 其他
- Cron: 默认 maxConcurrentRuns=8
- 图片后端: Sharp → Rastermill
- Codex CLI: 更新到 0.134.0
- OpenAI 采样参数通过 Gateway 转发
- 上下文预算状态暴露

---

## 建议行动
1. **P0**: 考虑升级到 2026.5.27，差距约 2 个月，变更量很大
2. **P1**: 新安全特性（SSRF 防护、auth 限速、prompt 注入过滤）值得升级
3. **P2**: Telegram 打字/progress 上下文改进对我们当前通道直接有益
4. **注意**: 仓库已迁移到 `openclaw/openclaw`
