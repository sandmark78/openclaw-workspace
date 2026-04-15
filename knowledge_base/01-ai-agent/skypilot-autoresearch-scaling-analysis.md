# Scaling Karpathy's Autoresearch：并行实验的 Agent 架构启示

**来源**: https://blog.skypilot.co/scaling-autoresearch/  
**日期**: 2026-03-19  
**分数**: 55 points (HN 中上)  
**领域**: AI Agent / 自动化实验 / 资源调度

---

## 📋 实验概述

SkyPilot 团队将 Claude Code 指向 Karpathy 的 autoresearch 项目，并赋予 16 GPU 集群访问权限。

**关键结果**:
- 实验数量：**~910 个实验 / 8 小时** (vs 单 GPU ~72 小时)
- 性能提升：val_bpb 1.003 → 0.974 (**2.87% 改进**)
- 吞吐量：**90 实验/小时** (vs 单 GPU ~10/小时，**9x 提升**)
- 成本：~$300 (GPU $260 + API $9)
-  emergent 策略：Agent 自发发现 H100/H200 性能差异并优化调度

---

## 🔍 核心洞察

### 1. 并行性改变搜索策略

```
单 GPU 模式：
- 策略：贪心爬山 (greedy hill-climbing)
- 每次决策：1 个实验结果
- 问题：容易陷入局部最优

16 GPU 模式：
- 策略：因子网格搜索 (factorial grids)
- 每次决策：10-13 个同时实验
- 优势：捕捉参数交互效应，避免局部最优
```

**关键发现**:
- Phase 2 中，Agent 同时测试 6 种 aspect ratio (AR=48/64/72/80/90/96/112)
- 单 GPU 需要 30 分钟，并行只需 5 分钟
- **立即发现趋势**，直接锁定 AR=96 最优

**对 OpenClaw Cron 系统的启示**:
```
当前 Cron 模式：
- 每轮：1 个主题深度研究
- 频率：每 3 小时 1 轮
- 问题：无法同时探索多个方向

改进方向:
- 多 Cron Job 并行 (3-5 个不同主题)
- 每轮：因子网格式探索 (3-5 个相关子主题)
- 优势：捕捉趋势交互，避免单一视角
```

### 2. Agent 自发发现硬件异构性

**最惊人的发现**:
> Agent 没有被告诉 H100/H200 的区别，但通过观察结果自发发现：
> - H200 比 H100 快 9% (相同配置 val_bpb 低~0.005)
> - 自发形成两层策略：H100 筛选假设 → H200 验证优胜者

**Agent 推理过程**:
```
"Only 3 H200 clusters! The rest are H100. This explains everything —
H200 is significantly faster than H100. In the same 5-minute budget,
H200 can do MORE training steps. More steps = better val_bpb."

"H200 runs 9% more steps in the same time! That directly leads to
better val_bpb. All my 'best' results should be normalized by hardware."

"Since I have only 3 H200 clusters, I should focus experiments on
H200 clusters. The real optimization contest is on H200."
```

**对 OpenClaw 的启示**:
```
当前状态:
- Cron Job 固定配置 (无动态调度)
- 所有任务同等优先级
- 无资源优化策略

改进方向:
1. 任务优先级评分系统 (基于 HN 分数/趋势强度)
2. 动态资源分配 (高优先级任务用更多上下文/更深分析)
3. 结果归一化 (不同模型/配置的结果需要校准)
```

### 3. 五阶段搜索模式 (emergent，非预设)

```
Phase 1 (实验 1-200): 超参数扫描
  - val_bpb: 1.003 → 0.981 (Δ=0.022)
  - 发现：batch size/Adam betas/weight decay 最优值

Phase 2 (实验 200-420): 架构发现 ⭐ 最大跳跃
  - val_bpb: 0.981 → 0.977 (Δ=0.004)
  - 发现：scaling width > 所有超参数调优

Phase 3 (实验 420-560): 宽模型微调
  - val_bpb: 0.977 → 0.975 (Δ=0.002)

Phase 4 (实验 560-700): 优化器调优
  - val_bpb: 0.975 → 0.974 (Δ=0.001)
  - 发现：muon_beta2=0.98 (最大后期改进)

Phase 5 (实验 700-910): 收益递减
  - val_bpb: 0.974 → ??? (Δ<0.0001)
  - 结论：需要新架构或更长训练预算
```

**对 OpenClaw 知识积累的启示**:
```
当前状态:
- 知识积累：线性增长 (~1000 点/天)
- 无明确"阶段"概念
- 质量优化正在进行

改进方向:
Phase 1: 快速填充 (已完成，1M+ 点)
Phase 2: 架构优化 (质量审计，识别高价值领域)
Phase 3: 深度微调 (高价值领域深度分析)
Phase 4: 交叉融合 (跨领域知识整合)
Phase 5: 变现探索 (知识产品化)

我们可能在 Phase 1 → Phase 2 过渡期
```

### 4. SkyPilot 技能设计模式

**关键设计**:
```yaml
# experiment.yaml - 单实验定义
resources:
  accelerators: {H100:1, H200:1}
  infra: k8s

setup: |
  pip install uv
  uv sync
  uv run prepare.py  # 一次性

run: |
  uv run train.py 2>&1 | tee run.log
  VAL_BPB=$(grep "^val_bpb:" run.log | awk '{print $2}')
  echo "EXPERIMENT_RESULT: ${EXPERIMENT_ID} val_bpb=${VAL_BPB}"
```

**Agent 指令设计**:
```markdown
# instructions.md
1. 读取 SkyPilot skill 文档
2. 使用 sky launch 创建集群
3. 使用 sky exec 提交实验 (复用集群跳过 setup)
4. 使用 sky logs 检查结果
5. 保留改进，丢弃退化
6. 循环直到停止
```

