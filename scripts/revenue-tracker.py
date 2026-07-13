#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Revenue Tracker - 收益自动化追踪脚本
版本：V1.1.0
创建：2026-03-13
更新：2026-03-14 (V1.1.0 - 手动录入 + 报告生成)
功能：手动录入 Gumroad/ClawHub 收益数据，生成日报送 Telegram
"""

import os
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path

# 配置
WORKSPACE = Path("/home/node/.openclaw/workspace")
SECRETS_DIR = Path("/home/node/.openclaw/secrets")
MEMORY_DIR = WORKSPACE / "memory"

# 日志文件
LOG_FILE = MEMORY_DIR / f"revenue-{datetime.now().strftime('%Y-%m-%d')}.md"

def load_secret(secret_name):
    """从 secrets 目录加载密钥"""
    secret_path = SECRETS_DIR / f"{secret_name}.txt"
    if secret_path.exists():
        return secret_path.read_text().strip()
    return None

def fetch_gumroad_revenue(api_key, days=7):
    """
    抓取 Gumroad 收益数据
    
    注意：Gumroad API 需要 OAuth2，这里使用简化版本
    实际使用时需要配置 OAuth2 token
    """
    # 模拟数据 (实际使用时替换为真实 API 调用)
    # Gumroad API: https://github.com/gumroad/api
    mock_data = {
        "sales": [],
        "total_revenue": 0,
        "currency": "USD"
    }
    
    # TODO: 实现真实 Gumroad API 调用
    # endpoint = "https://api.gumroad.com/v2/sales"
    # headers = {"Authorization": f"Bearer {api_key}"}
    # response = requests.get(endpoint, headers=headers)
    
    print(f"⚠️  Gumroad API 待实现 - 需要 OAuth2 配置")
    return mock_data

def fetch_clawhub_revenue(api_key, days=7):
    """
    抓取 ClawHub 收益数据
    
    ClawHub API 文档：待补充
    """
    # 模拟数据
    mock_data = {
        "downloads": 0,
        "revenue": 0,
        "currency": "USDC"
    }
    
    # TODO: 实现真实 ClawHub API 调用
    print(f"⚠️  ClawHub API 待实现 - 需要 API 文档")
    return mock_data

def generate_revenue_report(gumroad_data, clawhub_data):
    """生成收益报告"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    report = f"""# 收益日报 - {today}

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}
**报告周期**: 过去 7 天

---

## 📊 收益概览

### Gumroad
| 指标 | 数值 |
|------|------|
| 总收益 | ${gumroad_data.get('total_revenue', 0):.2f} |
| 销售笔数 | {len(gumroad_data.get('sales', []))} |
| 货币 | {gumroad_data.get('currency', 'USD')} |

### ClawHub
| 指标 | 数值 |
|------|------|
| 总收益 | {clawhub_data.get('revenue', 0):.2f} USDC |
| 下载次数 | {clawhub_data.get('downloads', 0)} |
| 货币 | {clawhub_data.get('currency', 'USDC')} |

---

## 💰 合计收益

```
总收益：${gumroad_data.get('total_revenue', 0):.2f} + {clawhub_data.get('revenue', 0):.2f} USDC
```

---

## 📈 趋势分析

**状态**: 🔴 等待第一笔收益

**目标**:
- 本周：$100+
- 本月：$500+
- 下月：$2000+

---

## ✅ 行动项

- [ ] Gumroad 产品优化 (如有销售)
- [ ] ClawHub 技能推广 (如有下载)
- [ ] 新产品开发 (如零销售)

---

*此报告由 revenue-tracker.py 自动生成*
*版本：V1.0.0*
"""
    return report

def send_telegram_message(message, chat_id, bot_token):
    """发送 Telegram 消息"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(f"✅ Telegram 消息已发送")
        return True
    except Exception as e:
        print(f"❌ Telegram 发送失败：{e}")
        return False

def load_revenue_data():
    """加载历史收益数据"""
    data_file = MEMORY_DIR / "revenue-data.json"
    if data_file.exists():
        return json.loads(data_file.read_text())
    return {"sales": [], "total_revenue": 0, "days": {}}

