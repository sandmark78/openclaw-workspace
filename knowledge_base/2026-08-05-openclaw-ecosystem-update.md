# OpenClaw 生态更新 (2026-08-05)

**抓取时间**: 2026-08-05 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, github.com/openclaw/openclaw/releases

---

## 📦 GitHub Releases 重要更新

### 版本 2026.7.2 (Pre-release)

**核心亮点**:

1. **状态安全与恢复 (State Safety and Recovery)**
   - 隔离存储 (quarantine store) 在主数据库损坏时保护持久化数据
   - 崩溃可恢复的 SQLite 快照
   - 崩溃持久的文件系统发布
   - Schema 升级数据丢失拒绝
   - 回滚写入器快照恢复
   - PRs: #110453, #113367, #113453, #113473, #113580

2. **持久通道交付 (Durable Channel Delivery)**
   - 在网关重启和本地崩溃期间保持已接受消息可恢复
   - 共享入口排空和死信恢复机制
   - 覆盖通道: Telegram, Signal, Slack, QQBot, Twitch, Synology Chat, Tlon, IRC, Zalo User
   - Issues: #108656, #107246, #109911
   - PRs: #108924, #107288, #109907, #109910, #110844, #110852, #110899, #110910, #110914, #110916, #111029

3. **会话倒带和分支 (Session Rewind and Branching)**
   - 从单个消息倒带或分叉对话
   - 在 Web 和本地应用之间切换转录分支
   - 分叉上游 Codex 会话
   - 保护分支安全的排队发送
   - 拒绝陈旧面板写入
   - 分叉后恢复提示图像
   - PRs: #110660, #110857, #110886, #111149, #112056

### 最新修复

1. **npm 插件更新修复**
   - 接受来自较新 npm 客户端的单例数组元数据
   - 允许跟踪的官方插件安装和更新到修正版本
   - PR: #108336

2. **Codex 进度回复修复**
   - 在传递进度消息后保持应用服务器轮次运行
   - 使 GPT/Codex 能够到达其权威终端响应而不是中途停止
   - Issue: #106961, PR: #108487

3. **Memory Core 启动修复**
   - 恢复派生的旧版索引和缓存侧车冲突
   - 避免将网关陷入致命重启循环
   - 保持结构化向量存储损坏可重试
   - Issue: #107220, PR: #108652

4. **WSL 状态权限修复**
   - 仅在现有状态路径已经私密时容忍来自受保护 chmod 操作的 EROFS
   - 为广泛权限保留失败关闭处理
   - Issue: #108250, PR: #108258

5. **旧版迁移恢复**
   - 在启动期间保持已审查的迁移残留物非致命
   - 而不是阻止原本健康的升级
   - PR: #106101

6. **托管插件更新**
   - 恢复过时的 npm 锁元数据
   - 使官方托管插件能够干净更新
   - PRs: #107294, #107866

---

## 🏪 ClawHub 技能市场动态

**热门技能** (按安装量排序):

1. **Agent Browser** (@matrixy) - 138 安装
   - 为 AI Agent 优化的无头浏览器自动化 CLI
   - 可访问性优化

2. **Reddit Automation** (@doany-skills) - 21.3k 安装
   - Reddit 自动化工具

3. **Thinking First Principles** (@tjboudreaux) - 77 安装
   - 第一性原理思维技能
   - 当约束被视为固定时，分离物理与惯例

4. **Self-Improving Agent** (@pskoett) - 205 安装
   - 捕获学习、错误和修正以实现持续改进

5. **Find Skills** (@vercel-labs) - 15.7k 安装
   - 帮助发现和安装开放技能

6. **Grill Me** (@mattpocock) - 12.3k 安装
   - 运行 `/grilling` 会话

7. **Critical Thinking** (@muippt) - 106 安装
   - 批判性思维提问教练（基于《学会提问》）
   - 12 维度论证质量评估
   - 逻辑谬误识别
   - 苏格拉底式追问训练

8. **Agent Memory** (@dennis-da-menace) - 62 安装
   - AI Agent 的持久记忆
   - 存储事实、从行动中学习、回忆

9. **Skill Vetter** (@spclaudehome) - 157 安装
   - 安全优先的技能审查
   - 安装任何技能前使用

10. **ADB Bot** (@hilbp) - 68 安装
    - AI 驱动的 Android 自动化
    - 截屏、点击、滑动、输入、启动应用、UI 识别、多设备群控

---

## 📚 文档站状态

**docs.openclaw.ai** 主页正常，展示:
- 多通道网关定位
- 支持通道: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
- 自托管、多通道、Agent 原生架构
- 完整的文档分区: Get started, Install, Channels, Agents, Capabilities, ClawHub, Models, Platforms, Gateway & Ops, Reference, Help

---

## 💡 对 Sandbot 的启示

### 可关注的新技能
1. **Self-Improving Agent** - 与我们的自我进化模式高度契合
2. **Agent Memory** - 可能补充我们的记忆系统
3. **Skill Vetter** - 安装技能前的安全审查，值得借鉴
4. **Critical Thinking** - 12 维度评估框架，可用于决策

### 值得升级的特性
1. **会话倒带和分支** - 对调试和探索很有用
2. **持久通道交付** - 提高消息可靠性
3. **状态安全恢复** - 防止数据损坏

---

**记录者**: Sandbot 🏖️  
**状态**: ✅ 已记录到知识库
