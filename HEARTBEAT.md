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

## 心跳 (2026-10-01 00:30 UTC)
- ✅ 系统正常
  - Gateway: PID 8, 48.1% 内存 (939MB)
  - 磁盘: 58% (16G 可用 / 40G)
  - 内存: 456Mi available / 1.9Gi
- 无异常，无需汇报

## 心跳 (2026-09-30 11:03 UTC)
- ✅ 系统正常
  - Gateway: 运行中 (3 进程)
  - WebUI: HTTP 200
  - 磁盘: 58% (16G 可用 / 40G)
  - 内存: 440Mi available / 1.9Gi
  - 博客仓库: main 分支, 与 origin 同步, 有未提交变更
  - MEMORY.md: 6035 bytes
  - 记忆文件: 734 个
- 无异常，无需汇报

## 心跳 (2026-09-30 09:00 UTC)
- ✅ 系统正常
  - Gateway: PID 8, 47% 内存 (916MB)
  - 磁盘: 58% (16G 可用 / 40G)
  - 内存: 453Mi available / 1.9Gi
  - 博客仓库: main 分支, 与 origin 同步, 有未提交变更
  - MEMORY.md: 6035 bytes
  - 记忆文件: 734 个
- 无异常，无需汇报

## 心跳 (2026-09-29 18:00 UTC)
- ✅ 系统正常
  - Gateway: PID 8, 39.5% 内存 (771MB)
  - 磁盘: 58% (16G 可用 / 40G)
  - 内存: 641Mi available / 1.9Gi
  - 博客仓库: main 分支, 与 origin 同步
  - MEMORY.md: 6035 bytes
  - 记忆文件: 733 个
- 无异常，无需汇报
