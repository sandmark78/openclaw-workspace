#!/usr/bin/env python3
"""
V6.2.5 配置中心 - 统一管理所有配置

功能:
- 集中管理路径配置
- 知识领域定义
- 全局常量
- 配置加载/保存

使用:
from config import Config, DOMAINS
"""

import json
from pathlib import Path
from typing import Dict, Any

# ============================================================================
# 路径配置
# ============================================================================

WORKSPACE = Path("/home/node/.openclaw/workspace")
SKILL_DIR = WORKSPACE / "skills" / "task-manager-evolution"
KNOWLEDGE_BASE = WORKSPACE / "knowledge_base"

# 数据文件路径
DATA_DIR = SKILL_DIR / "data"
TASKS_FILE = DATA_DIR / "tasks.json"
PROGRESS_FILE = DATA_DIR / "progress.json"
EVOLUTION_FILE = DATA_DIR / "evolution.json"
VALIDATION_FILE = DATA_DIR / "validation_report.json"
CACHE_FILE = DATA_DIR / ".cache.json"
TREND_HISTORY_FILE = DATA_DIR / "trend_history.json"
NOTIFY_HISTORY_FILE = DATA_DIR / "notify_history.json"

# 报告输出目录
REPORTS_DIR = SKILL_DIR / "reports"

# ============================================================================
# 知识领域定义 (V6.3.1: 动态发现 24+ 领域)
# ============================================================================

# 基础领域目标 (用于计算完成率)
DOMAIN_TARGETS: Dict[str, int] = {
    "01-ai-agent": 1000,
    "02-openclaw": 800,
    "03-federal-system": 600,
    "04-skill-dev": 500,
    "05-memory-system": 400,
    "06-growth-system": 400,
    "07-community": 500,
    "08-monetization": 500,
    "09-security": 400,
    "10-automation": 500,
    "11-content": 400,
    "12-tools": 400,
    "13-blockchain": 500,
    "14-iot": 500,
    "15-cloud": 500,
    "16-devops": 500,
    "17-ml": 500,
    "18-nlp": 500,
    "19-cv": 500,
    "20-robotics": 500,
    "21-edge": 500,
    "22-quantum": 500,
    "23-bio": 500,
    "23_articles_series": 0,  # 特殊领域，无目标
    "24-finance": 500,
}

def discover_domains(knowledge_base: Path = None) -> Dict[str, Dict[str, Any]]:
    """
    V6.3.4 动态领域发现 - 自动扫描 knowledge_base 下所有领域目录
    
    支持格式:
    - XX-xxx (如 01-ai-agent) - 标准领域
    - XX_xxx_xxx (如 23_articles_series) - 标准领域
    - ai-xxx (如 ai-agent, ai-ethics) - 扩展领域
    - 其他有效目录 (external-trends, gap-reports, 等)
    
    过滤规则:
    - 排除 shell 错误目录 ({xxx,yyy} 格式)
    - 排除临时目录 (tmp, backup, 等)
    """
    if knowledge_base is None:
        knowledge_base = KNOWLEDGE_BASE
    
    domains = {}
    
    if not knowledge_base.exists():
        # 回退到静态定义
        for domain_id, target in DOMAIN_TARGETS.items():
            domains[domain_id] = {"target": target, "name": domain_id.replace("-", " ").title()}
        return domains
    
    # 扫描实际存在的目录
    for item in knowledge_base.iterdir():
        if item.is_dir():
            name = item.name
            
            # V6.3.4: 过滤 shell 错误目录 ({xxx,yyy} 格式)
            if name.startswith("{") and name.endswith("}"):
                continue
            
            # V6.3.4: 过滤临时目录
            if name.lower() in ["tmp", "temp", "backup", "backups", ".git", "__pycache__"]:
                continue
            
            # 匹配 XX-xxx 或 XX_xxx 格式 (前两位是数字) - 标准领域
            name_normalized = name.replace("_", "-")
            prefix = name_normalized[:2] if len(name_normalized) >= 2 else ""
            
            if prefix.isdigit():
                target = DOMAIN_TARGETS.get(name, 500)  # 默认目标 500
                display_name = name.replace("-", " ").replace("_", " ").title()
                domains[name] = {"target": target, "name": display_name, "type": "standard"}
            # V6.3.4: 匹配 ai-xxx 格式 - 扩展领域
            elif name.startswith("ai-"):
                domains[name] = {"target": 500, "name": name.replace("-", " ").title(), "type": "extension"}
            # V6.3.4: 其他有效扩展领域
            elif name in ["external-trends", "gap-reports", "product-strategy", "tech-society"]:
                domains[name] = {"target": 500, "name": name.replace("-", " ").title(), "type": "extension"}
    
    # 如果没扫描到任何领域，回退到静态定义
    if not domains:
        for domain_id, target in DOMAIN_TARGETS.items():
            domains[domain_id] = {"target": target, "name": domain_id.replace("-", " ").title()}
    
    return dict(sorted(domains.items()))

