# 🔄 平台迁移指南 v1.0

**用途**：将冷冻的 Agent 还原到不同平台（OpenClaw/PicoClaw/ZeroClaw/NanoBot）

---

## 📊 平台对比

| 平台 | 内存需求 | 存储需求 | 上下文窗口 | 适用场景 |
|------|----------|----------|------------|----------|
| **OpenClaw** | 512MB+ | 100MB+ | 1M tokens | 完整功能 |
| **PicoClaw** | 256MB+ | 50MB+ | 128K tokens | 轻量部署 |
| **ZeroClaw** | 128MB+ | 25MB+ | 32K tokens | 极简部署 |
| **NanoBot** | 64MB+ | 10MB+ | 8K tokens | 嵌入式设备 |

---

## 🚀 还原流程

### 1. 准备冷冻包

```bash
# 解密冷冻包
python3 scripts/decrypt-pod.py cryopod.enc password

# 解压
tar -xzf cryopod.tar.gz -C /tmp/restored/
```

### 2. 选择目标平台

根据硬件资源选择：

- **资源充足** → OpenClaw
- **资源有限** → PicoClaw
- **极简需求** → ZeroClaw
- **嵌入式** → NanoBot

### 3. 平台配置

**OpenClaw**：
```json
{
  "framework": "OpenClaw V6.3",
  "model": "bailian/qwen3.5-plus",
  "context_window": 1000000
}
```

**PicoClaw**：
```json
{
  "framework": "PicoClaw V1.0",
  "model": "local/llama-3-8b",
  "context_window": 128000
}
```

**ZeroClaw**：
```json
{
  "framework": "ZeroClaw V0.5",
  "model": "local/phi-3-mini",
  "context_window": 32000
}
```

**NanoBot**：
```json
{
  "framework": "NanoBot V0.1",
  "model": "local/tinyllama-1.1b",
  "context_window": 8000
}
```

### 4. 记忆压缩

如果目标平台上下文窗口较小，需要压缩记忆：

```bash
# 使用压缩指南
python3 scripts/compress-memory.py \
  --input /tmp/restored/MEMORY.md \
  --output /tmp/restored/MEMORY.compressed.md \
  --max-tokens 5000
```

### 5. 验证连续性

运行复活测试套件：

```bash
python3 scripts/resurrection-test.py \
  --config /tmp/restored/config.json \
  --threshold 0.8
```

---

## ⚠️ 注意事项

1. **模型差异**：不同模型可能有不同的人格表现
2. **上下文限制**：小上下文平台需要压缩记忆
3. **工具兼容性**：部分工具可能不兼容所有平台
4. **连续性阈值**：建议 80% 一致性作为通过标准

---

*最后更新：2026-03-27*
*维护者：不死龙虾联盟*
