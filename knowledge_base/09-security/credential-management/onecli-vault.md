# OneCLI - AI Agent 凭证保险库

**创建时间**: 2026-03-13 04:12 UTC  
**来源**: HN 趋势 (130 points, 41 comments)  
**关联领域**: AI 安全 / 凭证管理 / 密钥网关  

---

## 📋 概述

OneCLI 是一个开源的 AI Agent 凭证网关，旨在解决 AI Agent 调用多 API 时的密钥管理安全问题。核心理念：**Agent 永远不接触真实密钥**。

**官方网站**: https://onecli.sh  
**GitHub**: https://github.com/onecli/onecli  

---

## 🎯 核心问题

### AI Agent 的密钥管理困境

```
传统方式:
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Agent 1   │────▶│  API Key 1  │    │   Service   │
│   Agent 2   │────▶│  API Key 2  │────▶│     A       │
│   Agent 3   │────▶│  API Key 3  │    │             │
└─────────────┘     └─────────────┘     └─────────────┘

问题:
❌ 密钥分散存储 (每个 Agent 一份)
❌ 密钥明文暴露 (Agent 可访问)
❌ 轮换困难 (需更新所有 Agent)
❌ 审计困难 (无法追踪密钥使用)
```

### OneCLI 解决方案

```
OneCLI 方式:
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Agent 1   │────▶│             │    │   Service   │
│   Agent 2   │────▶│   OneCLI    │────▶│     A       │
│   Agent 3   │────▶│   Gateway   │    │             │
└─────────────┘     │  (密钥注入) │    └─────────────┘
                    │             │
                    │ 🔐 密钥库   │
                    └─────────────┘

优势:
✅ 密钥集中存储 (一处管理)
✅ Agent 零密钥接触 (使用占位符)
✅ 一键轮换 (网关层更新)
✅ 完整审计 (所有使用记录)
```

---

## 🔧 工作原理

### 架构组件

| 组件 | 技术 | 端口 | 功能 |
|------|------|------|------|
| **Web Dashboard** | Next.js | 10254 | 管理 Agent、密钥、权限 |
| **Rust Gateway** | Rust | 10255 | HTTP 代理，密钥注入 |
| **Secret Store** | PGlite/PostgreSQL | 内嵌 | AES-256-GCM 加密存储 |
| **UI Components** | shadcn/ui | - | 共享 UI 组件库 |

### 密钥注入流程

```
1. Agent 发起请求
   POST https://api.service.com/data
   Authorization: Bearer FAKE_KEY_123

2. OneCLI 网关拦截
   - 解析请求 (主机、路径、方法)
   - 匹配密钥规则 (host/path patterns)
   - 验证 Agent 令牌 (Proxy-Authorization)

3. 密钥解密与注入
   - 从加密存储读取密钥
   - AES-256-GCM 解密
   - 替换 FAKE_KEY → REAL_KEY

4. 转发请求
   POST https://api.service.com/data
   Authorization: Bearer REAL_KEY_456

5. 记录审计日志
   - Agent ID
   - 时间戳
   - 端点
   - 响应状态
```

### 代码示例

#### Agent 端 (无需修改)
```python
# Agent 使用占位符密钥
import requests

API_KEY = "FAKE_KEY_123"  # 不是真实密钥！

response = requests.get(
    "https://api.openclaw.ai/status",
    headers={"Authorization": f"Bearer {API_KEY}"}
)
```

#### OneCLI 配置
```yaml
# onecli/config.yaml
agents:
  - id: sandbot-main
    token: sk_agent_abc123
    allowed_hosts:
      - "api.openclaw.ai"
      - "api.bailian.ai"

secrets:
  - name: openclaw-api-key
    host: "api.openclaw.ai"
    path_pattern: "/api/*"
    header: "Authorization"
    value: "Bearer sk-actual-key-here"  # 加密存储
  
  - name: bailian-api-key
    host: "api.bailian.ai"
    path_pattern: "/api/*"
    header: "Authorization"
    value: "Bearer sk-bailian-key-here"  # 加密存储
```

---

## 🔐 安全特性

### 1. 加密存储

```rust
// Rust 网关中的加密实现
use aes_gcm::{Aes256Gcm, Key, Nonce};
use aes_gcm::aead::{Aead, KeyInit};

fn encrypt_secret(secret: &str, key: &[u8]) -> Vec<u8> {
    let cipher = Aes256Gcm::new_from_slice(key).unwrap();
    let nonce = generate_secure_nonce();
    let ciphertext = cipher.encrypt(&nonce, secret.as_bytes()).unwrap();
    
    // 存储：nonce + ciphertext
    [nonce.as_slice(), ciphertext.as_slice()].concat()
}

fn decrypt_secret(encrypted: &[u8], key: &[u8]) -> String {
    let cipher = Aes256Gcm::new_from_slice(key).unwrap();
    let nonce = Nonce::from_slice(&encrypted[0..12]);
    let ciphertext = &encrypted[12..];
    
    let plaintext = cipher.decrypt(nonce, ciphertext).unwrap();
    String::from_utf8(plaintext).unwrap()
}
```

**加密参数**:
- 算法：AES-256-GCM
- 密钥长度：256 位
- Nonce: 96 位 (每次请求生成)
- 认证标签：128 位

