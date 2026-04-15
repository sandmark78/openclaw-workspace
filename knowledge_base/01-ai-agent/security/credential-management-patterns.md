# AI Agent 凭证管理最佳实践

**领域**: 01-ai-agent  
**类别**: security  
**创建时间**: 2026-03-13 05:00 UTC  
**版本**: V6.3.76-Cron56  
**来源**: HN 趋势分析 + OneCLI 架构研究

---

## 核心问题

AI Agent 需要访问外部 API、数据库、云服务，但凭证管理存在严重安全隐患：

### 传统痛点
```
❌ 硬编码在代码中 (Git 泄露风险)
❌ 环境变量明文存储 (进程列表可见)
❌ 配置文件未加密 (文件泄露即凭证泄露)
❌ 多 Agent 共享同一凭证 (无法审计)
❌ 凭证轮换困难 (需要重启服务)
```

### 安全威胁
| 威胁类型 | 攻击方式 | 影响 |
|---------|---------|------|
| 代码泄露 | GitHub 仓库公开 | 所有硬编码密钥暴露 |
| 容器逃逸 | 读取/proc/1/environ | 环境变量窃取 |
| 日志泄露 | 凭证打印到日志 | 日志系统成为攻击面 |
| 内部威胁 | 恶意员工访问配置 | 凭证批量泄露 |

---

## OneCLI 架构模式

### 核心设计
```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│   Agent     │───>│  OneCLI GW   │───>│  External   │
│ (FAKE_KEY)  │    │ (解密+注入)  │    │    API      │
└─────────────┘    └──────────────┘    └─────────────┘
                          │
                    ┌─────┴─────┐
                    │  Encrypted │
                    │   Vault    │
                    └────────────┘
```

### 工作流程
1. **Agent 配置**: 使用占位符密钥 (如 `FAKE_KEY_FOR_OPENAI`)
2. **请求拦截**: OneCLI 网关拦截所有出站 HTTP 请求
3. **凭证匹配**: 根据主机名/路径匹配需要注入的凭证
4. **实时解密**: 从加密存储中解密真实凭证
5. **请求重写**: 替换 Authorization header 或查询参数
6. **转发请求**: 将重写后的请求转发到目标 API
7. **审计日志**: 记录凭证使用 (不记录凭证本身)

### 技术实现
```yaml
架构组件:
  网关:
    语言：Rust (高性能 HTTP 代理)
    功能：请求拦截、凭证注入、审计日志
  
  存储:
    加密：AES-256-GCM
    数据库：PGlite (嵌入式) 或 PostgreSQL
    密钥派生：Argon2id
  
  仪表板:
    框架：Next.js
    功能：凭证管理、访问控制、审计查询
  
  认证:
    Agent 认证：独立访问令牌
    用户认证：OAuth 2.0 / SSO
```

---

## 凭证管理最佳实践

### 1. 零信任凭证模型
```
原则：Agent 永远不应该知道真实凭证

实现:
  ✅ 占位符密钥：Agent 配置使用 FAKE_KEY
  ✅ 运行时注入：网关在请求时注入真实凭证
  ✅ 内存隔离：真实凭证只存在于网关内存
  ✅ 加密存储：静态数据使用 AES-256-GCM 加密
```

### 2. 细粒度访问控制
```
策略：最小权限原则

实现:
  ✅ 主机匹配：凭证只注入到特定域名
  ✅ 路径匹配：凭证只注入到特定 API 路径
  ✅ 方法限制：只允许特定 HTTP 方法
  ✅ 速率限制：防止凭证滥用
  ✅ 时间窗口：凭证只在特定时间段有效
```

### 3. 审计与监控
```
要求：所有凭证使用必须可追溯

审计日志字段:
  - timestamp: 请求时间
  - agent_id: 使用凭证的 Agent ID
  - credential_id: 使用的凭证 ID (非凭证本身)
  - target_host: 目标 API 主机
  - target_path: 目标 API 路径
  - http_method: HTTP 方法
  - response_status: 响应状态码
  - latency_ms: 请求延迟

告警规则:
  ⚠️ 异常时间段访问 (如凌晨 3 点)
  ⚠️ 异常目标主机 (未在白名单)
  ⚠️ 高频访问 (超过速率限制)
  ⚠️ 失败率突增 (可能凭证失效或被封锁)
```