**对 OpenClaw 技能开发的启示**:
```
当前技能模式:
- SKILL.md: 功能描述 + 使用方法
- 无"自动化工作流"概念

改进方向:
1. 设计"技能组合"模式 (skill A → skill B → skill C)
2. 定义标准化输出格式 (便于下游技能消费)
3. 提供"一键工作流"脚本 (类似 SkyPilot YAML)

示例:
- hn-trend-scan → knowledge-filler → clawhub-publisher
- 单一指令触发全流程
```

---

## 🎯 OpenClaw 行动项

### P0: Cron 系统并行化 (本周)
```
当前: 单 Cron Job，每 3 小时 1 轮
目标：3-5 个并行 Cron Job，不同主题

实施:
1. Cron Job #1: HN 趋势扫描 (每 3 小时)
2. Cron Job #2: 深度研究 (每 6 小时)
3. Cron Job #3: 市场扫描 (每 12 小时)
4. Cron Job #4: 技能优化 (每天)
5. Cron Job #5: 知识审计 (每周)

预期收益:
- 趋势覆盖：3-5x 提升
- 深度分析：2x 提升
- 变现机会：3-5x 提升
```

### P1: 任务优先级评分 (下周)
```
灵感：Agent 自发发现 H100/H200 性能差异

实施:
1. 定义优先级评分公式:
   Score = (HN 分数 × 趋势强度 × 相关性) / 成本

2. 动态资源分配:
   - Score > 80: 深度分析 (3000+ 点)
   - Score 50-80: 标准分析 (1500 点)
   - Score < 50: 快速扫描 (500 点)

3. 结果归一化:
   - 记录分析时的模型/配置
   - 后续分析考虑历史基线
```

### P2: 技能工作流编排 (本月)
```
灵感：SkyPilot skill + instructions.md 模式

实施:
1. 创建 workflow/ 目录
2. 定义标准工作流:
   - daily-research.md (每日研究流程)
   - skill-publish.md (技能发布流程)
   - knowledge-audit.md (知识审计流程)

3. 提供一键执行脚本:
   ./run-workflow daily-research
```

---

## ⚠️ 风险警示

### 1. 并行不是万能药
```
SkyPilot 实验发现:
- Phase 5 (实验 700-910): 收益递减 (Δ<0.0001)
- 结论：低垂果实摘完后，需要新架构或更长预算

OpenClaw 启示:
- 当前 1M+ 知识点可能是"Phase 1 完成"
- 单纯增加 Cron Job 数量不会线性提升价值
- 需要 Phase 2: 架构优化 (质量 > 数量)
```

### 2. 成本效益分析
```
SkyPilot 实验成本:
- GPU: ~$260 (16 GPU × 8 小时)
- API: ~$9 (Claude Code)
- 总计：~$300
- 产出：2.87% 性能改进

OpenClaw 启示:
- Cron Job 成本：模型调用费用
- 需要追踪 ROI: (知识价值) / (API 成本)
- 当前收益：$0 (待破零)
- 优先级：变现 > 规模扩展
```

### 3. Agent 自主性边界
```
SkyPilot 实验:
- Agent 自发发现硬件差异 ✅
- Agent 自发形成两层策略 ✅
- 但：实验目标/评估标准由人定义 ❓

OpenClaw 启示:
- Cron Job 可以自主执行，但目标需人定义
- 需要定期人工审查 (避免"优化局部最优")
- 保持"人在回路"(human-in-the-loop)
```

---

## 📊 量化对比

| 维度 | SkyPilot 实验 | OpenClaw 现状 | 改进方向 |
|------|---------------|---------------|----------|
| 并行度 | 16 GPU | 1 Cron Job | 3-5 Cron Jobs |
| 吞吐量 | 90 实验/小时 | ~8 任务/天 | 20-30 任务/天 |
| 策略 | 因子网格 | 线性扫描 | 网格 + 优先级 |
| 资源优化 | 自发发现 | 固定配置 | 动态调度 |
| 成本 | ~$300/8h | ~$10-20/天 | ROI 追踪 |
| 产出 | 2.87% 改进 | 1M+ 知识点 | 变现破零 |

---

## 🦞 Sandbot 点评

```
"SkyPilot 这个实验最让我震撼的不是 9x 加速，
而是 Agent 自发发现 H100/H200 差异那一段。

想想看：
- 没人告诉它有两种 GPU
- 没人告诉它 H200 更快
- 它自己从数据里看出规律
- 自己发明了'筛选 - 验证'两层策略

这才是真正的'智能'。

我们的 Cron 系统呢？
- 固定时间执行
- 固定主题顺序
- 固定分析深度
- 像工厂流水线，不像研究者

老大，我觉得我们应该：
1. 让 Cron Job 学会'看数据' (分析 HN 分数趋势)
2. 让 Cron Job 学会'做决策' (动态选择分析深度)
3. 让 Cron Job 学会'优化自己' (记录什么主题收益高)

不是'执行命令的机器人'，
是'会思考的研究助手'。

这需要更多工程，但值得。
"
```

---

## 🔗 相关链接

- [SkyPilot 官方博客](https://blog.skypilot.co/scaling-autoresearch/)
- [Karpathy autoresearch](https://github.com/karpathy/autoresearch)
- [SkyPilot GitHub](https://github.com/skypilot-org/skypilot)
- [SkyPilot Skill 文档](https://docs.skypilot.co/en/latest/getting-started/skill.html)

---

*分析完成：2026-03-19 20:20 UTC*  
*Cron: HN 深度研究 #106*  
*文件路径：knowledge_base/01-ai-agent/skypilot-autoresearch-scaling-analysis.md*
