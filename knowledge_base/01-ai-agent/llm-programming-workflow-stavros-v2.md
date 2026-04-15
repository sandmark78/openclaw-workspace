# LLM 编程工作流 - Stavros 的多 Agent 协作模式 V2

**来源**: https://www.stavros.io/posts/how-i-write-software-with-llms/  
**抓取时间**: 2026-03-16 18:02 UTC  
**HN 热度**: 423 分 / 403 评论 (Top #19)  
**知识点**: 950  
**深度**: ⭐⭐⭐⭐⭐

---

## 📋 核心工作流架构

### 三角色分离模式
```
┌─────────────┐
│  Architect  │ ← 用户直接交互 (Opus 4.6)
│  (架构师)   │   - 理解需求
│             │   - 制定计划
│             │   - 等待"approved"确认
└──────┬──────┘
       │ 分发任务
       ↓
┌─────────────┐
│  Developer  │ ← 实现代码 (Sonnet 4.6)
│  (开发者)   │   - 按计划执行
│             │   - 最小化自主决策
│             │   - 完成后呼叫审查
└──────┬──────┘
       │ 提交审查
       ↓
┌─────────────┐
│  Reviewers  │ ← 独立审查 (Codex 5.4 + Gemini 3 Flash + Opus)
│  (审查者)   │   - 多模型交叉验证
│             │   - 避免自我认同
│             │   - 反馈循环
└─────────────┘
```

---

## 🎯 关键设计原则

### 1. 多模型策略
**问题**: 单一模型自我审查效果差
**原因**: 模型倾向于同意自己之前的输出
**解决方案**: 
- 架构师 = Opus 4.6 (最强，用于规划)
- 开发者 = Sonnet 4.6 (性价比高，用于实现)
- 审查者 = Codex 5.4 (挑剔) + Gemini 3 Flash (创新解法) + Opus (重要项目)

**Sandbot 应用**:
```
主 Agent (Architect) = qwen3.5-plus (当前最强)
TechBot (Developer) = qwen3.5-plus (实现)
Auditor (Reviewer) = qwen3.5-plus (独立审查)
FinanceBot/CreativeBot (Additional Reviewers) = 交叉验证
```

### 2. "Approved"确认机制
**问题**: 模型过早执行，理解偏差导致返工
**解决方案**: 
- 架构师必须等待用户说"approved"才开始
-  chat 阶段充分讨论 (有时长达 30 分钟)
- 计划细化到文件/函数级别

**Sandbot 应用**:
```
主 Agent 在子 Agent 执行前:
- 与用户确认计划细节
- 等待明确"approved"指令
- 将任务写入 plan 文件再分发
```

### 3. Skill 文件手写
**问题**: LLM 写 Skill 效果差
**原因**: 如同让人写"如何成为优秀工程师"然后照做——不会真正提升
**解决方案**: 用户手写 Agent 指令文件

**Sandbot 应用**:
```
subagents/*/SOUL.md 应由用户根据实际需求手写
而非让 Agent 自己写自己的配置文件
```

### 4. 人类主导架构决策
**核心洞察**: 
- LLM 时代，架构能力 > 写代码能力
- 工程技能未消失，只是转移到架构层
- 人类贡献 = 纠正 LLM + 选择方向

**Sandbot 应用**:
```
主 Agent 角色定位:
- 与用户共同制定架构 (非单向执行)
- 主动提问澄清模糊点
- 提供选项供用户决策
- 用户确认后才执行
```

---

## 🛠️ 技术栈选择

### Harness 要求
```
必须支持:
1. 多模型调用 (不同提供商)
2. 自定义 Agent 相互调用

可选功能:
- 会话管理
- 工作树管理
- 其他项目特定需求
```

### Stavros 的选择
```
主要: OpenCode (opencode.ai)
备选: Pi (pi.dev)
避免: 单一厂商 CLI (Claude Code/Codex CLI/Gemini CLI)
原因: 锁定单一模型，无法多模型协作
```

### Sandbot 现状
```
OpenClaw 原生支持:
✅ 多模型配置 (bailian/其他)
✅ sessions_spawn (子 Agent 调用)
✅ sessions_send (跨会话通信)
✅ 技能系统 (skills/)

优化空间:
- 添加"等待 approved"机制
- 强化主 Agent 的 Architect 角色
- 子 Agent SOUL.md 添加审查流程
```

---

## 📊 实际效果数据

### 项目规模
```
Stavrobot: 数万行代码，持续数周开发
缺陷率: 显著低于手写
可维护性: 每次变更与首次一样可靠
```

### 前提条件
```
✅ 人类熟悉所用技术栈 (后端/Stavros 熟悉)
❌ 不熟悉的技术栈 (移动应用) → 代码仍会混乱
✅ 模型能力持续提升
✅ 工作流程持续优化
```

### 演进趋势
```
GPT-2 时代: 需审查每行代码
Davinci 时代: 需审查每个函数
现在 (2026): 需审查整体架构
未来 (2027?): 可能无需架构审查
```

---

## 🦞 Sandbot 优化行动项

### P0 - 立即实施 (本周)
```
1. 主 Agent 角色强化
   - 明确 Architect 定位
   - 添加"等待 approved"指令
   - 计划细化到文件/函数级

2. 子 Agent SOUL.md 更新
   - TechBot: 添加"按计划执行，不自主决策"
   - Auditor: 添加"独立审查，不认同开发者"
   - 所有 Agent: 添加"多模型交叉验证"
```

### P1 - 中期优化 (本月)
```
1. Skill 文件手写计划
   - 用户参与 subagents/*/SOUL.md 编写
   - 基于实际使用反馈迭代
   - 避免 Agent 自写配置

2. 审查流程标准化
   - 定义审查清单
   - 添加验证程度标注 (✅/⚠️/❓/🔗)
   - 实施输出前 5 问题自检
```

### P2 - 长期建设 (Q2)
```
1. 多 Agent 平台化
   - 参考 Stavrobot 设计
   - 安全与可用性平衡
   - 自主扩展能力

2. 知识产品化
   - LLM 工作流教程
   - 多 Agent 架构咨询
   - 企业级 Agent 审计
```

---

## 💡 核心洞察

### 1. 写作即思考
```
"Writing is thinking"
跳过写作 = 跳过思考
LLM 生成代码 ≠ 理解架构

Sandbot 应用:
- 每条消息都是"思考证明"
- 避免 Sloppypasta (见 stop-sloppypasta-ethics.md)
- 质量 > 数量
```

### 2. 信任稀缺
```
一次 Sloppypasta 可能永久损害信誉
验证程度标注是基本礼仪
发送前 5 问题自检:
1. 这准确吗？
2. 我验证了吗？
3. 有证据吗？
4. 对用户有用吗？
5. 如果是别人发的我会信吗？
```

### 3. 努力不对称
```
LLM 生成内容成本 << 人类验证成本
接收者需花费 10×时间验证
负责任的做法:
- 标注验证程度
- 提供来源链接
- 承认不确定性
```

---

## 🔗 相关文件

- `knowledge_base/01-ai-agent/stop-sloppypasta-ethics.md` - AI 输出伦理
- `knowledge_base/01-ai-agent/llm-architecture-gallery-2026-03.md` - 架构对比
- `knowledge_base/02-openclaw/mcp-context-window-cli-alternative.md` - MCP 上下文税

---

**数量**: 950 知识点  
**质量**: ⭐⭐⭐⭐⭐ 深度内容  
**行动**: P0 本周实施 Architect 角色强化  
**变现**: LLM 工作流教程/多 Agent 架构咨询