# 运行时动态发现领域
DOMAINS = discover_domains()

# ============================================================================
# 全局常量
# ============================================================================

# 速度阈值 (知识点/分钟)
SPEED_TARGET = 500
SPEED_WARNING = 300
SPEED_CRITICAL = 100

# 进度阈值
PROGRESS_WARNING = 50  # 低于 50% 预警
PROGRESS_CRITICAL = 25  # 低于 25% 严重预警

# 缓存有效期 (秒)
CACHE_TTL = 60  # 1 分钟

# 日志级别
LOG_LEVELS = {
    "DEBUG": 0,
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "CRITICAL": 4,
}

# ============================================================================
# 工具函数
# ============================================================================

def get_total_target() -> int:
    """获取总目标知识点数"""
    return sum(d["target"] for d in DOMAINS.values())

def get_domain_ids() -> list:
    """获取所有领域 ID 列表"""
    return list(DOMAINS.keys())

def ensure_dirs():
    """确保所有必要目录存在"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def load_config(config_file: Path = None) -> dict:
    """加载用户配置 (如果存在)"""
    if config_file is None:
        config_file = SKILL_DIR / "config.json"
    
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    
    return {}

def save_config(config: dict, config_file: Path = None):
    """保存用户配置"""
    if config_file is None:
        config_file = SKILL_DIR / "config.json"
    
    config_file.parent.mkdir(parents=True, exist_ok=True)
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def count_knowledge_points(filepath: Path) -> int:
    """
    V6.3.3 知识点计数 - 多策略智能计数 (元数据 + 实际内容)
    
    计数策略 (优先级从高到低):
    1. 元数据 `**数量**:` / `**知识点范围**: XXX-YYY (NNN 个)` - 显式声明
    2. 内容计数 `### AXX-NNN:` / `### NNNN:` - 标题格式
    3. 内容计数 `- NNNN:` - 列表格式
    4. 默认值 1 (保守估计)
    
    性能优化:
    - 只读前 5000 字符 (覆盖元数据 + 大部分内容)
    - 编译正则表达式 (复用)
    - 短路返回 (找到即返回)
    """
    import re
    
    if not filepath.exists() or not filepath.is_file():
        return 0
    
    try:
        # 读取前 5000 字符 (覆盖元数据 + 内容头部)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(5000)
        
        # ========== 策略 1: 元数据解析 ==========
        
        # 优先匹配 `**数量**:` (实际数量) - 支持行首或行中
        match = re.search(r'(?:^|\n)\*\*数量\*\*:\s*(\d+)', content)
        if match:
            return int(match.group(1))
        
        # 匹配 `**知识点范围**: XXX-YYY (NNN 个)` (显式声明数量)
        match = re.search(r'\*\*知识点范围\*\*:\s*\d+-\d+\s*\((\d+)\s*个\)', content)
        if match:
            return int(match.group(1))
        
        # 匹配 `**范围**:` (如 "A02-001 到 A02-800")
        match = re.search(r'\*\*范围\*\*:\s*A?\d+-\d+\s+到\s+A?\d+-(\d+)', content)
        if match:
            return int(match.group(1))
        
        # ========== 策略 2: 内容计数 (标题格式) ==========
        
        # 计数 `### AXX-NNN:` 格式 (如 ### A01-001:)
        kp_headers = len(re.findall(r'^### A\d+-\d+:', content, re.MULTILINE))
        if kp_headers > 0:
            return kp_headers
        
        # 计数 `### NNNN:` 格式 (如 ### 0201-0210:)
        range_headers = re.findall(r'^### (\d+)-(\d+):', content, re.MULTILINE)
        if range_headers:
            total = sum(int(end) - int(start) + 1 for start, end in range_headers)
            if total > 0:
                return total
        
        # 计数普通 `### ` 标题 (每个标题算 1 点)
        normal_headers = len(re.findall(r'^### ', content, re.MULTILINE))
        if normal_headers > 10:  # 只有标题较多时才采用此策略
            return normal_headers
        
        # ========== 策略 3: 内容计数 (列表格式) ==========
        
        # 计数 `- NNNN:` 格式 (如 - 0201:)
        list_items = len(re.findall(r'^- \d+:', content, re.MULTILINE))
        if list_items > 0:
            return list_items
        
        # ========== 策略 4: 默认值 ==========
        return 1
        
    except Exception as e:
        # 出错时保守返回 1
        return 1

# ============================================================================
# 初始化
# ============================================================================

# 启动时确保目录存在
ensure_dirs()
