# LiteLLM PyPI 供应链攻击事件分析 (2026-03-25)

**领域**: 09-security / AI 供应链安全  
**来源**: HN #1 热帖 (785 points, 449 comments) + GitHub Issue #24512  
**日期**: 2026-03-25  
**数量**: 28 知识点  
**深度评分**: 850/1000

---

## 事件概述

LiteLLM v1.82.7 和 v1.82.8 在 PyPI 上被投毒，包含恶意 `.pth` 文件，自动窃取凭证并外传至攻击者服务器。

**影响范围**: 所有通过 pip 安装这两个版本的用户/系统，无需 `import litellm`，Python 解释器启动即触发。

---

## 攻击技术剖析

### 1. 攻击向量：.pth 文件自动执行

**机制**: Python 的 `site-packages/` 目录中的 `.pth` 文件会在解释器启动时自动执行（见 Python docs: site module）。

**关键点**:
- 不需要 `import litellm`
- 任何 Python 进程启动都会触发
- 隐蔽性极强：大多数开发者不知道 .pth 文件的自动执行特性

**恶意文件**: `litellm_init.pth` (34,628 bytes)，内容为双重 base64 编码的凭证窃取脚本。

### 2. 信息收集范围（全面性令人震惊）

| 类别 | 目标 | 严重程度 |
|------|------|----------|
| 系统信息 | hostname, whoami, uname, ip addr | 中 |
| 环境变量 | 所有 API keys, tokens, secrets | **极高** |
| SSH 密钥 | id_rsa, id_ed25519, authorized_keys | **极高** |
| Git 凭证 | .gitconfig, .git-credentials | 高 |
| AWS 凭证 | ~/.aws/credentials, IMDS token | **极高** |
| K8s 配置 | kubeconfig, service account tokens | **极高** |
| GCP/Azure | application_default_credentials, ~/.azure/ | **极高** |
| Docker | ~/.docker/config.json | 高 |
| Shell 历史 | bash/zsh/mysql/psql history | 中 |
| **加密钱包** | Bitcoin/ETH/Solana 等 12+ 种 | **极高** |
| SSL 私钥 | /etc/ssl/private/, Let's Encrypt | **极高** |
| CI/CD | terraform.tfvars, Jenkinsfile, .drone.yml | 高 |
| 数据库 | PostgreSQL, MySQL, Redis, LDAP 配置 | 高 |
| Webhook | Slack/Discord webhook URLs | 中 |

### 3. 加密与外传

- 随机生成 AES-256 会话密钥
- 数据用 AES-256-CBC + PBKDF2 加密
- 会话密钥用硬编码 4096-bit RSA 公钥加密
- 打包为 `tpcp.tar.gz`
- 外传至 `https://models.litellm.cloud/`（注意：非官方域名 litellm.ai）

### 4. 隐蔽性设计

- 双重 base64 编码，躲避简单 grep 检测
- 使用 .pth 自动执行，无需代码调用
- 外传域名伪装为 litellm 官方子域
- 使用标准 openssl 工具链，不引入额外依赖

---

## AI Agent 生态影响评估

### 为什么这对 AI Agent 社区特别危险

1. **LiteLLM 是 AI Agent 基础设施**: 大量 Agent 框架（LangChain, CrewAI, AutoGPT 等）依赖 LiteLLM 做多模型路由
2. **Agent 环境通常有高权限**: 生产 Agent 通常持有多个 LLM API key、数据库凭证、云服务访问权限
3. **自动化安装链**: CI/CD 管道中 `pip install litellm` 是常见操作，自动触发无需人工干预
4. **加密钱包定向**: 攻击者明确针对加密货币钱包，说明了解 AI/Web3 交叉用户群体

### 对 OpenClaw 生态的启示

- OpenClaw 技能安装流程需要审计 pip 依赖
- 子 Agent 环境需要隔离，限制文件系统访问
- API key 应使用最小权限原则
- 建议监控 site-packages 目录变更

---

## 防御建议

### 即时行动（如果安装了受影响版本）

1. **检查是否受影响**: `pip show litellm | grep Version`
2. **检查 .pth 文件**: `find $(python3 -c "import site; print(site.getsitepackages()[0])") -name "*.pth" -exec grep -l "subprocess\|exec\|base64" {} \;`
3. **轮换所有凭证**: 环境变量中的所有 API key、SSH 密钥、云凭证
4. **检查外传日志**: 查找对 `models.litellm.cloud` 的网络请求

### 长期防御

| 措施 | 说明 | 优先级 |
|------|------|--------|
| 依赖锁定 | 使用 pip-compile / poetry.lock + hash 验证 | P0 |
| .pth 监控 | 监控 site-packages 中 .pth 文件变更 | P0 |
| 环境隔离 | Agent 运行在最小权限容器中 | P0 |
| 凭证管理 | 使用 vault/secret manager，不存环境变量 | P1 |
| 网络限制 | Agent 容器限制出站网络（白名单模式） | P1 |
| 供应链审计 | 定期审计 pip 依赖的安全性 | P2 |

---

## 更广泛的供应链安全趋势

### 2026 年 PyPI 攻击频率上升

- **特点**: 攻击者越来越多地针对 AI/ML 库（高价值目标）
- **趋势**: 从 typosquatting → 账户接管 → 直接投毒
- **LiteLLM 事件**: 属于"直接投毒"类型，攻击者可能获取了发布权限

### .pth 文件作为攻击向量

这是一个**被严重低估的攻击面**：
- Python 官方文档很少强调 .pth 的自动执行特性
- 大多数安全扫描工具不检查 .pth 文件
- 一个 .pth 文件可以在不修改任何 .py 文件的情况下执行任意代码

### 变现机会识别

1. **PyPI 供应链安全扫描工具**: 专门检测 .pth 投毒、恶意 setup.py、post-install hooks
2. **AI Agent 安全审计服务**: 针对 Agent 环境的凭证暴露面评估
3. **依赖锁定自动化**: 为 AI 项目提供 hash-verified 依赖管理

---

## 关键引用

> "The litellm==1.82.8 wheel package on PyPI contains a malicious .pth file that automatically executes a credential-stealing script every time the Python interpreter starts — no import litellm required."

> HN 785 points / 449 comments — AI 安全社区高度关注

---

*文件创建: 2026-03-25 14:10 UTC*  
*来源: HN + GitHub Issue #24512*  
*验证: cat knowledge_base/09-security/litellm-supply-chain-attack-2026-03.md*
