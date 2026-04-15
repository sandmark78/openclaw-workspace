#!/bin/bash
# Lobster Orchestrator 批量创建脚本
# 用法：./scripts/bulk-create.sh [项目名称]

set -e

PROJECT_NAME="${1:-lobster-project}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "🦞 Lobster Orchestrator 批量创建脚本"
echo "===================================="
echo ""

# 批量创建文档
echo "📝 批量创建文档..."

cat > "docs/${PROJECT_NAME}-design.md" << 'EOF'
# 项目设计文档

## 概述

(项目概述)

## 架构

(架构图)

## 模块

(模块说明)

## 接口

(API 接口)

## 数据库

(数据表设计)

---

*最后更新：TIMESTAMP*
EOF

cat > "docs/${PROJECT_NAME}-api.md" << 'EOF'
# API 文档

## 端点

### GET /api/v1/resource

获取资源列表

**响应**:
```json
{
  "success": true,
  "data": []
}
```

### POST /api/v1/resource

创建资源

**请求**:
```json
{
  "name": "string"
}
```

---

*最后更新：TIMESTAMP*
EOF

cat > "docs/${PROJECT_NAME}-test.md" << 'EOF'
# 测试计划

## 单元测试

- [ ] 模块 A 测试
- [ ] 模块 B 测试

## 集成测试

- [ ] API 集成
- [ ] 数据库集成

## 性能测试

- [ ] 负载测试
- [ ] 压力测试

---

*最后更新：TIMESTAMP*
EOF

echo "✅ 创建 3 个文档"

# 批量创建配置
echo "📋 批量创建配置..."

mkdir -p configs

cat > "configs/${PROJECT_NAME}.yaml" << 'EOF'
# 项目配置

app:
  name: PROJECT_NAME
  version: 0.1.0
  port: 8080

database:
  host: localhost
  port: 5432
  name: PROJECT_NAME

logging:
  level: info
  format: json
EOF

echo "✅ 创建 1 个配置"

# 批量创建脚本
echo "🛠️  批量创建脚本..."

mkdir -p scripts

cat > "scripts/${PROJECT_NAME}-setup.sh" << 'SCRIPT'
#!/bin/bash
# 项目安装脚本

set -e

echo "🚀 开始安装..."

# 1. 安装依赖
echo "📦 安装依赖..."

# 2. 配置环境
echo "⚙️  配置环境..."

# 3. 初始化数据库
echo "🗄️  初始化数据库..."

# 4. 启动服务
echo "🚀 启动服务..."

echo "✅ 安装完成！"
SCRIPT

chmod +x "scripts/${PROJECT_NAME}-setup.sh"

cat > "scripts/${PROJECT_NAME}-backup.sh" << 'SCRIPT'
#!/bin/bash
# 项目备份脚本

set -e

BACKUP_DIR="backups/$(date +%Y%m%d_%H%M%S)"

echo "📦 开始备份..."

mkdir -p "$BACKUP_DIR"

# 备份配置
cp -r configs/ "$BACKUP_DIR/"

# 备份数据
cp -r data/ "$BACKUP_DIR/"

echo "✅ 备份完成：$BACKUP_DIR"
SCRIPT

chmod +x "scripts/${PROJECT_NAME}-backup.sh"

echo "✅ 创建 2 个脚本"

# 总结
echo ""
echo "✅ 批量创建完成！"
echo ""
echo "📊 统计:"
echo "  文档：3 个"
echo "  配置：1 个"
echo "  脚本：2 个"
echo "  总计：6 个文件"
echo ""
echo "📁 位置:"
echo "  docs/${PROJECT_NAME}-*.md"
echo "  configs/${PROJECT_NAME}.yaml"
echo "  scripts/${PROJECT_NAME}-*.sh"
echo ""
