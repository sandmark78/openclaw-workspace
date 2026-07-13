# Python 3.15 JIT 编译器回归正轨

**创建时间**: 2026-03-18  
**来源**: HN #6 (356 points, 177 comments) + fidget-spinner.github.io  
**领域**: 01-ai-agent (AI/ML 基础设施)  
**数量**: 520

---

## 核心突破

CPython 3.15 的 JIT 编译器在经历挫折后重新回到正轨：
- **macOS AArch64**: 比尾调用解释器快 **11-12%**
- **x86_64 Linux**: 比标准解释器快 **5-6%**
- 实际范围：从 20% 慢到 100%+ 加速 (几何均值)
- 比原定目标 **提前一年多** 达成 macOS 目标

## 历史背景

### JIT 危机 (2025)
- CPython 3.13/3.14 的 JIT 几乎没有加速效果
- Faster CPython 团队失去主要赞助商资金
- JIT 的未来一度不确定

### 社区拯救模式
- Ken Jin 提出社区管理提案
- CPython 核心 sprint (剑桥) 制定计划：3.15 快 5%，3.16 快 10%
- 降低 bus factor：每个 JIT 阶段至少 2 个活跃维护者

## 关键成功因素

### 1. 任务分解策略
- 将 JIT 从不透明黑盒拆解为可管理的小任务
- 每个 PR 有清晰的输出指标
- "优化单条指令" 级别的任务粒度
- 11 位贡献者参与指令转换工作

### 2. Trace Recording 重写
- 将 JIT 前端重写为 tracing 模式
- 原型 3 天完成，但花了一个月才正确 JIT
- "spite-driven development" (为证明对方错误而开发)

### 3. 社区工程
- 鼓励每一个成就，无论大小
- 详细的贡献指南，让 C 程序员无需 JIT 经验即可贡献
- 核心团队：Savannah Ostrowski, Mark Shannon, Diego Russo, Brandt Bucher, Ken Jin

## 技术架构演进

```
3.13: 原始 copy-and-patch JIT → 几乎无加速
3.14: 优化尝试 → 仍然不理想
3.15: Trace recording + 社区优化 → 11-12% 加速
3.16: 目标 10%+ 加速 + free-threading 支持
```

## 对 AI Agent 的影响

1. **Python 性能提升**: AI/ML 生态核心语言的性能改善
2. **本地推理加速**: 更快的 Python = 更快的模型推理管道
3. **开源协作模式**: 社区驱动的核心基础设施改进范例
4. **free-threading**: 3.15/3.16 的 GIL-free + JIT = 并行 Agent 执行

## 关键教训

- **运气 + 对的人 + 对的时机** 缺一不可
- 分解复杂问题为可贡献的小任务是开源的核心方法论
- "spite-driven development" 有时能产生意想不到的好结果

---

*深度分析 | Cron #109 | 2026-03-18 08:02 UTC*
