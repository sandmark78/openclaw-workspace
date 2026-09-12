#!/bin/bash
# 缓存读取封装 - 优先读缓存，miss 时读源文件并缓存
# 用法: source scripts/cache-read.sh
#        cached_read "config" "MEMORY.md" "/path/to/MEMORY.md"

CACHE_DIR="/home/node/.openclaw/workspace/memory/cache"
CACHE_SCRIPT="/home/node/.openclaw/workspace/scripts/cache-manager.py"

cached_read() {
    local cache_type="$1"    # config / file / fetch / search
    local identifier="$2"    # 缓存标识
    local source_path="$3"   # 源文件路径（缓存 miss 时读取）
    
    # 尝试从缓存读取
    local cached=$(python3 "$CACHE_SCRIPT" get "$cache_type" "$identifier" 2>/dev/null)
    
    if [ -n "$cached" ] && [ "$cached" != "❌ 缓存未命中或已过期" ]; then
        echo "$cached"
        return 0
    fi
    
    # 缓存 miss，从源文件读取并缓存
    if [ -f "$source_path" ]; then
        local content=$(cat "$source_path")
        python3 "$CACHE_SCRIPT" set "$cache_type" "$identifier" "$content" 2>/dev/null
        echo "$content"
        return 0
    fi
    
    return 1
}

# 快速缓存检查（不读源文件，只检查缓存是否存在）
cache_check() {
    local cache_type="$1"
    local identifier="$2"
    python3 "$CACHE_SCRIPT" get "$cache_type" "$identifier" >/dev/null 2>&1
}

# 缓存清理（每日心跳时调用）
cache_cleanup() {
    python3 "$CACHE_SCRIPT" cleanup 2>/dev/null
}
