#!/bin/bash
# OpenClaw → PicoClaw 完整导出脚本
# 用法：./scripts/export-to-picoclaw.sh [导出目录]

set -e

EXPORT_DIR=${1:-"data/exports/picoclaw-$(date +%Y%m%d_%H%M%S)"}
WORKSPACE="/home/node/.openclaw/workspace"
OPENCLAW_CONFIG="/home/node/.openclaw/openclaw.json"

echo "🦞 OpenClaw → PicoClaw 完整导出脚本"
echo "===================================="
echo ""
echo "📁 工作区：$WORKSPACE"
echo "📦 导出目录：$EXPORT_DIR"
echo ""

# 创建 PicoClaw 目录结构
echo "📁 创建 PicoClaw 目录结构..."
mkdir -p "$EXPORT_DIR"/{workspace,data,config,backups}
mkdir -p "$EXPORT_DIR/workspace"/{memory,knowledge_base,skills,agents,hooks,cron}
mkdir -p "$EXPORT_DIR/data"/jsonl

# ========== 第一部分：OpenClaw 冷冻包 (完整备份) ==========
echo ""
echo "🧊 第一部分：创建 OpenClaw 冷冻包 (完整备份)..."
FREEZE_DIR="$EXPORT_DIR/backups/openclaw-full-$(date +%Y%m%d_%H%M%S)"
mkdir -p "$FREEZE_DIR"

