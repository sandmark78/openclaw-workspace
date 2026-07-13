# Lobster Orchestrator 架构设计

**版本**: V0.2.2  
**最后更新**: 2026-03-30 18:20 UTC

---

## 📋 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                    Web Browser                          │
│              http://localhost:8080                      │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP
┌────────────────────▼────────────────────────────────────┐
│              Lobster Orchestrator                       │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Web Server (port 8080)                          │  │
│  │  ├─ Dashboard (HTML/JS)                          │  │
│  │  └─ RESTful API (/api/v1/*)                      │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Instance Manager                                │  │
│  │  ├─ Start/Stop/Restart                           │  │
│  │  ├─ Health Check (30s)                           │  │
│  │  └─ Auto Restart                                 │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Configuration                                   │  │
│  │  ├─ YAML Parser                                  │  │
│  │  ├─ Validator                                    │  │
│  │  └─ Hot Reload (TODO)                            │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │ Process Spawn
┌────────────────────▼────────────────────────────────────┐
│              PicoClaw Instances × 50                    │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │ lobster-001  │ │ lobster-002  │ │ ...          │   │
│  │ port 18790   │ │ port 18791   │ │              │   │
│  │ workspace_1  │ │ workspace_2  │ │              │   │
│  └──────────────┘ └──────────────┘ └──────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 核心模块

### 1. Web Server

**职责**: HTTP 请求处理 + 路由

**文件**: `pkg/api/handlers.go`

**接口**:
```
GET  /api/v1/instances          # 获取所有实例
GET  /api/v1/instances/{id}     # 获取单个实例
POST /api/v1/instances/{id}     # 启动实例
DELETE /api/v1/instances/{id}   # 停止实例
GET  /api/v1/health             # 健康检查
GET  /                          # Dashboard
```

**技术栈**:
- Go `net/http` 标准库
- 无框架依赖 (轻量级)

---

### 2. Instance Manager

**职责**: 实例生命周期管理

**文件**: `pkg/instance/instance.go`

**核心方法**:
```go
NewManager(configPath)  // 创建管理器
Start(id)               // 启动实例
Stop(id)                // 停止实例
Restart(id)             // 重启实例
AutoStart()             // 自动启动
GetStatus(id)           // 获取状态
CheckHealth(id)         // 健康检查
```

**并发控制**:
- `sync.RWMutex` 保护共享状态
- 读操作使用 RLock (并发)
- 写操作使用 Lock (互斥)

---

### 3. Config Validator

**职责**: 配置验证

**文件**: `pkg/instance/validator.go`

**验证项**:
- ID 唯一性
- 端口范围 (1024-65535)
- 端口冲突检测
- 内存限制 (5-1024MB)
- 工作目录可写性
- 全局配置合理性

---

### 4. Health Monitor

**职责**: 健康监控 + 自动重启

**文件**: `pkg/monitor/health.go`

**机制**:
```go
ticker := time.NewTicker(30 * time.Second)
for range ticker.C {
    checkAndRecover(manager)
}
```

**检查项**:
- 进程是否存活
- 自动重启崩溃实例
- 记录重启次数

---

## 📁 目录结构

```
lobster-orchestrator/
├── cmd/orchestrator/
│   └── main.go              # 程序入口
├── pkg/
│   ├── instance/
│   │   ├── instance.go      # 实例管理
│   │   ├── config.go        # 配置加载
│   │   └── validator.go     # 配置验证
│   ├── api/
│   │   └── handlers.go      # API 处理
│   └── monitor/
│       └── health.go        # 健康监控
├── web/
│   └── dashboard.html       # Web UI
├── configs/
│   └── instances.yaml       # 配置模板
├── scripts/
│   ├── deploy-termux.sh     # 部署脚本
│   ├── stress-test.sh       # 压力测试
│   ├── generate-config.sh   # 配置生成
│   └── monitor.sh           # 性能监控
├── docs/
│   ├── DESIGN.md            # 设计文档
│   ├── API.md               # API 文档
│   ├── TEST_PLAN.md         # 测试计划
│   ├── CODE_REVIEW.md       # 代码审查
│   ├── TROUBLESHOOTING.md   # 故障排查
│   └── BEST_PRACTICES.md    # 最佳实践
├── go.mod                   # Go 模块定义
├── README.md                # 项目说明
└── CHANGELOG.md             # 变更日志
```

---

## 🔄 数据流

### 启动流程

```
1. main() 入口
   ↓
2. NewManager(configPath)
   ↓
3. LoadConfig() → 加载 YAML
   ↓
4. ValidateConfig() → 验证配置
   ↓
5. ValidateAllWorkspaces() → 验证工作目录
   ↓
6. Start Health Monitor
   ↓
7. Start API Server
   ↓
8. AutoStart() → 启动标记为 auto_start 的实例
```

### 实例启动流程

```
1. POST /api/v1/instances/{id}
   ↓
2. handlers.InstanceHandler()
   ↓
3. manager.Start(id)
   ↓
4. 检查实例是否存在
   ↓
5. 检查工作目录
   ↓
6. exec.Command("/usr/local/bin/picoclaw", ...)
   ↓
7. cmd.Start() → 启动进程
   ↓
8. 更新状态 (PID, Status, StartTime)
   ↓
9. 返回成功
```

### 健康检查流程

```
1. ticker (30s)
   ↓
2. checkAndRecover(manager)
   ↓
3. GetAllStatus() → 获取所有实例
   ↓
4. for each instance:
   ↓
5.   CheckHealth(id) → 检查进程状态
   ↓
6.   if crashed:
   ↓
7.     Restart(id) → 自动重启
   ↓
8.     log.Printf("重启成功")
```

---

## 🔐 安全设计

### 1. 进程隔离

- 每个实例独立进程
- 独立进程组 (Setpgid)
- 独立工作目录

### 2. 资源限制

- 内存限制 (MemoryLimitMB)
- 端口范围限制
- 实例数量限制 (MaxInstances)

### 3. 配置验证

- 启动前验证所有配置
- 防止端口冲突
- 防止无效路径

---

## 📈 性能优化

### 1. 并发控制

```go
// 读操作 (并发)
m.mutex.RLock()
defer m.mutex.RUnlock()

// 写操作 (互斥)
m.mutex.Lock()
defer m.mutex.Unlock()
```

### 2. 分批启动

```go
// 避免同时启动 50 个实例
for i := 0; i < 50; i++ {
    go Start(id)
    time.Sleep(200 * time.Millisecond)
}
```

### 3. 延迟加载

- 配置启动时加载
- 实例按需启动
- 日志延迟写入

---

## 🚀 扩展方向

### 短期 (V0.3.x)

- [ ] 配置热重载 (SIGHUP)
- [ ] API Key 轮询池
- [ ] 日志轮转 (lumberjack)

### 中期 (V1.x)

- [ ] Prometheus 指标导出
- [ ] WebSocket 实时推送
- [ ] 实例模板功能

### 长期 (V2.x)

- [ ] 多机集群支持
- [ ] 负载均衡
- [ ] Kubernetes Operator

---

**🦞 架构简洁，易于扩展！**
