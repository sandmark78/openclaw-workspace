# HEARTBEAT.md - 心跳检查清单

## 系统健康（每次必查）
```bash
# Gateway 进程
ps aux | grep -E "(openclaw|gateway)" | grep -v grep | head -3

# 磁盘空间
df -h / | tail -1

# 内存使用
free -h | head -2
```

## 博客系统（每 2 小时）
```bash
# 检查最新 Cron 执行
cron list | grep -E "文章|素材" | head -5

# 检查博客仓库状态
cd /home/node/.openclaw/workspace/sandbot-blog && git status | head -5
```

## 记忆系统（每天 1 次）
```bash
# 检查记忆文件大小
wc -c MEMORY.md
ls memory/*.md | wc -l
```

## 异常处理
- 无异常 → HEARTBEAT_OK
- 有异常 → 记录到 memory/YYYY-MM-DD.md，严重时通知老大

---
*最后更新: 2026-08-01*
