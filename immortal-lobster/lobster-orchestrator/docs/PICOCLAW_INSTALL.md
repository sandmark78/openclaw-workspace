# PicoClaw 安装指南

**Lobster Orchestrator** 是编排器，需要配合 **PicoClaw** 使用！

---

## 📋 架构说明

```
Lobster Orchestrator (编排器)
    ↓ 管理
PicoClaw × N (实际运行的 AI Agent)
```

- **Lobster Orchestrator**: 管理器 (启动/停止/监控实例)
- **PicoClaw**: 实际运行的 AI Agent (需要单独安装)

---

## 🚀 PicoClaw 安装

### Termux/Android (ARM64)

```bash
# 1. 下载 PicoClaw
wget https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_Linux_arm64.tar.gz

# 2. 解压
tar xzf picoclaw_Linux_arm64.tar.gz

# 3. 移动到 PATH
mkdir -p $HOME/bin
mv picoclaw $HOME/bin/
chmod +x $HOME/bin/picoclaw

# 4. 验证
picoclaw --version
```

### Linux (x86_64)

```bash
# 1. 下载 PicoClaw
wget https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_Linux_amd64.tar.gz

# 2. 解压
tar xzf picoclaw_Linux_amd64.tar.gz

# 3. 移动到 PATH
sudo mv picoclaw /usr/local/bin/
chmod +x /usr/local/bin/picoclaw

# 4. 验证
picoclaw --version
```

### macOS

```bash
# 1. 下载 PicoClaw
wget https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_Darwin_amd64.tar.gz

# 2. 解压
tar xzf picoclaw_Darwin_amd64.tar.gz

# 3. 移动到 PATH
sudo mv picoclaw /usr/local/bin/
chmod +x /usr/local/bin/picoclaw

# 4. 验证
picoclaw --version
```

---

## ⚙️ PicoClaw 配置

```bash
# 创建配置目录
mkdir -p ~/.picoclaw

# 创建配置文件
cat > ~/.picoclaw/config.json << 'EOF'
{
  "model": {
    "provider": "bailian",
    "name": "qwen3.5-plus"
  },
  "api_key": "你的 API Key"
}
EOF
```

---

## 🔧 Lobster Orchestrator 配置

### 方式 1: 环境变量 (推荐)

```bash
# 设置 PicoClaw 路径
export PICOCLAW_PATH=$HOME/bin/picoclaw

# 启动 Lobster
./orchestrator -config configs/instances.yaml
```

### 方式 2: 修改配置

```bash
# 编辑配置文件
nano configs/instances.yaml

# 添加全局配置
global:
  picoclaw_path: "/home/用户名/bin/picoclaw"  # 替换为实际路径
```

### 方式 3: 自动检测

如果 PicoClaw 在 PATH 中，Lobster 会自动找到：

```bash
# 验证 PicoClaw 是否在 PATH 中
which picoclaw

# 输出示例：/home/用户名/bin/picoclaw
```

---

## ✅ 完整启动流程

```bash
# 1. 安装 PicoClaw
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

# 4. 启动 Lobster Orchestrator
cd lobster-orchestrator
./orchestrator -config configs/instances.yaml

# 5. 验证
curl http://localhost:8080/api/v1/health
```

---

## ⚠️ 常见问题

### Q1: `picoclaw: command not found`

**解决**:
```bash
# 检查 PATH
echo $PATH

# 添加 PicoClaw 到 PATH
export PATH=$HOME/bin:$PATH
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
```

### Q2: `permission denied`

**解决**:
```bash
# 添加执行权限
chmod +x $HOME/bin/picoclaw
```

### Q3: Lobster 找不到 PicoClaw

**解决**:
```bash
# 设置环境变量
export PICOCLAW_PATH=$HOME/bin/picoclaw

# 或修改配置
nano configs/instances.yaml
# 添加：picoclaw_path: "/home/用户名/bin/picoclaw"
```

---

## 📊 验证安装

```bash
# 检查 PicoClaw
picoclaw --version
which picoclaw

# 检查 Lobster
./orchestrator -config configs/instances.yaml

# 检查实例状态
curl http://localhost:8080/api/v1/instances
```

---

## 🦞 Lobster + PicoClaw = 完整系统

| 组件 | 功能 | 必须 |
|------|------|------|
| Lobster Orchestrator | 实例管理/监控/备份 | ✅ |
| PicoClaw | AI Agent 运行时 | ✅ |
| 配置文件 | 实例配置/API Key | ✅ |
| 工作目录 | 记忆/知识库/技能 | ✅ |

---

**🦞 先安装 PicoClaw，再启动 Lobster！**
