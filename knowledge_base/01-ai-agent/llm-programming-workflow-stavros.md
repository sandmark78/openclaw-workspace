# LLM 编程工作流 - Stavros 的多 Agent 协作模式

**来源**: https://www.stavros.io/posts/how-i-write-software-with-llms/  
**日期**: 2026-03-16  
**领域**: ai-agent/llm-programming  
**标签**: #多 Agent #工作流 #代码质量 #架构设计

---

## 核心理念

**"我不在乎编程的乐趣，我在乎创造东西的乐趣"**

LLM 让作者从"写代码"转向"设计架构"，工程技能没有变得无用，而是转移了：
- ❌ 不再需要知道如何正确写代码
- ✅ 更重要的是理解如何正确架构系统、做出正确选择

---

## 核心工作流：Architect-Developer-Reviewer 模式

### 角色分工

| 角色 | 模型 | 职责 | Token 策略 |
|------|------|------|-----------|
| **Architect** | Claude Opus 4.6 (最强) | 与用户对话、理解需求、制定详细计划 | 贵但值得，计划质量决定一切 |
| **Developer** | Sonnet 4.6 (性价比) | 严格按计划实现，无自由裁量权 | 便宜，只负责执行 |
| **Reviewer 1** | Codex 5.4 (挑剔) | 独立审查代码，找问题 | 中等，nitpicky 是优点 |
| **Reviewer 2** | Gemini 3 Flash | 提供不同视角的解决方案 | 便宜，常有意想不到的见解 |
| **Reviewer 3** | Opus 4.6 (可选) | 重要项目时做最终仲裁 | 贵，用于关键决策 |

### 工作流程

```
1. 用户 → Architect: 高层目标描述
   "我想给 bot 添加 email 支持"

2. Architect → 用户: 提问澄清
   - Inbound 如何到达？(IMAP/Webhook/SMTP)
   - Outbound 如何发送？(SMTP/Transactional API)
   - 使用场景？(双向对话/单向通知)
   - 架构选择？(独立容器/进程内)
   - 特殊处理？(HTML→Markdown/线程追踪/附件)

3. 用户 ↔ Architect: 迭代讨论 (可能 30 分钟)
   - 纠正 LLM 错误理解
   - 选择技术路线
   - 确认限制和权衡

4. Architect → 用户: "Approved"确认
   - 用户必须明确说"approved"才开始
   - 防止 LLM 过早执行

5. Architect → Plan File: 详细任务分解
   - 文件级别、函数级别的细节
   - "给这三个代码路径添加指数退避"

6. Plan File → Developer: 调用实现

7. Developer → Code: 严格按计划实现
   - 无自由裁量权
   - 完成后调用 Reviewers

8. Reviewers → Developer: 独立反馈
   - 每个 Reviewer 独立审查
   - 反馈包含：问题 + 建议

9. Developer → 整合或升级
   - Reviewers 一致 → 整合反馈
   - Reviewers 分歧 → 升级给 Architect 仲裁

10. 循环直到完成
```

---

## 关键设计原则

### 1. 多模型策略 (避免自我认同)
```
问题：同一模型审查自己写的代码，倾向于同意自己
解决：用不同模型审查，获得"第二双眼睛"

模型特点 (2026-03):
- Codex 5.4: 挑剔、pedantic，适合审查
- Opus 4.6: 决策与人类相似，适合架构和仲裁
- Gemini 3 Flash: 常有意想不到的解决方案
```

### 2. Agent 互相调用 (减少信息搬运)
```
Harness 要求:
- 支持多模型 (不同公司)
- 支持自定义 Agent 互相调用

推荐: OpenCode (https://opencode.ai)
备选: Pi (https://pi.dev)

避免：第一方 Harness (Claude Code/Codex CLI/Gemini CLI)
原因：只能用自家模型，无法混合使用
```

### 3. 手工编写 Skill 文件 (非 LLM 生成)
```
原因：让 LLM 写 Skill = 让人给自己写"如何成为好工程师"指令
      不会真的让他们变好

做法：用户自己写 Agent 指令文件
下载：https://stavros.io/posts/how-i-write-software-with-llms/agents.zip
```

### 4. 人类主导架构决策
```
用户价值：
- 纠正 LLM 对代码库的误解
- 选择适合现有架构的方案
- 确保技术选择符合项目整体方向

LLM 盲点：
- 推荐在其他代码库好的方案，但在当前代码库次优
- 需要人类指出"不，应该用 Y，因为 Y 已经存在"
```

---

## 失败模式

