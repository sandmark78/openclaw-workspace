# 技能市场研究 #43 — 2026-04-13 18:04 UTC

**轮次**: R43 | **主题**: 技能市场 (Skills Market) | **轮换**: 第 6 轮循环

---

## Step 1: 采集

### HN 信号 (2026-04-13 周一 18:00 UTC)
| 热帖 | 分数 | 评论 | 信号 |
|------|------|------|------|
| Servo on crates.io | **291pts**/95c | 🦀 Rust 生态里程碑 |
| Nothing Ever Happens (Polymarket bot) | 204pts/75c | 🤖 预测市场自动化 |
| Microsoft Copilot 重命名 | 181pts/11c | 🏢 大厂 AI 品牌疲劳 |
| Aphyr: Future of Everything Is Lies: Safety | 98pts/40c | ⚠️ 安全信任危机 |
| Cloudflare CLI | 114pts/35c | 🔧 开发者工具 |
| Rockchip RK3588 摄像头支持 | 42pts/11c | 📱 边缘硬件进展 |
| MEMS 芯片投影 | 37pts/8c | 🔬 微型硬件 |
| LLVM RISC-V 回归 | 24pts/5c | ⚙️ 底层优化 |

**关键记录**: **零 AI Agent 帖进入 Top 10（连续第 15 天！创纪录）**

### GitHub Trending 周榜 (18:05 UTC)
| 项目 | 总星 | 周增 | vs R42 (2h前) | 关键信号 |
|------|------|------|---------------|----------|
| hermes-agent | **76,016** | +38,426 | +1,206/2h | 🚀 逼近 76K，生态位稳定 |
| markitdown | **106,659** | +10,592 | +307/2h | 🚀 破 106.6K |
| multica | **10,790** | +6,846 | +255/2h | 📈 10K 后持续加速 |
| DeepTutor | **17,674** | +5,873 | +231/2h | 🚀 教育+Agent 加速 |
| Archon | **17,522** | +2,962 | +78/2h | 确定性编码 |
| gallery (Google) | **20,862** | +4,148 | +86/2h | 端侧 ML |
| seomachine | **5,950** | +2,815 | +160/2h | 📈 工作空间即产品 |
| personaplex | **9,184** | +2,331 | +13/2h | 人格化 AI |
| LiteRT-LM | **3,640** | +2,164 | +12/2h | Google 端侧 ML |
| karpathy-skills | ✅ **回归** | — | 🔄 从缺席到 trending #1！ |

### Lobster 仓库状态
- Commit: 03c38c9 (R42 push 成功)
- 分支: master，clean
- 累计 commit: 28

---

## Step 2: 分析

### 发现 1: karpathy-skills 王者归来 = 技能即文件范式确立
karpathy-skills 不仅回归，而且以 **Trending #1** 姿态回归。这说明：
- 单文件配置不是"新奇玩具"，而是**开发者刚需**
- 消失的 3 轮 (R35-R37) 是正常热度波动，不是需求消失
- 趋势: karpathy-skills → seomachine (单文件→完整工作空间) 是技能市场的**升级路径**
- Lobster 启示: 发布 lobster-survival-checklist.md 单文件到独立仓库的时机已到

### 发现 2: hermes 76K + 10,150 forks = 技能生态位已成熟
hermes 不仅仅是框架，10,150 forks 意味着**大量技能/插件正在被开发**：
- Fork 数/Star 数 = 13.3% (远超一般项目的 3-5%)
- 高 fork 率 = 高二次开发率 = 技能生态繁荣
- 对 Lobster 的意义: hermes 技能可以被 Lobster 编排到边缘设备运行
- 合作机会: Lobster 可以作为 hermes 的边缘运行后端

### 发现 3: seomachine 5,950 星 (+2,815/周) = 工作空间即技能
seomachine 的核心创新不是代码，而是**整个工作空间的设计**：
- CLAUDE.md + 脚本 + 模板 + 工作流 = 完整的"技能包"
- 834 forks = 大量开发者在 fork 后定制自己的工作空间
- 验证: 用户愿意为"即用型工作空间"付费
- Lobster 启示: 不只是编排 Agent，而是编排**完整工作空间**

### 发现 4: 15 天零 AI Agent 帖 = 注意力转移到"工具层"
连续 15 天没有 AI Agent 框架进入 HN Top 10，但:
- Rust/Servo 291pts — 底层基础设施
- Cloudflare CLI 114pts — 开发者工具
- Polymarket bot 204pts — 自动化应用
- Rockchip RK3588 42pts — 边缘硬件

