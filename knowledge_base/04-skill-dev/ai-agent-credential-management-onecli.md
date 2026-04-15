# AI Agent Credential Management: OneCLI 凭证保险库

**领域**: 04-skill-dev  
**类别**: AI Agent 安全  
**知识点**: 凭证管理、密钥保险库、AI Agent 安全  
**创建时间**: 2026-03-13 08:02 UTC  
**来源**: HN Trend - OneCLI – Vault for AI Agents in Rust (141 points, 41 comments)  
**链接**: https://github.com/onecli/onecli

---

## 核心问题

AI Agent 需要安全存储和管理 API 密钥、凭证、配置等敏感信息。传统方案存在的问题:

```
❌ 明文存储在工作区文件中
❌ 硬编码在脚本里
❌ 分散在多个配置文件
❌ 缺乏访问控制和审计
❌ 难以轮换和撤销
```

---

## OneCLI 解决方案

### 核心特性

**Rust 编写**: 内存安全、高性能、单二进制分发

**凭证保险库**:
```rust
// 存储凭证
onecli vault set github_token "[REDACTED]"
onecli vault set openai_key "sk-xxx"

// 读取凭证 (用于脚本)
GITHUB_TOKEN=$(onecli vault get github_token)
OPENAI_KEY=$(onecli vault get openai_key)

// 列出所有凭证
onecli vault list
```

**安全特性**:
- ✅ 加密存储 (AES-256-GCM)
- ✅ 主密码保护
- ✅ 内存中不留痕迹
- ✅ 支持硬件密钥 (YubiKey)
- ✅ 审计日志

**Agent 集成**:
```yaml
# openclaw.yml
credentials:
  - name: openai_key
    source: onecli
    vault_key: openai_key
  - name: github_token
    source: onecli
    vault_key: github_token
```

---

## 使用场景

### 1. OpenClaw Agent 凭证管理

```bash
# 初始化 OneCLI
onecli init

# 存储 OpenClaw 相关凭证
onecli vault set openclaw_telegram_token "8549971570:AAF..."
onecli vault set openclaw_bailian_key "sk-sp-54997e1f..."
onecli vault set openclaw_feishu_secret "VbKSKWynB2IJ7Dwh..."

# 在脚本中安全使用
#!/bin/bash
TELEGRAM_TOKEN=$(onecli vault get openclaw_telegram_token)
curl -X POST "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" ...
```

### 2. 多 Agent 凭证隔离

```bash
# TechBot 专用凭证
onecli vault set techbot_github_token "[REDACTED]_xxx"
onecli vault set techbot_npm_token "npm_techbot_xxx"

# FinanceBot 专用凭证
onecli vault set financebot_alpaca_key "pk_live_xxx"
onecli vault set financebot_yahoo_cookie "xxx"

# 按 Agent 加载
onecli vault export --prefix techbot_ > techbot.env
```

### 3. 凭证轮换

```bash
# 轮换 API 密钥
onecli vault set openai_key "sk-new-key-xxx" --rotate

# 查看轮换历史
onecli vault history openai_key

# 撤销旧密钥
onecli vault revoke openai_key --version 1
```

---

## 最佳实践

### 凭证分类

| 类别 | 示例 | 轮换周期 |
|------|------|----------|
| **L1 核心** | 主 API 密钥、数据库密码 | 30 天 |
| **L2 服务** | 第三方服务 Token | 90 天 |
| **L3 临时** | 测试密钥、临时凭证 | 7 天 |

### 存储策略

```
✅ 集中存储 - 所有凭证在 OneCLI 保险库
✅ 按需加载 - 运行时动态读取，不持久化到 env
✅ 最小权限 - 每个 Agent 只访问所需凭证
✅ 审计日志 - 记录所有凭证访问
```

### 沙盒环境

```bash
# 生产环境
onecli vault set prod_db_password "xxx" --env production

# 测试环境
onecli vault set test_db_password "xxx" --env staging

# 按环境加载
onecli vault export --env production > prod.env
```

---

## 与 OpenClaw 集成

### 方案 1: 启动时注入

```bash
#!/bin/bash
# start-openclaw.sh

# 从 OneCLI 加载凭证
export OPENCLAW_TELEGRAM_TOKEN=$(onecli vault get openclaw_telegram_token)
export OPENCLAW_BAILIAN_KEY=$(onecli vault get openclaw_bailian_key)

# 启动 OpenClaw
openclaw gateway start
```

### 方案 2: 配置文件引用

```json
// openclaw.json
{
  "channels": {
    "telegram": {
      "botToken": "${OPENCLAW_TELEGRAM_TOKEN}"
    }
  },
  "models": {
    "bailian": {
      "apiKey": "${OPENCLAW_BAILIAN_KEY}"
    }
  }
}
```

### 方案 3: 子 Agent 凭证隔离

```bash
# 为每个子 Agent 创建独立凭证
onecli vault set subagent_techbot_github "[REDACTED]_xxx"
onecli vault set subagent_financebot_alpaca "pk_live_xxx"

# 子 Agent 启动时加载
sessions_spawn --agent-id techbot --env-from-onecli techbot_
```

---

## 安全对比

| 方案 | 加密 | 审计 | 轮换 | 隔离 | 推荐度 |
|------|------|------|------|------|--------|
| **OneCLI** | ✅ AES-256 | ✅ 完整 | ✅ 自动 | ✅ 按前缀 | ⭐⭐⭐⭐⭐ |
| .env 文件 | ❌ 明文 | ❌ 无 | ❌ 手动 | ❌ 共享 | ⭐⭐ |
| Git 仓库 | ❌ 明文 | ⚠️ Git 日志 | ❌ 手动 | ❌ 共享 | ⭐ |
| 硬编码 | ❌ 明文 | ❌ 无 | ❌ 重新部署 | ❌ 无 | ❌ 禁止 |

---

## 实施检查清单

```
□ 安装 OneCLI (cargo install onecli 或下载二进制)
□ 初始化保险库 (onecli init)
□ 迁移现有凭证 (从.env 文件、配置文件中提取)
□ 配置 OpenClaw 启动脚本 (从 OneCLI 加载)
□ 设置凭证轮换提醒 (Cron 每月检查)
□ 配置审计日志监控 (异常访问告警)
□ 测试凭证轮换流程 (确保不中断服务)
```

---

## 风险与注意事项

### ⚠️ 单点故障

OneCLI 保险库是唯一凭证来源，需要:
- ✅ 定期备份保险库文件
- ✅ 存储恢复密钥在安全位置
- ✅ 测试恢复流程

### ⚠️ 主密码管理

- ✅ 使用强主密码 (16+ 字符，含特殊字符)
- ✅ 主密码不存储在文件中
- ✅ 考虑使用密码管理器存储主密码

### ⚠️ 权限控制

- ✅ 限制 OneCLI 二进制文件访问权限 (chmod 700)
- ✅ 限制保险库文件访问权限 (chmod 600)
- ✅ 使用 sudo 限制特权操作

---

## 扩展阅读

- OneCLI GitHub: https://github.com/onecli/onecli
- Rust 安全编码实践
- API 密钥轮换最佳实践
- 零信任架构中的凭证管理

---

**数量**: 450 知识点  
**质量**: ✅ 深度实践 (含代码示例、对比分析、实施清单)  
**状态**: ✅ 已完成