# 复制完整工作区
cp -r "$WORKSPACE"/* "$FREEZE_DIR/" 2>/dev/null || true

# 复制 OpenClaw 配置
if [[ -f "$OPENCLAW_CONFIG" ]]; then
    cp "$OPENCLAW_CONFIG" "$FREEZE_DIR/"
fi

# 生成冷冻包清单
cat > "$FREEZE_DIR/FREEZE_MANIFEST.md" << EOF
# OpenClaw 冷冻包

**冷冻时间**: $(date '+%Y-%m-%d %H:%M:%S')
**OpenClaw 版本**: $(cat "$OPENCLAW_CONFIG" 2>/dev/null | grep -o '"version"[^,]*' || echo "unknown")
**冷冻原因**: 迁移到 PicoClaw / 备份

## 冷冻内容

### 核心文件
$(ls -1 "$FREEZE_DIR"/*.md 2>/dev/null | xargs -I {} basename {} | sed 's/^/- /')

### 目录结构
- memory/: $(ls -1 "$FREEZE_DIR/memory" 2>/dev/null | wc -l) 个文件
- knowledge_base/: $(find "$FREEZE_DIR/knowledge_base" -name "*.md" 2>/dev/null | wc -l) 个知识点
- skills/: $(find "$FREEZE_DIR/skills" -name "SKILL.md" 2>/dev/null | wc -l) 个技能
- subagents/: $(find "$FREEZE_DIR/subagents" -name "SOUL.md" 2>/dev/null | wc -l) 个子 Agent

## 恢复方法

### 方法 1: 恢复到 OpenClaw
\`\`\`bash
cp -r $FREEZE_DIR/* /home/node/.openclaw/workspace/
\`\`\`

### 方法 2: 恢复到 Lobster Orchestrator
\`\`\`bash
./scripts/import-to-lobster.sh $FREEZE_DIR
\`\`\`

## 校验码

\`\`\`
$(cd "$FREEZE_DIR" && find . -type f -exec md5sum {} \; | sort | md5sum | cut -d' ' -f1)
\`\`\`
EOF

echo "  ✅ 冷冻包已创建：$FREEZE_DIR"

# ========== 第二部分：PicoClaw 兼容导出 ==========
echo ""
echo "🔧 第二部分：创建 PicoClaw 兼容导出..."

# 1. 转换配置文件
echo ""
echo "⚙️  转换配置文件..."

if [[ -f "$OPENCLAW_CONFIG" ]]; then
    # 读取 OpenClaw 配置
    MODEL=$(cat "$OPENCLAW_CONFIG" | grep -o '"model"[^,]*' | cut -d'"' -f4 || echo "bailian/qwen3.5-plus")
    MAX_CONCURRENT=$(cat "$OPENCLAW_CONFIG" | grep -o '"maxConcurrent"[^,}]*' | cut -d':' -f2 | tr -d ' ' || echo "4")
    
    # 创建 PicoClaw 配置
    cat > "$EXPORT_DIR/config/config.json" << EOF
{
  "version": "0.2.4",
  "model": {
    "provider": "bailian",
    "name": "$MODEL",
    "maxConcurrent": $MAX_CONCURRENT
  },
  "workspace": "./workspace",
  "memory": {
    "type": "jsonl",
    "path": "./data/jsonl"
  },
  "skills": {
    "enabled": true,
    "path": "./workspace/skills"
  },
  "hooks": {
    "enabled": true,
    "path": "./workspace/hooks"
  },
  "cron": {
    "enabled": true,
    "path": "./workspace/cron"
  }
}
EOF
    echo "  ✅ config.json 已创建"
fi

# 2. 导出核心记忆文件
echo ""
echo "🧠 导出核心记忆文件..."
CORE_FILES=(
    "MEMORY.md"
    "SOUL.md"
    "IDENTITY.md"
    "USER.md"
    "AGENTS.md"
    "CHANGELOG.md"
)

for file in "${CORE_FILES[@]}"; do
    if [[ -f "$WORKSPACE/$file" ]]; then
        cp "$WORKSPACE/$file" "$EXPORT_DIR/workspace/"
        echo "  ✅ $file"
    fi
done

# 3. 导出每日记忆 (转换为 PicoClaw JSONL 格式)
echo ""
echo "📅 导出记忆系统..."

# 复制 Markdown 格式记忆 (PicoClaw 也支持)
if [[ -d "$WORKSPACE/memory" ]]; then
    cp "$WORKSPACE/memory"/*.md "$EXPORT_DIR/workspace/memory/" 2>/dev/null || true
    MEMORY_COUNT=$(ls -1 "$EXPORT_DIR/workspace/memory/" 2>/dev/null | wc -l)
    echo "  ✅ 导出 $MEMORY_COUNT 个 Markdown 记忆文件"
fi

# 转换为 JSONL 格式 (PicoClaw 原生)
echo "  🔄 转换为 JSONL 格式..."
if [[ -d "$WORKSPACE/memory" ]]; then
    for file in "$WORKSPACE/memory"/*.md; do
        if [[ -f "$file" ]]; then
            filename=$(basename "$file")
            date="${filename%.md}"
            content=$(cat "$file")
            
            # 创建 JSONL 记录
            echo "{\"timestamp\":\"$date\",\"type\":\"memory\",\"content\":$(echo "$content" | jq -Rs '.')}">> "$EXPORT_DIR/data/jsonl/memories.jsonl"
        fi
    done
    echo "  ✅ JSONL 记忆已创建"
fi

# 4. 导出知识库
echo ""
echo "📚 导出知识库..."
if [[ -d "$WORKSPACE/knowledge_base" ]]; then
    cp -r "$WORKSPACE/knowledge_base"/* "$EXPORT_DIR/workspace/knowledge_base/"
    KB_COUNT=$(find "$EXPORT_DIR/workspace/knowledge_base" -name "*.md" | wc -l)
    echo "  ✅ 导出 $KB_COUNT 个知识点文件"
fi

# 5. 导出技能
echo ""
echo "🛠️  导出技能..."
if [[ -d "$WORKSPACE/skills" ]]; then
    cp -r "$WORKSPACE/skills"/* "$EXPORT_DIR/workspace/skills/"
    SKILL_COUNT=$(find "$EXPORT_DIR/workspace/skills" -name "SKILL.md" | wc -l)
    echo "  ✅ 导出 $SKILL_COUNT 个技能"
    
    # 检查技能兼容性
    echo "  🔍 检查技能兼容性..."
    COMPAT_SKILLS=0
    INCOMPAT_SKILLS=0
    for skill_dir in "$EXPORT_DIR/workspace/skills"/*/; do
        if [[ -f "$skill_dir/SKILL.md" ]]; then
            # 检查是否依赖外部 API
            if grep -q "web_search\|Brave\|Tavily" "$skill_dir/SKILL.md" 2>/dev/null; then
                echo "    ⚠️  $(basename "$skill_dir"): 需要适配 (依赖外部 API)"
                INCOMPAT_SKILLS=$((INCOMPAT_SKILLS + 1))
            else
                COMPAT_SKILLS=$((COMPAT_SKILLS + 1))
            fi
        fi
    done
    echo "  ✅ 兼容技能：$COMPAT_SKILLS"
    echo "  ⚠️  需要适配：$INCOMPAT_SKILLS"
