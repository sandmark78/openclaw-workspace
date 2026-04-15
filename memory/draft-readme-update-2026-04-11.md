# Lobster README 更新建议 — 2026-04-11

基于 R26 开源增长研究的 README 更新建议。

## 更新 1: 加 "Assisted-by 友好" 章节

在 Features 部分新增：

```markdown
### 🏷️ Assisted-by 友好

遵循 Linux 内核 AI 协作规范，Lobster 原生支持 AI 贡献追踪：

- 每个实例自动记录 `Assisted-by: Lobster:V0.5.0` 标签
- 人类监督链：每个决策都可追溯到操作者
- AI 不自签认证：严格遵守 "只有人类可以 DCO 签名" 原则
```

**理由**: Linux 内核刚刚 (2026-04-11) 正式接纳 AI 编码助手，这是行业最高背书。Lobster 作为编排器，天然适合做合规的 AI 协作平台。

## 更新 2: 加 "What We Can't Do" 章节

```markdown
## What We Can't Do (Yet)

我们相信透明度是最好的增长策略：

- ❌ 自动跨设备同步（当前仅支持单机）
- ❌ 崩溃自动恢复（需手动重启实例）
- ❌ 全平台编译测试（CI/CD 待建设）
- ❌ 企业级 SSO（这是 side project）

我们知道问题在哪。我们正在修。
```

**理由**: 模仿 nuwa-skill 和 mempalace 的透明度策略，建立信任。

## 更新 3: 加 Lobster Manifesto 链接

在 README 顶部加入：

```markdown
> 📜 [Read The Undying Lobster Manifesto](docs/MANIFESTO.md)
> *"An agent that forgets is not an agent. It's a calculator."*
```

**理由**: 模仿 karpathy-skills 的单文件叙事策略，一个好故事比一堆代码传播更快。

## 更新 4: 加竞品对比表

```markdown
## Lobster vs Others

| | Lobster | hermes-agent | rowboat | Archon |
|---|---------|-------------|---------|--------|
| 定位 | 编排器 | Agent 框架 | AI 同事 | 编码 harness |
| 多实例 | ✅ 50+ | ❌ 单实例 | ❌ 单实例 | ❌ 单实例 |
| 旧设备 | ✅ 支持 | ❌ 需要 GPU | ❌ 云端 | ❌ 云端 |
| 延续层 | L1-L4 | L1 仅 | L1-L2 | N/A |
| Assisted-by | ✅ 原生 | ❌ | ❌ | ❌ |
| 开源 | ✅ MIT | ✅ Apache | ✅ MIT | ✅ MIT |
```

---

*建议直接更新 README.md 后 push 到 GitHub*
