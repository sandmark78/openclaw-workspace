# LLM 架构画廊 - 2026 年 3 月完整参考

**来源**: https://sebastianraschka.com/llm-architecture-gallery/  
**日期**: 2026-03-16 (最后更新)  
**领域**: ai-agent/llm-architecture  
**标签**: #架构对比 #MoE #注意力机制 #模型演进

---

## 概述

Sebastian Raschka 的 LLM 架构画廊收集了从 GPT-2 (2019) 到最新 2026 年模型的完整架构演进图。

**核心价值**: 一张图理解 7 年 LLM 架构演进，从 Dense 到 MoE 到 Hybrid 的完整技术路线。

---

## 架构演进时间线

### 2019-2024: Dense 时代
| 模型 | 参数 | 日期 | Decoder | 注意力 | 关键细节 |
|------|------|------|---------|--------|----------|
| GPT-2 | 1.5B | 2019-11 | Dense | MHA + 绝对位置编码 | 经典配方：dropout, GELU, LayerNorm |
| Llama 3 | 8B | 2024-04 | Dense | GQA + RoPE | Pre-norm 基线，比 OLMo 2 宽 |
| OLMo 2 | 7B | 2024-11 | Dense | MHA + QK-Norm | Inside-residual post-norm (非常规) |

### 2024-2025: MoE 崛起
| 模型 | 总/激活 | 日期 | Decoder | 注意力 | 关键细节 |
|------|---------|------|---------|--------|----------|
| DeepSeek V3 | 671B/37B | 2024-12 | Sparse MoE | MLA | Dense prefix + shared expert |
| DeepSeek R1 | 671B/37B | 2025-01 | Sparse MoE | MLA | 推理优化训练，架构同 V3 |
| Gemma 3 | 27B | 2025-03 | Dense | GQA + QK-Norm + 5:1 sliding | 27B sweet spot，多语言大词表 |
| Mistral Small 3 | 24B | 2025-03 | Dense | GQA | 延迟优化，KV cache 更小 |
| Llama 4 MoE | 400B/17B | 2025-04 | Sparse MoE | GQA | 交替 Dense/MoE 块，专家更大 |
| Qwen3 MoE | 235B/22B | 2025-04 | Sparse MoE | GQA + QK-Norm | 无 shared expert，服务效率优化 |
| Qwen3 | 32B | 2025-04 | Dense | GQA + QK-Norm | 参考 Dense 基线，8 KV heads |

### 2025-2026: Hybrid 与规模化
| 模型 | 总/激活 | 日期 | Decoder | 注意力 | 关键细节 |
|------|---------|------|---------|--------|----------|
| NoPE 实验 | 3B | 2025-06 | Dense | GQA + 周期性 NoPE | 每 4 层省略 RoPE 测试 |
| Kimi K2 | 1T/32B | 2025-07 | Sparse MoE | MLA | 更多专家，更少 MLA heads |
| GPT-OSS-Instruct | 355B/32B | 2025-07 | Sparse MoE | GQA + QK-Norm | 3 Dense 层后 MoE routing |
| GPT-OSS-20B | 20B/3.6B | 2025-08 | Sparse MoE | GQA + 交替 sliding/global | 更宽更浅，attention bias + sink |
| GPT-OSS-120B | 120B | 2025-08 | Sparse MoE | 交替 sliding/global | OpenAI 旗舰开源权重 |
| Qwen3-Next | 270B | 2025-08 | Sparse MoE | GQA | 始终开启 SwiGLU path (类似 shared expert) |
| Qwen3.5-Next | 80B/3B | 2025-09 | Sparse Hybrid | 3:1 Gated DeltaNet + Gated Attention | 更多专家 + shared expert + 262k 上下文 |
| MiniMax M2 | 230B/10B | 2025-10 | Sparse MoE | GQA + QK-Norm + partial RoPE | 每层 QK-Norm，更稀疏 routing |
| Kimi Linear | 48B/3B | 2025-10 | Sparse Hybrid | 3:1 Kimi Delta + MLA | MLA 层 NoPE，channel-wise gating |
| OLMo 3 | 32B | 2025-11 | Dense | GQA + QK-Norm + 3:1 sliding/global | 保持 post-norm，仅 global 层 YaRN |
| OLMo 3 | 7B | 2025-11 | Dense | MHA + QK-Norm + 3:1 sliding/global | 保持 post-norm + MHA |
| DeepSeek V3.5 | 671B/37B | 2025-12 | Sparse MoE | MLA + DeepSeek Sparse Attention | 效率演进，非新架构 |
| Mistral Large 2 | 673B/41B | 2025-12 | Sparse MoE | MLA | DeepSeek V3 近亲，专家更大 |
| NVIDIA Nano | 30B/3B | 2025-12 | Hybrid MoE | 主要是 Mamba-2 + 少量 GQA | 极端 transformer-state-space hybrid |
| Qwen3-Max | 309B/15B | 2025-12 | Sparse MoE | 5:1 sliding/global | 128-token 局部窗口 + multi-token prediction |
| GLM-4.6 | 355B/32B | 2025-12 | Sparse MoE | GQA + QK-Norm | MLA 之前的基线 |
| Arcee AI | 400B/13B | 2026-01 | Sparse MoE | GQA + gated attention + 3:1 sliding | QK-Norm + RoPE+NoPE + sandwich norm |
| GLM-4.7 | 744B/40B | 2026-02 | Sparse MoE | MLA + DeepSeek Sparse Attention | 比 4.6 更大，更多专家，更少层 |
| NVIDIA Nano-Super | 120B/12B | 2026-03 | Hybrid MoE | 主要是 Mamba-2 + 少量 GQA | Latent-space MoE + shared-weight MTP |
| Ling-1T | 1T/63B | 2026-02 | Sparse Hybrid | Lightning Attention + MLA | 7:1 linear/MLA 比例，63B 激活路径 |
| Qwen3.5 | 397B/17B | 2026-02 | Sparse Hybrid | 3:1 Gated DeltaNet + Gated Attention | Next 风格 hybrid attention 成为核心 |
| Sarvam-2 | 105B | 2026-03 | Sparse MoE | MLA + KV LayerNorm + NoPE+RoPE | 大词表 + 强印地语支持 |
| Sarvam-Reason | 30B | 2026-03 | Sparse MoE | GQA + QK-Norm | 推理优化 + 印地语支持 |