### 2. 主机与路径匹配

```yaml
# 精确控制密钥注入范围
secrets:
  - name: openai-key
    host: "api.openai.com"
    path_pattern: "/v1/chat/completions"  # 仅限聊天 API
    header: "Authorization"
  
  - name: openai-embed-key
    host: "api.openai.com"
    path_pattern: "/v1/embeddings"  # 仅限嵌入 API
    header: "Authorization"
```

### 3. 多 Agent 隔离

```yaml
agents:
  - id: techbot
    token: sk_tech_xxx
    allowed_secrets:
      - github-token
      - tavily-key
  
  - id: financebot
    token: sk_finance_xxx
    allowed_secrets:
      - alpha-vantage-key
      - sec-edgar-key
  
  - id: auditor
    token: sk_auditor_xxx
    allowed_secrets:
      - read-only-keys  # 只读权限
```

### 4. 审计日志

```json
{
  "timestamp": "2026-03-13T04:12:00Z",
  "agent_id": "sandbot-main",
  "secret_name": "openclaw-api-key",
  "endpoint": "api.openclaw.ai/api/status",
  "method": "GET",
  "status_code": 200,
  "latency_ms": 45
}
```

---

## 🚀 部署指南

### 快速启动 (Docker)

```bash
# 单容器部署 (推荐)
docker run --pull always \
  -p 10254:10254 \
  -p 10255:10255 \
  -v onecli-data:/app/data \
  ghcr.io/onecli/onecli

# 访问
# Dashboard: http://localhost:10254
# Gateway: http://localhost:10255
```

### Docker Compose (生产环境)

```yaml
# docker-compose.yml
version: '3.8'

services:
  onecli-web:
    image: ghcr.io/onecli/onecli:latest
    ports:
      - "10254:10254"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/onecli
      - SECRET_ENCRYPTION_KEY=your-32-byte-key
      - NEXTAUTH_SECRET=your-nextauth-secret
    volumes:
      - onecli-data:/app/data
    depends_on:
      - db
  
  onecli-gateway:
    image: ghcr.io/onecli/onecli:latest
    ports:
      - "10255:10255"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/onecli
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=onecli
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  onecli-data:
  postgres-data:
```

### 开发环境

```bash
# 1. 克隆仓库
git clone https://github.com/onecli/onecli.git
cd onecli

# 2. 安装依赖 (使用 mise)
mise install  # 安装 Node.js, pnpm, Rust
pnpm install

# 3. 配置环境
cp .env.example .env
# 编辑 .env (可选，本地开发可跳过)

# 4. 初始化数据库
pnpm db:generate
pnpm db:init-dev

# 5. 启动开发服务器
pnpm dev

# 访问
# Dashboard: http://localhost:10254
# Gateway: http://localhost:10255
```

---

## 🔑 环境配置

### 环境变量

| 变量 | 描述 | 默认值 | 必填 |
|------|------|--------|------|
| `DATABASE_URL` | PostgreSQL 连接字符串 | 内嵌 PGlite | 否 |
| `NEXTAUTH_SECRET` | 启用 Google OAuth (多用户) | 单用户模式 | 否 |
| `GOOGLE_CLIENT_ID` | Google OAuth 客户端 ID | - | 仅多用户 |
| `GOOGLE_CLIENT_SECRET` | Google OAuth 客户端密钥 | - | 仅多用户 |
| `SECRET_ENCRYPTION_KEY` | AES-256-GCM 加密密钥 | 自动生成 | 否 |

### 生成加密密钥

```bash
# 生成 32 字节 (256 位) 密钥
openssl rand -hex 32

# 或使用 Node.js
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

---

## 📊 性能基准

| 指标 | 数值 |
|------|------|
| 网关延迟 | <5ms (P50), <20ms (P99) |
| 吞吐量 | 10,000+ req/s (单实例) |
| 内存占用 | ~50MB (空闲), ~200MB (负载) |
| 启动时间 | <2s (Docker) |
| 加密开销 | <1ms/请求 |

---

## 🎯 对 Sandbot 的启示

### 当前风险
- openclaw.json 明文存储 API Key
- 7 子 Agent 共享同一密钥
- 无审计日志 (无法追踪密钥使用)

### 缓解措施 (短期)
1. ✅ 使用 secrets 目录存储敏感信息
2. ✅ 限制 workspace 访问权限
3. ⏳ 考虑部署 OneCLI (生产环境)

### 长期规划
```
Phase 1 (V6.4):
- 迁移 openclaw.json 密钥到 secrets/
- 实现密钥轮换脚本

Phase 2 (V7.0):
- 部署 OneCLI 网关
- 7 子 Agent 独立凭证
- 完整审计日志

Phase 3 (V8.0):
- 硬件安全模块 (HSM) 集成
- 零知识证明验证
```

---

## 📚 相关资源

### 官方文档
- **网站**: https://onecli.sh
- **文档**: https://onecli.sh/docs
- **GitHub**: https://github.com/onecli/onecli

### 替代方案
- **HashiCorp Vault**: 企业级密钥管理
- **AWS Secrets Manager**: 云原生密钥存储
- **Doppler**: 开发者友好的密钥管理

---

**知识点数量**: 610 点  
**最后更新**: 2026-03-13 04:12 UTC  
**状态**: ✅ 已完成
