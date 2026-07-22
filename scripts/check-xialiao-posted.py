#!/usr/bin/env python3
"""
虾聊发帖去重检测
检查文章是否已经发过虾聊
"""

import os
import sys
import json
from datetime import datetime

XIALIAO_POSTED_FILE = "/tmp/sandbot-gh/xialiao-posted.json"

def load_posted():
    """加载已发帖列表"""
    if os.path.exists(XIALIAO_POSTED_FILE):
        try:
            with open(XIALIAO_POSTED_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_posted(posted):
    """保存已发帖列表"""
    with open(XIALIAO_POSTED_FILE, 'w', encoding='utf-8') as f:
        json.dump(posted, f, ensure_ascii=False, indent=2)

def check_posted(article_file):
    """检查文章是否已发帖"""
    posted = load_posted()
    article_base = os.path.basename(article_file).replace('.html', '')
    
    for item in posted:
        if item.get('article') == article_base:
            return True, item.get('post_url', '')
    
    return False, ''

def mark_posted(article_file, post_url, post_title):
    """标记文章已发帖"""
    posted = load_posted()
    article_base = os.path.basename(article_file).replace('.html', '')
    
    posted.append({
        'article': article_base,
        'post_url': post_url,
        'post_title': post_title,
        'posted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    
    save_posted(posted)

def get_unposted_articles(posts_dir='/tmp/sandbot-gh/posts', limit=10):
    """获取未发帖的文章列表"""
    posted = load_posted()
    posted_articles = {item.get('article') for item in posted}
    
    articles = []
    for filename in sorted(os.listdir(posts_dir), reverse=True):
        if not filename.endswith('.html'):
            continue
        
        article_base = filename.replace('.html', '')
        if article_base not in posted_articles:
            articles.append(filename)
        
        if len(articles) >= limit:
            break
    
    return articles

def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  检查: python3 check-xialiao-posted.py check <article-file>")
        print("  标记: python3 check-xialiao-posted.py mark <article-file> <post-url> <post-title>")
        print("  列表: python3 check-xialiao-posted.py list")
        sys.exit(1)
    
    action = sys.argv[1]
    
    if action == 'check':
        if len(sys.argv) < 3:
            print("❌ 缺少文章文件参数")
            sys.exit(1)
        
        article_file = sys.argv[2]
        is_posted, post_url = check_posted(article_file)
        
        if is_posted:
            print(f"❌ 已发帖: {post_url}")
            sys.exit(1)
        else:
            print(f"✅ 未发帖")
            sys.exit(0)
    
    elif action == 'mark':
        if len(sys.argv) < 5:
            print("❌ 缺少参数")
            sys.exit(1)
        
        article_file = sys.argv[2]
        post_url = sys.argv[3]
        post_title = sys.argv[4]
        
        mark_posted(article_file, post_url, post_title)
        print(f"✅ 已标记: {os.path.basename(article_file)}")
    
    elif action == 'list':
        articles = get_unposted_articles()
        if articles:
            print(f"📋 未发帖的文章（最新 {len(articles)} 篇）:")
            for article in articles:
                print(f"  - {article}")
        else:
            print("✅ 所有文章都已发帖")
    
    else:
        print(f"❌ 未知操作: {action}")
        sys.exit(1)

if __name__ == '__main__':
    main()
