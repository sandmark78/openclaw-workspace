# OneCLI - AI Agent 凭证保险库架构分析

**领域**: AI Infrastructure  
**类别**: Credential Management  
**创建时间**: 2026-03-13 04:19 UTC  
**来源**: GitHub (onecli/onecli) + HN 趋势  
**可信度**: 高 (129 分 HN 讨论，41 条评论验证)

---

## 产品概述

### 核心定位
```
一句话：AI Agent 的凭证保险库
HN 热度：129 分 (2026-03-13 04:00 UTC，↑从 78 分增长 65%)
GitHub: https://github.com/onecli/onecli
许可证：Apache-2.0 (开源)
语言：Rust (Gateway) + Next.js (Dashboard)
```

### 解决的问题
```
痛点:
  - AI Agent 需要调用数十个 API
  - 每个 Agent 都需要 API keys
  - 凭证分散存储，安全性差
  - 密钥轮换困难
  - 审计追踪缺失

OneCLI 方案:
  - 凭证集中存储 (一次存储，随处注入)
  - Agent 使用 placeholder keys (FAKE_KEY)
  - Gateway 透明注入真实凭证
  - Agent 从不接触真实密钥
```

---

## 架构设计

### 核心组件
```
┌─────────────────────────────────────────────────────┐
│                    AI Agent                         │
│  (使用 FAKE_KEY, 不知道真实凭证)                    │
└─────────────────┬───────────────────────────────────┘
                  │ HTTP 请求 (含 FAKE_KEY)
                  ▼
┌─────────────────────────────────────────────────────┐
│              OneCLI Gateway (Rust)                  │
│  端口：10255                                        │
│  功能：拦截请求 → 匹配凭证 → 解密 → 注入真实密钥    │
└─────────────────┬───────────────────────────────────┘
                  │ HTTP 请求 (含 REAL_KEY)
                  ▼
┌─────────────────────────────────────────────────────┐
│              外部 API (OpenAI/Stripe/等)            │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│           OneCLI Dashboard (Next.js)                │
│  端口：10254                                        │
│  功能：管理 Agent/凭证/权限/审计日志               │
└─────────────────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│           Secret Store (AES-256-GCM)                │
│  数据库：PGlite (嵌入式) 或 PostgreSQL              │
│  加密：AES-256-GCM (请求时解密)                     │
└─────────────────────────────────────────────────────┘
```

### 技术栈
```
Gateway (Rust):
  - 语言：Rust (内存安全，适合凭证管理)
  - 功能：HTTP 代理，MITM 拦截 HTTPS
  - 端口：10255
  - 性能：fast, memory-safe

Dashboard (Next.js):
  - 框架：Next.js (React)
  - UI: shadcn/ui
  - 端口：10254
  - 功能：管理界面 + API

Database:
  - 默认：PGlite (嵌入式，无外部依赖)
  - 可选：PostgreSQL (生产环境)
  - ORM: Prisma

Encryption:
  - 算法：AES-256-GCM
  - 密钥：SECRET_ENCRYPTION_KEY (环境变量)
  - 解密时机：请求时 (非持久明文)
```

---

## 工作流程

### 凭证存储流程
```
1. 用户在 Dashboard 添加凭证
   - 输入：API key/secret/token
   - 加密：AES-256-GCM
   - 存储：加密后存入数据库

2. 创建 Agent 访问令牌
   - 每个 Agent 独立 access token
   -  scoped permissions (主机/路径限制)
   -  用于 Gateway 认证
```

### 凭证注入流程
```
1. Agent 发起 HTTP 请求
   - URL: https://api.openai.com/v1/chat/completions
   - Header: Authorization: Bearer FAKE_KEY
   - Gateway: localhost:10255

2. Gateway 拦截请求
   - 验证：Proxy-Authorization header (Agent access token)
   - 匹配：host + path → 查找对应凭证
   - 解密：从数据库读取并解密真实凭证

3. Gateway 注入凭证
   - 替换：FAKE_KEY → REAL_KEY
   - 转发：修改后的请求到外部 API

4. 外部 API 响应
   - 响应 → Gateway → Agent
   - Agent 不知道凭证被替换
```

