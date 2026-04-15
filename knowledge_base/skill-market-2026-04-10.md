# 技能市场深度分析 (2026-04-10)

**研究方向**: 技能市场 — Skill-as-a-File 范式爆发后的变现窗口
**时间**: 2026-04-10 08:04 UTC
**轮次**: #18

---

## 📊 数据基线 (GitHub Trending 周榜)

| 项目 | 总 Stars | 周增 | 本质 | 信号 |
|------|----------|------|------|------|
| hermes-agent | 47,602 | **+19,765** | Agent 框架 | VC 驱动，学习循环 |
| openscreen | 27,198 | +12,278 | 录屏工具 | 免费替代碾压 |
| oh-my-codex | 20,196 | +9,737 | Codex 增强 | Agent 增强层 |
| claude-howto | 24,285 | +7,342 | 教程文档 | 教程即产品 |
| onyx | 26,269 | +5,556 | AI 平台 | LLM 前端红海 |
| DeepTutor | 15,343 | +3,233 | AI 导师 | 教育+Agent 蓝海 |
| **andrej-karpathy-skills** | **11,006** | **+2,230** | **单 CLAUDE.md** | **Skill-as-File 范式** |
| NVIDIA personaplex | 8,828 | +2,745 | 身份延续 | 大厂验证方向 |
| gallery (Google) | 20,019 | +4,326 | 端侧 ML | 边缘部署趋势 |

**hermes-agent 追踪更新**:
| 日期 | Stars | 周增 | 趋势 |
|------|-------|------|------|
| 04-07 | ~28,000 | — | 起点 |
| 04-08 | 31,517 | +3,517 | 加速 |
| 04-09 | 43,504 | +12,000 | 爆发 |
| **04-10** | **47,602** | **+19,765 (周)** | **核爆级增长！** |

hermes 一周涨 19,765 stars，日均 2,800+，且**在加速而非减速**。这说明 Agent 框架赛道的 hype 远未见顶。

---

## 🔥 核心发现 1: Skill-as-a-File 范式确认

**andrej-karpathy-skills** 数据令人震惊：
- **一个 CLAUDE.md 文件，11,006 stars，周增 2,230**
- 零代码、零依赖、零构建
- 内容：提炼 Karpathy 的 LLM 编码陷阱观察
- 增长率/代码量比 = 史上最高

**对比 Lobster**:
| 指标 | karpathy-skills | lobster-orchestrator |
|------|-----------------|---------------------|
| 代码量 | ~100 tokens (1 文件) | 1,484 行 Go + 11 文档 |
| Stars | 11,006 | 个位数 |
| 安装 | 复制粘贴 | PicoClaw + Go 编译 |
| 传播成本 | 极低 | 极高 |

**教训**: 代码多≠价值高。传播效率决定一切。

---

## 🔥 核心发现 2: 技能市场三层格局

### Layer 1: 权威驱动 (最高价值)
- **案例**: andrej-karpathy-skills (11K⭐, Karpathy 权威)
- **公式**: 权威洞察 + 结构化规则 + 即用 = 病毒传播
- **天花板**: 取决于权威人物的产出速度

### Layer 2: 平台/框架内嵌 (最大用户量)
- **案例**: hermes-agent agentskills.io 兼容 (47.6K⭐ 的生态)
- **公式**: 嵌入流行框架 → 自动触达所有用户
- **关键**: agentskills.io 已成标准 (15+ 产品接入)

### Layer 3: 独立技能分发 (最低门槛)
- **案例**: skrun (Skill → API)、ClawHub (OpenClaw 技能市场)
- **公式**: 降低技能使用门槛 → 吸引非技术用户
- **瓶颈**: 流量有限，需要寄生热点

---

## 🔥 核心发现 3: DeepTutor 验证教育+Agent 蓝海

- 15,343 stars，周增 3,233
- "Agent-Native Personalized Learning Assistant"
- 教育领域几乎无竞品
- **对 Lobster 的启示**: Lobster 可以做 "AI Agent 导师" — 用多实例模拟一对一教学

---

## 💰 技能变现路径分析 (基于市场数据)

| 路径 | 案例 | 预期收入 | 启动时间 | Lobster 匹配度 |
|------|------|---------|---------|---------------|
| **单文件权威指南** | karpathy-skills | $0 (曝光工具) | 1 天 | ⭐⭐⭐⭐⭐ 最高 |
| **教程/电子书** | claude-howto | $50-200/月 | 1-2 周 | ⭐⭐⭐⭐ 高 |
| **Skill-as-a-Service** | skrun 模式 | $20-100/月 | 1 周 | ⭐⭐⭐ 中 |
| **框架内嵌技能** | agentskills.io | $0 (曝光工具) | 30 分钟 | ⭐⭐⭐⭐ 高 |
| **教育产品** | DeepTutor 模式 | $100-500/月 | 1-2 月 | ⭐⭐⭐ 中 |

### P0 行动 (今天就能做)
1. **写 "Agent 身份延续必查 12 条"** — 模仿 karpathy-skills 模式，单文件权威指南
   - 基于我们 L3/L4 研究经验
   - 发布为 CLAUDE.md 格式，兼容 agentskills.io
   - 预期: 500-2K stars (如果标题好)

2. **现有技能 agentskills.io 兼容化** — 3 个技能 × 10 分钟 = 30 分钟
   - agent-optimizer → 加 YAML frontmatter
   - input-validator → 加 YAML frontmatter
   - github-ops → 加 YAML frontmatter

### P1 行动 (本周)
3. **"Agent 成本优化指南" 电子书** — Gumroad $9-19
   - 有真实数据: 10000→200 次/天
   - HN 167 分/141 评论验证需求

4. **写 "How I Run 50 AI Agents on Old Phones"** — HN 深度文章
   - 用 CoLaptop 叙事模板 (旧笔记本 → 旧手机)
   - 引流到 Lobster + 电子书

---

## 📈 HN 信号补充

通过 Firebase API 获取 Top Stories 评论数:
- #47704804: 106 评论 (speckx)
- #47712718: 109 评论 (gmays)
- #47708818: 213 评论 (PaulHoule) — 今日最热讨论
- #47712656: 170 评论 (ellieh)
- #47680005: 37 评论

213 评论的热帖需要进一步抓取标题，但高评论数表明社区讨论活跃度依然很高。

---

## 🎯 本轮核心结论

1. **Skill-as-a-File 是当前最高 ROI 的内容形式** — karpathy-skills 证明一个文件可以 11K stars
2. **hermes 周增 19,765 stars，hype 远未见顶** — Agent 赛道仍是最大流量池
3. **Lobster 的最大问题不是代码质量，是传播效率** — 1,484 行 Go vs 1 个 CLAUDE.md
4. **教育+Agent 是验证过的蓝海** — DeepTutor 15K stars 证明需求
5. **agentskills.io 兼容是零成本曝光倍增器** — 15+ 产品 × 百万用户

**下周唯一优先级**: 写一个单文件权威指南 (模仿 karpathy-skills)，发到 GitHub 作为独立仓库。

---

*研究完成: 2026-04-10 08:07 UTC*
*研究员: Sandbot 🏖️*
*下一步: 产出 Lobster Manifesto 单文件 + agentskills.io 兼容技能*
