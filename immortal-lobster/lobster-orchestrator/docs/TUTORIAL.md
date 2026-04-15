# 🦞 Lobster Orchestrator 小白教程

**版本**: V0.2.4  
**目标**: 零基础也能安装使用

---

## 📋 目录

1. [安装前准备](#安装前准备)
2. [一键安装](#一键安装)
3. [配置说明](#配置说明)
4. [启动服务](#启动服务)
5. [使用 Dashboard](#使用-dashboard)
6. [备份恢复](#备份恢复)
7. [常见问题](#常见问题)

---

## 安装前准备

### 1. 检查系统

**支持的系统**:
- ✅ Android (Termux)
- ✅ Linux (Ubuntu/Debian)
- ❌ Windows (需要 WSL)

**检查命令**:
```bash
# Android/Termux
uname -a
# 预期包含 "android"

# Linux
uname -a
# 预期包含 "Linux"
```

### 2. 确保网络畅通

需要访问 GitHub 下载代码。

---

## 一键安装

### 方式 A: 自动安装 (推荐)

**⚠️ 前提条件：先安装 PicoClaw！**

```bash
# 1. 安装 PicoClaw (AI Agent 运行时)
wget https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_Linux_arm64.tar.gz
tar xzf picoclaw_Linux_arm64.tar.gz
mkdir -p $HOME/bin
mv picoclaw $HOME/bin/
chmod +x $HOME/bin/picoclaw

# 2. 配置 PicoClaw
mkdir -p ~/.picoclaw
cat > ~/.picoclaw/config.json << 'EOF'
{
  "model": {
    "provider": "bailian",
    "name": "qwen3.5-plus"
  },
  "api_key": "你的 API Key"
}
EOF

# 3. 设置环境变量
export PICOCLAW_PATH=$HOME/bin/picoclaw

# 4. 安装 Lobster Orchestrator (编排器)
curl -sL https://raw.githubusercontent.com/immortal-lobster/lobster-orchestrator/master/scripts/install.sh | bash
```

**一行命令搞定 (已安装 PicoClaw 后)**:

```bash
# Android/Termux
curl -sL https://raw.githubusercontent.com/immortal-lobster/lobster-orchestrator/master/scripts/install.sh | bash

# Linux
curl -sL https://raw.githubusercontent.com/immortal-lobster/lobster-orchestrator/master/scripts/install.sh | sudo bash
```

**注意**: 使用 `master` 分支，不是 `main`！

**安装过程**:
```
╔════════════════════════════════════════════════════════╗
║     🦞 Lobster Orchestrator 一键安装脚本              ║
║     不死龙虾编排器 - 手机运行 50 个 PicoClaw 实例        ║
╚════════════════════════════════════════════════════════╝

[INFO] 检测系统环境...
[INFO] 检测到 Termux (Android)
[INFO] 检查依赖...
[SUCCESS] Git 已安装
[SUCCESS] Go 已安装 (go version go1.21.0)
[INFO] 克隆项目...
[SUCCESS] 项目已克隆
[INFO] 安装 Go 依赖...
[SUCCESS] 依赖已安装
[INFO] 编译项目...
[SUCCESS] 编译成功！
-rwxr-xr-x 1 node node 15M Mar 30 18:00 orchestrator
[INFO] 创建工作目录...
[SUCCESS] 目录已创建
[INFO] 生成配置文件...
[SUCCESS] 配置已生成 (10 个实例)

╔════════════════════════════════════════════════════════╗
║              🎉 安装完成！                             ║
╚════════════════════════════════════════════════════════╝
```

### 方式 B: 手动安装

```bash
# 1. 克隆项目
git clone https://github.com/immortal-lobster/lobster-orchestrator
cd lobster-orchestrator

# 2. 安装依赖
go mod tidy

# 3. 编译
go build -o orchestrator ./cmd/orchestrator

# 4. 创建目录
mkdir -p data/workspaces data/backups logs

# 5. 生成配置
./scripts/generate-config.sh 10
```

---

## 配置说明

### 配置文件位置

```
lobster-orchestrator/configs/instances.yaml
```

### 编辑配置

```bash
# 使用 nano 编辑器
nano configs/instances.yaml

# 或使用 vim
vim configs/instances.yaml
```

### 配置示例

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

global:
  orchestrator_port: 8080
  health_check_interval_s: 30
  log_level: "info"
  max_instances: 50
```

### 配置说明

| 字段 | 说明 | 示例 |
|------|------|------|
| `id` | 实例唯一 ID | `lobster-001` |
| `name` | 实例名称 | `Sandbot #1` |
| `workspace` | 工作目录 | `data/workspaces/lobster-001` |
| `port` | 实例端口 | `18790` |
| `model` | AI 模型 | `qwen3.5-plus` |
| `api_key_env` | API Key 环境变量 | `BAILOU_API_KEY_1` |
| `memory_limit_mb` | 内存限制 (MB) | `10` |
| `auto_start` | 是否自动启动 | `true` |

---

## 启动服务

### 启动

```bash
./orchestrator -config configs/instances.yaml
```

**预期输出**:
```
🦞 INFO [orchestrator] 2026/03/30 18:00:00 加载配置文件：configs/instances.yaml
🦞 INFO [orchestrator] 2026/03/30 18:00:00 ✅ 配置验证通过
🦞 INFO [orchestrator] 2026/03/30 18:00:00 ✅ 加载 10 个实例配置
🦞 INFO [orchestrator] 2026/03/30 18:00:00 ✅ 健康监控已启动
🦞 INFO [orchestrator] 2026/03/30 18:00:00 🌐 API 服务器已启动 (http://localhost:8080)
🦞 INFO [orchestrator] 2026/03/30 18:00:00 🚀 开始自动启动...
🦞 INFO [orchestrator] 2026/03/30 18:00:00 🚀 启动实例：Sandbot #1 (端口：18790)
🦞 INFO [orchestrator] 2026/03/30 18:00:01 ✅ 实例 Sandbot #1 已启动 (PID: 12345, Port: 18790)
🦞 INFO [orchestrator] 2026/03/30 18:00:01 ✅ 自动启动完成 (10 个实例)
```

### 后台运行

```bash
# 使用 nohup
nohup ./orchestrator -config configs/instances.yaml &

# 或使用 screen
screen -S lobster
./orchestrator -config configs/instances.yaml
# 按 Ctrl+A, D 退出 screen
```

### 开机自启 (Termux)

```bash
# 创建启动脚本
mkdir -p ~/.termux/boot
cat > ~/.termux/boot/lobster.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/lobster-orchestrator
./orchestrator -config configs/instances.yaml
EOF
chmod +x ~/.termux/boot/lobster.sh
```

---

## 使用 Dashboard

### 访问 Dashboard

打开浏览器，访问：
```
http://localhost:8080
```

### Dashboard 功能

1. **实例列表**: 查看所有实例状态
2. **启动/停止**: 控制实例运行
3. **实时监控**: 查看内存/CPU 使用
4. **日志查看**: 查看实例日志

### 手机访问

如果在手机上运行：
```
http://127.0.0.1:8080
```

---

## 备份恢复

### 备份数据

```bash
./scripts/backup.sh
```

**备份内容**:
- ✅ 配置文件
- ✅ 工作区数据 (可选)
- ✅ 日志文件 (最近 7 天)

**备份位置**:
```
data/backups/YYYYMMDD_HHMMSS/
```

### 恢复数据

```bash
# 查看可用备份
./scripts/restore.sh

# 恢复到指定备份
./scripts/restore.sh 20260330_180000
```

### 自动备份

```bash
# 添加到 crontab (每天凌晨 2 点备份)
0 2 * * * cd ~/lobster-orchestrator && ./scripts/backup.sh
```

---

## 常见问题

### Q1: 安装失败

**问题**: `curl: command not found`

**解决**:
```bash
# Termux
pkg install curl

# Linux
sudo apt-get install curl
```

### Q2: 编译失败

**问题**: `go: command not found`

**解决**:
```bash
# Termux
pkg install golang

# Linux
sudo apt-get install golang
```

### Q3: 端口被占用

**问题**: `bind: address already in use`

**解决**:
```bash
# 查找占用进程
lsof -i :8080

# 杀死进程
kill -9 <PID>

# 或修改配置
nano configs/instances.yaml
# 修改 orchestrator_port: 8081
```

### Q4: 实例启动失败

**问题**: `exec: "/usr/local/bin/picoclaw": not found`

**解决**:
```bash
# 安装 PicoClaw
git clone https://github.com/sipeed/picoclaw
cd picoclaw
go build -o picoclaw ./cmd/picoclaw
sudo mv picoclaw /usr/local/bin/
```

### Q5: 内存不足

**问题**: `out of memory`

**解决**:
```bash
# 减少实例数量
nano configs/instances.yaml
# 删除部分实例配置

# 或降低内存限制
memory_limit_mb: 5  # 从 10 改为 5
```

---

## 📞 获取帮助

### 查看日志

```bash
# 实时查看日志
tail -f logs/orchestrator.log

# 查看错误日志
grep "ERROR" logs/orchestrator.log
```

### 社区支持

- **GitHub Issues**: https://github.com/immortal-lobster/lobster-orchestrator/issues
- **文档**: https://github.com/immortal-lobster/lobster-orchestrator/tree/main/docs

---

## 🎓 进阶学习

- [API 文档](docs/API.md) - 完整 API 接口说明
- [架构设计](docs/ARCHITECTURE.md) - 系统架构详解
- [最佳实践](docs/BEST_PRACTICES.md) - 运维优化建议
- [故障排查](docs/TROUBLESHOOTING.md) - 常见问题解决

---

**🦞 不死龙虾，从零开始！**