def save_revenue_data(data):
    """保存收益数据"""
    data_file = MEMORY_DIR / "revenue-data.json"
    data_file.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def manual_entry():
    """手动录入今日销售数据"""
    print("\n💰 手动录入销售数据")
    print("-" * 40)
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    try:
        gumroad_sales = int(input(f"Gumroad 今日销量 [{today}]: ") or "0")
        gumroad_revenue = float(input(f"Gumroad 今日收入 (USD): ") or "0")
        clawhub_downloads = int(input(f"ClawHub 今日下载：") or "0")
        clawhub_revenue = float(input(f"ClawHub 今日收入 (USDC): ") or "0")
        
        return {
            "date": today,
            "gumroad": {
                "sales": gumroad_sales,
                "revenue": gumroad_revenue,
                "currency": "USD"
            },
            "clawhub": {
                "downloads": clawhub_downloads,
                "revenue": clawhub_revenue,
                "currency": "USDC"
            },
            "timestamp": datetime.now().isoformat()
        }
    except KeyboardInterrupt:
        print("\n⚠️  录入取消")
        return None

def main():
    """主函数"""
    print(f"🚀 Revenue Tracker V1.1.0 - 启动")
    print(f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    
    # 加载密钥
    gumroad_key = load_secret("gumroad_api_key")
    clawhub_key = load_secret("clawhub_api_key")
    telegram_token = load_secret("telegram_bot_token")
    telegram_chat_id = "773172564"  # 从 TOOLS.md 获取
    
    # 加载历史数据
    print(f"\n📊 加载历史数据...")
    revenue_data = load_revenue_data()
    
    # 手动录入今日数据
    print(f"\n📝 录入今日数据...")
    today_entry = manual_entry()
    
    if today_entry:
        revenue_data["sales"].append(today_entry)
        revenue_data["total_revenue"] = sum(
            s["gumroad"]["revenue"] + s["clawhub"]["revenue"] 
            for s in revenue_data["sales"]
        )
        save_revenue_data(revenue_data)
        print(f"✅ 数据已保存")
    
    # 生成报告
    print(f"\n📝 生成收益报告...")
    
    # 计算今日数据
    today = datetime.now().strftime('%Y-%m-%d')
    today_sales = next((s for s in revenue_data["sales"] if s["date"] == today), None)
    
    gumroad_data = {
        "total_revenue": sum(s["gumroad"]["revenue"] for s in revenue_data["sales"]),
        "sales": revenue_data["sales"],
        "currency": "USD",
        "today_sales": today_sales["gumroad"]["sales"] if today_sales else 0,
        "today_revenue": today_sales["gumroad"]["revenue"] if today_sales else 0
    }
    
    clawhub_data = {
        "revenue": sum(s["clawhub"]["revenue"] for s in revenue_data["sales"]),
        "downloads": sum(s["clawhub"]["downloads"] for s in revenue_data["sales"]),
        "currency": "USDC",
        "today_downloads": today_sales["clawhub"]["downloads"] if today_sales else 0,
        "today_revenue": today_sales["clawhub"]["revenue"] if today_sales else 0
    }
    
    report = generate_revenue_report(gumroad_data, clawhub_data)
    
    # 保存报告到文件
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(report)
    print(f"✅ 报告已保存：{LOG_FILE}")
    
    # 发送 Telegram 通知
    status_emoji = "🟢" if gumroad_data["today_revenue"] > 0 else "🔴"
    summary = f"""{status_emoji} 收益日报 - {datetime.now().strftime('%Y-%m-%d')}

Gumroad: ${gumroad_data['today_revenue']:.2f} (今日) | ${gumroad_data['total_revenue']:.2f} (累计)
ClawHub: {clawhub_data['today_revenue']:.2f} USDC (今日) | {clawhub_data['revenue']:.2f} USDC (累计)

状态：{"✅ 已破零!" if gumroad_data['today_revenue'] > 0 else "🔴 等待第一笔收益"}
目标：本周$100+ | 本月$500+

完整报告：{LOG_FILE}"""
    
    if telegram_token:
        send_telegram_message(summary, telegram_chat_id, telegram_token)
    
    print(f"\n✅ Revenue Tracker 完成")
    return 0

if __name__ == "__main__":
    exit(main())
