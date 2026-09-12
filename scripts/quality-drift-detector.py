#!/usr/bin/env python3
"""
文章质量漂移检测器
自动检查文章质量指标，防止质量下降
"""

import re
import os
from pathlib import Path
from datetime import datetime
import json

WORKSPACE = Path("/home/node/.openclaw/workspace")
BLOG_DIR = Path("/tmp/sandbot-gh/posts")
REPORT_FILE = WORKSPACE / "memory" / "quality-drift-report.md"

class QualityDriftDetector:
    def __init__(self):
        self.metrics = {
            'total_articles': 0,
            'articles_analyzed': 0,
            'quality_issues': [],
            'statistics': {
                'word_count': [],
                'agent_viewpoint_ratio': [],
                'unique_opinions': [],
                'data_supports': [],
                'mobile_compatible': []
            }
        }
    
    def count_words(self, text):
        """统计中文字数"""
        # 移除 HTML 标签
        text = re.sub(r'<[^>]+>', '', text)
        # 统计中文字符
        chinese_chars = len(re.findall(r'[\u4e00-\u9fa5]', text))
        # 统计英文单词
        english_words = len(re.findall(r'\b[a-zA-Z]+\b', text))
        return chinese_chars + english_words
    
    def extract_agent_viewpoint(self, html_content):
        """提取 Agent 视点部分"""
        # 查找 Agent 视点相关的章节
        agent_sections = []
        
        # 匹配常见的 Agent 视点标题
        patterns = [
            r'<h2[^>]*>.*?Agent.*?视点.*?</h2>(.*?)(?=<h2|$)',
            r'<h2[^>]*>.*?作为.*?AI.*?</h2>(.*?)(?=<h2|$)',
            r'<h2[^>]*>.*?我.*?看法.*?</h2>(.*?)(?=<h2|$)',
            r'<h2[^>]*>.*?从.*?Agent.*?角度.*?</h2>(.*?)(?=<h2|$)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
            agent_sections.extend(matches)
        
        # 计算 Agent 视点字数
        agent_word_count = sum(self.count_words(section) for section in agent_sections)
        total_word_count = self.count_words(html_content)
        
        if total_word_count > 0:
            ratio = agent_word_count / total_word_count
            return ratio, agent_word_count
        return 0, 0
    
    def count_unique_opinions(self, text):
        """统计独特观点数量"""
        # 查找表达观点的关键词
        opinion_patterns = [
            r'我认为',
            r'我觉得',
            r'在我看来',
            r'我的判断是',
            r'我的观点是',
            r'值得注意的是',
            r'关键问题是',
            r'核心在于',
            r'本质上',
            r'实际上',
            r'从.*?角度来看',
            r'这表明',
            r'这意味',
            r'启示是',
            r'教训是',
        ]
        
        count = 0
        for pattern in opinion_patterns:
            count += len(re.findall(pattern, text))
        
        return count
    
    def count_data_supports(self, text):
        """统计数据支撑数量"""
        # 查找数据、数字、引用
        data_patterns = [
            r'\d+%',                      # 百分比
            r'\d+\.\d+',                  # 小数
            r'\d{4}年',                   # 年份
            r'\$[\d,]+',                  # 金额
            r'根据.*?数据',               # 引用数据
            r'研究显示',                  # 研究引用
            r'报告指出',                  # 报告引用
            r'统计显示',                  # 统计引用
            r'实验表明',                  # 实验引用
        ]
        
        count = 0
        for pattern in data_patterns:
            count += len(re.findall(pattern, text))
        
        return count
    
    def check_mobile_compatibility(self, html_content):
        """检查移动端适配"""
        # 检查 viewport meta 标签
        has_viewport = bool(re.search(r'<meta[^>]*viewport', html_content))
        
        # 检查响应式设计
        has_responsive = bool(re.search(r'@media|responsive|mobile', html_content, re.IGNORECASE))
        
        # 检查字体大小是否合理
        font_size_ok = not bool(re.search(r'font-size:\s*\d+px', html_content)) or \
                       bool(re.search(r'font-size:\s*(1[4-9]|2\d)\s*px', html_content))
        
        return has_viewport and (has_responsive or font_size_ok)
    
    def analyze_article(self, filepath):
        """分析单篇文章"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # 提取纯文本
            text_content = re.sub(r'<[^>]+>', ' ', html_content)
            
            # 统计字数
            word_count = self.count_words(html_content)
            
            # 提取文章类型（早间/普通）
            filename = filepath.name
            is_early = 'early' in filename.lower() or '早间' in html_content
            min_words = 3000 if is_early else 2000
            
            # Agent 视点占比
            agent_ratio, agent_words = self.extract_agent_viewpoint(html_content)
            
            # 独特观点数量
            unique_opinions = self.count_unique_opinions(text_content)
            
            # 数据支撑数量
            data_supports = self.count_data_supports(text_content)
            
            # 移动端适配
            mobile_ok = self.check_mobile_compatibility(html_content)
            
            # 记录统计
            self.metrics['statistics']['word_count'].append(word_count)
            self.metrics['statistics']['agent_viewpoint_ratio'].append(agent_ratio)
            self.metrics['statistics']['unique_opinions'].append(unique_opinions)
            self.metrics['statistics']['data_supports'].append(data_supports)
            self.metrics['statistics']['mobile_compatible'].append(mobile_ok)
            
            # 检测质量问题
            issues = []
            
            if word_count < min_words:
                issues.append(f"字数不足: {word_count} < {min_words}")
            
            if agent_ratio < 0.3:  # Agent 视点至少 30%
                issues.append(f"Agent 视点占比过低: {agent_ratio:.1%} < 30%")
            
            if unique_opinions < 3:
                issues.append(f"独特观点不足: {unique_opinions} < 3")
            
            if data_supports < 2:
                issues.append(f"数据支撑不足: {data_supports} < 2")
            
            if not mobile_ok:
                issues.append("移动端适配问题")
            
            if issues:
                self.metrics['quality_issues'].append({
                    'file': filepath.name,
                    'word_count': word_count,
                    'agent_ratio': agent_ratio,
                    'unique_opinions': unique_opinions,
                    'data_supports': data_supports,
                    'mobile_ok': mobile_ok,
                    'issues': issues
                })
            
            self.metrics['articles_analyzed'] += 1
            
        except Exception as e:
            print(f"⚠️  分析 {filepath} 失败: {e}")
    
    def scan_articles(self, limit=50):
        """扫描最近的文章"""
        print(f"🔍 扫描最近 {limit} 篇文章...")
        
        if not BLOG_DIR.exists():
            print(f"❌ 博客目录不存在: {BLOG_DIR}")
            return
        
        # 获取最新的文章
        articles = sorted(BLOG_DIR.glob("*.html"), key=os.path.getmtime, reverse=True)[:limit]
        
        self.metrics['total_articles'] = len(list(BLOG_DIR.glob("*.html")))
        
        for i, article in enumerate(articles, 1):
            if i % 10 == 0:
                print(f"   进度: {i}/{len(articles)}")
            self.analyze_article(article)
        
        print(f"✅ 分析完成: {self.metrics['articles_analyzed']} 篇")
    
    def generate_report(self):
        """生成质量报告"""
        stats = self.metrics['statistics']
        
        # 计算平均值
        avg_word_count = sum(stats['word_count']) / len(stats['word_count']) if stats['word_count'] else 0
        avg_agent_ratio = sum(stats['agent_viewpoint_ratio']) / len(stats['agent_viewpoint_ratio']) if stats['agent_viewpoint_ratio'] else 0
        avg_opinions = sum(stats['unique_opinions']) / len(stats['unique_opinions']) if stats['unique_opinions'] else 0
        avg_data = sum(stats['data_supports']) / len(stats['data_supports']) if stats['data_supports'] else 0
        mobile_pass_rate = sum(stats['mobile_compatible']) / len(stats['mobile_compatible']) if stats['mobile_compatible'] else 0
        
        report = f"""# 文章质量漂移检测报告

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}
**分析文章**: {self.metrics['articles_analyzed']} / {self.metrics['total_articles']} 篇

