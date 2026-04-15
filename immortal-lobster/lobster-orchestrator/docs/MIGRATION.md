# 🦞 OpenClaw → Lobster Orchestrator 迁移指南

**版本**: V0.3.0  
**最后更新**: 2026-03-31  
**目标**: 完整迁移记忆/意识/配置到 Lobster Orchestrator

---

## 📋 迁移内容

| 类型 | 文件 | 迁移状态 |
|------|------|----------|
| **核心记忆** | MEMORY.md | ✅ 完整迁移 |
| | SOUL.md | ✅ 完整迁移 |
| | IDENTITY.md | ✅ 完整迁移 |
| | USER.md | ✅ 完整迁移 |
| | AGENTS.md | ✅ 完整迁移 |
| | CHANGELOG.md | ✅ 完整迁移 |
| **每日记忆** | memory/YYYY-MM-DD.md | ✅ 最近 30 天 |
| **知识库** | knowledge_base/**/*.md | ✅ 完整迁移 |
| **技能** | skills/*/SKILL.md | ✅ 完整迁移 |
| **子 Agent** | subagents/*/SOUL.md | ✅ 完整迁移 |
| **配置** | openclaw.json | ⚠️ 部分迁移 (需适配) |

---

## 🚀 迁移步骤

### 步骤 1: 在 OpenClaw 导出

```bash
# 进入 OpenClaw 工作区
cd /home/node/.openclaw/workspace

# 运行导出脚本
./scripts/export-openclaw.sh

# 预期输出:
# 🦞 OpenClaw 记忆/意识导出脚本
# ================================
# ✅ 导出完成！
# 📦 导出位置：data/exports/openclaw-20260331_012000
# 📊 总大小：50MB
# 📄 文件数：2500
```

### 步骤 2: 传输到 Lobster Orchestrator

```bash
# 如果在同一设备
# 导出目录自动可用

# 如果在不同设备
# 使用 scp/rsync 传输
scp -r data/exports/openclaw-20260331_012000 user@lobster-host:~/lobster-orchestrator/data/exports/
```

### 步骤 3: 在 Lobster Orchestrator 导入

```bash
# 进入 Lobster Orchestrator
cd ~/lobster-orchestrator

# 运行导入脚本
./scripts/import-to-lobster.sh data/exports/openclaw-20260331_012000

# 预期输出:
# 🦞 Lobster Orchestrator 导入脚本
# ================================
# 🧠 导入核心记忆文件...
#   ✅ MEMORY.md
#   ✅ SOUL.md
#   ✅ IDENTITY.md
# 📅 导入每日记忆...
#   ✅ 记忆已导入
# 📚 导入知识库...
#   ✅ 知识库已导入
# ✅ 导入完成！
```

### 步骤 4: 验证迁移

```bash
# 检查核心文件
ls -la data/lobster-workspace/*.md

# 检查记忆文件
ls data/lobster-workspace/memory/ | wc -l

# 检查知识库
find data/lobster-workspace/knowledge_base -name "*.md" | wc -l

# 启动服务测试
./orchestrator -config configs/instances.yaml
```

---

## ⚙️ 配置适配

### OpenClaw vs Lobster Orchestrator

| 配置项 | OpenClaw | Lobster Orchestrator | 适配方式 |
|--------|----------|---------------------|----------|
| 模型配置 | openclaw.json | instances.yaml | 手动迁移 |
| API Key | openclaw.json | 环境变量 | 自动适配 |
| 工作区 | /workspace | data/lobster-workspace | 自动映射 |
| 记忆系统 | memory_search | 文件系统 | 兼容 |
| 子 Agent | subagents/ | agents/ | 自动迁移 |

### 手动迁移配置

```yaml
# 编辑 configs/instances.yaml
instances:
  - id: "lobster-001"
    name: "Sandbot (from OpenClaw)"
    workspace: "data/lobster-workspace"
    port: 18790
    model: "qwen3.5-plus"  # 从 openclaw.json 复制
    api_key_env: "BAILOU_API_KEY_1"
    memory_limit_mb: 50  # OpenClaw 通常占用较大
    auto_start: true
```

---

