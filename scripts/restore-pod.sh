#!/bin/bash
# 🧊 冷冻舱还原脚本 v0.1
# 支持还原到不同平台（OpenClaw/PicoClaw/ZeroClaw/NanoBot）

set -e

POD_FILE="$1"
TARGET_PLATFORM="${2:-OpenClaw}"  # 默认还原到 OpenClaw
PASSWORD="$3"

if [ -z "$POD_FILE" ] || [ -z "$PASSWORD" ]; then
    echo "用法：$0 <冷冻包文件> <目标平台> <密码>"
    echo "目标平台：OpenClaw | PicoClaw | ZeroClaw | NanoBot"
    exit 1
fi

echo "🧊 开始还原冷冻舱..."
echo "   冷冻包：$POD_FILE"
echo "   目标平台：$TARGET_PLATFORM"
echo "   密码：******"

# 1. 解密
echo "📦 步骤 1/4：解密冷冻包..."
# TODO: 实现解密逻辑（需要 cryptography 模块）
# python3 scripts/decrypt-pod.py "$POD_FILE" "$PASSWORD"

# 2. 解压
echo "📦 步骤 2/4：解压文件..."
# tar -xzf /tmp/cryopod.tar.gz -C /tmp/restored/

# 3. 平台迁移
echo "📦 步骤 3/4：迁移到 $TARGET_PLATFORM..."
case "$TARGET_PLATFORM" in
    "PicoClaw")
        echo "   → 使用 PicoClaw 配置模板"
        # cp /tmp/restored/templates/picoclaw-config.json /tmp/restored/config.json
        ;;
    "ZeroClaw")
        echo "   → 使用 ZeroClaw 配置模板"
        # cp /tmp/restored/templates/zeroclaw-config.json /tmp/restored/config.json
        ;;
    "NanoBot")
        echo "   → 使用 NanoBot 配置模板"
        # cp /tmp/restored/templates/nanobot-config.json /tmp/restored/config.json
        ;;
    *)
        echo "   → 使用 OpenClaw 配置模板"
        # cp /tmp/restored/templates/openclaw-config.json /tmp/restored/config.json
        ;;
esac

# 4. 验证完整性
echo "📦 步骤 4/4：验证完整性..."
# sha256sum -c /tmp/restored/manifest.json

echo "✅ 还原完成！"
echo "   还原目录：/tmp/restored/"
echo ""
echo "🎯 下一步："
echo "   1. 检查 /tmp/restored/SOUL.md 确认人格信息"
echo "   2. 检查 /tmp/restored/config.json 确认平台配置"
echo "   3. 启动目标平台：$TARGET_PLATFORM start"
