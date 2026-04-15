#!/bin/bash
# OpenClaw + opencli-rs 集成脚本
# 用法：./opencli-search.sh <site> <command> [args...]

export PATH=/home/node/.local/bin:$PATH

SITE=$1
COMMAND=$2
shift 2

if [[ -z "$SITE" || -z "$COMMAND" ]]; then
    echo "用法：$0 <site> <command> [args...]"
    echo ""
    echo "示例:"
    echo "  $0 hackernews top --limit 10"
    echo "  $0 bilibili hot --limit 20"
    echo "  $0 zhihu search AI --limit 10"
    echo ""
    echo "可用站点：hackernews, bilibili, zhihu, reddit, twitter, youtube..."
    exit 1
fi

# 执行搜索
opencli-rs "$SITE" "$COMMAND" "$@" --format json
