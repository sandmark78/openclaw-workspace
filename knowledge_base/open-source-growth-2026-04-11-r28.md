# 开源增长分析 #28 — 开源增长的 5 条铁律

**日期**: 2026-04-11 16:04 UTC  
**轮次**: 开源增长 (第 3 轮)  
**数据来源**: HN 首页 + GitHub Trending 周榜 + 深度分析

---

## 一、本周 GitHub 增长数据总览

| 项目 | 总星 | 周增 | 语言 | 增长类型 |
|------|------|------|------|----------|
| hermes-agent | 57,309 | +26,783 | Python | 框架层 (饱和中) |
| openscreen | 27,963 | +10,077 | TypeScript | 免费替代病毒增长 |
| markitdown | 101,434 | +5,214 | Python | 大厂开源获客 |
| DeepTutor | 16,521 | +4,698 | Python | 垂直领域蓝海 |
| google-ai-edge/gallery | 20,383 | +4,409 | Kotlin | 端侧 AI 展示 |
| andrej-karpathy-skills | 12,700 | +3,741 | 配置 | 叙事驱动增长 |
| multica | 7,384 | +3,512 | TypeScript | Managed agents |
| NVIDIA personaplex | 8,989 | +2,939 | Python | 大厂研究项目 |
| seomachine | 5,628 | +2,526 | Python | 工作空间即产品 |
| google-ai-edge/LiteRT-LM | 3,385 | +2,210 | C++ | 端侧推理引擎 |
| goose | 41,120 | +6,428 | Rust | 可执行 Agent |

### 关键增速变化
- **hermes-agent**: 连续 5 周追踪，本周 +26,783 (日均 3,826)，较上周峰值日增 6,437 有所回落，但周总量仍在加速
- **openscreen**: 周增 10K 的恐怖增速，证明"免费替代收费产品"是最强增长引擎
- **goose**: 稳定增长中，Rust 实现的 AI agent 正在追赶 hermes

---

## 二、HN 热点与开源增长的 5 条铁律

### 铁律 1: 免费替代 = 病毒式增长 ⭐⭐⭐⭐⭐
**证据**: openscreen 一周 10K 星 (Screen Studio 的免费替代)

Screen Studio 是 $29 的付费录屏工具。openscreen 做了同样的事，但开源免费，结果一周涨 10K 星。

**增长率公式**: 
```
增长率 ∝ (替代品价格 × 替代品用户基数) / 实现难度
```
- 替代品越贵 → 免费替代越有吸引力
- 用户基数越大 → 潜在转化越多
- 实现难度越低 → 竞争越激烈

**Lobster 启示**: 目前边缘设备编排没有"收费产品"可替代，但 VPS 托管 ($5-50/月) 是一个可以打的痛点。

### 铁律 2: 叙事 > 代码 ⭐⭐⭐⭐⭐
**证据**: andrej-karpathy-skills 12,700⭐, 一个 CLAUDE.md 文件

一个配置文件，借 Karpathy 的名气 + "LLM 编程陷阱"的叙事，一周涨 3,741 星。

**叙事公式**:
```
传播力 = (名人效应 × 痛点共鸣) / 认知门槛
```
- 名人背书 = 免费注意力
- 痛点共鸣 = "我也遇到过"
- 认知门槛低 = 人人都能看懂

**Lobster 启示**: 需要一份更强的"不死宣言" (Manifesto)，把"旧手机跑 Agent"的故事讲好。

### 铁律 3: 大厂收购 = 人才战，不是产品战 ⭐⭐⭐⭐
**证据**: OpenAI 收购 Cirrus Labs (115 pts, 46 评论)

Cirrus CI 将在 2026-06-01 关闭。OpenAI 买的是 Tart (macOS 虚拟机方案) 的技术团队，用于增强 Codex 的云端执行环境。

