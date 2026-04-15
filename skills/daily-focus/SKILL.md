# Daily Focus 技能 - 每日优先级与专注追踪

**版本**: V1.0.0  
**创建时间**: 2026-03-23 04:05 UTC  
**作者**: Sandbot 🏖️  
**状态**: ✅ 新建完成

---

## 🎯 技能描述

轻量级每日专注管理工具，帮助设定 3 个核心优先级并追踪专注会话。

**核心价值**:
- 避免任务蔓延，聚焦最重要的 3 件事
- Pomodoro 风格专注会话追踪
- 自动生成每日总结报告

---

## 📋 功能列表

### 1. 设定每日优先级
```bash
# 设定今日 3 个核心任务
daily-focus set "任务 1" "任务 2" "任务 3"
```

### 2. 开始专注会话
```bash
# 开始 25 分钟专注 (默认)
daily-focus start

# 开始自定义时长
daily-focus start --minutes 45
```

### 3. 结束专注会话
```bash
# 结束当前会话，记录完成情况
daily-focus stop "完成了什么"
```

### 4. 查看今日状态
```bash
# 查看今日优先级和专注会话
daily-focus status
```

### 5. 生成每日总结
```bash
# 生成今日总结报告
daily-focus summary
```

---

## 📁 文件结构

```
skills/daily-focus/
├── SKILL.md           # 本文件
├── daily-focus.py     # 主脚本
└── data/
    └── YYYY-MM-DD.md  # 每日记录
```

---

## 🔧 使用方法

### 首次使用
```bash
cd /home/node/.openclaw/workspace/skills/daily-focus
python3 daily-focus.py init
```

### 设定优先级 (每日早晨)
```bash
python3 daily-focus.py set "完成 Cron#107" "发布 Reddit 帖子" "优化 heartbeat 脚本"
```

### 开始专注
```bash
python3 daily-focus.py start
# 输出：🍅 专注开始 (25 分钟) - 任务：完成 Cron#107
#      结束时间：04:35 UTC
#      加油！🏖️
```

### 结束专注
```bash
python3 daily-focus.py stop "完成了 Cron#107 知识获取，+3 文件"
# 输出：✅ 专注完成！耗时 28 分钟
#      记录已保存到 data/2026-03-23.md
```

### 查看状态
```bash
python3 daily-focus.py status
# 输出：📊 今日状态 (2026-03-23)
#      优先级：
#        ✅ 完成 Cron#107
#        ⏳ 发布 Reddit 帖子
#        ⏳ 优化 heartbeat 脚本
#      专注会话：2/4 (50 分钟)
```

### 生成总结
```bash
python3 daily-focus.py summary
# 输出完整的每日总结报告
```

---

## 📊 数据格式

### 每日记录文件 (data/YYYY-MM-DD.md)
```markdown
# 2026-03-23 每日专注记录

## 优先级
1. ✅ 完成 Cron#107
2. ⏳ 发布 Reddit 帖子
3. ⏳ 优化 heartbeat 脚本

## 专注会话
| # | 开始时间 | 结束时间 | 时长 | 任务 | 备注 |
|---|----------|----------|------|------|------|
| 1 | 04:10 | 04:38 | 28m | Cron#107 | +3 文件 |
| 2 | 05:00 | 05:25 | 25m | Reddit 帖子 | r/opensource |

## 统计
- 专注会话：2/4
- 总时长：53 分钟
- 优先级完成：1/3
```

---

## 🎨 设计理念

### 1. 极简主义
- 只有 3 个优先级，避免任务蔓延
- 专注会话默认 25 分钟 (Pomodoro)
- 命令行界面，无 GUI 依赖

### 2. 数据本地
- 所有数据存储在本地 Markdown 文件
- 易于查看、编辑、版本控制
- 无外部 API 依赖

### 3. Sandbot 风格
- Emoji 丰富的输出
- 毒舌但鼓励的提示语
- 抠搜但实用的功能

---

## 🚀 扩展建议

### V1.1 (未来)
- [ ] Telegram 通知集成
- [ ] 专注会话提醒
- [ ] 每周/每月统计报告

### V1.2 (未来)
- [ ] 与 tasks.md 集成
- [ ] 自动优先级建议
- [ ] 专注时长 ROI 分析

---

## 📝 更新记录

| 版本 | 日期 | 变更 |
|------|------|------|
| V1.0.0 | 2026-03-23 | 初始版本创建 |

---

*此技能已真实写入服务器*
*验证：ls -la /home/node/.openclaw/workspace/skills/daily-focus/*
