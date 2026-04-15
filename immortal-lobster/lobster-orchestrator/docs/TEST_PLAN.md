# Lobster Orchestrator 测试计划

**版本**: V0.1.0  
**目标**: 验证 50 实例并发运行稳定性

---

## 📋 测试环境

### 硬件要求
- **CPU**: 4 核+ (手机/旧电脑)
- **内存**: 512MB+ (推荐 1GB+)
- **存储**: 2GB+ 可用空间
- **网络**: 稳定互联网连接

### 软件要求
- **OS**: Android 8.0+ / Linux
- **Go**: 1.21+
- **PicoClaw**: 预安装到 `/usr/local/bin/picoclaw`

---

## 🧪 测试用例

### 1. 单实例测试 (优先级：高)

**目标**: 验证基本功能正常

```bash
# 准备
cp configs/instances.yaml configs/instances-single.yaml
# 编辑只保留 1 个实例

# 启动
./orchestrator -config configs/instances-single.yaml

# 验证
curl http://localhost:8080/api/v1/instances
curl http://localhost:18790  # PicoClaw 端口
```

**预期结果**:
- [ ] Orchestrator 正常启动
- [ ] Dashboard 可访问
- [ ] 实例状态显示 running
- [ ] PicoClaw 响应正常

---

### 2. 10 实例测试 (优先级：高)

**目标**: 验证多实例并发

```bash
# 生成 10 实例配置
./scripts/generate-config.sh 10

# 启动
./orchestrator -config configs/instances.yaml

# 监控
watch -n1 'curl -s http://localhost:8080/api/v1/instances | jq'
```

**预期结果**:
- [ ] 10 个实例全部启动
- [ ] 总内存<100MB
- [ ] CPU<30%
- [ ] 无崩溃

---

### 3. 50 实例压力测试 (优先级：中)

**目标**: 验证极限负载

```bash
# 生成 50 实例配置
./scripts/generate-config.sh 50

# 启动并测试
./scripts/stress-test.sh
```

**预期结果**:
- [ ] 50 个实例全部启动
- [ ] 启动时间<5 分钟
- [ ] 总内存<500MB
- [ ] CPU<50%
- [ ] 24 小时无崩溃

---

### 4. 稳定性测试 (优先级：中)

**目标**: 验证长期运行

```bash
# 运行 24 小时
timeout 24h ./orchestrator -config configs/instances.yaml

# 监控脚本
./scripts/monitor.sh > logs/stability.log
```

**监控指标**:
- 内存使用趋势
- CPU 使用趋势
- 实例重启次数
- API 响应时间

---

### 5. 故障恢复测试 (优先级：低)

**目标**: 验证自动重启

```bash
# 手动杀死一个实例
kill $(pgrep -f "picoclaw.*18790")

# 等待 30 秒，检查是否自动重启
curl http://localhost:8080/api/v1/instances/lobster-001
```

**预期结果**:
- [ ] 30 秒内检测到崩溃
- [ ] 自动重启成功
- [ ] 重启次数+1

---

## 📊 性能基准

| 指标 | 目标 | 测试方法 |
|------|------|----------|
| 单实例内存 | <10MB | `ps aux \| grep picoclaw` |
| 50 实例总内存 | <500MB | 同上 |
| 启动时间 (50 实例) | <300s | `time ./orchestrator` |
| CPU 占用 | <50% | `top` |
| 重启时间 | <5s | 手动测试 |
| API 响应时间 | <100ms | `curl -w` |

---

## 🔧 测试工具

### 内存监控
```bash
#!/bin/bash
while true; do
    echo "$(date): $(ps aux | grep picoclaw | awk '{sum+=$6} END {print sum/1024 "MB"}')"
    sleep 5
done
```

### CPU 监控
```bash
#!/bin/bash
while true; do
    echo "$(date): $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')%"
    sleep 5
done
```

### 实例状态监控
```bash
#!/bin/bash
while true; do
    curl -s http://localhost:8080/api/v1/instances | \
    jq '.instances | group_by(.status) | map({status: .[0].status, count: length})'
    sleep 10
done
```

---

## ⚠️ 常见问题

### Q1: 实例启动失败
**原因**: PicoClaw 未安装或路径错误  
**解决**: 确认 `/usr/local/bin/picoclaw` 存在

### Q2: 内存溢出
**原因**: 实例数过多或内存限制不足  
**解决**: 减少实例数或增加 `memory_limit_mb`

### Q3: 端口冲突
**原因**: 18790-18839 被占用  
**解决**: 修改配置文件中的端口

### Q4: API Key 不足
**原因**: 需要 50 个独立 API Key  
**解决**: 使用 Key Pool 或共享 Key

---

## 📈 测试报告模板

```markdown
# 测试报告 - YYYY-MM-DD

**测试环境**: 
- 设备：[手机型号/电脑配置]
- 内存：[GB]
- CPU: [核心数]

**测试结果**:
- 单实例：✅/❌
- 10 实例：✅/❌
- 50 实例：✅/❌
- 稳定性：✅/❌

**性能数据**:
- 总内存：[MB]
- CPU: [%]
- 启动时间：[s]

**问题记录**:
1. ...
2. ...

**改进建议**:
1. ...
2. ...
```

---

**🦞 测试是质量的保证！**