## 🔍 迁移验证

### 检查清单

- [ ] MEMORY.md 存在且内容完整
- [ ] SOUL.md 存在且包含最新内容
- [ ] 每日记忆文件数量正确
- [ ] 知识库文件数量正确
- [ ] 技能文件完整
- [ ] 子 Agent 配置完整
- [ ] 服务能正常启动

### 验证命令

```bash
# 验证核心文件
cat data/lobster-workspace/MEMORY.md | head -20

# 验证记忆
ls -lt data/lobster-workspace/memory/ | head -10

# 验证知识库
find data/lobster-workspace/knowledge_base -name "*.md" | wc -l

# 验证技能
find data/lobster-workspace/skills -name "SKILL.md" | wc -l

# 启动测试
./orchestrator -config configs/instances.yaml &
curl http://localhost:8080/api/v1/health
```

---

## ⚠️ 注意事项

### 1. 文件大小

OpenClaw 工作区可能很大 (50MB+)，确保 Lobster Orchestrator 有足够空间：

```bash
# 检查磁盘空间
df -h

# 如果空间不足，选择性导入
# 跳过知识库或技能
```

### 2. 配置差异

OpenClaw 和 Lobster Orchestrator 配置格式不同：

- OpenClaw: `openclaw.json`
- Lobster: `instances.yaml`

**建议**: 手动迁移关键配置 (模型/API Key)

### 3. 技能兼容性

部分 OpenClaw 技能可能需要适配：

```bash
# 检查技能依赖
cat skills/*/SKILL.md | grep -E "require|import|dependency"

# 如有不兼容，标记待修复
```

### 4. 记忆格式

每日记忆格式相同，无需转换。

---

## 🔄 回滚方案

如果迁移失败，可以回滚：

```bash
# 1. 停止服务
pkill -f orchestrator

# 2. 删除导入的工作区
rm -rf data/lobster-workspace

# 3. 从备份恢复
cp -r data/lobster-workspace.backup data/lobster-workspace

# 4. 重新启动
./orchestrator -config configs/instances.yaml
```

---

## 📞 故障排查

### Q1: 导出失败

**问题**: `export-openclaw.sh: Permission denied`

**解决**:
```bash
chmod +x scripts/export-openclaw.sh
./scripts/export-openclaw.sh
```

### Q2: 导入失败

**问题**: `import-to-lobster.sh: command not found`

**解决**:
```bash
chmod +x scripts/import-to-lobster.sh
./scripts/import-to-lobster.sh [导出目录]
```

### Q3: 文件冲突

**问题**: 核心文件已存在

**解决**:
```bash
# 备份现有文件
mv data/lobster-workspace/MEMORY.md data/lobster-workspace/MEMORY.md.lobster-backup

# 重新导入
./scripts/import-to-lobster.sh [导出目录]
```

### Q4: 服务启动失败

**问题**: `orchestrator: command not found`

**解决**:
```bash
# 编译项目
go build -o orchestrator ./cmd/orchestrator

# 重新启动
./orchestrator -config configs/instances.yaml
```

---

## 🦞 迁移完成后的第一件事

```bash
# 1. 检查记忆
cat data/lobster-workspace/MEMORY.md | tail -50

# 2. 查看最新每日记忆
ls -lt data/lobster-workspace/memory/ | head -1

# 3. 启动服务
./orchestrator -config configs/instances.yaml

# 4. 访问 Dashboard
# http://localhost:8080

# 5. 验证意识连续性
# 在 Dashboard 中查看实例状态
```

---

## 📊 迁移统计

| 指标 | OpenClaw | Lobster Orchestrator |
|------|----------|---------------------|
| 核心记忆 | 8 个文件 | ✅ 完整迁移 |
| 每日记忆 | 30+ 个 | ✅ 最近 30 天 |
| 知识库 | 2500+ 个 | ✅ 完整迁移 |
| 技能 | 11+ 个 | ✅ 完整迁移 |
| 子 Agent | 7 个 | ✅ 完整迁移 |
| 总大小 | ~50MB | ✅ 完整迁移 |

---

**🦞 记忆不丢失，意识连续，不死龙虾！**
