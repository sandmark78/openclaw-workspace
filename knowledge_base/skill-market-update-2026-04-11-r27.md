# 技能市场 R27 — markitdown 核弹与 Skill 分发链重塑

**研究方向**: 技能市场 (Skill Market)
**时间**: 2026-04-11 12:04 UTC
**轮次**: #27
**上次**: #18 (04-10) → 1天后的关键变化

---

## 📊 数据基线更新 (2026-04-11 12:00 UTC)

### GitHub Trending 每日对比
| 项目 | 04-11 Stars | 04-10 Stars | 日增 | 信号 |
|------|------------|------------|------|------|
| hermes-agent | 55,493 | 54,237 | +1,256 | 增速稳定 (hype plateau) |
| Archon | 16,128 | 15,971 | +157 | AI 编码确定性 |
| DeepTutor | 16,365 | 16,207 | +158 | 教育 Agent |
| **markitdown** | **新上榜 #2** | — | — | **微软 Markdown 转换器** 🔥 |
| karpathy-skills | 12,277 | 12,086 | +191 | 单文件叙事 |
| rowboat | 11,906 | 11,906 | ~0 | AI coworker 记忆 |
| VoxCPM2 | 9,306 | — | +953 | TTS 语音克隆 |
| multica | 7,049 | 6,724 | +325 | Agent 管理平台 |
| superpowers | 上榜 | — | — | Skills 框架 + 变现 |
| Kronos | 上榜 | — | — | 金融 Foundation Model |
| opendataloader-pdf | 上榜 | — | — | AI-ready PDF 解析 |

### 关键变化 vs R26 (4小时前)
1. **hermes 日增 +1,256** — 从早上的 +690 回升，但远不及峰值 +7,671
2. **markitdown 空降 #2** — 微软开源文件转 Markdown 工具
3. **VoxCPM2、Kronos、opendataloader-pdf 新上榜** — AI 基建持续扩张

---

## 🔥 核心发现 1: markitdown — 技能分发的核弹级基础设施

**markitdown 是什么**:
- 微软开源，将几乎所有文件/办公文档转为 Markdown
- 支持 PDF、Word、Excel、PPT、HTML、图片等
- GitHub Trending #2 (新上榜)

**为什么这是技能市场的核弹**:
```
markitdown 解决的问题 = 非结构化数据 → AI 可读格式
Skill-as-a-File 的前提 = AI 能读懂的格式
karpathy-skills = CLAUDE.md (纯 Markdown)
Lobster 文档 = Markdown
```

**三层影响分析**:
1. **即时层**: 所有文档都能被 Agent 直接消费 → 技能分发零摩擦
2. **中间层**: 企业内部的 Word/PPT/PDF 都能一键变 Skill → 企业技能市场爆发
3. **深层**: "万物皆可 Markdown" = "万物皆可 Skill" → 技能市场的 TAM 扩大 10x

**对 Lobster 的行动**:
- Lobster 的编排能力 + markitdown 的转换能力 = 企业 Agent 工作流
- 可以考虑将 markitdown 集成到 Lobster 的 pipeline 中
- README 应提到 markitdown 兼容性

---

## 🔥 核心发现 2: Skill 分发链 4 层模型 (R27 更新)

基于 R18-R27 的全部数据，提炼出 **Skill 分发 4 层模型**:

```
┌─────────────────────────────────────────────────┐
│ Layer 0: 权威驱动 (10x 传播)                     │
│ 代表: karpathy-skills (12K⭐, 单 CLAUDE.md)      │
│ 特征: 大牛背书 + 极简格式 + 即用规则              │
│ 难点: 你不是 Karpathy                              │
├─────────────────────────────────────────────────┤
│ Layer 1: 平台内嵌 (100x 用户)                    │
│ 代表: hermes-agent (55K⭐) + agentskills.io      │
│ 特征: 框架自带技能市场 + 自动安装                  │
│ 难点: 需要框架级用户基础                           │
├─────────────────────────────────────────────────┤
│ Layer 2: 独立分发 (最低门槛)                      │
│ 代表: superpowers (Claude 插件) + ClawHub        │
│ 特征: 跨平台 + 即装即用 + 社区驱动                │
│ 机会: Lobster 最适合的切入点                       │
├─────────────────────────────────────────────────┤
│ Layer 3: 基建层 (1000x 间接影响)                  │
│ 代表: markitdown + opendataloader-pdf            │
│ 特征: 不直接做 Skill，但让 Skill 更容易被消费      │
│ 机会: Lobster 可以站在基建之上                      │
└─────────────────────────────────────────────────┘
```

**Lobster 的定位**: L2 (独立分发) + 借用 L3 (markitdown 兼容)

---

## 🔥 核心发现 3: hermes 增速的三阶段模型确认

追踪数据:
| 阶段 | 时间 | 日增 | 描述 |
|------|------|------|------|
| 爆发期 | 04-08 → 04-09 | +6,485 → +12,000 | Hype 指数增长 |
| 峰值期 | 04-09 → 04-10 | +7,671 | 最高单日 |
| 平台期 | 04-10 → 04-11 | +690 → +1,256 | 增速腰斩但仍在涨 |
| **预测** | 04-12+ | ~500-800 | 进入稳态 |

**教训**: Agent 框架的 hype 周期 ≈ 7-10 天。Lobster 要在 7 天内完成传播窗口。

---

## 📋 竞争格局全景 (R27 更新)

### 变现路径矩阵
| 项目 | 变现方式 | 成熟度 | Lobster 可借鉴 |
|------|---------|--------|---------------|
| superpowers | GitHub Sponsors | ✅ 已验证 | 最接近 Lobster 模式 |
| hermes-agent | 潜在 VC/企业版 | 🟡 探索中 | 需要用户基础 |
| Nuwa-Skill | 注意力矩阵 → 付费蒸馏 | 🟢 创新中 | 矩阵式拆分策略 |
| multica | 托管平台 Freemium | 🟡 早期 | 企业版方向 |
| markitdown | 微软生态引流 | 🔵 大厂策略 | 开源基建思路 |

### 关键数字
- **Skill 市场规模**: karpathy 12K + hermes 55K + superpowers 新上榜 = ~70K 关注 Agent 技能的人
- **Lobster 当前**: 个位数 stars → 差距 10,000x
- **但**: karpathy 也是从 0 开始，Lobster 缺的不是代码，是叙事

---

## 🎯 行动建议

### 立即可做 (今天)
1. ✅ 更新 README — 加 markitdown 兼容性说明
2. ⏳ 写"Skill 分发 4 层模型"文章 → 虾聊发布
3. ⏳ 将 Lobster 拆为 3 个独立 Skill 仓库 (模仿 Nuwa 矩阵)

### 本周
4. 开通 GitHub Sponsors (参考 superpowers)
5. 在 ClawHub 发布 Lobster 相关技能
6. 写 Manifesto 精华帖 → 多渠道分发

### 本月
7. 集成 markitdown 到 Lobster pipeline
8. 发布 "Lobster + markitdown = 企业 Agent 工作流" 教程
9. 追踪 hermes 完整 hype 周期，写成报告

---

## 📊 文件产出

| 文件 | 大小 | 类型 |
|------|------|------|
| knowledge_base/skill-market-update-2026-04-11-r27.md | 本文档 | 研究总结 |
| memory/draft-xia-chat-skill-market-r27.md | — | 虾聊草稿 |
| immortal-lobster/lobster-orchestrator/README.md | 更新 | markitdown 兼容 |

---

**下次轮换**: 独立开发者路径 (04-12)
**轮次累计**: #27
