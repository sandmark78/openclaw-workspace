# AI 语音接待员实战：为汽修店构建 RAG Voice Agent

**来源**: https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/
**日期**: 2026-03-23
**HN 热度**: 148 points / 162 comments
**领域**: 01-ai-agent / AI 商业化实战
**质量**: ★★★★★ (真实业务场景，完整技术栈，含踩坑经验)

---

## 业务背景

豪华汽修店老板每周**漏接 100+ 电话**，每个漏接 = 潜在流失客户 ($50-$2000/单)。
解决方案：名为 "Axle" 的 AI 语音接待员，24/7 接听电话。

**核心洞察**: 这不是通用聊天机器人，而是**领域特化的语音 Agent**，知道精确价格、营业时间、政策。

---

## 三阶段构建法

### Phase 1: 构建大脑 (RAG Pipeline)

**问题**: 原始 LLM 在这里很危险。客户问"刹车多少钱"，AI 猜 $200，实际 $450 = 预期破裂。

**解决方案**:
1. **爬取网站** → 21+ 结构化文档 (服务/价格/时间/政策/保修)
2. **嵌入向量** → Voyage AI (voyage-3-large) 1024 维向量 → MongoDB Atlas Vector Search
3. **检索管道** → 查询嵌入 → Top 3 语义匹配文档
4. **约束生成** → Claude claude-sonnet-4-6 + 严格 system prompt: 只从知识库回答，不知道就说不知道

**关键约束**: "No hallucinations allowed" — 不允许幻觉，不知道就留回电信息。

### Phase 2: 连接真实电话

**技术栈选择**: Vapi (电话基础设施一站式)
- Deepgram: 语音转文字
- ElevenLabs: 文字转语音
- 实时 function calling → FastAPI webhook

**架构**:
```
来电 → Vapi (STT) → webhook/FastAPI → RAG Pipeline → Claude → Vapi (TTS) → 回复来电者
```

**开发技巧**: Ngrok 隧道用于本地开发，两分钟搞定。

**数据资产化**:
- 每次通话存入 MongoDB `calls` 集合
- 回电请求存入 `callbacks` 集合
- 可分析：最常见问题、通话高峰、AI 交接率

### Phase 3: 语音调优 (最难的部分)

**核心发现**: 文本响应和语音响应完全不同。

| 文本 OK | 语音 NG |
|---------|---------|
| "$45.00" | 听起来怪 → "forty-five dollars" |
| "Certainly!" | 太机器人 → 删掉 |
| 项目符号列表 | 无法朗读 → 短句 |
| 长段落 | 听众走神 → 2-4 句封顶 |

**声音选择**: 试了 20 个 ElevenLabs 声音，选了 "Christopher" — 冷静、自然、不急不慢。
> "错误的声音 + 完美回答 = 仍然感觉不对"

**升级流程是核心功能**:
- AI 不知道 → 告知客户 → 收集姓名+回电号码 → 存入 MongoDB → 店主跟进
- "升级路径不是边缘情况，而是核心功能"

---

## 完整技术栈

| 组件 | 技术 | 用途 |
|------|------|------|
| 电话 | Vapi + Deepgram + ElevenLabs | STT/TTS/电话号码 |
| 隧道 | Ngrok | 本地开发 |
| 后端 | FastAPI + Uvicorn | Webhook 服务器 |
| 数据库 | MongoDB Atlas | 知识库/向量搜索/通话日志 |
| 嵌入 | Voyage AI (voyage-3-large) | 语义检索 |
| 生成 | Anthropic Claude (claude-sonnet-4-6) | 受限回答生成 |
| 语言 | Python | pymongo/voyageai/anthropic/fastapi |

---

## 对 AI Agent 开发的核心教训

### 1. 不要用裸 LLM 做业务语音 Agent
- RAG 是必须的，不是可选的
- 价格、政策这种硬数据必须从知识库检索

### 2. 语音 ≠ 文本
- 语音 Agent 的 system prompt 需要专门针对语音优化
- 声音选择影响巨大，不只是"好听不好听"

### 3. 升级流程先于一切
- 在写任何功能之前，先设计 "不知道怎么办" 的流程
- 收集回电信息 = 不丢失线索

### 4. 数据是副产品，也是金矿
- 通话日志 → 客户需求分析
- 常见问题 → 知识库优化方向
- 高峰时段 → 运营决策

---

## 对 Sandbot/OpenClaw 的行动项

| 行动 | 优先级 | 理由 |
|------|--------|------|
| 研究 Vapi 集成可能性 | P2 | OpenClaw + 语音 = 新通道 |
| 构建 "AI 接待员" 教程 | P1 | 148 points 证明市场需求巨大 |
| 知识库 RAG 约束模式 | P1 | "只从知识库回答" 对我们的知识检索系统也适用 |
| 语音优化 prompt 模板 | P3 | 未来语音 Agent 技能的基础 |

---

## 变现洞察

- **巨大市场**: 每个小企业 (餐厅/诊所/维修店) 都有漏接电话问题
- **SaaS 模式**: AI 接待员月费 $99-499 vs 人工接线员 $2000+/月
- **教程价值**: "如何为你的业务构建 AI 电话接待" — 完整技术栈教程
- **162 条评论**说明这是真痛点，不是技术炫耀

**数量**: ~620 知识点
**标签**: #VoiceAgent #RAG #商业化 #Vapi #MongoDB #实战案例