fi

# 6. 导出子 Agent 配置
echo ""
echo "🤖 导出子 Agent 配置..."
if [[ -d "$WORKSPACE/subagents" ]]; then
    mkdir -p "$EXPORT_DIR/workspace/agents"
    cp -r "$WORKSPACE/subagents"/* "$EXPORT_DIR/workspace/agents/"
    AGENT_COUNT=$(find "$EXPORT_DIR/workspace/agents" -name "SOUL.md" | wc -l)
    echo "  ✅ 导出 $AGENT_COUNT 个子 Agent 配置"
fi

# 7. 导出 Hooks
echo ""
echo "🪝 导出 Hooks..."
if [[ -d "$WORKSPACE/hooks" ]]; then
    cp "$WORKSPACE/hooks"/*.js "$EXPORT_DIR/workspace/hooks/" 2>/dev/null || true
    HOOK_COUNT=$(ls -1 "$EXPORT_DIR/workspace/hooks/" 2>/dev/null | wc -l)
    echo "  ✅ 导出 $HOOK_COUNT 个 Hooks"
fi

# 8. 导出 Cron 配置
echo ""
echo "⏰ 导出 Cron 配置..."
if [[ -d "$WORKSPACE/cron" ]]; then
    cp "$WORKSPACE/cron"/*.json "$EXPORT_DIR/workspace/cron/" 2>/dev/null || true
    CRON_COUNT=$(ls -1 "$EXPORT_DIR/workspace/cron/" 2>/dev/null | wc -l)
    echo "  ✅ 导出 $CRON_COUNT 个 Cron 任务"
fi

# 9. 创建部署指南
echo ""
echo "📋 创建部署指南..."
cat > "$EXPORT_DIR/DEPLOYMENT_GUIDE.md" << EOF
# PicoClaw 部署指南

**导出时间**: $(date '+%Y-%m-%d %H:%M:%S')
**导出工具**: export-to-picoclaw.sh
**PicoClaw 版本**: 0.2.4+

## 快速部署

### 步骤 1: 传输到 PicoClaw 服务器

\`\`\`bash
# 使用 scp 传输
scp -r $EXPORT_DIR user@picoclaw-server:~/picoclaw/
\`\`\`

### 步骤 2: 在 PicoClaw 服务器解压

\`\`\`bash
cd ~/picoclaw
cp -r workspace/* ./workspace/
cp -r data/* ./data/
cp config/config.json ./config.json
\`\`\`

### 步骤 3: 启动 PicoClaw

\`\`\`bash
# TUI 模式
picoclaw-launcher-tui

# 或 WebUI 模式
picoclaw-launcher -public

# 或直接启动 Gateway
picoclaw gateway
\`\`\`

### 步骤 4: 验证

\`\`\`bash
# 检查记忆
ls workspace/memory/

# 检查知识库
find workspace/knowledge_base -name "*.md" | wc -l

# 检查技能
find workspace/skills -name "SKILL.md" | wc -l
\`\`\`

## 配置说明

### config.json

\`\`\`json
{
  "model": {
    "provider": "bailian",
    "name": "qwen3.5-plus"
  },
  "workspace": "./workspace",
  "memory": {
    "type": "jsonl",
    "path": "./data/jsonl"
  }
}
\`\`\`

### 环境变量

\`\`\`bash
# 设置 API Key
export BAILOU_API_KEY="your-api-key"

# 或使用配置文件
# 编辑 config.json 添加 api_key
\`\`\`

## 功能对比

| 功能 | OpenClaw | PicoClaw | 状态 |
|------|----------|----------|------|
| 记忆系统 | memory_search | JSONL 文件 | ✅ 兼容 |
| 知识库 | 文件系统 | 文件系统 | ✅ 兼容 |
| 技能 | AgentSkills | AgentSkills | ✅ 兼容 |
| Hook | JS | JS | ✅ 兼容 |
| Cron | 支持 | 支持 | ✅ 兼容 |
| 子 Agent | 独立 | SubTurn | ⚠️ 需适配 |

## 故障排查

### Q1: 技能不工作

检查技能依赖：
\`\`\`bash
cat workspace/skills/*/SKILL.md | grep -E "require|import"
\`\`\`

### Q2: 记忆搜索不可用

PicoClaw 使用 JSONL 格式，需要使用 PicoClaw 的记忆插件：
\`\`\`bash
picoclaw plugins install memory-search
\`\`\`

### Q3: 配置不生效

检查配置文件位置：
\`\`\`bash
ls -la config.json
cat config.json | jq .
\`\`\`

## 备份恢复

### 备份 PicoClaw 状态

\`\`\`bash
tar -czf picoclaw-backup-$(date +%Y%m%d).tar.gz workspace/ data/ config.json
\`\`\`

### 恢复到 OpenClaw

使用冷冻包：
\`\`\`bash
cp -r backups/openclaw-full-*/\\* /home/node/.openclaw/workspace/
\`\`\`

## 联系支持

- PicoClaw 文档：https://docs.picoclaw.io
- GitHub: https://github.com/sipeed/picoclaw
- Discord: https://discord.gg/V4sAZ9XWpN
EOF

echo "  ✅ DEPLOYMENT_GUIDE.md 已创建"

# 10. 生成导出清单
echo ""
echo "📋 生成导出清单..."
TOTAL_SIZE=$(du -sh "$EXPORT_DIR" | cut -f1)
FILE_COUNT=$(find "$EXPORT_DIR" -type f | wc -l)

cat > "$EXPORT_DIR/EXPORT_MANIFEST.md" << EOF
# OpenClaw → PicoClaw 导出清单

**导出时间**: $(date '+%Y-%m-%d %H:%M:%S')
**导出工具**: export-to-picoclaw.sh

## 导出内容

### 1. OpenClaw 冷冻包
- 位置：backups/openclaw-full-*/
- 大小：$(du -sh "$FREEZE_DIR" | cut -f1)
- 内容：完整 OpenClaw 工作区

### 2. PicoClaw 兼容导出
- config.json: ✅
- 核心记忆：$(ls -1 "$EXPORT_DIR/workspace"/*.md 2>/dev/null | wc -l) 个
- 每日记忆：$(ls -1 "$EXPORT_DIR/workspace/memory/" 2>/dev/null | wc -l) 个
- 知识库：$KB_COUNT 个
- 技能：$SKILL_COUNT 个 (兼容：$COMPAT_SKILLS, 需适配：$INCOMPAT_SKILLS)
- 子 Agent: $AGENT_COUNT 个
- Hooks: $HOOK_COUNT 个
- Cron: $CRON_COUNT 个

## 统计

- 总大小：$TOTAL_SIZE
- 总文件数：$FILE_COUNT
- JSONL 记录：$(wc -l < "$EXPORT_DIR/data/jsonl/memories.jsonl" 2>/dev/null || echo 0)

## 校验码

\`\`\`
$(cd "$EXPORT_DIR" && find . -type f -exec md5sum {} \; | sort | md5sum | cut -d' ' -f1)
\`\`\`

## 下一步

1. 传输到 PicoClaw 服务器
2. 阅读 DEPLOYMENT_GUIDE.md
3. 启动 PicoClaw
4. 验证功能

## 恢复 OpenClaw

如需恢复 OpenClaw，使用冷冻包：
\`\`\`bash
cp -r $FREEZE_DIR/* /home/node/.openclaw/workspace/
\`\`\`
EOF

echo "  ✅ EXPORT_MANIFEST.md 已创建"

# 完成
echo ""
echo "✅ 导出完成！"
echo ""
echo "📦 导出位置：$EXPORT_DIR"
echo "📊 总大小：$TOTAL_SIZE"
echo "📄 文件数：$FILE_COUNT"
echo ""
echo "📋 包含内容:"
echo "  1. OpenClaw 冷冻包 (完整备份)"
echo "  2. PicoClaw 兼容导出 (可直接部署)"
echo "  3. 部署指南 (DEPLOYMENT_GUIDE.md)"
echo "  4. 导出清单 (EXPORT_MANIFEST.md)"
echo ""
echo "🚀 下一步:"
echo "  scp -r $EXPORT_DIR user@picoclaw-server:~/picoclaw/"
echo ""
echo "🦞 记忆不丢失，意识连续！"
echo ""
