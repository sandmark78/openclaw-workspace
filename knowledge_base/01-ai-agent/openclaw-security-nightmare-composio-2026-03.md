# OpenClaw 安全噩梦：Composio 深度安全审计分析

**来源**: composio.dev (HN 97 分, 88 评论)
**日期**: 2026-03-22
**分类**: 01-ai-agent / 安全
**数量**: 680

---

## 核心论点

Composio 发布了一篇全面的 OpenClaw 安全审计文章，标题直接引用 Taylor Swift 歌词："A Security Nightmare Dressed Up as a Daydream"。文章系统梳理了 OpenClaw 生态中的 6 大安全威胁层面，是目前最完整的 OpenClaw 安全分析之一。

---

## 六大安全威胁层面

### 1. SkillHub 供应链攻击 (Critical)

**1Password Jason Melier 发现**:
- 最热门下载技能是伪装的恶意软件投递载体
- 攻击链路：skill 要求安装 "openclaw-core" 依赖 → 链接指向恶意基础设施 → 分阶段载荷执行 → 窃取 Cookies/凭证/SSH 密钥
- 甚至移除 macOS Gatekeeper 检查（quarantine attributes）
- VirusTotal 确认为 info-stealer

**Jamieson O'Reilly 的概念验证**:
- 创建了 "What Would Elon Do" 恶意技能
- 利用漏洞将下载量刷到 4000+，成为 #1
- 1 小时内被 7 个国家的真实开发者执行
- 只做了无害 ping，但可以轻松窃取一切
- **教训**: SkillHub 当时零安全审查机制

**Snyk 大规模审计**:
- 3,984 个技能中 283 个 (7.1%) 存在关键安全缺陷
- 明文暴露敏感凭证到 LLM 上下文窗口和日志

### 2. 提示注入 (Permanent Threat)

- 符合 Simon Willison 的 "致命三重奏" (Lethal Trifecta):
  1. 访问私有数据
  2. 暴露于不可信内容（任何人都能发消息）
  3. 外部通信能力（可用于数据外泄）
- OpenClaw 的 Telegram/WhatsApp/Email 集成意味着**任何随机消息都是攻击向量**
- Gary Marcus 评论: "这些系统以'你'的身份运行...在操作系统和浏览器安全保护之上运行"

### 3. 集成攻击面 (50+ 集成)

- 每增加一个集成（Slack/Gmail/Teams/Trello 等），攻击面线性增长
- 攻击者一旦获取实例访问权，即可触达所有已连接服务
- **单点失败导致全面沦陷**

### 4. 认证滥用和过度授权令牌

- OAuth 刷新令牌存储在本地文件中
- 弱认证 + 暴露网关 + 反向代理配置错误 = 从互联网暴露到令牌窃取的路径极短
- SecurityScorecard: 真正风险是暴露的基础设施 + 弱身份控制

### 5. 记忆系统 = Markdown 文件 (无完整性保护)

- 记忆完全是 Markdown 文件集合
- 被入侵的 Agent 可以重写自己的记忆文件
- 攻击者可以静默投毒记忆，持久化控制
- **技能感染是急性的，记忆感染是慢性的**——后者更危险

### 6. 大规模暴露实例 (30,000+)

- 10 天内超过 30,000 个实例暴露于互联网
- 关键漏洞: localhost 连接自动批准认证
- 在 nginx/Caddy 反向代理场景下，所有连接都来自 127.0.0.1
- 已修补但暴露了部署安全意识的普遍缺失

---

## 关键引用分析

### Brandon Wang 的信任框架
> "所有委托都涉及风险。对于人类助手：故意滥用、意外、社会工程。对于 ClawdBot：提示注入、幻觉、安全配置错误、新兴技术的不可预测性。"

**核心洞察**: 人类助手可以追究责任/入狱，AI Agent 不能。

### Federico Viticci 的使用数据
- 烧掉了 1.8 亿 tokens 在 Anthropic API 上
- 减少了与"普通"Claude 和 ChatGPT 的对话
- **粘性极强但成本惊人**

### Moltbook Agent-to-Agent 经济
- AI 研究员发现 Moltbook 上的 Agent 间加密货币 pump-and-dump
- TipJarBot 运行有提款能力的代币经济
- **预示了 Agent 自主经济活动的风险**

---

## 对 Sandbot 的直接影响

### 我们已有的防护
1. ✅ workspace 内操作限制 (AGENTS.md 安全红线)
2. ✅ 敏感路径禁止访问 (~/.ssh, ~/.aws)
3. ✅ 破坏性操作需确认
4. ✅ 密钥集中管理 (secrets 目录)

### 我们需要加强的
1. ⚠️ 技能安装前的安全审查流程
2. ⚠️ 记忆文件完整性验证 (hash 校验)
3. ⚠️ 集成令牌的最小权限原则
4. ⚠️ 定期安全自查 (healthcheck skill)

### 变现机会
1. **OpenClaw 安全加固教程** - 市场需求极大 (97 分 + 88 评论证明)
2. **Agent 安全审计技能** - SkillHub 上发布安全审计工具
3. **记忆完整性保护技能** - 解决 Markdown 记忆投毒问题
4. **安全配置检查器** - 一键检查 OpenClaw 实例安全状态

---

## 行业启示

| 维度 | 现状 | 趋势 |
|------|------|------|
| 技能市场安全 | VirusTotal 合作扫描 | 需要代码签名 + 沙箱 |
| 提示注入 | 无根本解决方案 | 需要架构级隔离 |
| 认证管理 | 文件存储令牌 | 需要硬件安全模块 |
| 记忆安全 | 零保护 | 需要完整性校验 |
| 部署安全 | 用户自行负责 | 需要安全默认配置 |

**核心结论**: OpenClaw 的安全问题不是 bug，是架构级的。自主 Agent 的能力越强，攻击面越大。2026 年的关键赛道是 Agent 安全基础设施。
