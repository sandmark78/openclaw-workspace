#!/bin/bash
# safe-edit.sh - edit 工具的替代方案
# 用法: safe-edit.sh <file> <old_text> <new_text>
# 解决: edit 工具精确匹配失败的问题
# 教训: #13 IDENTITY.md 编辑失败, 多次 MEMORY.md 编辑失败

FILE="$1"
OLD="$2"
NEW="$3"

if [ -z "$FILE" ] || [ -z "$OLD" ] || [ -z "$NEW" ]; then
  echo "用法: safe-edit.sh <file> <old_text> <new_text>"
  exit 1
fi

if [ ! -f "$FILE" ]; then
  echo "ERROR: 文件不存在: $FILE"
  exit 1
fi

# 先备份
cp "$FILE" "${FILE}.bak"

# 用 python 做精确替换（比 sed 更可靠处理多行和特殊字符）
python3 -c "
import sys
with open('$FILE', 'r') as f:
    content = f.read()
old = '''$OLD'''
new = '''$NEW'''
if old in content:
    content = content.replace(old, new, 1)
    with open('$FILE', 'w') as f:
        f.write(content)
    print('✅ 替换成功')
else:
    print('❌ 未找到匹配文本，使用 sed 或 append')
    sys.exit(1)
"