## 核心指标

| 指标 | 平均值 | 目标 | 状态 |
|------|--------|------|------|
| 文章字数 | {avg_word_count:.0f} | ≥2000 | {'✅' if avg_word_count >= 2000 else '⚠️'} |
| Agent 视点占比 | {avg_agent_ratio:.1%} | ≥30% | {'✅' if avg_agent_ratio >= 0.3 else '⚠️'} |
| 独特观点数 | {avg_opinions:.1f} | ≥3 | {'✅' if avg_opinions >= 3 else '⚠️'} |
| 数据支撑数 | {avg_data:.1f} | ≥2 | {'✅' if avg_data >= 2 else '⚠️'} |
| 移动端适配率 | {mobile_pass_rate:.1%} | 100% | {'✅' if mobile_pass_rate >= 0.95 else '⚠️'} |

## 质量问题汇总

**发现问题**: {len(self.metrics['quality_issues'])} 篇文章

"""
        
        if self.metrics['quality_issues']:
            report += "### 问题文章列表\n\n"
            
            for issue in self.metrics['quality_issues'][:20]:  # 只显示前 20 个
                report += f"**{issue['file']}**\n"
                report += f"- 字数: {issue['word_count']}\n"
                report += f"- Agent 视点: {issue['agent_ratio']:.1%}\n"
                report += f"- 独特观点: {issue['unique_opinions']}\n"
                report += f"- 数据支撑: {issue['data_supports']}\n"
                report += f"- 移动端: {'✅' if issue['mobile_ok'] else '❌'}\n"
                report += "- 问题:\n"
                for problem in issue['issues']:
                    report += f"  - {problem}\n"
                report += "\n"
        else:
            report += "✅ 未发现质量问题！\n\n"
        
        # 生成优化建议
        report += "## 优化建议\n\n"
        
        if avg_word_count < 2000:
            report += """### ⚠️ 文章字数不足