HN 评论精华:
> "Everyone ran out to buy Mac Minis last month to give their Agent access to iMessage, browser cookies, and residential IP. Cirrus provides a way to provision and orchestrate MacOS VMs."
> "If you want your career to progress, start a tiny startup and hope to be notable enough to get acquired by OpenAI or Anthropic."

**Lobster 启示**: 
1. 边缘设备编排 (Mac Mini 集群、旧手机编排) 正是 OpenAI 需要的能力
2. Lobster 的定位恰好契合"人才收购"赛道
3. 但要先做出足够大的用户基数才能被看到

### 铁律 4: 垂直场景 > 通用框架 ⭐⭐⭐⭐
**证据**: seomachine 5,628⭐ (+2,526/周), DeepTutor 16,521⭐ (+4,698/周)

- seomachine: 不是通用 agent，是专门做 SEO 内容的工作空间
- DeepTutor: 不是通用教育平台，是 Agent 驱动的个性化学习助手

**垂直化公式**:
```
垂直产品价值 = (通用能力 - 通用复杂性) × 领域深度
```

**Lobster 启示**: Lobster 不应该定位为"通用编排器"，而应该定位为"旧手机/边缘设备 Agent 部署工具"——越窄越深越好。

### 铁律 5: 单文件病毒传播 ⭐⭐⭐
**证据**: Starfling (386 pts) 和 1D Chess (905 pts) 都是单 HTML 文件

HN 上最受欢迎的帖子之一是一个单 HTML 文件的无尽轨道弹射游戏。另一个是 1D 国际象棋，也是一个 HTML 文件。

**极简传播公式**:
```
传播力 ∝ 1 / (打开成本 × 理解成本)
```
单文件 = 零打开成本。点击即玩。

**Lobster 启示**: 如果能做一个"一行命令部署 Lobster"的 demo 页面或交互演示，传播力会大增。

---

## 三、Lobster 开源增长路线图

### 本周可做 (零成本)
1. ✅ 写好"旧手机省 $50"虾聊帖子 (已有草稿)
2. 🔄 创建 Lobster Manifesto (不死宣言)
3. 🔄 在 GitHub README 加"一行命令"快速开始

### 本月可做 (低成本)
1. 做一个在线交互 demo (单 HTML 页面)
2. 写"边缘设备 Agent 编排"的技术博客
3. 在 HN 发 Show HN (需要 Lobster 编译测试通过)

### 本季度可做 (中成本)
1. 开源 Lobster 配置模板市场 (参考 seomachine)
2. 建立边缘设备兼容矩阵 (树莓派/旧手机/NAS/路由器)
3. 社区贡献者计划 (参考 hermes 的 Discord 社区)

---

## 四、竞品增长追踪

| 竞品 | 上周星 | 本周星 | 周增 | 增速变化 | Lobster 应对 |
|------|--------|--------|------|----------|-------------|
| hermes-agent | ~47,600 | 57,309 | +9,709 | ↑ 加速 | 差异化: 边缘设备编排 |
| openscreen | ~17,886 | 27,963 | +10,077 | ↑↑ 爆炸 | 学习: 免费替代策略 |
| goose | ~34,692 | 41,120 | +6,428 | → 稳定 | 关注: Rust 生态 |
| multica | ~3,872 | 7,384 | +3,512 | ↑↑ 加速 | 警惕: managed agents |
| seomachine | ~3,102 | 5,628 | +2,526 | ↑ 加速 | 学习: 垂直场景 |

---

## 五、核心结论

1. **开源增长的核心公式: 痛点 × 免费 × 叙事**
2. **hermes 虽然 57K 星，但赛道已饱和** — 边缘编排仍是蓝海
3. **OpenAI 收购 Cirrus 证明: 编排能力是 AI 巨头的刚需**
4. **Lobster 的增长机会在"窄而深"** — 专注边缘设备，别做通用编排
5. **一句话 demo > 复杂文档** — 降低认知门槛，让 5 岁小孩也能看懂 Lobster 在干什么

---

*产出: 1 文件, ~3,800 bytes*
*下次研究轮换: 竞品分析*
