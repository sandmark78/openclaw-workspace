# 管理 50 个 PicoClaw 实例指南

**版本**: V0.3.3  
**最后更新**: 2026-03-31

---

## 🏗️ 架构对比

### Claworc 方式 (Docker 容器)

```
Claworc (控制平面)
    ↓ Docker
PicoClaw × 50 (50 个独立容器)
    - 每个容器 ~100MB
    - 总内存 ~5GB
    - 需要 Docker 支持
```

### Lobster 方式 (进程管理)

```
Lobster Orchestrator (单进程 ~10MB)
    ↓ 进程管理
PicoClaw × 50 (50 个独立进程)
    - 每个进程 ~10MB
    - 总内存 ~500MB
    - 无需 Docker
```

**优势**:
- ✅ 内存占用减少 90% (5GB → 500MB)
- ✅ 无需 Docker (手机也能跑)
- ✅ 启动更快 (秒级 vs 分钟级)
- ✅ 管理简单 (单二进制)

---

## 📋 50 实例部署步骤

### 步骤 1: 安装 PicoClaw (一次即可)

```bash
# 下载
wget https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_Linux_arm64.tar.gz

# 解压
tar xzf picoclaw_Linux_arm64.tar.gz

# 安装
mkdir -p $HOME/bin
mv picoclaw $HOME/bin/
chmod +x $HOME/bin/picoclaw

# 验证
which picoclaw
# 输出：/data/data/com.termux/files/home/bin/picoclaw
```

---

### 步骤 2: 生成 50 实例配置

```bash
cd lobster-orchestrator

# 自动生成 50 个实例配置
./scripts/generate-config.sh 50
```

**生成的配置** (`configs/instances.yaml`):
```yaml
instances:
  - id: "lobster-001"
    name: "Sandbot #1"
    workspace: "data/workspaces/lobster-001"
    port: 18790
    model: "qwen3.5-plus"
    api_key_env: "BAILOU_API_KEY_1"
    memory_limit_mb: 10
    auto_start: true

  - id: "lobster-002"
    name: "Sandbot #2"
    workspace: "data/workspaces/lobster-002"
    port: 18791
    model: "qwen3.5-plus"
    api_key_env: "BAILOU_API_KEY_2"
    memory_limit_mb: 10
    auto_start: true

  # ... 共 50 个实例
```

---

### 步骤 3: 准备工作目录

```bash
# 批量创建工作目录
for i in $(seq 1 50); do
    mkdir -p data/workspaces/lobster-$(printf "%03d" $i)
done

# 验证
ls data/workspaces/ | wc -l
# 输出：50
```

---

### 步骤 4: 准备 API Key

**方式 A: 单个 API Key (共享)**

编辑 `configs/instances.yaml`:
```yaml
instances:
  - id: "lobster-001"
    api_key_env: "BAILOU_API_KEY"  # 所有实例共享
  - id: "lobster-002"
    api_key_env: "BAILOU_API_KEY"  # 相同
```

设置环境变量:
```bash
export BAILOU_API_KEY="sk-你的 API Key"
```

**方式 B: 多个 API Key (轮询)**

```bash
# 设置多个 API Key
export BAILOU_API_KEY_1="sk-key1"
export BAILOU_API_KEY_2="sk-key2"
# ...
export BAILOU_API_KEY_50="sk-key50"
```

---

### 步骤 5: 启动服务

```bash
# 设置 PicoClaw 路径
export PICOCLAW_PATH=$HOME/bin/picoclaw

# 启动 Lobster
./orchestrator -config configs/instances.yaml
```

---

### 步骤 6: 批量启动实例

**方式 A: 自动启动 (配置 auto_start: true)**

Lobster 会自动逐个启动 50 个实例，无需手动操作。

**方式 B: 分批启动 (推荐)**

```bash
# 第一批：1-10
for i in $(seq 1 10); do
    curl -X POST http://localhost:8080/api/v1/instances/lobster-$(printf "%03d" $i)
    sleep 2  # 间隔 2 秒
done

# 等待稳定
sleep 30

# 第二批：11-20
for i in $(seq 11 20); do
    curl -X POST http://localhost:8080/api/v1/instances/lobster-$(printf "%03d" $i)
    sleep 2
done

# ... 重复直到 50 个
```

