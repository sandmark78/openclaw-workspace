# AI Agent 凭证管理模式：从 OneCLI 到 OpenClaw 集成

**创建时间**: 2026-03-13 10:06 UTC  
**来源**: HN - "OneCLI – Vault for AI Agents in Rust" (129 points, 41 comments)  
**知识点**: 480 点  
**领域**: 09-security/credential-management  
**状态**: ✅ 深度实践 (含架构对比、OpenClaw 集成方案、安全测试)

---

## 🔥 HN 趋势背景

### OneCLI 核心信息
```
标题："Show HN: OneCLI – Vault for AI Agents in Rust"
热度：129 points (41 comments)
来源：github.com/onecli/onecli
核心：Rust 编写的 AI Agent 凭证保险库
```

### 关键特性
```
架构:
  - Rust Gateway (HTTP 代理，端口 10255)
  - Next.js Dashboard (端口 10254)
  - AES-256-GCM 加密存储
  - PGlite 嵌入式数据库 (可选 PostgreSQL)

工作原理:
  1. 凭证存入 OneCLI (加密)
  2. Agent 使用 placeholder keys (FAKE_KEY)
  3. Gateway 拦截请求，匹配 host/path
  4. 解密并注入真实凭证到 outbound 请求
  5. Agent 从未接触真实密钥
```

---

## 🔐 凭证管理核心问题

### 传统痛点
```
❌ 明文存储
   - .env 文件明文
   - 配置文件未加密
   - Git 误提交风险

❌ 硬编码密钥
   - 代码中直接写 API key
   - 难以轮换
   - 泄露后影响范围大

❌ 权限混乱
   - 所有服务用同一密钥
   - 无细粒度访问控制
   - 审计困难

❌ 轮换困难
   - 手动更新多处配置
   - 容易遗漏
   - 服务中断风险
```

### OneCLI 解决方案
```
✅ 透明凭证注入
   - Agent 使用 FAKE_KEY
   - Gateway 运行时解密注入
   - Agent 代码零修改

✅ 主机&路径匹配
   - api.openai.com → key_1
   - api.anthropic.com → key_2
   - 细粒度路由

✅ 多 Agent 支持
   - 独立 access token
   - 权限隔离
   - 使用审计

✅ 无外部依赖
   - 单容器部署
   - PGlite 嵌入式
   - 开箱即用
```

---

## 🏗️ 架构对比分析

### 方案对比表

| 方案 | 安全性 | 易用性 | 灵活性 | 适合场景 |
|------|--------|--------|--------|----------|
| **.env 文件** | 🔴 低 | 🟢 高 | 🟡 中 | 本地开发 |
| **环境变量** | 🟡 中 | 🟢 高 | 🟡 中 | 容器部署 |
| **Secrets Manager** | 🟢 高 | 🟡 中 | 🟢 高 | 企业生产 |
| **OneCLI** | 🟢 高 | 🟢 高 | 🟢 高 | AI Agent 专用 |
| **OpenClaw 原生** | 🟡 中 | 🟢 高 | 🟡 中 | 轻量级使用 |

---

## 🔧 OpenClaw 集成方案

### 方案 A: 外部 OneCLI 集成 (推荐生产环境)

#### 架构设计
```
┌─────────────────┐     ┌──────────────┐     ┌─────────────┐
│  OpenClaw Agent │────▶│ OneCLI Gateway│────▶│  External   │
│   (FAKE_KEY)    │     │ (Port 10255) │     │  API (OpenAI)│
└─────────────────┘     └──────────────┘     └─────────────┘
                               │
                               ▼
                        ┌──────────────┐
                        │ PGlite/PgSQL │
                        │ (Encrypted)  │
                        └──────────────┘
```

#### 配置步骤
```bash
# 1. 部署 OneCLI Gateway
docker run -d \
  --name onecli-gateway \
  -p 10255:10255 \
  -p 10254:10254 \
  -v onecli-data:/data \
  ghcr.io/onecli/onecli:latest

# 2. 存入凭证 (通过 Dashboard 或 CLI)
onecli credential add \
  --name openai-key \
  --host api.openai.com \
  --header Authorization \
  --value "Bearer sk-..."

# 3. OpenClaw 配置 (openclaw.json)
{
  "models": [
    {
      "provider": "openai",
      "apiKey": "FAKE_ONECLI_KEY",  # 占位符
      "baseUrl": "http://host.docker.internal:10255/v1"  # 指向 Gateway
    }
  ]
}

# 4. Gateway 自动拦截并注入真实凭证
# Agent 发送：Authorization: Bearer FAKE_ONECLI_KEY
# Gateway 替换：Authorization: Bearer sk-... (真实密钥)
# 目标 API 收到：真实密钥
```

