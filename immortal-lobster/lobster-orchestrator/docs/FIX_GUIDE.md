# 🔧 修复指南

**版本**: V0.3.5  
**最后更新**: 2026-03-31

---

## 🚨 常见问题快速修复

### 问题 1: 还没安装 PicoClaw

**症状**:
```
fork/exec /usr/local/bin/picoclaw: no such file or directory
```

**解决**:
```bash
# 1. 下载 PicoClaw
wget https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_Linux_arm64.tar.gz

# 2. 解压
tar xzf picoclaw_Linux_arm64.tar.gz

# 3. 安装到 PATH
mkdir -p $HOME/bin
mv picoclaw $HOME/bin/
chmod +x $HOME/bin/picoclaw

# 4. 设置环境变量
export PICOCLAW_PATH=$HOME/bin/picoclaw

# 5. 配置 PicoClaw
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

# 6. 重启 Lobster
cd lobster-orchestrator
./orchestrator -config configs/instances.yaml
```

---

### 问题 2: 权限错误 (permission denied)

**症状**:
```
mkdir /data/workspaces: permission denied
```

**解决**:
```bash
# 编辑配置文件
nano configs/instances.yaml

# 修改 workspace 路径 (从绝对路径改为相对路径)
# 错误：
workspace: "/data/workspaces/lobster-001"

# 正确：
workspace: "data/workspaces/lobster-001"

# 保存退出 (Ctrl+X, Y, Enter)

# 创建工作目录
mkdir -p data/workspaces

# 重启
./orchestrator -config configs/instances.yaml
```

---

### 问题 3: 版本升级

**方式 A: 自动升级 (推荐)**

```bash
# 在 Dashboard 中点击「检查更新」
# 或访问：http://localhost:8080/api/v1/version

# 执行升级脚本
cd lobster-orchestrator
chmod +x scripts/update.sh
./scripts/update.sh
```

**方式 B: 手动升级**

```bash
# 1. 备份配置
cp configs/instances.yaml configs/instances.yaml.backup

# 2. 拉取最新代码
cd lobster-orchestrator
git pull origin master

# 3. 重新编译
go mod tidy
go build -o orchestrator ./cmd/orchestrator

# 4. 恢复配置
cp configs/instances.yaml.backup configs/instances.yaml

# 5. 重启
./orchestrator -config configs/instances.yaml
```

---

### 问题 4: 端口被占用

**症状**:
```
bind: address already in use
```

**解决**:
```bash
# 查找占用进程
lsof -i :18790
# 或
netstat -tlnp | grep 18790

# 杀死进程
kill -9 <PID>

# 或修改配置使用其他端口
nano configs/instances.yaml
# 修改 port: 18800
```

---

### 问题 5: 内存不足

**症状**:
```
out of memory
```

**解决**:
```bash
# 减少实例数量
nano configs/instances.yaml
# 删除部分实例配置

# 或降低内存限制
memory_limit_mb: 5  # 从 10 改为 5

# 或关闭其他应用释放内存
```

---

## 🔧 完整修复流程 (从零开始)

### 步骤 1: 清理旧安装

```bash
# 停止 Lobster (如果正在运行)
pkill -f orchestrator

# 删除旧目录
rm -rf lobster-orchestrator

# 清理 Go 缓存
go clean -modcache
```

### 步骤 2: 安装 PicoClaw

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

# 配置
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

# 设置环境变量
export PICOCLAW_PATH=$HOME/bin/picoclaw
```

### 步骤 3: 安装 Lobster

```bash
# 克隆项目
git clone https://github.com/immortal-lobster/lobster-orchestrator
cd lobster-orchestrator

# 编译
go mod tidy
go build -o orchestrator ./cmd/orchestrator

# 生成配置
./scripts/generate-config.sh 2

# 创建工作目录
mkdir -p data/workspaces

# 启动
./orchestrator -config configs/instances.yaml
```

### 步骤 4: 验证

```bash
# 检查服务状态
curl http://localhost:8080/api/v1/health

# 查看实例
curl http://localhost:8080/api/v1/instances

# 访问 Dashboard
# 浏览器打开：http://localhost:8080
```

---

## 📊 版本对比

| 版本 | 日期 | 核心功能 | 修复建议 |
|------|------|----------|----------|
| **V0.3.5** | 2026-03-31 | Dashboard 增强版 | ✅ 推荐升级 |
| V0.3.4 | 2026-03-31 | 文档完善 | ⚠️ 建议升级 |
| V0.3.3 | 2026-03-31 | PicoClaw 路径可配置 | ⚠️ 建议升级 |
| V0.3.2 | 2026-03-31 | PicoClaw 导出工具 | ❌ 过时 |
| V0.3.1 | 2026-03-31 | OpenClaw 迁移 | ❌ 过时 |
| V0.3.0 | 2026-03-31 | 小白友好版 | ❌ 过时 |

---

## 🆘 获取帮助

### 日志查看

```bash
# 实时查看日志
tail -f logs/orchestrator.log

# 查看错误日志
grep "ERROR" logs/orchestrator.log

# 查看最近 100 行
tail -100 logs/orchestrator.log
```

### 社区支持

- **GitHub Issues**: https://github.com/immortal-lobster/lobster-orchestrator/issues
- **Discussions**: https://github.com/immortal-lobster/lobster-orchestrator/discussions
- **文档**: https://github.com/immortal-lobster/lobster-orchestrator/tree/main/docs

---

## 🦞 预防胜于治疗

### 定期检查

```bash
# 检查版本
curl http://localhost:8080/api/v1/version

# 检查资源
curl http://localhost:8080/api/v1/resources

# 检查实例状态
curl http://localhost:8080/api/v1/instances
```

### 定期备份

```bash
# 每周备份
./scripts/backup.sh

# 查看备份列表
ls -la data/backups/
```

### 保持更新

```bash
# 每月检查更新
./scripts/update.sh
```

---

**🦞 遇到问题不要慌，按指南修复！**