---

## 📊 资源监控

### 查看实例状态

```bash
# 所有实例
curl http://localhost:8080/api/v1/instances | jq

# 运行中的实例数
curl http://localhost:8080/api/v1/instances | jq '.instances | map(select(.status=="running")) | length'

# Dashboard
# 浏览器打开：http://localhost:8080
```

### 监控内存使用

```bash
# 总内存
ps aux | grep -E "(orchestrator|picoclaw)" | awk '{sum+=$6} END {printf "总内存：%.2fMB\n", sum/1024}'

# 单个实例
ps aux | grep picoclaw | head -5
```

### 监控 CPU 使用

```bash
top -bn1 | grep "Cpu(s)"
```

---

## 🎯 性能基准

| 指标 | 目标 | 实测 (参考) |
|------|------|-------------|
| 单实例内存 | <10MB | ~8MB |
| 50 实例总内存 | <500MB | ~400MB |
| 启动时间 (50 实例) | <5 分钟 | ~3 分钟 |
| CPU 占用 | <50% | ~30% |
| 稳定性 | 24h 无崩溃 | 待测试 |

---

## 🔧 高级配置

### 分批启动配置

```yaml
instances:
  # 第一批：1-10 (立即启动)
  - id: "lobster-001"
    auto_start: true
  # ...
  - id: "lobster-010"
    auto_start: true

  # 第二批：11-20 (手动启动)
  - id: "lobster-011"
    auto_start: false
  # ...
  - id: "lobster-020"
    auto_start: false
```

### 内存限制

```yaml
instances:
  - id: "lobster-001"
    memory_limit_mb: 10  # 每实例 10MB
```

### 端口分配

```yaml
instances:
  - id: "lobster-001"
    port: 18790  # 连续端口
  - id: "lobster-002"
    port: 18791
  # ...
  - id: "lobster-050"
    port: 18839
```

---

## ⚠️ 常见问题

### Q1: 实例启动失败

**问题**: `fork/exec: resource temporarily unavailable`

**解决**:
```bash
# 减少并发启动数量
# 编辑配置，设置 auto_start: false
# 然后分批手动启动
```

### Q2: 内存不足

**问题**: `out of memory`

**解决**:
```bash
# 减少实例数量
./scripts/generate-config.sh 20  # 只运行 20 个

# 或降低内存限制
nano configs/instances.yaml
# memory_limit_mb: 5  # 从 10 改为 5
```

### Q3: API Key 限流

**问题**: `rate limit exceeded`

**解决**:
```bash
# 使用多个 API Key 轮询
export BAILOU_API_KEY_1="sk-key1"
export BAILOU_API_KEY_2="sk-key2"
# ...

# 或降低请求频率
```

### Q4: 端口冲突

**问题**: `bind: address already in use`

**解决**:
```bash
# 检查占用
netstat -tlnp | grep 18790

# 修改配置使用其他端口
nano configs/instances.yaml
```

---

## 📈 扩展建议

### 水平扩展 (多设备)

```
手机 1: Lobster + PicoClaw × 25
手机 2: Lobster + PicoClaw × 25
总计：50 实例
```

### 负载均衡

```
Nginx 反向代理
    ↓
Lobster 实例 1 (25 个 PicoClaw)
Lobster 实例 2 (25 个 PicoClaw)
```

---

## 🦞 Lobster vs Claworc

| 特性 | Claworc | Lobster |
|------|---------|---------|
| 隔离方式 | Docker 容器 | 进程 |
| 内存占用 | ~5GB (50 实例) | ~500MB |
| 启动时间 | ~5 分钟 | ~3 分钟 |
| 依赖 | Docker | 无 |
| 手机支持 | ❌ | ✅ |
| 管理复杂度 | 中 | 低 |

---

**🦞 50 个实例，500MB 内存，手机也能跑！**