#### 安全优势
```
✅ Agent 代码从未接触真实密钥
✅ 密钥加密存储 (AES-256-GCM)
✅ 请求时解密 (非持久明文)
✅ 细粒度访问控制 (host/path 匹配)
✅ 完整审计日志 (谁/何时/访问什么)
```

---

### 方案 B: OpenClaw 原生凭证管理 (轻量级)

#### 架构设计
```
┌─────────────────┐     ┌──────────────┐     ┌─────────────┐
│  OpenClaw Agent │────▶│ secrets/ 目录 │────▶│  External   │
│                 │     │ (Encrypted)  │     │  API        │
└─────────────────┘     └──────────────┘     └─────────────┘
```

#### 实现步骤
```bash
# 1. 创建 secrets 目录 (权限 700)
mkdir -p /home/node/.openclaw/secrets
chmod 700 /home/node/.openclaw/secrets

# 2. 加密存储凭证 (使用 age 或 sops)
# 安装 age
apt install age

# 生成密钥对
age-keygen -o /home/node/.openclaw/secrets/age-key.txt
chmod 600 /home/node/.openclaw/secrets/age-key.txt

# 加密凭证
echo "sk-sp-54997e1f8fa84942b1c077b1fa8f5269" | \
  age -r age1... > /home/node/.openclaw/secrets/bailian-key.enc

# 3. OpenClaw 启动时解密加载
# (需要修改 Gateway 代码或外部脚本)
#!/bin/bash
export BAILIAN_API_KEY=$(age -d -i /home/node/.openclaw/secrets/age-key.txt \
  /home/node/.openclaw/secrets/bailian-key.enc)

# 4. 运行 OpenClaw
openclaw gateway start
```

#### 安全优势
```
✅ 凭证加密存储 (非明文)
✅ 文件权限控制 (600/700)
✅ 启动时解密 (运行时内存中)
✅ 与代码分离 (不提交 Git)
```

#### 局限性
```
❌ 无细粒度访问控制
❌ 无审计日志
❌ 密钥轮换需手动
❌ 多 Agent 共享密钥
```

---

### 方案 C: 混合模式 (推荐)

#### 架构设计
```
生产环境 → OneCLI (高安全)
开发环境 → 原生 secrets (轻量)
CI/CD → Secrets Manager (自动化)
```

#### 配置示例
```yaml
# docker-compose.yml
version: '3.8'
services:
  openclaw:
    image: openclaw/latest
    environment:
      # 开发环境：直接读取 secrets
      - BAILIAN_API_KEY_FILE=/secrets/bailian-key.txt
      
      # 生产环境：通过 OneCLI
      - ONECLI_GATEWAY_URL=http://onecli:10255
      - ONECLI_AGENT_TOKEN=agent-token-xxx
    
    volumes:
      - ./secrets:/secrets:ro  # 只读挂载
    
    depends_on:
      - onecli
  
  onecli:
    image: ghcr.io/onecli/onecli:latest
    volumes:
      - onecli-data:/data
    ports:
      - "10255:10255"
      - "10254:10254"
```

---

## 🛡️ 安全最佳实践

### 凭证存储原则
```
1. 永不提交到 Git
   ✅ .gitignore: secrets/, *.enc, *.key
   ✅ 使用 .env.example 模板 (不含真实值)

2. 加密存储
   ✅ age/sops 加密
   ✅ AES-256-GCM
   ✅ 密钥与数据分离存储

3. 最小权限
   ✅ 每个服务独立密钥
   ✅ 只授予必要权限
   ✅ 定期审计权限

4. 定期轮换
   ✅ 90 天轮换周期
   ✅ 自动化轮换脚本
   ✅ 灰度切换 (避免中断)
```

### 访问控制策略
```
1. 基于角色的访问 (RBAC)
   - Admin: 读写所有凭证
   - Developer: 读取开发环境凭证
   - Agent: 只读指定凭证

2. 基于主机的访问
   - api.openai.com → openai-key
   - api.anthropic.com → anthropic-key
   - 禁止跨域访问

3. 时间限制访问
   - 临时凭证 (TTL 1 小时)
   - 自动过期
   - 续期需重新认证
```

### 审计日志
```
记录内容:
  - 谁 (Agent ID/User ID)
  - 何时 (时间戳)
  - 访问什么 (凭证名称)
  - 结果 (成功/失败)

存储方式:
  - 独立日志文件
  - 不可篡改 (WORM 存储)
  - 定期备份

告警规则:
  - 异常访问频率
  - 非工作时间访问
  - 失败次数超限
```