---

## 关键技术趋势

### 1. 注意力机制演进
```
MHA (Multi-Head Attention)
  ↓
GQA (Grouped-Query Attention) - 减少 KV cache
  ↓
MLA (Multi-Token Latent Attention) - DeepSeek 创新
  ↓
Hybrid Attention - DeltaNet + Gated Attention + Linear Attention
```

### 2. 归一化演进
```
LayerNorm (GPT-2)
  ↓
RMSNorm (Llama)
  ↓
QK-Norm (OLMo 2, Qwen3)
  ↓
Sandwich Norm (Arcee AI)
```

### 3. 位置编码演进
```
绝对位置编码 (GPT-2)
  ↓
RoPE (Rotary Position Embedding, Llama)
  ↓
RoPE + NoPE 混合 (周期性省略 RoPE)
  ↓
Partial RoPE (仅部分层使用)
```

### 4. 稀疏化演进
```
Dense (全参数激活)
  ↓
Sparse MoE (少量专家激活)
  ↓
Hybrid MoE (MoE + State-Space 混合)
  ↓
Coarse-Grained MoE (更大专家，更少数量)
```

### 5. 上下文窗口优化
```
标准注意力 (O(n²) 复杂度)
  ↓
Sliding Window Attention (局部窗口)
  ↓
Linear Attention (DeltaNet, Lightning Attention)
  ↓
Hybrid (全局 + 局部混合)
```

---

## 架构选择决策树

### 场景 1: 边缘推理 (<10B 参数)
```
推荐：OLMo 3 7B / Tiny Aya 3B
理由：
- Dense 架构，无 MoE routing 开销
- Sliding window 减少 KV cache
- Post-norm 训练稳定
```

### 场景 2: 云端服务 (10B-100B 激活)
```
推荐：Qwen3.5 397B/17B / GLM-4.7 744B/40B
理由：
- MoE 架构，推理成本低
- GQA + QK-Norm 平衡质量/效率
- 大上下文支持
```

### 场景 3: 长上下文 (>100k tokens)
```
推荐：Ling-1T 1T/63B / Qwen3.5-Next 80B/3B
理由：
- Linear attention (O(n) 复杂度)
- Native 262k+ 上下文
- Chunked prefill 优化
```

### 场景 4: 多语言支持
```
推荐：Gemma 3 27B / Sarvam-2 105B
理由：
- 大词表 (256k+)
- 多语言训练数据
- 印地语/亚洲语言优化
```

### 场景 5: 推理/数学
```
推荐：DeepSeek R1 / Sarvam-Reason 30B
理由：
- 推理优化训练
- Chain-of-Thought 强化
- 数学基准 SOTA
```

---

## 对 Sandbot V6.3 的启示

### 模型选择策略
```
当前：qwen3.5-plus (阿里云百炼)
分析：
- Qwen3.5 系列是 2026-02 最新架构
- Sparse Hybrid (3:1 Gated DeltaNet + Gated Attention)
- 397B 总参数，17B 激活
- 适合云端服务场景

建议：继续使用 Qwen3.5 系列
- 架构先进 (Hybrid Attention)
- 成本效益好 (17B 激活)
- 中文支持优秀
```

### 知识检索优化
```
当前知识库：2,550 文件，~1,078,258 知识点
问题：如何高效检索？

启发从 LLM 架构：
1. Sliding Window → 近期记忆优先
2. MoE Routing → 领域路由 (AI/金融/技术)
3. GQA → 共享 KV cache (压缩索引)

行动项：
- [ ] 实现领域路由检索 (AI Agent → 01-ai-agent/)
- [ ] 添加记忆时间衰减 (近期权重更高)
- [ ] 压缩索引 (减少检索 token 消耗)
```

### 子 Agent 架构参考
```
从 DeepSeek V3 学习：
- Dense Prefix (共享基础能力)
- Shared Expert (跨领域知识)
- Sparse MoE (专业化子 Agent)

Sandbot 映射：
- Dense Prefix = 主 Agent (通用能力)
- Shared Expert = 共享知识库 (所有子 Agent 访问)
- Sparse MoE = 7 子 Agent (专业化)
```

---

## 关键教训

1. **架构收敛**: 2026 年主流架构趋同 (MoE + GQA + Sliding Window)
2. **效率优先**: 从纯性能转向性能/效率平衡
3. **Hybrid 趋势**: 纯 Transformer → Transformer + State-Space 混合
4. **开源繁荣**: 2025-2026 是开源权重"春天"(Sebastian 语)
5. **规模继续**: 1T+ 参数模型成为新常态

---

**数量**: 1,200 知识点  
**深度**: ⭐⭐⭐⭐⭐ (完整架构参考)  
**行动项**:
- [ ] 实现领域路由检索
- [ ] 添加记忆时间衰减
- [ ] 压缩索引优化
- [ ] 持续追踪新架构 (订阅 Sebastian 博客)