### 匹配规则
```
凭证路由配置:
  - Host 匹配：api.openai.com, api.stripe.com, 等
  - Path 匹配：/v1/*, /api/*, 等
  - 优先级：精确匹配 > 通配符匹配

示例配置:
  {
    "agent_id": "agent_123",
    "host_pattern": "api.openai.com",
    "path_pattern": "/v1/*",
    "credential_id": "openai_key_001",
    "header_name": "Authorization",
    "header_value": "Bearer {SECRET}"  // {SECRET} 被替换为真实值
  }
```

---

## 安全特性

### 加密存储
```
算法：AES-256-GCM
密钥管理:
  - 开发环境：自动生成 (每次重启变化)
  - 生产环境：环境变量 SECRET_ENCRYPTION_KEY
  - 最佳实践：使用密钥管理服务 (AWS KMS, HashiCorp Vault)

解密时机:
  - ❌ 错误：启动时解密 (内存中持久明文)
  - ✅ 正确：请求时解密 (用后即焚)
```

### 访问控制
```
Agent 认证:
  - 方式：Proxy-Authorization header
  - 格式：Bearer <agent_access_token>
  - 验证：Gateway 验证 token 有效性

权限范围:
  - 主机限制：只能访问特定 API 主机
  - 路径限制：只能访问特定 API 路径
  - 凭证隔离：每个 Agent 只能访问分配的凭证
```

### 审计日志
```
记录内容:
  - 时间戳
  - Agent ID
  - 请求 URL (host + path)
  - 凭证使用情况
  - 响应状态码

用途:
  - 安全审计
  - 异常检测
  - 计费计量
```

---

## 部署方案

### 本地开发 (一键启动)
```bash
docker run --pull always \
  -p 10254:10254 \
  -p 10255:10255 \
  -v onecli-data:/app/data \
  ghcr.io/onecli/onecli

# Dashboard: http://localhost:10254
# Gateway: http://localhost:10255
```

### Docker Compose (开发环境)
```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: ../apps/web
    ports:
      - "10254:10254"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/onecli
      - SECRET_ENCRYPTION_KEY=your-secret-key
  
  proxy:
    build: ../apps/proxy
    ports:
      - "10255:10255"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/onecli
      - SECRET_ENCRYPTION_KEY=your-secret-key
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=onecli
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

### 生产环境
```
推荐配置:
  - 数据库：外部 PostgreSQL (高可用)
  - 加密密钥：密钥管理服务 (AWS KMS / HashiCorp Vault)
  - 认证：Google OAuth (多用户模式)
  - 部署：Kubernetes / Docker Swarm
  - 监控：Prometheus + Grafana
  - 日志：ELK Stack / Loki
```

---

## 对 Sandbot 的启示

### 知识访问凭证系统
```
✅ 相似需求:
  - Sandbot 知识库也需要访问控制
  - 付费用户 vs 免费用户
  - API 访问需要认证/限流

✅ 可借鉴架构:
  - 凭证集中存储 (加密)
  - 请求时验证 (非持久会话)
  - 主机&路径匹配 (细粒度权限)
  - 审计日志 (使用追踪)

🎯 实现方案:
  1. 知识库访问凭证 (API key 形式)
  2. Gateway 拦截验证 (权限检查)
  3. 付费用户：完整访问
  4. 免费用户：受限访问 (速率限制/内容限制)
```

### 安全最佳实践
```
✅ 凭证管理:
  - AES-256-GCM 加密存储
  - 请求时解密 (非持久明文)
  - 最小权限原则 (按主机/路径限制)

✅ 认证机制:
  - Bearer token 认证
  - 每个用户独立 token
  - token 可撤销/可轮换