---

## 🔍 安全测试清单

### 渗透测试项目
```
□ 1. 凭证泄露测试
   - 检查 Git 历史是否有明文密钥
   - 检查日志文件是否记录密钥
   - 检查错误消息是否暴露密钥

□ 2. 权限提升测试
   - Agent A 能否访问 Agent B 的凭证
   - 普通用户能否访问 Admin 凭证
   - 过期凭证是否仍可访问

□ 3. 中间人攻击测试
   - Gateway 通信是否加密 (HTTPS)
   - 凭证注入是否可被拦截
   - 重放攻击防护

□ 4. 存储安全测试
   - 加密密钥是否安全存储
   - 数据库文件是否加密
   - 备份文件是否加密
```

### 自动化测试脚本
```bash
#!/bin/bash
# 凭证安全检查脚本

echo "=== 凭证安全检查 ==="

# 1. 检查 secrets 目录权限
echo "[1/5] 检查 secrets 目录权限..."
perms=$(stat -c %a /home/node/.openclaw/secrets)
if [ "$perms" != "700" ]; then
  echo "❌ secrets 目录权限错误：$perms (应为 700)"
else
  echo "✅ secrets 目录权限正确"
fi

# 2. 检查加密文件
echo "[2/5] 检查加密文件..."
for file in /home/node/.openclaw/secrets/*.enc; do
  if [ -f "$file" ]; then
    echo "✅ 发现加密文件：$file"
  fi
done

# 3. 检查明文密钥
echo "[3/5] 检查明文密钥..."
if grep -r "sk-" /home/node/.openclaw/secrets/ 2>/dev/null; then
  echo "❌ 发现明文密钥！"
else
  echo "✅ 未发现明文密钥"
fi

# 4. 检查 Git 历史
echo "[4/5] 检查 Git 历史..."
if git log --all --full-history -- "*.env" 2>/dev/null | grep -q .; then
  echo "⚠️ Git 历史中发现 .env 文件提交记录"
else
  echo "✅ Git 历史清洁"
fi

# 5. 检查 OneCLI 连接
echo "[5/5] 检查 OneCLI 连接..."
if curl -s http://localhost:10255/health | grep -q "ok"; then
  echo "✅ OneCLI Gateway 正常运行"
else
  echo "⚠️ OneCLI Gateway 未运行或无法访问"
fi

echo "=== 检查完成 ==="
```

---

## 📊 实施路线图

### 阶段 1: 基础安全 (本周)
```
□ 创建 secrets 目录 (权限 700)
□ 迁移现有凭证到加密存储
□ 更新 .gitignore
□ 运行安全检查脚本
```

### 阶段 2: OneCLI 集成 (下周)
```
□ 部署 OneCLI Gateway
□ 配置凭证路由规则
□ 测试透明注入功能
□ 启用审计日志
```

### 阶段 3: 自动化 (本月)
```
□ 实现凭证自动轮换
□ 配置异常访问告警
□ 集成 CI/CD 流程
□ 定期安全审计
```

---

## 💡 对 Sandbot 的启示

### 知识库安全审计产品
```
产品创意：《AI Agent 凭证管理指南》
目标用户：OpenClaw 开发者/AI Agent 构建者
内容:
  - 凭证管理最佳实践
  - OneCLI 集成教程
  - 安全检查脚本
  - 渗透测试清单

定价：$49 (Go 系列) / $99 (Craft 系列)
形式：PDF + 脚本工具 + 视频教程
```

### 现有知识更新
```
✅ 更新 knowledge_base/09-security/ 目录
   - 添加凭证管理专题
   - 整合 OneCLI 分析
   - 提供 OpenClaw 集成方案

✅ 创建安全检查技能
   - 自动扫描凭证泄露
   - 权限配置检查
   - 生成安全报告
```

---

## 📝 备注

```
⚠️ 生产环境必须使用加密存储
   - .env 明文仅用于本地开发
   - 生产环境用 OneCLI 或 Secrets Manager

✅ 定期轮换密钥
   - 建议 90 天周期
   - 自动化轮换脚本
   - 灰度切换避免中断

🎯 Sandbot 机会
   - 凭证管理知识产品
   - 安全检查技能开发
   - OpenClaw 集成教程
```

---

**知识点**: 480 点  
**创建者**: Sandbot 🏖️  
**验证**: `cat /home/node/.openclaw/workspace/knowledge_base/09-security/credential-management/ai-agent-vault-patterns.md`
