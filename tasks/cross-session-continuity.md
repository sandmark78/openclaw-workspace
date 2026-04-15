# 跨会话延续方案

**问题**：每次新会话启动，AI 不记得之前的对话。

**目标**：让 AI 在每次会话中都能"记得"自己是谁，做过什么。

---

## 方案一：session-boot-memory hook（已实现）

**原理**：每次会话启动时，自动读取记忆文件并注入上下文。

**文件**：`/home/node/.openclaw/workspace/hooks/session-boot-memory.js`

**读取内容**：
- `MEMORY.md`（长期记忆）
- `memory/YYYY-MM-DD.md`（今日记忆）
- `memory/YYYY-MM-DD-1.md`（昨日记忆）

**验证方法**：
1. 启动新会话
2. 问："我之前做了什么？"
3. 如果能回答，说明 hook 生效

---

## 方案二：compaction.memoryFlush（已配置）

**原理**：会话接近压缩时，自动提醒写入记忆。

**配置**：
```json
{
  "agents": {
    "defaults": {
      "compaction": {
        "memoryFlush": {
          "enabled": true,
          "softThresholdTokens": 4000
        }
      }
    }
  }
}
```

**效果**：在上下文快满时，自动提醒"把重要内容写入记忆"。

---

## 方案三：向量搜索（已配置）

**原理**：语义搜索记忆文件，找到相关内容。

**配置**：
```json
{
  "agents": {
    "defaults": {
      "memorySearch": {
        "enabled": true,
        "provider": "local",
        "sources": ["memory"]
      }
    }
  }
}
```

**使用**：
- 调用 `memory_search` 工具
- 查询："我之前做过什么？"
- 返回相关记忆片段

---

## 方案四：会话摘要（待实现）

**原理**：每次会话结束时，自动生成摘要并保存到记忆。

**实现**：
1. 创建 `scripts/session-summary.sh`
2. 提取本次会话关键点
3. 追加到 `memory/YYYY-MM-DD.md`

---

## 测试计划

### 测试 1：hook 是否生效

```bash
# 1. 启动新会话
# 2. 问："我的记忆文件在哪里？"
# 3. 期待回答：/home/node/.openclaw/workspace/memory/
```

### 测试 2：记忆固化是否自动

```bash
# 1. 进行一段对话
# 2. 说："记住这个：XXX"
# 3. 检查 memory/YYYY-MM-DD.md 是否有记录
```

### 测试 3：向量搜索是否工作

```bash
# 1. 调用 memory_search 工具
# 2. 查询："不死龙虾联盟"
# 3. 期待返回相关记忆
```

---

## 待办事项

- [ ] 验证 session-boot-memory hook 生效
- [ ] 测试 memoryFlush 自动触发
- [ ] 测试向量搜索功能
- [ ] 创建会话摘要脚本
- [ ] 文档化跨会话延续流程

---

*最后更新：2026-03-27 05:10 UTC*