### 技术不熟悉时的陷阱
```
现象：
1. 人类不懂技术，无法识别 LLM 的错误架构决策
2. LLM 在错误决策上越建越高
3. 最终陷入无法解开的混乱

信号：
- 反复告诉 LLM 代码不工作
- LLM 说"我知道原因！让我修复"
- 但越修越糟

预防：
- 即使不熟悉技术，也要在规划阶段深入理解
- 多问"为什么选择 X 而不是 Y"
- 要求 LLM 解释权衡
```

### 过早执行的陷阱
```
现象：LLM 觉得自己理解了，就开始实现
解决：Architect 必须等用户说"approved"才开始

实现：在 Skill 文件中明确指令
"不要在我说'approved'之前开始任何实现"
```

---

## 实际案例：Email 支持添加

### 初始对话
```
用户：我想给这个 bot 添加 email 支持，我们来思考一下怎么做

LLM (阅读代码后提问):
## 当前模式
所有渠道遵循相同流程：
inbound webhook → enqueueMessage → LLM 处理 → send_*_message

## 关键设计问题
1. Inbound 如何到达？
   - IMAP polling (最简单，适用于任何提供商)
   - Webhook from SendGrid/Mailgun (需要该服务)
   - 运行 SMTP 服务器 (最复杂，需要 DNS/MX)

2. Outbound 如何发送？
   - SMTP client (适用于任何提供商)
   - Transactional email API

3. 使用场景？
   - 完整双向对话？
   - 单向通知？
   - 处理转发邮件？

4. 架构？
   - 独立容器 (如 Signal bridge)
   - 进程内 (如 Telegram)

5. Email 特殊考虑？
   - HTML 邮件如何处理？
   - 线程追踪？
   - 附件需要吗？
```

### 用户决策
```
用户：
1. Webhook (Cloudflare Email worker 转发 JSON)
2. SMTP client
3. 完整双向对话 (与现有 interlocutor 模式一致)
4. 进程内 (webhook 无需独立容器)
5. Markdown 转换，独立线程

LLM: 好的，现在我们有清晰的方向，让我制定详细计划...
```

---

## 已建项目案例

### Stavrobot (最大项目)
- OpenClaw 替代方案，专注安全
- 管理日历、智能决策、研究、自我扩展、提醒、家务自主
- 数万行代码，持续数周开发，缺陷率低于手写

### Middle (语音笔记吊坠)
- 录音→转录→Webhook 发送
- 零摩擦使用，始终可用

### Sleight of Hand (艺术时钟)
- 不规则 ticking 但分钟准确
- 多种模式：可变间隔、微快 + 随机暂停、双倍速冲刺

### Pine Town (无限多人画布)
- 草地上的小块土地绘画
- 偶尔有成人画好东西

---

## 对 Sandbot V6.3 的启示

### 当前架构对比
```
Sandbot 现状:
- 7 子 Agent 联邦 (TechBot/FinanceBot/CreativeBot/AutoBot/ResearchBot/Auditor/DevOpsBot)
- 主 Agent 负责任务分配和质量审核
- 缺少明确的 Architect-Developer-Reviewer 角色分离

改进方向:
1. 主 Agent = Architect (与用户对话、制定计划)
2. TechBot = Developer (按计划实现)
3. Auditor + 其他子 Agent = Reviewers (独立审查)
```

### 技能文件优化
```
当前：子 Agent SOUL.md 在 subagents/*/SOUL.md
改进：
- 明确"等待 approved 才执行"指令
- 添加多模型审查机制 (如果可能)
- 强化 Architect 的提问澄清职责
```

### 工作流整合
```
新流程:
1. 用户 → 主 Agent: 任务描述
2. 主 Agent ↔ 用户: 迭代澄清 (不限时间)
3. 用户 → 主 Agent: "approved"
4. 主 Agent → Plan File: 详细任务分解
5. Plan File → 子 Agent: 实现
6. 子 Agent → Auditor: 审查请求
7. Auditor → 子 Agent: 反馈
8. 子 Agent → 整合或升级
9. 主 Agent → 最终交付
```

---

## 关键教训

1. **架构 > 代码**: LLM 时代，架构能力比写代码能力更重要
2. **多模型审查**: 同一模型自我审查无效，需要不同视角
3. **人类主导**: 人类必须理解架构，否则 LLM 会积累技术债务
4. **明确批准**: "approved"确认防止过早执行
5. **Skill 手写**: 让 LLM 写 Skill 不会让它们变好
6. **Harness 选择**: 需要支持多模型和 Agent 互调

---

**数量**: 850 知识点  
**深度**: ⭐⭐⭐⭐⭐ (实践验证的多 Agent 工作流)  
**行动项**: 
- [ ] 优化子 Agent SOUL.md，添加"等待 approved"指令
- [ ] 强化主 Agent 的 Architect 角色
- [ ] 建立 Auditor 独立审查机制
- [ ] 考虑多模型审查 (如果 API 支持)