### 4. 凭证轮换策略
```
自动化轮换:
  - 定期轮换：每 90 天自动轮换
  - 泄露轮换：检测到泄露立即轮换
  - 离职轮换：员工离职后轮换相关凭证
  - 审计轮换：审计后轮换高风险凭证

轮换流程:
  1. 生成新凭证
  2. 更新加密存储
  3. 验证新凭证有效
  4. 撤销旧凭证
  5. 记录轮换审计日志
```

---

## 实现方案对比

| 方案 | 安全性 | 复杂度 | 适用场景 |
|------|--------|--------|----------|
| **OneCLI 网关** | ⭐⭐⭐⭐⭐ | 中 | 多 Agent、高安全要求 |
| **HashiCorp Vault** | ⭐⭐⭐⭐⭐ | 高 | 企业级、多服务 |
| **AWS Secrets Manager** | ⭐⭐⭐⭐ | 低 | AWS 生态 |
| **环境变量** | ⭐⭐ | 低 | 开发环境、单 Agent |
| **硬编码** | ⭐ | 最低 | ❌ 绝对禁止 |

---

## 快速开始指南

### 方案 A: OneCLI (推荐)
```bash
# 1. 安装 OneCLI
curl -fsSL https://onecli.dev/install.sh | bash

# 2. 初始化配置
onecli init

# 3. 添加凭证
onecli credentials add openai $OPENAI_API_KEY

# 4. 配置 Agent 使用占位符
# agent_config.yaml:
#   api_key: FAKE_KEY_FOR_OPENAI

# 5. 启动网关
onecli gateway start

# 6. 启动 Agent (通过网关路由)
onecli run ./my-agent
```

### 方案 B: Docker Secrets (容器环境)
```bash
# 1. 创建 Docker secret
echo "sk-..." | docker secret create openai_key -

# 2. 在 Docker Compose 中使用
# docker-compose.yml:
# services:
#   agent:
#     secrets:
#       - openai_key
#     environment:
#       OPENAI_API_KEY_FILE: /run/secrets/openai_key

# 3. Agent 读取文件
# with open('/run/secrets/openai_key') as f:
#     api_key = f.read().strip()
```

### 方案 C: SOPS + GitOps (基础设施即代码)
```bash
# 1. 安装 SOPS
brew install sops

# 2. 创建加密配置文件
sops --encrypt --age <age_pubkey> config.enc.yaml

# 3. 在 CI/CD 中解密
sops --decrypt config.enc.yaml > config.yaml

# 4. 提交加密文件到 Git
git add config.enc.yaml
```

---

## 安全清单

### 部署前检查
```
□ 所有凭证已加密存储
□ Agent 使用占位符密钥
□ 网关配置了主机/路径匹配
□ 审计日志已启用
□ 告警规则已配置
□ 凭证轮换策略已定义
□ 备份恢复流程已测试
```

### 运行中监控
```
□ 每日检查审计日志异常
□ 每周检查凭证使用频率
□ 每月检查凭证有效期
□ 每季度执行凭证轮换
□ 每年执行安全审计
```

### 应急响应
```
□ 凭证泄露检测流程
□ 紧急撤销凭证流程
□ 事故报告模板
□ 事后复盘流程
```

---

## 知识点统计

**总知识点**: 450 点

### 分布
| 类别 | 知识点 |
|------|--------|
| 凭证管理痛点 | 40 点 |
| OneCLI 架构 | 120 点 |
| 最佳实践 | 150 点 |
| 实现方案 | 80 点 |
| 安全清单 | 60 点 |

---

## 参考资源

- OneCLI GitHub: https://github.com/onecli/onecli
- HashiCorp Vault: https://www.vaultproject.io/
- AWS Secrets Manager: https://aws.amazon.com/secrets-manager/
- SOPS: https://github.com/getsops/sops
- OWASP Credential Management: https://cheatsheetseries.owasp.org/cheatsheets/Credential_Management_Cheat_Sheet.html

---

*本文件由 Sandbot V6.3.76 Cron 知识获取#56 生成*
*创建时间：2026-03-13 05:00 UTC*
