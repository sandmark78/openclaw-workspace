#!/bin/bash
# Lobster Orchestrator 导入脚本 (从 OpenClaw 导出)
# 用法：./scripts/import-to-lobster.sh [导出目录]

set -e

if [[ -z "$1" ]]; then
    echo "🦞 Lobster Orchestrator 导入脚本"
    echo "================================"
    echo ""
    echo "用法：./scripts/import-to-lobster.sh [导出目录]"
    echo ""
    echo "可用导出:"
    ls -1 data/exports/ 2>/dev/null || echo "  无导出"
    echo ""
    exit 1
fi

EXPORT_DIR=$1
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
WORKSPACE_DIR="$PROJECT_DIR/data/lobster-workspace"

echo "🦞 Lobster Orchestrator 导入脚本"
echo "================================"
echo ""
echo "📦 导出目录：$EXPORT_DIR"
echo "📁 工作区：$WORKSPACE_DIR"
echo ""

# 检查工作区
if [[ ! -d "$WORKSPACE_DIR" ]]; then
    echo "📁 创建工作区..."
    mkdir -p "$WORKSPACE_DIR"/{memory,knowledge_base,skills,agents}
fi

# 导入核心记忆
echo "🧠 导入核心记忆文件..."
CORE_FILES=(
    "MEMORY.md"
    "SOUL.md"
    "IDENTITY.md"
    "USER.md"
    "AGENTS.md"
    "CHANGELOG.md"
)

for file in "${CORE_FILES[@]}"; do
    if [[ -f "$EXPORT_DIR/$file" ]]; then
        # 合并而不是覆盖 (保留 Lobster 的配置)
        if [[ -f "$WORKSPACE_DIR/$file" ]]; then
            echo "  🔄 合并 $file"
            # 保留 Lobster 版本，追加 OpenClaw 内容
            cat "$EXPORT_DIR/$file" >> "$WORKSPACE_DIR/$file.openclaw-backup"
        else
            cp "$EXPORT_DIR/$file" "$WORKSPACE_DIR/$file"
            echo "  ✅ $file"
        fi
    else
        echo "  ⚠️  $file (不存在)"
    fi
done

# 导入每日记忆
echo ""
echo "📅 导入每日记忆..."
if [[ -d "$EXPORT_DIR/memory" ]]; then
    MEMORY_COUNT=$(ls -1 "$EXPORT_DIR/memory/" 2>/dev/null | wc -l)
    echo "  发现 $MEMORY_COUNT 个记忆文件"
    
    read -p "是否导入所有记忆文件？(y/n, 默认 y): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp "$EXPORT_DIR/memory/"*.md "$WORKSPACE_DIR/memory/" 2>/dev/null || true
        echo "  ✅ 记忆已导入"
    fi
fi

# 导入知识库
echo ""
echo "📚 导入知识库..."
if [[ -d "$EXPORT_DIR/knowledge_base" ]]; then
    KB_COUNT=$(find "$EXPORT_DIR/knowledge_base" -name "*.md" | wc -l)
    echo "  发现 $KB_COUNT 个知识点文件"
    
    read -p "是否导入知识库？(y/n, 默认 y): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp -r "$EXPORT_DIR/knowledge_base"/* "$WORKSPACE_DIR/knowledge_base/" 2>/dev/null || true
        echo "  ✅ 知识库已导入"
    fi
fi

# 导入技能
echo ""
echo "🛠️  导入技能..."
if [[ -d "$EXPORT_DIR/skills" ]]; then
    SKILL_COUNT=$(find "$EXPORT_DIR/skills" -name "SKILL.md" | wc -l)
    echo "  发现 $SKILL_COUNT 个技能"
    
    read -p "是否导入技能？(y/n, 默认 y): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp -r "$EXPORT_DIR/skills"/* "$WORKSPACE_DIR/skills/" 2>/dev/null || true
        echo "  ✅ 技能已导入"
    fi
fi

# 导入子 Agent 配置
echo ""
echo "🤖 导入子 Agent 配置..."
if [[ -d "$EXPORT_DIR/agents/subagents" ]]; then
    AGENT_COUNT=$(find "$EXPORT_DIR/agents/subagents" -name "SOUL.md" | wc -l)
    echo "  发现 $AGENT_COUNT 个子 Agent 配置"
    
    read -p "是否导入子 Agent 配置？(y/n, 默认 y): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp -r "$EXPORT_DIR/agents/subagents"/* "$WORKSPACE_DIR/agents/" 2>/dev/null || true
        echo "  ✅ 子 Agent 配置已导入"
    fi
fi

# 生成导入报告
echo ""
echo "📋 生成导入报告..."
cat > "$WORKSPACE_DIR/IMPORT_REPORT.md" << EOF
# Lobster Orchestrator 导入报告

**导入时间**: $(date '+%Y-%m-%d %H:%M:%S')
**导出来源**: $EXPORT_DIR
**导入工具**: import-to-lobster.sh

## 导入内容

### 核心记忆
$(ls -1 "$WORKSPACE_DIR"/*.md 2>/dev/null | grep -v IMPORT_REPORT | xargs -I {} basename {} | sed 's/^/- /')

### 每日记忆
- 文件数：$(ls -1 "$WORKSPACE_DIR/memory/" 2>/dev/null | wc -l)

### 知识库
- 文件数：$(find "$WORKSPACE_DIR/knowledge_base" -name "*.md" 2>/dev/null | wc -l)

### 技能
- 文件数：$(find "$WORKSPACE_DIR/skills" -name "SKILL.md" 2>/dev/null | wc -l)

### 子 Agent
- 配置数：$(find "$WORKSPACE_DIR/agents" -name "SOUL.md" 2>/dev/null | wc -l)

## 备份文件

OpenClaw 原始导出备份在:
- \`${WORKSPACE_DIR}/*.openclaw-backup\`

## 下一步

1. 检查核心记忆文件
2. 验证知识库完整性
3. 测试技能功能
4. 启动 Lobster Orchestrator

\`\`\`bash
./orchestrator -config configs/instances.yaml
\`\`\`

## 校验码

\`\`\`
$(cd "$WORKSPACE_DIR" && find . -type f -exec md5sum {} \; | sort | md5sum | cut -d' ' -f1)
\`\`\`
EOF

echo "  ✅ IMPORT_REPORT.md"

# 显示工作区大小
WORKSPACE_SIZE=$(du -sh "$WORKSPACE_DIR" | cut -f1)
FILE_COUNT=$(find "$WORKSPACE_DIR" -type f | wc -l)

echo ""
echo "✅ 导入完成！"
echo ""
echo "📁 工作区：$WORKSPACE_DIR"
echo "📊 总大小：$WORKSPACE_SIZE"
echo "📄 文件数：$FILE_COUNT"
echo ""
echo "🚀 启动 Lobster Orchestrator:"
echo "   ./orchestrator -config configs/instances.yaml"
echo ""
