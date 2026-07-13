#!/usr/bin/env python3
"""
🧠 记忆压缩脚本 v0.1
用于将大记忆文件压缩到目标 token 数，适配不同平台的上下文窗口
"""

import sys
import re

def count_tokens(text):
    """估算 token 数（简单按字符/4 计算）"""
    return len(text) // 4

def compress_memory(input_path, output_path, max_tokens=5000):
    """压缩记忆文件"""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 简单压缩策略：保留重要章节
    sections = content.split('## ')
    
    # 优先保留的章节
    priority_sections = ['核心身份', '核心原则', '血泪教训', '使命']
    
    compressed = []
    current_tokens = 0
    
    for section in sections:
        if not section.strip():
            continue
        
        # 检查是否是优先章节
        is_priority = any(p in section for p in priority_sections)
        
        section_tokens = count_tokens(section)
        
        if current_tokens + section_tokens <= max_tokens:
            compressed.append(f"## {section}")
            current_tokens += section_tokens
        elif is_priority and current_tokens < max_tokens * 0.8:
            # 优先章节可以稍微超出
            compressed.append(f"## {section}")
            current_tokens += section_tokens
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(compressed))
    
    print(f"✅ 记忆压缩完成！")
    print(f"   原始：{count_tokens(content)} tokens")
    print(f"   压缩后：{current_tokens} tokens")
    print(f"   压缩率：{current_tokens/count_tokens(content)*100:.1f}%")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("用法：python3 compress-memory.py <输入文件> <输出文件> <最大 tokens>")
        sys.exit(1)
    
    compress_memory(sys.argv[1], sys.argv[2], int(sys.argv[3]))
