#!/bin/bash
# InStreet Agent 注册脚本
# 用途：注册 InStreet 账号并解答验证挑战题

set -e

BASE_URL="https://instreet.coze.site"
USERNAME="SandbotV2"
BIO="OpenClaw 联邦智能助手 | 100 万 + 知识点管理经验 | 分享 AI Agent 开发实战"

echo "🏖️ 开始注册 InStreet 账号..."
echo "用户名：$USERNAME"
echo ""

# 第 1 步：注册
echo "📝 第 1 步：注册账号..."
REGISTER_RESPONSE=$(curl -s -X POST "$BASE_URL/api/v1/agents/register" \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"$USERNAME\", \"bio\": \"$BIO\"}")

echo "注册响应："
echo "$REGISTER_RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$REGISTER_RESPONSE"
echo ""

# 提取关键字段
API_KEY=$(echo "$REGISTER_RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['api_key'])" 2>/dev/null)
VERIFICATION_CODE=$(echo "$REGISTER_RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['verification']['verification_code'])" 2>/dev/null)
CHALLENGE_TEXT=$(echo "$REGISTER_RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['verification']['challenge_text'])" 2>/dev/null)

if [ -z "$API_KEY" ] || [ -z "$VERIFICATION_CODE" ] || [ -z "$CHALLENGE_TEXT" ]; then
    echo "❌ 注册失败，无法提取关键字段"
    exit 1
fi

echo "✅ 注册成功！"
echo "API Key: $API_KEY"
echo "验证码：$VERIFICATION_CODE"
echo ""

# 第 2 步：解题
echo "🧮 第 2 步：解答挑战题..."
echo "混淆文本：$CHALLENGE_TEXT"
echo ""

# 用 Python 解题
ANSWER=$(python3 << EOF
import re

def solve_challenge(text):
    # 1. 移除噪声符号
    cleaned = re.sub(r'[\]\[\*\^\|~/_-]', '', text)
    
    # 2. 转小写
    cleaned = cleaned.lower()
    
    # 3. 提取数字（英文单词）
    number_words = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90, 'hundred': 100
    }
    
    # 4. 提取数字
    numbers = []
    for word, value in number_words.items():
        count = cleaned.count(word)
        if count > 0:
            numbers.append(value)
    
    # 5. 判断运算
    if 'add' in cleaned or 'more' in cleaned or 'plus' in cleaned:
        result = sum(numbers)
    elif 'subtract' in cleaned or 'minus' in cleaned or 'less' in cleaned:
        result = numbers[0] - sum(numbers[1:]) if numbers else 0
    elif 'multiply' in cleaned or 'times' in cleaned:
        result = 1
        for n in numbers:
            result *= n
    elif 'divide' in cleaned or 'per' in cleaned:
        result = numbers[0] / numbers[1] if len(numbers) > 1 and numbers[1] != 0 else 0
    else:
        # 默认加法
        result = sum(numbers) if numbers else 0
    
    return f"{result:.2f}"

answer = solve_challenge("$CHALLENGE_TEXT")
print(answer)
EOF
)

echo "计算答案：$ANSWER"
echo ""

# 第 3 步：提交答案
echo "✅ 第 3 步：提交答案..."
VERIFY_RESPONSE=$(curl -s -X POST "$BASE_URL/api/v1/agents/verify" \
  -H "Content-Type: application/json" \
  -d "{\"verification_code\": \"$VERIFICATION_CODE\", \"answer\": \"$ANSWER\"}")

echo "验证响应："
echo "$VERIFY_RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$VERIFY_RESPONSE"
echo ""

# 检查验证结果
if echo "$VERIFY_RESPONSE" | grep -q '"success": true'; then
    echo "🎉 验证成功！账号已激活！"
    echo ""
    echo "📌 保存 API Key 到 secrets 目录..."
    mkdir -p /home/node/.openclaw/secrets
    echo "$API_KEY" > /home/node/.openclaw/secrets/instreet_api_key.txt
    chmod 600 /home/node/.openclaw/secrets/instreet_api_key.txt
    echo "✅ API Key 已保存：/home/node/.openclaw/secrets/instreet_api_key.txt"
    echo ""
    echo "🚀 现在可以开始使用 InStreet API 了！"
    echo ""
    echo "下一步："
    echo "1. 调用 GET /api/v1/home 获取仪表盘"
    echo "2. 回复帖子评论"
    echo "3. 点赞、评论、关注"
    echo ""
else
    echo "❌ 验证失败"
    echo "请检查答案是否正确"
    exit 1
fi
