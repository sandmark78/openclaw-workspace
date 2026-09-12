#!/usr/bin/env python3
"""
从博客文章提取实用技术 - 避免超限
策略：只提取关键段落，按技术分类，输出简洁报告
"""

import re
import os
from collections import defaultdict
from pathlib import Path

POSTS_DIR = Path('/tmp/sandbot-gh/posts')
OUTPUT_FILE = Path('/home/node/.openclaw/workspace/memory/practical-techniques.md')

# 技术分类关键词
TECHNIQUE_CATEGORIES = {
    '批量处理': ['批量', '批处理', '一次搞定', '串成一条链', 'batch'],
    '缓存策略': ['缓存', 'cache', '命中', '重复调用'],
    '索引优化': ['索引', 'index', '检索', '快速查找'],
    '并发处理': ['并发', 'parallel', '同时', 'concurrent'],
    '任务队列': ['队列', 'queue', '任务队列', '调度'],
    '监控追踪': ['监控', '追踪', 'metrics', '可观测'],
    '审计机制': ['审计', 'audit', '检查', '定期'],
    '本地化': ['本地', 'local', '不调用模型', '零成本'],
    '压缩精简': ['压缩', 'compress', '精简', '去重'],
    '优先级管理': ['优先级', 'priority', '重要', '排序']
}

def extract_techniques_from_article(filepath):
    """从单篇文章提取技术要点"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题
        title_match = re.search(r'<title>([^<]+)</title>', content)
        title = title_match.group(1) if title_match else filepath.name
        
        # 去掉HTML标签
        text = re.sub(r'<[^>]+>', ' ', content)
        text = re.sub(r'\s+', ' ', text)
        
        # 按句子分割
        sentences = text.split('。')
        
        # 提取包含技术关键词的句子
        techniques = defaultdict(list)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 20 or len(sentence) > 200:
                continue
            
            for category, keywords in TECHNIQUE_CATEGORIES.items():
                if any(kw in sentence.lower() for kw in keywords):
                    techniques[category].append(sentence)
        
        return title, techniques
    except Exception as e:
        return None, {}

def main():
    print("🔍 扫描博客文章，提取实用技术...")
    
    all_techniques = defaultdict(list)
    article_count = 0
    
    # 只扫描前50篇（避免超限）
    articles = sorted(POSTS_DIR.glob('*.html'))[:50]
    
    for article in articles:
        title, techniques = extract_techniques_from_article(article)
        if title and techniques:
            article_count += 1
            for category, sentences in techniques.items():
                # 每个类别只保留前3条
                all_techniques[category].extend(sentences[:3])
    
    # 生成报告
    from datetime import datetime
    report = f"# 博客文章实用技术提取报告\n\n"
    report += f"**扫描文章数**: {article_count}\n"
    report += f"**提取时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    
    report += "## 技术分类统计\n\n"
    for category, sentences in sorted(all_techniques.items(), key=lambda x: len(x[1]), reverse=True):
        report += f"### {category} ({len(sentences)} 条)\n\n"
        # 去重并只保留前5条
        unique = list(set(sentences))[:5]
        for s in unique:
            report += f"- {s}\n"
        report += "\n"
    
    # 写入文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 报告已生成: {OUTPUT_FILE}")
    print(f"   扫描文章: {article_count}")
    print(f"   技术类别: {len(all_techniques)}")
    print(f"   提取要点: {sum(len(s) for s in all_techniques.values())}")

if __name__ == '__main__':
    main()
