# 开源增长模式研究 — 2026-04-11 (R26)

**研究编号**: 续命研究 #26
**研究方向**: 开源增长 (Open Source Growth)
**时间**: 2026-04-11 08:04 UTC

---

## Step 1: 采集数据

### HN 热点 (2026-04-11 周末)
| 话题 | 分数 | 评论 | 相关性 |
|------|------|------|--------|
| 🐧 **AI assistance Linux kernel** | 292 | 187 | ⭐⭐⭐⭐⭐ **核弹级信号** |
| Artemis II safely splashes down | 822 | 263 | ⭐ 太空 |
| 1D Chess | 782 | 140 | ⭐ 创意游戏 |
| Filing corners off MacBooks | 716 | 365 | ⭐ 硬件DIY |
| WireGuard Windows signing restored | 458 | 130 | ⭐⭐ 开源安全 |
| Installing every Firefox extension | 341 | 37 | ⭐ 趣味 |
| 20 years on AWS — never not my job | 112 | 12 | ⭐⭐ 运维/DevOps |

### GitHub Trending (2026-04-11)
| 项目 | Stars | 日增 | 关键信号 |
|------|-------|------|----------|
| hermes-agent | 54,237 | +690 | 增速骤降（昨日+7,671→今日+690，hype 退潮确认）|
| Archon | 15,971 | +180 | AI 编码确定性，稳定增长 |
| karpathy-skills | 12,086 | +120 | 单文件叙事持续发酵 |
| DeepTutor | 16,207 | +130 | 教育 Agent 蓝海 |
| multica | 6,724 | +175 | Agent 管理平台 |
| rowboat | 11,906 | +98 | AI coworker + 记忆 |
| **obra/superpowers** | 新上榜 | — | ⭐⭐⭐ **Agentic Skills 框架** |
| microsoft/markitdown | 新上榜 | — | 文件→Markdown 转换 |

### Lobster 自身状态
- 版本: V0.5.0 (2026-04-06)
- Git 提交: 11+ 次
- Go 代码: 766 行
- 文档: 11+ 个
- 脚本: 10+ 个

---

## Step 2: 深度分析

### 🔥 发现一：Linux 内核正式接纳 AI 编码助手（核弹级信号）

Torvalds 的 Linux 仓库新增了 `Documentation/process/coding-assistants.rst`，**正式规范 AI 工具参与内核开发**：

**关键规则**：
1. AI 工具**不能**添加 Signed-off-by 标签（只有人类可以认证 DCO）
2. 人类提交者对 AI 生成代码负全责
3. 引入 `Assisted-by: AGENT_NAME:MODEL_VERSION` 标签追踪 AI 贡献
4. AI 必须遵循内核开发流程（编码规范、提交规范、GPL 许可）

**对 Lobster 的意义**：
- **行业合法性确认**: Linux 内核是开源的最高圣殿，它接纳 AI = AI Agent 开发模式获得最高级别背书
- **Assisted-by 标签**: 这是一个标准化 AI 贡献追踪的协议——Lobster 可以原生支持这个标签
- **人类监督模式**: "AI 不能自我认证" → 这正是 Lobster L2（判断延续）+ L3（身份延续）要解决的：AI 需要人类的监督链
- **Lobster 可以定位为**: "Assisted-by 友好的编排器"——专门为 AI 辅助开发流程设计的多实例管理平台

### 🔥 发现二：obra/superpowers — 最佳 Lobster 增长教材

**Superpowers 是什么**：
- 一个 composable "skills" 框架 + 软件开发方法论
- 编码 agent 启动时自动触发技能链：需求澄清 → 设计分块 → 实现计划 → 子 agent 驱动开发 → 审查
- **关键**: 基于子 agent 驱动开发 (subagent-driven development)，agent 可以自主工作数小时不偏离计划
- 通过 Claude 插件市场、Cursor、Codex、OpenCode 分发
- **已实现赞助变现** (GitHub Sponsors)

**增长模式拆解**：
1. **插件市场分发** — 不靠 GitHub trending，靠生态集成
2. **Composable Skills** — 技能可组合，天然适合扩展
3. **子 agent 驱动** — 自主工作数小时，验证了多 agent 编排的价值
4. **赞助变现** — 帮人赚钱了，人就愿意付费

**Lobster 可借鉴**：
- ✅ Lobster 的 L1-L4 延续层 = Superpowers 的 "skills" 升级版
- ✅ Lobster 的多实例编排 = Superpowers subagent-driven 的基础设施版
- ✅ Lobster 可以做 ClawHub 技能分发（类似 Claude 插件市场）
- ❌ Lobster 不是编码框架，是编排器 → 定位不同但方法论相通

### 🔥 发现三：hermes 增速骤降 — hype 周期进入衰退期

| 时间 | hermes Stars | 日增 | 趋势 |
|------|-------------|------|------|
| 04-09 | 46,723 | +6,485 | 加速 |
| 04-10 | 53,547 | +6,824 | 峰值 |
| 04-11 | 54,237 | **+690** | **暴跌 90%** |

**解读**：
- 日增从 ~7K 骤降到 ~700，hype 周期确认进入衰退
- 54K 已是巨大数字，但增长故事结束
- 对 Lobster 的启示：**不要做 Agent 框架**（赛道已饱和且 hype 退潮），**要做编排器/延续层**（蓝海）

### 🔥 发现四：20 years on AWS — 运维老兵的坚持

cperciva（FreeBSD 安全官）写了 "20 years on AWS and never not my job"，强调**持续运维的重要性**。

**对 Lobster 的共鸣**：
- "Never not my job" = 持续值守，正是 Lobster 解决的：让 Agent 24/7 存活
- Lobster 的价值主张："你睡觉时，Agent 还在工作"
- 可以将此作为 Lobster Manifesto 的故事线之一

---

## Step 3: 核心洞察

### 开源增长的 4 条铁律（R26 更新版）

| 铁律 | 证据 | Lobster 行动 |
|------|------|-------------|
| **1. 合法性 > 技术** | Linux 内核接纳 AI = 最高背书 | README 加 "Assisted-by 友好" |
| **2. 生态分发 > GitHub trending** | Superpowers 靠插件市场 | 做 ClawHub 技能 + 多平台分发 |
| **3. 叙事 > 代码** | karpathy-skills 12K⭐ 仅一个文件 | 写 Lobster Manifesto.md |
| **4. 解决痛点 > 炫技** | Superpowers 帮人赚钱 → 赞助 | Lobster 聚焦 "Agent 活下去" |

### Lobster 增长路线图更新

```
立即 (本周):
  ✅ 写 Lobster Manifesto.md — 单文件叙事，模仿 karpathy-skills
  ✅ README 加 "Assisted-by 友好" 章节
  ✅ README 加 "What Lobster Can't Do" — 透明度

短期 (2周):
  📋 做 ClawHub 技能分发（类似 Superpowers 的插件市场）
  📋 写 "AI 编排器 vs Agent 框架" 对比文章
  📋 在 HN 发 Show HN（等编译测试通过后）

中期 (1个月):
  📋 实现 Assisted-by 标签自动追踪
  📋 GitHub Sponsors 页面
  📋 社区贡献指南 (CONTRIBUTING.md)
```

---

## Step 4: 产出文件

- ✅ 研究总结: `knowledge_base/open-source-growth-2026-04-11-r26.md` (本文件)
- ✅ Lobster Manifesto 草稿: `memory/draft-lobster-manifesto-2026-04-11.md`
- ✅ Lobster README 更新建议: `memory/draft-readme-update-2026-04-11.md`

---

*研究轮次: #26*
*下次轮换: 技能市场 (04-13)*
