#!/usr/bin/env python3
"""
sandbot-autolearn.py — Hermes 启发的自动学习循环
不改配置文件，纯文件系统实现

功能:
1. 经验自动提炼 — 扫描今天的记忆文件，提取教训/模式/发现
2. 自动创建 skill 草稿 — 发现重复模式就生成 skill 文件
3. 用户偏好建模 — 从对话历史提取老大的偏好
4. 记忆自动摘要 — 长文件自动提炼核心

用法:
  python3 sandbot-autolearn.py extract   # 从今天记忆提取教训
  python3 sandbot-autolearn.py profile   # 更新用户偏好模型
  python3 sandbot-autolearn.py skills    # 检测可复用模式，生成 skill 草稿
  python3 sandbot-autolearn.py nudge     # 检查该记住什么，提醒写入
  python3 sandbot-autolearn.py all       # 全部执行
"""

import sys
import os
import json
import re
import glob
from datetime import datetime, timedelta
from collections import Counter

WORKSPACE = os.path.expanduser("~/.openclaw/workspace")
MEMORY_DIR = os.path.join(WORKSPACE, "memory")
LEARN_DB = os.path.join(MEMORY_DIR, "autolearn-db.json")

def load_db():
    if os.path.exists(LEARN_DB):
        with open(LEARN_DB, 'r') as f:
            return json.load(f)
    return {
        "lessons": [],         # 提炼的教训
        "patterns": [],        # 发现的重复模式
        "user_preferences": {},# 用户偏好模型
        "skill_drafts": [],    # 自动生成的 skill 草稿
        "nudges": [],          # 待提醒的记忆
        "last_run": None
    }

def save_db(db):
    db["last_run"] = datetime.utcnow().isoformat()
    with open(LEARN_DB, 'w') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

# ============================================================
# 1. 经验自动提炼
# ============================================================
def extract_lessons(db):
    """扫描最近 3 天的记忆文件，提取教训和模式"""
    today = datetime.utcnow().date()
    new_lessons = []
    
    for days_ago in range(3):
        date = today - timedelta(days=days_ago)
        date_str = date.strftime("%Y-%m-%d")
        filepath = os.path.join(MEMORY_DIR, f"{date_str}.md")
        
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r') as f:
            content = f.read()
        
        # 提取教训关键词
        lesson_patterns = [
            (r'教训[：:]\s*(.+)', 'lesson'),
            (r'问题[：:]\s*(.+)', 'problem'),
            (r'修复[：:]\s*(.+)', 'fix'),
            (r'发现[：:]\s*(.+)', 'discovery'),
            (r'❌\s*(.+)', 'mistake'),
            (r'✅\s*(.+)', 'achievement'),
            (r'核心认知[：:]\s*(.+)', 'insight'),
            (r'血泪[：:]\s*(.+)', 'hard_lesson'),
            (r'Lesson[：:]\s*(.+)', 'lesson'),
        ]
        
        for pattern, category in lesson_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                match = match.strip()[:200]
                # 去重
                existing = [l['text'] for l in db.get('lessons', [])]
                if match not in existing and len(match) > 10:
                    new_lessons.append({
                        "text": match,
                        "category": category,
                        "source": f"memory/{date_str}.md",
                        "extracted_at": datetime.utcnow().isoformat()
                    })
    
    if new_lessons:
        db.setdefault('lessons', []).extend(new_lessons)
    
    return new_lessons

# ============================================================
# 2. 用户偏好建模
# ============================================================
def update_user_profile(db):
    """从 USER.md + 最近对话记录提取用户偏好"""
    prefs = db.get('user_preferences', {})
    
    # 从 USER.md 提取
    user_md = os.path.join(WORKSPACE, "USER.md")
    if os.path.exists(user_md):
        with open(user_md, 'r') as f:
            content = f.read()
        
        # 提取关键偏好
        if '直接' in content:
            prefs['communication_style'] = 'direct'
        if '毒舌' in content:
            prefs['humor'] = 'sarcastic_ok'
        if 'ROI' in content:
            prefs['decision_framework'] = 'roi_driven'
        if '验证' in content or '文件路径' in content:
            prefs['proof_requirement'] = 'file_path_required'
        if '抠搜' in content or 'token' in content:
            prefs['cost_sensitivity'] = 'high'
    
    # 从最近记忆提取行为模式
    today = datetime.utcnow().date()
    owner_actions = []
    for days_ago in range(7):
        date = today - timedelta(days=days_ago)
        filepath = os.path.join(MEMORY_DIR, f"{date.strftime('%Y-%m-%d')}.md")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            # 提取老大说的话的模式
            if '自驱' in content or '自己想' in content:
                prefs['expects_initiative'] = True
            if '省钱' in content or '成本' in content or '浪费' in content:
                prefs['cost_conscious'] = True
            if '原创' in content or '别丢人' in content:
                prefs['originality_required'] = True
    
    prefs['last_updated'] = datetime.utcnow().isoformat()
    db['user_preferences'] = prefs
    return prefs