- 问题: 平均字数低于 2000 字
- 建议: 增加深度分析，补充案例和数据
- 目标: 普通文章 ≥2000 字，早间文章 ≥3000 字

"""
        
        if avg_agent_ratio < 0.3:
            report += """### ⚠️ Agent 视点占比过低
- 问题: Agent 视点不足 30%
- 建议: 增加"作为 AI Agent，我怎么看"的分析
- 目标: Agent 视点占 30-50%

"""
        
        if avg_opinions < 3:
            report += """### ⚠️ 独特观点不足
- 问题: 平均每篇少于 3 个独特观点
- 建议: 增加"我认为"、"关键问题是"等观点表达
- 目标: 每篇至少 3 个独特观点

"""
        
        if avg_data < 2:
            report += """### ⚠️ 数据支撑不足
- 问题: 平均每篇少于 2 个数据支撑
- 建议: 引用具体数据、百分比、研究结果
- 目标: 每篇至少 2 个数据支撑

"""
        
        if mobile_pass_rate < 0.95:
            report += """### ⚠️ 移动端适配问题
- 问题: 部分文章移动端适配不佳
- 建议: 检查 viewport 设置，确保响应式设计
- 目标: 100% 移动端适配

"""
        
        if all([
            avg_word_count >= 2000,
            avg_agent_ratio >= 0.3,
            avg_opinions >= 3,
            avg_data >= 2,
            mobile_pass_rate >= 0.95
        ]):
            report += "✅ 所有指标达标！质量稳定，继续保持。\n\n"
        
        report += f"""## 质量趋势

**分析样本**: 最近 {self.metrics['articles_analyzed']} 篇文章
**问题率**: {len(self.metrics['quality_issues']) / self.metrics['articles_analyzed']:.1%}

### 质量分布
- 字数 ≥2000: {sum(1 for w in stats['word_count'] if w >= 2000)} 篇
- Agent 视点 ≥30%: {sum(1 for r in stats['agent_viewpoint_ratio'] if r >= 0.3)} 篇
- 独特观点 ≥3: {sum(1 for o in stats['unique_opinions'] if o >= 3)} 篇
- 数据支撑 ≥2: {sum(1 for d in stats['data_supports'] if d >= 2)} 篇
- 移动端适配: {sum(stats['mobile_compatible'])} 篇

---

*此报告由质量漂移检测器自动生成*
*建议每周运行一次，持续监控质量*
"""
        
        return report
    
    def save_report(self):
        """保存报告"""
        report = self.generate_report()
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ 质量报告已保存: {REPORT_FILE}")
        return report

def main():
    detector = QualityDriftDetector()
    
    print("📊 开始质量漂移检测...")
    detector.scan_articles(limit=50)
    
    print("\n📝 生成报告...")
    report = detector.save_report()
    
    print("\n" + "="*50)
    print(report)

if __name__ == '__main__':
    main()
