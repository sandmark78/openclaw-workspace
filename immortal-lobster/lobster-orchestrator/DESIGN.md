# Lobster Orchestrator - 龙虾编排器

**版本**: V0.1.0  
**创建时间**: 2026-03-30 16:30 UTC  
**目标**: 手机运行 50 个 PicoClaw 实例

---

## 📋 Claworc 架构分析

### Claworc 核心设计

| 组件 | 功能 | 大小 | 手机适配 |
|------|------|------|----------|
| **控制平面** | Web Dashboard + SSH 代理 | 20MB | 需精简到<5MB |
| **实例隔离** | Docker 容器 | ~1GB/实例 | 改用进程隔离 (<10MB) |
| **连接层** | SSH 隧道 (VNC+Gateway) | - | 改用 HTTP 反向代理 |
| **存储** | SQLite + 卷挂载 | - | 简化为文件系统 |

### Claworc 关键特性 (需保留)

1. ✅ **多实例管理** - 启动/停止/监控
2. ✅ **统一入口** - 单端口代理所有实例
3. ✅ **实例隔离** - 独立 workspace
4. ✅ **健康监控** - 自动重启
5. ❌ **Docker 依赖** - 手机不支持
6. ❌ **SSH 隧道** - 太重，改用 HTTP
7. ❌ **VNC 浏览器** - PicoClaw 无 GUI

---

## 🏗️ Lobster Orchestrator 架构设计

### 核心架构

```
┌─────────────────────────────────────────────────────────┐
│              Lobster Orchestrator (单进程)               │
├─────────────────────────────────────────────────────────┤
│  Web Server (Port 8080)                                 │
│  ├─ Dashboard (多实例管理 UI)                            │
│  ├─ Instance Proxy (/instance/{id}/...)                 │
│  └─ API (/api/v1/instances)                             │
├─────────────────────────────────────────────────────────┤
│  Instance Manager                                       │
│  ├─ 实例配置加载 (YAML/JSON)                            │
│  ├─ 进程管理 (spawn/kill/monitor)                       │
│  └─ 资源限制 (内存/CPU)                                 │
├─────────────────────────────────────────────────────────┤
│  PicoClaw Runtime × 50                                  │
│  ├─ 实例 1: workspace_001/, port 18790                  │
│  ├─ 实例 2: workspace_002/, port 18791                  │
│  ├─ ...                                                 │
│  └─ 实例 50: workspace_050/, port 18839                 │
├─────────────────────────────────────────────────────────┤
│  Shared Resources                                       │
│  ├─ LLM API Key Pool (轮询/负载均衡)                     │
│  └─ Common Cache (减少重复调用)                          │
└─────────────────────────────────────────────────────────┘
```

### 技术选型

| 组件 | 选型 | 理由 |
|------|------|------|
| **语言** | Go | PicoClaw 同源，性能高 |
| **Web 框架** | Gin | 轻量，路由灵活 |
| **进程管理** | os/exec + syscall | 原生支持 |
| **配置格式** | YAML | 易读易写 |
| **存储** | 文件系统 | 无需数据库 |
| **目标平台** | Android (Termux) | 旧手机可用 |

---

## 📁 目录结构

```
lobster-orchestrator/
├── cmd/
│   └── orchestrator/
│       └── main.go          # 主入口
├── pkg/
│   ├── instance/
│   │   ├── instance.go      # 实例管理
│   │   ├── manager.go       # 实例管理器
│   │   └── config.go        # 配置结构
│   ├── proxy/
│   │   └── reverse_proxy.go # 反向代理
│   ├── monitor/
│   │   └── health.go        # 健康检查
│   └── api/
│       └── handlers.go      # API 处理
├── web/
│   ├── dashboard.html       # 管理界面
│   └── static/              # 静态资源
├── configs/
│   └── instances.yaml       # 实例配置模板
├── scripts/
│   ├── build.sh             # 编译脚本
│   └── deploy-termux.sh     # Termux 部署
├── go.mod
├── go.sum
└── README.md
```

---

## ⚙️ 实例配置 (instances.yaml)

```yaml
instances:
  - id: "lobster-001"
    name: "Sandbot #1"
    workspace: "/data/workspaces/lobster-001"
    port: 18790
    model: "qwen3.5-plus"
    api_key_env: "BAILOU_API_KEY_1"
    memory_limit_mb: 10
    auto_start: true
    
  - id: "lobster-002"
    name: "Sandbot #2"
    workspace: "/data/workspaces/lobster-002"
    port: 18791
    model: "qwen3.5-plus"
    api_key_env: "BAILOU_API_KEY_2"
    memory_limit_mb: 10
    auto_start: true
    
  # ... 最多 50 个实例

global:
  orchestrator_port: 8080
  health_check_interval_s: 30
  log_level: "info"
  max_instances: 50
```

---

## 🚀 实施计划 (8 小时)

### 阶段 1: 理论研究 (已完成 50%) ⏰ 16:30-18:30
- [x] Claworc 架构分析
- [ ] PicoClaw 启动参数研究
- [x] 本设计文档

### 阶段 2: 核心开发 ⏰ 18:30-21:30 (3h)
- [ ] main.go - 主入口 + CLI
- [ ] instance.go - 实例启动/停止
- [ ] manager.go - 实例管理器 (50 实例并发)
- [ ] proxy.go - 反向代理 (端口路由)

### 阶段 3: Web UI ⏰ 21:30-22:30 (1h)
- [ ] dashboard.html - 管理界面
- [ ] API handlers - RESTful API

### 阶段 4: 测试优化 ⏰ 22:30-00:30 (2h)
- [ ] 单实例测试
- [ ] 10 实例压力测试
- [ ] 50 实例极限测试
- [ ] 内存/CPU 监控

---

## 📊 资源预估

| 资源 | 单实例 | 50 实例 | 手机可用 |
|------|--------|--------|----------|
| **内存** | <10MB | <500MB | ✅ (512MB 手机) |
| **CPU** | <5% | <50% | ✅ (4 核手机) |
| **存储** | ~20MB | ~1GB | ✅ (8GB+ 手机) |
| **网络** | 共享 API | 共享 API | ✅ |

---

## ⚠️ 风险与应对

| 风险 | 概率 | 影响 | 应对 |
|------|------|------|------|
| 内存溢出 | 中 | 高 | 严格内存限制 + OOM 监控 |
| CPU 过热 | 中 | 中 | 降频 + 限流 |
| API 限流 | 高 | 中 | Key Pool + 请求队列 |
| 进程崩溃 | 中 | 高 | 自动重启 + 状态保存 |
| 存储不足 | 低 | 高 | 日志轮转 + 清理机制 |

---

## ✅ 验收标准

1. **功能**
   - [ ] 50 个实例同时运行
   - [ ] Web Dashboard 可管理所有实例
   - [ ] 实例崩溃自动重启
   - [ ] 反向代理正常工作

2. **性能**
   - [ ] 总内存<500MB
   - [ ] CPU<50%
   - [ ] 启动时间<5 分钟 (50 实例)

3. **稳定性**
   - [ ] 连续运行 24 小时无崩溃
   - [ ] 内存无泄漏
   - [ ] 日志正常

---

**🦞 理论推演完成！开始编码！**