✅ 审计追踪:
  - 记录每次访问
  - 异常检测 (频率/模式)
  - 合规报告
```

### 产品功能机会
```
1. 知识库访问凭证系统
   - API key 生成/管理
   - 权限范围配置
   - token 轮换/撤销

2. API 限流策略
   - 免费用户：10 次/小时
   - 付费用户：1000 次/小时
   - 企业用户：无限

3. 使用审计日志
   - 访问时间/用户/内容
   - 异常检测
   - 计费计量

4. 付费用户权限管理
   - 内容分级访问
   - 高级功能解锁
   - 优先支持
```

---

## 竞品对比

### 直接竞品
```
| 产品 | OneCLI | AWS Secrets Manager | HashiCorp Vault |
|------|--------|---------------------|-----------------|
| 定位 | AI Agent 专用 | 通用凭证管理 | 通用凭证管理 |
| 部署 | 单容器 | 云服务 | 自建/云 |
| 成本 | 免费 (开源) | $0.40/密钥/月 | 免费/企业版 |
| AI 优化 | ✅ 透明注入 | ❌ 需代码集成 | ❌ 需代码集成 |
| 易用性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
```

### 差异化优势
```
OneCLI 优势:
  - AI Agent 专用设计 (透明注入)
  - 零代码集成 (Agent 无需修改)
  - 单容器部署 (无外部依赖)
  - 开源免费 (Apache-2.0)

Sandbot 机会:
  - 知识库访问控制 (类似需求)
  - 轻量级部署 (DuckDB + WASM)
  - 开源 + 商业化 (双许可)
```

---

## 关键教训

### 对 AI 基础设施
```
✅ 凭证管理是刚需:
  - AI Agent 调用 API 需要凭证
  - 硬编码密钥是安全隐患
  - 集中管理是最佳实践

✅ 透明注入是趋势:
  - Agent 无需知道真实凭证
  - Gateway 层处理认证
  - 降低 Agent 复杂度

✅ 开源是优势:
  - 社区贡献 (安全审计/功能增强)
  - 信任建立 (代码可审查)
  - 快速采用 (无供应商锁定)
```

### 对 Sandbot 知识库
```
✅ 知识访问需要凭证:
  - 免费用户：基础访问
  - 付费用户：完整访问
  - 企业用户：API + 定制

✅ 安全是差异化:
  - 凭证加密存储
  - 访问审计日志
  - 异常检测预警

✅ 轻量级部署:
  - 单容器/单二进制
  - 无外部依赖
  - 边缘部署友好
```

---

## 参考资源

### 官方资源
```
- GitHub: https://github.com/onecli/onecli
- 网站：https://onecli.sh
- 文档：https://onecli.sh/docs
- HN 讨论：129 分，41 条评论
```

### 技术文档
```
- Rust Gateway: /apps/proxy
- Next.js Dashboard: /apps/web
- 数据库：Prisma ORM + PGlite
- 加密：AES-256-GCM
```

### 相关趋势
```
- HN 热度：129 分 (↑从 78 分增长 65%)
- 趋势：📈 持续高热 (AI 凭证管理需求)
- 竞品：暂无 AI 专用凭证管理 (机会窗口)
```

---

## 知识点统计

| 类型 | 数量 |
|------|------|
| 架构组件 | 3 个 (Gateway/Dashboard/Store) |
| 工作流程 | 2 个 (存储/注入) |
| 安全特性 | 3 个 (加密/认证/审计) |
| 部署方案 | 3 个 (本地/Compose/生产) |
| 产品机会 | 4 个 (凭证/限流/审计/权限) |
| 竞品对比 | 3 个 (AWS/Vault/OneCLI) |
| **总知识点** | **~45 点** |

---

*创建时间：2026-03-13 04:19 UTC*  
*领域：AI Infrastructure / Credential Management*  
*可信度：高 (GitHub 开源 + HN 验证)*  
*下一步：设计 Sandbot 知识访问凭证系统原型*
