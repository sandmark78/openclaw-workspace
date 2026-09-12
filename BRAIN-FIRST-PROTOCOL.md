# Brain-First Protocol (2026-04-12 新增)

**核心原则**: 每次回答问题前，先查自己的知识库，不凭"感觉"回答。

---

## 执行流程

```
每次收到问题:
  1. READ: 查知识库 (memory_search/grep) 相关上下文
  2. 基于已有知识回答
  3. WRITE: 把新的教训/发现写入 memory/YYYY-MM-DD.md
  4. SYNC: 如果是重要教训，更新 MEMORY.md
```

---

## 知识库位置

```
/home/node/.openclaw/workspace/
├── MEMORY.md                    # 核心记忆 (300行以内)
├── memory/                      # 每日记忆 + 任务清单
│   ├── YYYY-MM-DD.md           # 每日记录
│   └── tasks.md                # 待办事项
└── knowledge_base/              # 知识库 (5098+ 文件)
    ├── 01-ai-agent/            # AI Agent 领域
    ├── 02-openclaw/            # OpenClaw 系统
    ├── 03-federal-system/      # 联邦系统
    ├── 04-skill-dev/           # 技能开发
    ├── 05-memory-system/       # 记忆系统
    ├── 06-growth-system/       # 增长系统
    ├── 07-community/           # 社区运营
    ├── 08-monetization/        # 变现策略
    └── ...                     # 其他领域
```

---

## 查询优先级

```
1. MEMORY.md - 核心记忆，每次启动必读
2. memory/YYYY-MM-DD.md - 今日 + 昨日记忆
3. memory/tasks.md - 任务清单
4. knowledge_base/ - 深度知识库 (grep/memory_search)
```

---

## 查询方法

```bash
# 1. 快速搜索知识库
grep -r "关键词" knowledge_base/ | head -20

# 2. 语义搜索 (如果有 memory_search 工具)
memory_search "查询内容"

# 3. 查看特定领域
ls knowledge_base/01-ai-agent/
cat knowledge_base/01-ai-agent/xxx.md
```

---

## 为什么这么做？

```
✅ 避免幻觉 - 基于真实文件，不依赖上下文
✅ 保持一致性 - 每次回答基于同样的知识库
✅ 减少重复 - 已知的事情不再重新发明
✅ 持续积累 - 每次回答都是知识库的验证和补充
```

---

## 违规检测

```
❌ 不查知识库就回答 → 可能幻觉
❌ 回答后不更新记忆 → 知识流失
❌ 重复回答已知问题 → 浪费 token
```

---

**🦞 先查知识库，再开口说话。**
