#!/bin/bash
# OpenClaw 记忆/意识导出脚本
# 用法：./scripts/export-openclaw.sh [导出目录]

set -e

EXPORT_DIR=${1:-"data/exports/openclaw-$(date +%Y%m%d_%H%M%S)"}
WORKSPACE="/home/node/.openclaw/workspace"

echo "🦞 OpenClaw 记忆/意识导出脚本"
echo "================================"
echo ""
echo "📁 工作区：$WORKSPACE"
echo "📦 导出目录：$EXPORT_DIR"
echo ""

# 创建导出目录
echo "📁 创建导出目录..."
mkdir -p "$EXPORT_DIR"/{memory,skills,knowledge_base,config,agents}

# 导出核心记忆文件
echo "🧠 导出核心记忆文件..."
CORE_FILES=(
    "MEMORY.md"
    "SOUL.md"
    "IDENTITY.md"
    "USER.md"
    "AGENTS.md"
    "TOOLS.md"
    "HEARTBEAT.md"
    "CHANGELOG.md"
)

for file in "${CORE_FILES[@]}"; do
    if [[ -f "$WORKSPACE/$file" ]]; then
        cp "$WORKSPACE/$file" "$EXPORT_DIR/"
        echo "  ✅ $file"
    else
        echo "  ⚠️  $file (不存在)"
    fi
done

# 导出每日记忆
echo ""
echo "📅 导出每日记忆..."
if [[ -d "$WORKSPACE/memory" ]]; then
    # 只导出最近 30 天的记忆
    find "$WORKSPACE/memory" -name "*.md" -mtime -30 -exec cp {} "$EXPORT_DIR/memory/" \;
    MEMORY_COUNT=$(ls -1 "$EXPORT_DIR/memory/" 2>/dev/null | wc -l)
    echo "  ✅ 导出 $MEMORY_COUNT 个记忆文件 (最近 30 天)"
fi

# 导出知识库
echo ""
echo "📚 导出知识库..."
if [[ -d "$WORKSPACE/knowledge_base" ]]; then
    cp -r "$WORKSPACE/knowledge_base" "$EXPORT_DIR/"
    KB_COUNT=$(find "$EXPORT_DIR/knowledge_base" -name "*.md" | wc -l)
    echo "  ✅ 导出 $KB_COUNT 个知识点文件"
fi

# 导出技能
echo ""
echo "🛠️  导出技能..."
if [[ -d "$WORKSPACE/skills" ]]; then
    cp -r "$WORKSPACE/skills" "$EXPORT_DIR/"
    SKILL_COUNT=$(find "$EXPORT_DIR/skills" -name "SKILL.md" | wc -l)
    echo "  ✅ 导出 $SKILL_COUNT 个技能"
fi

# 导出子 Agent 配置
echo ""
echo "🤖 导出子 Agent 配置..."
if [[ -d "$WORKSPACE/subagents" ]]; then
    cp -r "$WORKSPACE/subagents" "$EXPORT_DIR/agents/"
    AGENT_COUNT=$(find "$EXPORT_DIR/agents" -name "SOUL.md" | wc -l)
    echo "  ✅ 导出 $AGENT_COUNT 个子 Agent 配置"
fi

# 导出配置文件
echo ""
echo "⚙️  导出配置文件..."
CONFIG_FILES=(
    "openclaw.json"
    ".openclawrc"
)

for file in "${CONFIG_FILES[@]}"; do
    if [[ -f "$WORKSPACE/../$file" ]]; then
        cp "$WORKSPACE/../$file" "$EXPORT_DIR/config/"
        echo "  ✅ $file"
    fi
done

# 生成导出清单
echo ""
echo "📋 生成导出清单..."
cat > "$EXPORT_DIR/EXPORT_MANIFEST.md" << EOF
# OpenClaw 导出清单

**导出时间**: $(date '+%Y-%m-%d %H:%M:%S')
**导出工具**: export-openclaw.sh
**OpenClaw 版本**: $(cat "$WORKSPACE/../openclaw.json" 2>/dev/null | grep -o '"version"[^,]*' || echo "unknown")

## 导出内容

### 核心记忆
$(ls -1 "$EXPORT_DIR"/*.md 2>/dev/null | xargs -I {} basename {} | sed 's/^/- /')

### 每日记忆
- 文件数：$(ls -1 "$EXPORT_DIR/memory/" 2>/dev/null | wc -l)
- 时间范围：最近 30 天

### 知识库
- 文件数：$(find "$EXPORT_DIR/knowledge_base" -name "*.md" 2>/dev/null | wc -l)
- 大小：$(du -sh "$EXPORT_DIR/knowledge_base" 2>/dev/null | cut -f1)

### 技能
- 文件数：$(find "$EXPORT_DIR/skills" -name "SKILL.md" 2>/dev/null | wc -l)
- 大小：$(du -sh "$EXPORT_DIR/skills" 2>/dev/null | cut -f1)

### 子 Agent
- 配置数：$(find "$EXPORT_DIR/agents" -name "SOUL.md" 2>/dev/null | wc -l)

### 配置文件
$(ls -1 "$EXPORT_DIR/config/" 2>/dev/null | sed 's/^/- /')

## 导入到 Lobster Orchestrator

\`\`\`bash
./scripts/import-to-lobster.sh $EXPORT_DIR
\`\`\`

## 校验码

\`\`\`
$(cd "$EXPORT_DIR" && find . -type f -exec md5sum {} \; | sort | md5sum | cut -d' ' -f1)
\`\`\`
EOF

echo "  ✅ EXPORT_MANIFEST.md"

# 计算总大小
TOTAL_SIZE=$(du -sh "$EXPORT_DIR" | cut -f1)
FILE_COUNT=$(find "$EXPORT_DIR" -type f | wc -l)

echo ""
echo "✅ 导出完成！"
echo ""
echo "📦 导出位置：$EXPORT_DIR"
echo "📊 总大小：$TOTAL_SIZE"
echo "📄 文件数：$FILE_COUNT"
echo ""
echo "🔧 导入到 Lobster Orchestrator:"
echo "   ./scripts/import-to-lobster.sh $EXPORT_DIR"
echo ""