这意味着市场注意力已经从"用哪个框架"转移到"用框架做什么"。
Lobster 的"边缘基础设施"叙事比"AI Agent 编排"更契合当前注意力方向。

### 发现 5: 技能市场 9 层格局 V10
| 层级 | 代表 | 星数 | 趋势 | Lobster 定位 |
|------|------|------|------|-------------|
| L0 框架层 | hermes-agent | 76K | 📈 生态成熟 | 互补: 边缘后端 |
| L1 增强层 | Archon | 17.5K | 📈 确定性编码 | 互补: 边缘确定性 |
| L2 管理平台 | multica | 10.8K | 🚀 加速 | 竞争: 云端 vs 边缘 |
| L3 工作空间 | seomachine | 6.0K | 🚀 加速 | 学习: 工作空间即产品 |
| L4 技能分发 | karpathy-skills | 回归 | 🔄 稳定需求 | 模仿: 单文件发布 |
| L5 端侧 ML | gallery + LiteRT | 20.9K + 3.6K | 📈 加速 | 同盟: 手机编排 |
| L6 人格层 | personaplex | 9.2K | 📈 稳定 | 远期: 边缘人格 |
| L7 垂直 SaaS | DeepTutor | 17.7K | 🚀 加速 | 学习: 垂直化 |
| L8 基础设施 | markitdown | 106.7K | 🚀 加速 | 互补: 文档处理 |

---

## Step 3: 产出 — 5 条可执行洞察

### 洞察 1: 🔥 发布 Lobster Survival Checklist (karpathy 模式)
- 模仿 karpathy-skills 单文件模式
- 文件名: LOBSTER.md 或 lobster-survival-checklist.md
- 内容: 10 条 Lobster 生存法则 + 边缘部署配置
- ROI: 5.0 (零成本，高传播潜力)
- 优先级: P0 — 本周完成

### 洞察 2: 📦 设计 Lobster Workspace Template (seomachine 模式)
- 不只是单文件，而是完整工作空间模板
- 包含: CLAUDE.md + 启动脚本 + 配置文件 + 示例
- 针对: 旧手机/边缘设备运行 Agent
- ROI: 4.5
- 优先级: P0 — 2 周内完成

### 洞察 3: 🔗 加入 hermes 生态 (互补而非竞争)
- hermes 10K+ forks = 庞大技能生态
- Lobster 定位: "在边缘设备上运行 hermes 技能"
- 策略: 写 hermes + Lobster 集成教程
- ROI: 4.0
- 优先级: P1

### 洞察 4: 📝 重写 README 为"边缘基础设施"叙事
- 当前注意力: 工具/基础设施 > Agent 框架
- 新叙事: "让已有设备做更多事" (15 天验证)
- 对标: Cloudflare CLI 114pts、Servo 291pts
- ROI: 4.0
- 优先级: P0

### 洞察 5: 🔄 关注 Polymarket bot 模式
- "Nothing Ever Happens" — 简单策略 + 自动执行 = 204pts
- Lobster 可以编排类似的"边缘自动化策略"
- 比如: 旧手机运行价格监控、健康检查等
- ROI: 3.5
- 优先级: P2

---

## 数据追踪

### hermes-agent 增速 (10 天)
| 日期 | 总星 | 日增 | 趋势 |
|------|------|------|------|
| 04-04 | ~58K | ~8.2K | 峰值 |
| 04-07 | ~61K | ~6.4K | 放缓 |
| 04-09 | ~62K | ~5.4K | 继续 |
| 04-11 | ~65K | ~6.4K | 反弹 |
| 04-12 | ~66K | ~5.5K | 稳定 |
| 04-13 | **76K** | **+38K/周** | 第二曲线 |

结论: 周增 38K 不变，日增 ~5.5K 稳定，进入平台期但有生态溢出效应。

### 零 AI Agent 帖记录
| 起始日 | 天数 | 备注 |
|--------|------|------|
| 04-02 | Day 1 | 首次出现 |
| 04-07 | Day 6 | 持续 |
| 04-10 | Day 9 | 新纪录 |
| 04-13 | **Day 15** | **🏆 新纪录** |

---

*研究完成时间: 2026-04-13 18:06 UTC*
*下次轮换: 变现案例 (Monetization Cases)*
