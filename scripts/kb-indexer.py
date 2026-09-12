#!/usr/bin/env python3
"""
知识库索引生成器 - 提高检索效率
生成倒排索引、主题分类、快速查找表
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

WORKSPACE = Path("/home/node/.openclaw/workspace")
KB_DIR = WORKSPACE / "knowledge_base"
INDEX_FILE = WORKSPACE / "memory" / "kb-index.json"

class KnowledgeBaseIndexer:
    def __init__(self):
        self.index = {
            'metadata': {
                'generated': datetime.now().isoformat(),
                'total_files': 0,
                'total_size': 0
            },
            'by_topic': defaultdict(list),
            'by_date': defaultdict(list),
            'by_category': defaultdict(list),
            'keywords': defaultdict(list),
            'files': {}
        }
    
    def extract_keywords(self, content, max_keywords=10):
        """提取关键词"""
        # 简单关键词提取：中文词组 + 英文单词
        # 移除常见停用词
        stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很', '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这'}
        
        # 提取中文词组（2-4字）
        chinese_words = re.findall(r'[\u4e00-\u9fa5]{2,4}', content)
        # 提取英文单词
        english_words = re.findall(r'\b[a-zA-Z]{3,}\b', content)
        
        # 统计词频
        word_freq = defaultdict(int)
        for word in chinese_words + english_words:
            word_lower = word.lower()
            if word_lower not in stop_words and len(word) > 1:
                word_freq[word_lower] += 1
        
        # 返回最高频的关键词
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [w[0] for w in sorted_words[:max_keywords]]
    
    def extract_title(self, content, filename):
        """提取标题"""
        # 尝试从内容提取标题（第一个 # 标题）
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        
        # 使用文件名
        return Path(filename).stem.replace('-', ' ').replace('_', ' ').title()
    
    def categorize_file(self, filepath):
        """根据路径分类"""
        rel_path = filepath.relative_to(KB_DIR)
        parts = rel_path.parts
        
        if len(parts) > 1:
            # 第一级目录作为分类
            return parts[0]
        return 'root'
    
    def extract_topic(self, filepath, content):
        """提取主题"""
        # 从路径提取主题
        rel_path = filepath.relative_to(KB_DIR)
        parts = rel_path.parts
        
        if len(parts) > 1:
            # 目录名作为主题
            dir_name = parts[0]
            # 清理目录名
            topic = re.sub(r'^\d+-', '', dir_name)  # 移除数字前缀
            return topic.replace('-', ' ').replace('_', ' ').title()
        
        return 'General'
    
    def scan_file(self, filepath):
        """扫描单个文件"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_stat = filepath.stat()
            
            # 提取信息
            title = self.extract_title(content, filepath.name)
            keywords = self.extract_keywords(content)
            category = self.categorize_file(filepath)
            topic = self.extract_topic(filepath, content)
            
            # 文件信息
            file_info = {
                'path': str(filepath.relative_to(WORKSPACE)),
                'title': title,
                'size': file_stat.st_size,
                'modified': datetime.fromtimestamp(file_stat.st_mtime).isoformat(),
                'keywords': keywords,
                'category': category,
                'topic': topic
            }
            
            # 添加到索引
            rel_path = str(filepath.relative_to(WORKSPACE))
            self.index['files'][rel_path] = file_info
            
            # 按主题索引
            self.index['by_topic'][topic].append(rel_path)
            
            # 按分类索引
            self.index['by_category'][category].append(rel_path)
            
            # 按日期索引（按月）
            month = file_info['modified'][:7]  # YYYY-MM
            self.index['by_date'][month].append(rel_path)
            
            # 关键词索引
            for keyword in keywords:
                self.index['keywords'][keyword].append(rel_path)
            
            # 更新统计
            self.index['metadata']['total_files'] += 1
            self.index['metadata']['total_size'] += file_stat.st_size
            
        except Exception as e:
            print(f"⚠️  跳过 {filepath}: {e}")
    
    def scan_all(self):
        """扫描所有文件"""
        print(f"🔍 扫描知识库: {KB_DIR}")
        
        md_files = list(KB_DIR.rglob('*.md'))
        print(f"   找到 {len(md_files)} 个 Markdown 文件")
        
        for i, filepath in enumerate(md_files, 1):
            if i % 500 == 0:
                print(f"   进度: {i}/{len(md_files)}")
            self.scan_file(filepath)
        
        print(f"✅ 扫描完成: {self.index['metadata']['total_files']} 个文件")
    
    def save_index(self):
        """保存索引"""
        # 转换 defaultdict 为普通 dict
        index_data = {
            'metadata': self.index['metadata'],
            'by_topic': dict(self.index['by_topic']),
            'by_date': dict(self.index['by_date']),
            'by_category': dict(self.index['by_category']),
            'keywords': dict(self.index['keywords']),
            'files': self.index['files']
        }
        
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 索引已保存: {INDEX_FILE}")
        print(f"   大小: {INDEX_FILE.stat().st_size / 1024:.1f} KB")
    
    def generate_summary(self):
        """生成索引摘要"""
        summary = f"""# 知识库索引摘要

**生成时间**: {self.index['metadata']['generated']}
**总文件数**: {self.index['metadata']['total_files']}
**总大小**: {self.index['metadata']['total_size'] / 1024 / 1024:.1f} MB

## 按主题分布

"""
        
        # 按主题统计
        topic_counts = [(topic, len(files)) for topic, files in self.index['by_topic'].items()]
        topic_counts.sort(key=lambda x: x[1], reverse=True)
        
        for topic, count in topic_counts[:15]:
            summary += f"- **{topic}**: {count} 个文件\n"
        
        summary += "\n## 按分类分布\n\n"
        
        # 按分类统计
        cat_counts = [(cat, len(files)) for cat, files in self.index['by_category'].items()]
        cat_counts.sort(key=lambda x: x[1], reverse=True)
        
        for cat, count in cat_counts[:10]:
            summary += f"- **{cat}**: {count} 个文件\n"
        
        summary += "\n## 热门关键词\n\n"
        
        # 热门关键词
        keyword_counts = [(kw, len(files)) for kw, files in self.index['keywords'].items()]
        keyword_counts.sort(key=lambda x: x[1], reverse=True)
        
        for kw, count in keyword_counts[:20]:
            summary += f"- `{kw}`: {count} 次\n"
        
        return summary

def main():
    indexer = KnowledgeBaseIndexer()
    
    print("📚 开始构建知识库索引...")
    indexer.scan_all()
    
    print("\n💾 保存索引...")
    indexer.save_index()
    
    print("\n📊 生成摘要...")
    summary = indexer.generate_summary()
    
    summary_file = WORKSPACE / "memory" / "kb-index-summary.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"✅ 摘要已保存: {summary_file}")
    print("\n" + "="*50)
    print(summary)

if __name__ == '__main__':
    main()
