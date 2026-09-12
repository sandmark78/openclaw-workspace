#!/usr/bin/env python3
"""分批提取博客文章实用技术"""
import re, sys
from collections import defaultdict
from pathlib import Path
from datetime import datetime

POSTS_DIR = Path('/tmp/sandbot-gh/posts')
OUTPUT_FILE = Path('/home/node/.openclaw/workspace/memory/practical-techniques.md')

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

def extract(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        title_match = re.search(r'<title>([^<]+)</title>', content)
        title = title_match.group(1) if title_match else filepath.name
        text = re.sub(r'<[^>]+>', ' ', content)
        text = re.sub(r'\s+', ' ', text)
        sentences = text.split('。')
        techniques = defaultdict(list)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 20 or len(sentence) > 200:
                continue
            for category, keywords in TECHNIQUE_CATEGORIES.items():
                if any(kw in sentence.lower() for kw in keywords):
                    techniques[category].append(sentence)
        return title, techniques
    except:
        return None, {}

def main():
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    
    articles = sorted(POSTS_DIR.glob('*.html'))[start:end]
    all_techniques = defaultdict(list)
    article_count = 0
    
    for article in articles:
        title, techniques = extract(article)
        if title and techniques:
            article_count += 1
            for category, sentences in techniques.items():
                all_techniques[category].extend(sentences[:3])
    
    # 追加到现有报告
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n\n## 批次 {start}-{end} 统计\n\n")
        f.write(f"**扫描范围**: 第{start+1}-{end}篇\n")
        f.write(f"**有效文章**: {article_count}\n")
        f.write(f"**提取时间**: {datetime.now().strftime('%H:%M')}\n\n")
        
        for category, sentences in sorted(all_techniques.items(), key=lambda x: len(x[1]), reverse=True):
            if sentences:
                f.write(f"### {category} ({len(sentences)} 条)\n\n")
                unique = list(set(sentences))[:5]
                for s in unique:
                    f.write(f"- {s}\n")
                f.write("\n")
    
    print(f"✅ 批次{start}-{end}: {article_count}篇, {sum(len(s) for s in all_techniques.values())}条")

if __name__ == '__main__':
    main()
