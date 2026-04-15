# 代码审查与优化建议

**审查时间**: 2026-03-30 17:00 UTC  
**审查人**: Sandbot 🦞

---

## ✅ 优点

1. **架构清晰**: Manager-Instance 分层合理
2. **并发安全**: 使用 sync.RWMutex 保护共享状态
3. **错误处理**: 关键路径有错误返回
4. **配置驱动**: YAML 配置灵活易扩展
5. **健康监控**: 自动重启机制已实现

---

## ⚠️ 需改进

### 1. 错误处理不足

**问题**: Start() 失败后状态未更新

```go
// 当前代码
if err := cmd.Start(); err != nil {
    inst.Status = "crashed"  // ✅ 有更新
    return fmt.Errorf("启动失败：%v", err)
}

// 建议：增加重试逻辑
if err := cmd.Start(); err != nil {
    inst.Status = "crashed"
    inst.RestartCount++
    log.Printf("⚠️ 启动失败，尝试重试 (%d/3)...", inst.RestartCount)
    if inst.RestartCount < 3 {
        time.Sleep(2 * time.Second)
        return m.Start(id)  // 递归重试
    }
    return fmt.Errorf("启动失败 (已重试 3 次): %v", err)
}
```

### 2. 日志系统缺失

**问题**: 使用 fmt.Printf，无法控制日志级别

```go
// 建议：使用标准 log 包
import "log"

var (
    infoLog  = log.New(os.Stdout, "INFO: ", log.Ldate|log.Ltime)
    errorLog = log.New(os.Stderr, "ERROR: ", log.Ldate|log.Ltime)
)

// 使用
infoLog.Printf("实例 %s 已启动 (PID: %d)", inst.Name, inst.PID)
errorLog.Printf("实例 %s 启动失败：%v", inst.Name, err)
```

### 3. 内存限制未实现

**问题**: `MemoryLimitMB` 配置未使用

```go
// 建议：使用 ulimit 或 cgroups (Linux)
// 简单方案：使用 systemd-run
cmd := exec.Command("systemd-run", "--scope", "-p", 
    fmt.Sprintf("MemoryLimit=%dM", inst.MemoryLimitMB),
    "/usr/local/bin/picoclaw", "serve", "--port", fmt.Sprintf("%d", inst.Port))
```

### 4. 进程泄漏风险

**问题**: Stop() 可能无法完全杀死进程

```go
// 当前代码
syscall.Kill(-inst.cmd.Process.Pid, syscall.SIGTERM)
time.Sleep(2 * time.Second)
if inst.cmd.ProcessState == nil {
    syscall.Kill(-inst.cmd.Process.Pid, syscall.SIGKILL)
}

// 建议：增加等待和验证
syscall.Kill(-inst.cmd.Process.Pid, syscall.SIGTERM)
for i := 0; i < 10; i++ {
    if inst.cmd.ProcessState != nil {
        break  // 已退出
    }
    time.Sleep(500 * time.Millisecond)
}
if inst.cmd.ProcessState == nil {
    syscall.Kill(-inst.cmd.Process.Pid, syscall.SIGKILL)
    time.Sleep(1 * time.Second)
}
```

### 5. 配置验证缺失

**问题**: 未验证端口冲突、路径有效性

```go
// 建议：添加验证函数
func ValidateConfig(config *Config) error {
    ports := make(map[int]bool)
    for _, inst := range config.Instances {
        // 检查端口冲突
        if ports[inst.Port] {
            return fmt.Errorf("端口 %d 冲突", inst.Port)
        }
        ports[inst.Port] = true
        
        // 检查端口范围
        if inst.Port < 1024 || inst.Port > 65535 {
            return fmt.Errorf("端口 %d 超出范围", inst.Port)
        }
    }
    return nil
}
```

---

## 📋 待添加功能

### 1. 日志轮转

```go
// 建议：使用 lumberjack
import "gopkg.in/natefinch/lumberjack.v2"

log.SetOutput(&lumberjack.Logger{
    Filename:   "logs/orchestrator.log",
    MaxSize:    100,  // MB
    MaxBackups: 3,
    MaxAge:     28,   // days
})
```

### 2. 指标导出 (Prometheus)

```go
// 建议：添加监控指标
import "github.com/prometheus/client_golang/prometheus"

var (
    instancesTotal = prometheus.NewGauge(prometheus.GaugeOpts{
        Name: "lobster_instances_total",
        Help: "Total number of instances",
    })
    instancesRunning = prometheus.NewGauge(prometheus.GaugeOpts{
        Name: "lobster_instances_running",
        Help: "Number of running instances",
    })
)
```

### 3. 配置热重载

```go
// 建议：监听 SIGHUP 信号
signal.Notify(sigChan, syscall.SIGHUP)
case syscall.SIGHUP:
    log.Println("📋 重新加载配置...")
    if err := manager.ReloadConfig(); err != nil {
        log.Printf("❌ 配置重载失败：%v", err)
    } else {
        log.Println("✅ 配置重载成功")
    }
```

---

## 🎯 优化优先级

| 优化项 | 优先级 | 工作量 | 收益 |
|--------|--------|--------|------|
| 日志系统 | 高 | 1h | 高 |
| 错误重试 | 高 | 0.5h | 高 |
| 进程清理 | 高 | 0.5h | 中 |
| 配置验证 | 中 | 1h | 中 |
| 内存限制 | 中 | 2h | 高 |
| 配置热重载 | 低 | 2h | 低 |
| 指标导出 | 低 | 3h | 低 |

---

## ✅ 下一步行动

1. **立即**: 添加日志系统
2. **今天**: 实现错误重试 + 进程清理
3. **明天**: 配置验证 + 内存限制
4. **本周**: 配置热重载 + 指标导出

---

**🦞 代码质量是稳定性的基础！**
