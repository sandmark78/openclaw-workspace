# Lobster Orchestrator 故障排查指南

**版本**: V0.1.3  
**最后更新**: 2026-03-30 17:30 UTC

---

## 🔍 快速诊断流程

```
问题报告
    ↓
检查服务状态 (curl /api/v1/health)
    ↓
检查实例状态 (curl /api/v1/instances)
    ↓
查看日志 (logs/orchestrator.log)
    ↓
定位问题 → 参考下方具体章节
```

---

## ❌ 常见问题

### 1. 服务无法启动

**症状**:
```bash
./orchestrator: command not found
```

**原因**: 编译失败或未编译

**解决**:
```bash
# 检查 Go 环境
go version

# 安装 Go (Termux)
pkg install golang

# 重新编译
go mod tidy
go build -o orchestrator ./cmd/orchestrator
```

---

### 2. 实例启动失败

**症状**:
```json
{
  "error": "启动失败：exec: \"/usr/local/bin/picoclaw\": stat: No such file or directory"
}
```

**原因**: PicoClaw 未安装或路径错误

**解决**:
```bash
# 检查 PicoClaw 位置
which picoclaw

# 如果不存在，安装 PicoClaw
# 方法 1: 从源码编译
git clone https://github.com/sipeed/picoclaw
cd picoclaw && go build -o picoclaw ./cmd/picoclaw
sudo mv picoclaw /usr/local/bin/

# 方法 2: 修改配置
# 编辑 configs/instances.yaml，将命令改为实际路径
```

---

### 3. 端口冲突

**症状**:
```json
{
  "error": "端口 18790 已被占用"
}
```

**原因**: 端口被其他进程占用

**解决**:
```bash
# 查找占用端口的进程
lsof -i :18790
# 或
netstat -tlnp | grep 18790

# 杀死占用进程
kill -9 <PID>

# 或修改配置使用其他端口
# 编辑 configs/instances.yaml
```

---

### 4. 内存溢出

**症状**:
- 实例频繁崩溃
- 系统变慢
- OOM Killer 杀死进程

**原因**: 实例数过多或内存限制不足

**解决**:
```bash
# 检查内存使用
ps aux | grep -E "(orchestrator|picoclaw)" | awk '{sum+=$6} END {print sum/1024 "MB"}'

# 减少实例数
# 编辑 configs/instances.yaml，减少实例数量

# 或增加内存限制 (如果硬件允许)
# 编辑 configs/instances.yaml
memory_limit_mb: 20  # 从 10 增加到 20
```

---

### 5. API Key 不足

**症状**:
```json
{
  "error": "API key 无效或已用尽"
}
```

**原因**: 50 个实例需要 50 个独立 API Key

**解决**:
```bash
# 方案 1: 准备 50 个 API Key
# 在环境变量中设置
export BAILOU_API_KEY_1=sk-xxx1
export BAILOU_API_KEY_2=sk-xxx2
# ...

# 方案 2: 共享 API Key (不推荐，可能触发限流)
# 编辑 configs/instances.yaml
api_key_env: "BAILOU_API_KEY"  # 所有实例共享

# 方案 3: 使用 Key Pool (未来功能)
# 自动轮询多个 Key
```

---

### 6. 实例频繁重启

**症状**:
```json
{
  "restart_count": 15,
  "status": "crashed"
}
```

**原因**: 实例崩溃，自动重启机制触发

**解决**:
```bash
# 1. 查看日志
tail -f logs/orchestrator.log

# 2. 检查实例日志
tail -f /data/workspaces/lobster-001/logs/picoclaw.log

# 3. 常见原因:
#    - API Key 无效
#    - 网络连接问题
#    - PicoClaw 配置错误
#    - 内存不足

# 4. 临时禁用自动重启
# 编辑 configs/instances.yaml
auto_start: false
```

---

### 7. Dashboard 无法访问

**症状**:
- 浏览器显示 "无法连接"
- curl 返回错误

**解决**:
```bash
# 检查服务是否运行
curl http://localhost:8080/api/v1/health

# 如果失败，检查 Orchestrator 是否运行
ps aux | grep orchestrator

# 检查防火墙
# Android: 通常无防火墙
# Linux: sudo ufw allow 8080

# 检查端口监听
netstat -tlnp | grep 8080
```

---

### 8. 健康监控失效

**症状**:
- 实例崩溃但未自动重启
- 日志无健康检查记录

**原因**: 监控线程未启动或间隔过长

**解决**:
```bash
# 检查配置
cat configs/instances.yaml | grep health_check

# 确保间隔合理 (建议 30 秒)
health_check_interval_s: 30

# 重启服务
pkill orchestrator
./orchestrator -config configs/instances.yaml
```

---

## 🛠️ 调试工具

### 1. 日志查看

```bash
# 实时查看 Orchestrator 日志
tail -f logs/orchestrator.log

# 查看特定实例日志
tail -f /data/workspaces/lobster-001/logs/picoclaw.log

# 搜索错误
grep -r "ERROR" logs/
```

### 2. 性能监控

```bash
# 内存使用
ps aux | grep -E "(orchestrator|picoclaw)" | awk '{sum+=$6} END {printf "总内存：%.2fMB\n", sum/1024}'

# CPU 使用
top -bn1 | grep "Cpu(s)"

# 实例状态
curl -s http://localhost:8080/api/v1/instances | jq '.instances | group_by(.status) | map({status: .[0].status, count: length})'
```

### 3. 网络诊断

```bash
# 检查端口监听
netstat -tlnp | grep -E "(8080|1879[0-9])"

# 测试 API
curl http://localhost:8080/api/v1/health

# 测试实例
curl http://localhost:18790
```

---

## 📞 获取帮助

### 日志文件位置
- Orchestrator: `logs/orchestrator.log`
- 实例：`/data/workspaces/{id}/logs/picoclaw.log`

### 配置文件
- 主配置：`configs/instances.yaml`

### 社区支持
- GitHub Issues: https://github.com/immortal-lobster/lobster-orchestrator/issues
- Discord: [待添加]

---

## 🦞 预防胜于治疗

**最佳实践**:
1. 定期备份配置文件
2. 监控日志文件
3. 设置告警阈值
4. 定期重启清理内存
5. 保持 Go 和 PicoClaw 更新

---

**🦞 遇到问题不要慌，按流程排查！**
