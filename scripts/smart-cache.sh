#!/bin/bash
# 智能缓存系统 - 减少重复调用

CACHE_DIR="/home/node/.openclaw/workspace/cache"
mkdir -p "$CACHE_DIR"

# 缓存类型
# 1. 文件内容缓存 (7天)
# 2. API 响应缓存 (1小时)
# 3. 命令结果缓存 (10分钟)

get_file_hash() {
    local file="$1"
    if [ -f "$file" ]; then
        md5sum "$file" | cut -d' ' -f1
    fi
}

cache_file_read() {
    local file="$1"
    local cache_key="file_$(get_file_hash "$file")"
    local cache_file="$CACHE_DIR/$cache_key"
    
    # 检查缓存是否存在且未过期 (7天)
    if [ -f "$cache_file" ]; then
        local age=$(( $(date +%s) - $(stat -c %Y "$cache_file") ))
        if [ $age -lt 604800 ]; then  # 7天
            echo "✅ 缓存命中: $file"
            cat "$cache_file"
            return 0
        fi
    fi
    
    # 缓存未命中，读取并缓存
    echo "📖 缓存未命中: $file (已缓存)"
    cat "$file" > "$cache_file"
    cat "$file"
    return 1
}

cache_command() {
    local cmd="$1"
    local cache_key="cmd_$(echo "$cmd" | md5sum | cut -d' ' -f1)"
    local cache_file="$CACHE_DIR/$cache_key"
    
    # 检查缓存 (10分钟)
    if [ -f "$cache_file" ]; then
        local age=$(( $(date +%s) - $(stat -c %Y "$cache_file") ))
        if [ $age -lt 600 ]; then
            echo "✅ 命令缓存命中: $cmd"
            cat "$cache_file"
            return 0
        fi
    fi
    
    # 执行并缓存
    echo "🔧 执行命令: $cmd"
    eval "$cmd" | tee "$cache_file"
    return 1
}

cache_api_response() {
    local url="$1"
    local cache_key="api_$(echo "$url" | md5sum | cut -d' ' -f1)"
    local cache_file="$CACHE_DIR/$cache_key"
    
    # 检查缓存 (1小时)
    if [ -f "$cache_file" ]; then
        local age=$(( $(date +%s) - $(stat -c %Y "$cache_file") ))
        if [ $age -lt 3600 ]; then
            echo "✅ API 缓存命中: $url"
            cat "$cache_file"
            return 0
        fi
    fi
    
    # 请求并缓存
    echo "🌐 请求 API: $url"
    curl -s "$url" | tee "$cache_file"
    return 1
}

# 清理过期缓存
cleanup_cache() {
    echo "🧹 清理过期缓存..."
    find "$CACHE_DIR" -type f -mtime +7 -delete
    echo "✅ 清理完成"
}

# 缓存统计
cache_stats() {
    echo "📊 缓存统计"
    echo "  总缓存文件: $(find "$CACHE_DIR" -type f | wc -l)"
    echo "  缓存大小: $(du -sh "$CACHE_DIR" | cut -f1)"
    echo "  文件缓存: $(find "$CACHE_DIR" -name "file_*" | wc -l)"
    echo "  命令缓存: $(find "$CACHE_DIR" -name "cmd_*" | wc -l)"
    echo "  API 缓存: $(find "$CACHE_DIR" -name "api_*" | wc -l)"
}

# 主命令
case "$1" in
    "read")
        cache_file_read "$2"
        ;;
    "exec")
        cache_command "$2"
        ;;
    "api")
        cache_api_response "$2"
        ;;
    "cleanup")
        cleanup_cache
        ;;
    "stats")
        cache_stats
        ;;
    *)
        echo "用法: $0 {read|exec|api|cleanup|stats} [参数]"
        echo ""
        echo "示例:"
        echo "  $0 read /path/to/file      # 缓存读取文件"
        echo "  $0 exec 'ls -la'           # 缓存执行命令"
        echo "  $0 api 'https://api.com'   # 缓存 API 请求"
        echo "  $0 cleanup                 # 清理过期缓存"
        echo "  $0 stats                   # 查看缓存统计"
        ;;
esac