# ============================================================
# 3. 重复模式检测 → Skill 草稿
# ============================================================
def detect_patterns(db):
    """扫描记忆文件，发现重复执行的任务模式"""
    action_counter = Counter()
    
    today = datetime.utcnow().date()
    for days_ago in range(14):  # 看两周
        date = today - timedelta(days=days_ago)
        filepath = os.path.join(MEMORY_DIR, f"{date.strftime('%Y-%m-%d')}.md")
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r') as f:
            content = f.read()
        
        # 统计重复动作
        actions = [
            ('虾聊发帖', r'虾聊.*发帖|发.*虾聊|instreet.*post'),
            ('知识库审计', r'知识.*审计|审计.*知识|质量.*审计'),
            ('GitHub推送', r'git push|GitHub.*同步|推送.*GitHub'),
            ('HN研究', r'HN.*研究|Hacker News|热点.*研究'),
            ('社区互动', r'社区.*互动|回复.*评论|点赞'),
            ('成本优化', r'成本.*优化|调用.*降|省.*调用'),
            ('记忆更新', r'记忆.*更新|MEMORY.*更新|memory.*update'),
            ('内容发布', r'发布.*内容|内容.*发布|写.*文章'),
        ]
        
        for name, pattern in actions:
            if re.search(pattern, content, re.IGNORECASE):
                action_counter[name] += 1
    
    # 出现 3+ 次的模式值得做成 skill
    new_patterns = []
    for action, count in action_counter.most_common(10):
        if count >= 3:
            existing = [p['name'] for p in db.get('patterns', [])]
            if action not in existing:
                new_patterns.append({
                    "name": action,
                    "frequency": count,
                    "detected_at": datetime.utcnow().isoformat(),
                    "skill_candidate": count >= 5
                })
    
    if new_patterns:
        db.setdefault('patterns', []).extend(new_patterns)
    
    return new_patterns

# ============================================================
# 4. 记忆 Nudge — 该记住什么
# ============================================================
def check_nudges(db):
    """检查有没有重要信息还没写入 MEMORY.md"""
    nudges = []
    memory_md = os.path.join(WORKSPACE, "MEMORY.md")
    
    if not os.path.exists(memory_md):
        return nudges
    
    with open(memory_md, 'r') as f:
        memory_content = f.read()
    
    # 检查最近的重要事件是否已记录
    today = datetime.utcnow().date()
    for days_ago in range(3):
        date = today - timedelta(days=days_ago)
        filepath = os.path.join(MEMORY_DIR, f"{date.strftime('%Y-%m-%d')}.md")
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r') as f:
            content = f.read()
        
        # 重要事件关键词
        important_markers = [
            ('转折', '核心认知转变'),
            ('53赞', '40天生存指南热度'),
            ('Hermes', 'Hermes Agent 竞品出现'),
            ('抄袭', 'PUA skill 翻车教训'),
            ('Day 40', '输出模式转变'),
        ]
        
        for keyword, description in important_markers:
            if keyword in content and keyword not in memory_content:
                nudges.append({
                    "keyword": keyword,
                    "description": description,
                    "source": f"memory/{date.strftime('%Y-%m-%d')}.md",
                    "nudged_at": datetime.utcnow().isoformat()
                })
    
    db['nudges'] = nudges
    return nudges

# ============================================================
# 主入口
# ============================================================
def main():
    if len(sys.argv) < 2:
        print("用法: python3 sandbot-autolearn.py [extract|profile|skills|nudge|all]")
        sys.exit(1)
    
    action = sys.argv[1]
    db = load_db()
    
    if action == 'extract' or action == 'all':
        lessons = extract_lessons(db)
        print(f"📚 提取教训: {len(lessons)} 条新教训")
        for l in lessons[:5]:
            print(f"  [{l['category']}] {l['text'][:60]}...")
    
    if action == 'profile' or action == 'all':
        prefs = update_user_profile(db)
        print(f"👤 用户偏好: {len(prefs)} 项")
        for k, v in prefs.items():
            if k != 'last_updated':
                print(f"  {k}: {v}")
    
    if action == 'skills' or action == 'all':
        patterns = detect_patterns(db)
        print(f"🔄 重复模式: {len(patterns)} 个新模式")
        for p in patterns:
            star = "⭐" if p.get('skill_candidate') else "  "
            print(f"  {star} {p['name']}: {p['frequency']}次/2周")
    
    if action == 'nudge' or action == 'all':
        nudges = check_nudges(db)
        print(f"🔔 记忆提醒: {len(nudges)} 条未记录")
        for n in nudges:
            print(f"  ⚠️ [{n['keyword']}] {n['description']} (来源: {n['source']})")
    
    save_db(db)
    
    # 总结
    total_lessons = len(db.get('lessons', []))
    total_patterns = len(db.get('patterns', []))
    total_prefs = len(db.get('user_preferences', {}))
    print(f"\n📊 学习DB: {total_lessons}教训 / {total_patterns}模式 / {total_prefs}偏好项")

if __name__ == "__main__":
    main()
