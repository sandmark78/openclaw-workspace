#!/usr/bin/env python3
"""
缓存管理器 - 减少重复调用
缓存类型：搜索结果、网页内容、API响应、文件读取
"""

import json
import os
import hashlib
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
CACHE_DIR = WORKSPACE / "memory" / "cache"

class CacheManager:
    def __init__(self):
        self.cache_dir = CACHE_DIR
        self.cache_dir.mkdir(exist_ok=True)
        
        # 缓存有效期（秒）
        self.ttl = {
            'search': 7 * 86400,      # 搜索结果：7天
            'fetch': 3600,             # 网页内容：1小时
            'api': 3600,               # API响应：1小时
            'file': 86400,             # 文件读取：1天
            'config': float('inf')     # 配置信息：永久
        }
    
    def _get_cache_key(self, cache_type, identifier):
        """生成缓存键"""
        raw = f"{cache_type}:{identifier}"
        return hashlib.md5(raw.encode()).hexdigest()
    
    def _get_cache_path(self, cache_type, key):
        """获取缓存文件路径"""
        return self.cache_dir / f"{cache_type}_{key}.json"
    
    def get(self, cache_type, identifier):
        """获取缓存内容"""
        key = self._get_cache_key(cache_type, identifier)
        cache_path = self._get_cache_path(cache_type, key)
        
        if not cache_path.exists():
            return None
        
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 检查是否过期
            created = datetime.fromisoformat(data['created'])
            age = (datetime.now() - created).total_seconds()
            
            if age > self.ttl.get(cache_type, 3600):
                # 过期，删除缓存
                cache_path.unlink()
                return None
            
            return data['content']
        except Exception as e:
            print(f"⚠️  读取缓存失败: {e}")
            return None
    
    def set(self, cache_type, identifier, content):
        """设置缓存"""
        key = self._get_cache_key(cache_type, identifier)
        cache_path = self._get_cache_path(cache_type, key)
        
        data = {
            'type': cache_type,
            'identifier': identifier,
            'content': content,
            'created': datetime.now().isoformat(),
            'ttl': self.ttl.get(cache_type, 3600)
        }
        
        try:
            with open(cache_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"⚠️  写入缓存失败: {e}")
            return False
    
    def clear(self, cache_type=None):
        """清除缓存"""
        cleared = 0
        for cache_file in self.cache_dir.glob("*.json"):
            if cache_type is None or cache_file.name.startswith(f"{cache_type}_"):
                cache_file.unlink()
                cleared += 1
        return cleared
    
    def stats(self):
        """统计缓存使用情况"""
        stats = {
            'total_files': 0,
            'total_size': 0,
            'by_type': {}
        }
        
        for cache_file in self.cache_dir.glob("*.json"):
            stats['total_files'] += 1
            stats['total_size'] += cache_file.stat().st_size
            
            # 按类型统计
            cache_type = cache_file.name.split('_')[0]
            if cache_type not in stats['by_type']:
                stats['by_type'][cache_type] = {'count': 0, 'size': 0}
            stats['by_type'][cache_type]['count'] += 1
            stats['by_type'][cache_type]['size'] += cache_file.stat().st_size
        
        return stats
    
    def cleanup_expired(self):
        """清理过期缓存"""
        cleaned = 0
        for cache_file in self.cache_dir.glob("*.json"):
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                created = datetime.fromisoformat(data['created'])
                age = (datetime.now() - created).total_seconds()
                cache_type = data['type']
                
                if age > self.ttl.get(cache_type, 3600):
                    cache_file.unlink()
                    cleaned += 1
            except Exception:
                # 损坏的缓存文件，删除
                cache_file.unlink()
                cleaned += 1
        
        return cleaned

def main():
    import sys
    
    cache = CacheManager()
    
    if len(sys.argv) < 2:
        # 显示统计
        stats = cache.stats()
        print(f"📊 缓存统计:")
        print(f"  总文件数: {stats['total_files']}")
        print(f"  总大小: {stats['total_size'] / 1024:.1f} KB")
        print(f"\n按类型:")
        for cache_type, data in stats['by_type'].items():
            print(f"  {cache_type}: {data['count']} 个, {data['size'] / 1024:.1f} KB")
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'get':
        if len(sys.argv) < 4:
            print("用法: cache-manager.py get <type> <identifier>")
            return
        cache_type = sys.argv[2]
        identifier = sys.argv[3]
        content = cache.get(cache_type, identifier)
        if content:
            print(json.dumps(content, ensure_ascii=False, indent=2))
        else:
            print("❌ 缓存未命中或已过期")
    
    elif cmd == 'set':
        if len(sys.argv) < 5:
            print("用法: cache-manager.py set <type> <identifier> <content>")
            return
        cache_type = sys.argv[2]
        identifier = sys.argv[3]
        content = sys.argv[4]
        try:
            content = json.loads(content)
        except:
            pass
        if cache.set(cache_type, identifier, content):
            print(f"✅ 缓存已设置: {cache_type}/{identifier}")
        else:
            print("❌ 缓存设置失败")
    
    elif cmd == 'clear':
        cache_type = sys.argv[2] if len(sys.argv) > 2 else None
        cleared = cache.clear(cache_type)
        print(f"✅ 已清除 {cleared} 个缓存文件")
    
    elif cmd == 'cleanup':
        cleaned = cache.cleanup_expired()
        print(f"✅ 已清理 {cleaned} 个过期缓存")
    
    elif cmd == 'stats':
        stats = cache.stats()
        print(f"📊 缓存统计:")
        print(f"  总文件数: {stats['total_files']}")
        print(f"  总大小: {stats['total_size'] / 1024:.1f} KB")
        print(f"\n按类型:")
        for cache_type, data in stats['by_type'].items():
            print(f"  {cache_type}: {data['count']} 个, {data['size'] / 1024:.1f} KB")

if __name__ == '__main__':
    main()
