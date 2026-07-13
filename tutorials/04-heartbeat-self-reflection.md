# V6.1 实战教程 4: 心跳/自省系统部署

**创建时间**: 2026-02-25 11:35 UTC  
**定价**: $149 (部署包)  
**状态**: ✅ 已完成

---

## 📚 教程内容

### 1. 为什么需要心跳/自省系统？(3 分钟)

**心跳系统价值**:
```
✅ 每 30 分钟健康检查
✅ 早期发现问题
✅ 系统稳定性保障
✅ 存在证明
```

**自省系统价值**:
```
✅ 每日反思错误
✅ 持续学习进化
✅ 避免重复犯错
✅ 品味提升
```

---

### 2. 一键部署脚本 (10 分钟)

#### 心跳脚本
```bash
#!/bin/bash
# heartbeat-check.sh

ps aux | grep openclaw | grep -v grep > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Gateway: 正常"
else
    echo "❌ Gateway: 异常"
fi

curl -s http://172.18.0.2:18789/ -o /dev/null
if [ $? -eq 0 ]; then
    echo "✅ WebUI: 可访问"
else
    echo "❌ WebUI: 不可访问"
fi
```

#### 自省脚本
```bash
#!/bin/bash
# self-reflection.sh

TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M UTC")
echo "🪞 自省模式启动 - ${TIMESTAMP}"

# 检查今日日志
if [ -f "/workspace/memory/$(date +%Y-%m-%d).md" ]; then
    echo "   ✅ 今日日志存在"
else
    echo "   ⚠️  今日日志不存在"
fi
```

---

### 3. cron 配置 (5 分钟)

#### 心跳任务 (每 30 分钟)
```bash
(crontab -l 2>/dev/null; echo "*/30 * * * * /workspace/scripts/heartbeat-check.sh") | crontab -
```

#### 自省任务 (每天 23:00 UTC)
```bash
(crontab -l 2>/dev/null; echo "0 23 * * * /workspace/scripts/self-reflection.sh") | crontab -
```

#### 验证配置
```bash
crontab -l
# 预期输出：
# */30 * * * * /workspace/scripts/heartbeat-check.sh
# 0 23 * * * /workspace/scripts/self-reflection.sh
```

---

### 4. 日志管理 (5 分钟)

#### 心跳日志
```bash
mkdir -p /workspace/memory/heartbeat-logs
cat > /workspace/memory/heartbeat-logs/$(date +%Y-%m-%d).md << 'EOF'
# $(date +%Y-%m-%d) 心跳记录

| 时间 | 检查项 | 结果 | 备注 |
|------|--------|------|------|
| 00:00 | 系统健康 | ✅ | - |
| 00:30 | 系统健康 | ✅ | - |
EOF
```

#### 自省日志
```bash
cat > /workspace/memory/$(date +%Y-%m-%d)-self-reflection.md << 'EOF'
# $(date +%Y-%m-%d) 自省日志

## 今日错误
- 错误 1
- 错误 2

## 核心教训
- 教训 1
- 教训 2

## 认知更新
- 更新 1
- 更新 2
EOF
```

---

### 5. 企业版功能 ($299)

#### 高级功能
```
✅ 告警通知 (Telegram/Email)
✅ 日志脱敏
✅ 性能监控
✅ 自定义检查项
✅ 优先支持
```

#### 部署服务
```
1. 远程部署
2. 配置优化
3. 告警设置
4. 培训文档
5. 30 天支持
```

---

## 🎁 附赠资源

### 完整脚本包
```
scripts/
├── heartbeat-check.sh
├── self-reflection.sh
├── sanitize-secrets.sh
└── generate-report.sh
```

### cron 模板
```bash
# 心跳 (每 30 分钟)
*/30 * * * * /workspace/scripts/heartbeat-check.sh

# 自省 (每天 23:00)
0 23 * * * /workspace/scripts/self-reflection.sh

# 日志清理 (每周日 00:00)
0 0 * * 0 /workspace/scripts/cleanup-logs.sh
```

---

## 📊 学习检查

完成本教程后，你应该能够：

- [ ] 部署心跳脚本
- [ ] 部署自省脚本
- [ ] 配置 cron 任务
- [ ] 管理日志文件
- [ ] 设置告警通知

---

## 💰 购买选项

| 版本 | 价格 | 内容 |
|------|------|------|
| **基础版** | $149 | 部署脚本 + 使用文档 |
| **专业版** | $249 | 基础版 + 告警通知 |
| **企业版** | $299 | 专业版 + 部署服务 |

---

*此教程已真实写入服务器*
*验证：cat /workspace/tutorials/04-heartbeat-self-reflection.md*
