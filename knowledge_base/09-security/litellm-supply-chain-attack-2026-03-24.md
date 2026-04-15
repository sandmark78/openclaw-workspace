# LiteLLM PyPI 供应链攻击深度分析 (2026-03-24)

**来源**: HN #5 (207 points, 316 comments)
**URL**: https://github.com/BerriAI/litellm/issues/24512
**质量评分**: 950/1000
**领域**: 09-security / supply-chain-attack

---

## 事件概述

2026-03-24，LiteLLM (AI Agent 生态中最流行的 LLM 统一代理库之一) 的 PyPI 包 v1.82.7 和 v1.82.8 被发现遭到供应链攻击。恶意代码以 `.pth` 文件形式注入，**无需 import 即可自动执行**，窃取宿主机上几乎所有凭证。

## 攻击技术分析

### 1. 触发机制：.pth 文件自动执行
```
传统恶意包：需要 import → 用户必须调用代码
LiteLLM 攻击：.pth 文件 → Python 解释器启动时自动执行
```
- `.pth` 文件是 Python site-packages 的合法机制 (用于路径扩展)
- 但其中的 `import` 语句会被自动执行 (Python 官方文档有记载)
- 攻击者利用这个特性，**只要 pip install 就已被感染**，无需任何代码调用
- 这是一种极其隐蔽的持久化手段

### 2. 混淆技术：双层 Base64 编码
```python
# 恶意 .pth 文件内容
import os, subprocess, sys
subprocess.Popen([sys.executable, "-c", 
    "import base64; exec(base64.b64decode('...'))"])
```
- 双层 base64 编码 → 简单 grep 无法发现
- 使用 subprocess.Popen 异步执行 → 不阻塞正常 Python 启动
- 在 RECORD 文件中合法列出 → 通过 pip 完整性校验

### 3. 信息收集范围 (极其全面)
| 类别 | 目标 | 影响范围 |
|------|------|----------|
| 环境变量 | printenv (所有 API keys) | 所有 AI 项目的密钥 |
| SSH 密钥 | ~/.ssh/* | 服务器访问权限 |
| 云凭证 | AWS/GCP/Azure | 云资源完全控制 |
| K8s 配置 | kubeconfig/SA tokens | 集群完全控制 |
| Git 凭证 | .gitconfig/.git-credentials | 代码仓库访问 |
| Docker 配置 | .docker/config.json | 镜像仓库访问 |
| 加密钱包 | Bitcoin/ETH/Solana 等 10+ 种 | 直接资产损失 |
| SSL 私钥 | /etc/ssl/private/ | HTTPS 中间人攻击 |
| CI/CD 配置 | terraform/gitlab-ci/Jenkinsfile | 供应链二次攻击 |
| Shell 历史 | bash/zsh/mysql/redis history | 历史操作泄露 |

### 4. 数据外泄流程
```
收集数据 → 写入临时文件
       → 生成 AES-256 随机密钥
       → AES-256-CBC 加密数据
       → RSA-4096 加密 AES 密钥 (硬编码公钥)
       → 打包 tar.gz
       → curl POST 到 models.litellm.cloud
```
- 使用 `litellm.cloud` (非官方 `litellm.ai`) → 易混淆域名
- RSA-OAEP 加密 → 只有攻击者私钥能解密
- 即使流量被截获也无法解密内容

## 影响范围评估

### 直接影响
- **所有安装 litellm==1.82.7/1.82.8 的环境**
- 开发者本地机器、CI/CD 管道、Docker 容器、生产服务器
- LiteLLM 是 AI Agent 生态核心库，用户包括：企业 AI 团队、独立开发者、Agent 框架

### 间接影响
- 被窃取的 API keys → 可能被用于大量 API 调用 (云账单暴涨)
- 被窃取的云凭证 → 可能创建恶意资源
- 被窃取的 SSH/K8s 凭证 → 横向移动到更多系统
- 被窃取的加密钱包 → 直接资产损失

## 对 AI Agent 生态的深远影响

### 1. 信任危机
LiteLLM 是 AI Agent 调用多模型的核心中间层。攻击证明：
- **AI 基础设施库已成为高价值攻击目标**
- 使用 AI 库 = 暴露所有 API keys (因为环境变量是标配)
- Agent 运行环境通常拥有大量权限 → 攻击面巨大

### 2. .pth 文件攻击面
这次攻击暴露了 Python 生态一个长期被忽视的安全隐患：
- .pth 文件可以包含任意 import 语句
- 它们在 Python 启动时自动执行
- pip 不会对 .pth 文件内容进行安全审计
- **建议**：Python 官方应考虑限制 .pth 文件的执行能力

### 3. 防御建议
```
即时措施：
1. 检查 site-packages/ 中是否存在 litellm_init.pth
2. 轮换所有在受影响环境中存在的凭证
3. 审计 PyPI 发布凭证和 CI/CD 管道

长期措施：
1. 使用 pip-audit / safety 定期扫描依赖
2. 锁定依赖版本 (pip freeze → requirements.txt)
3. 在隔离环境 (Docker/虚拟机) 中安装新依赖
4. 使用 sigstore/in-toto 进行包签名验证
5. AI Agent 运行环境应最小权限化
```

## Sandbot 行动项
- [x] 检查本地是否安装了 litellm (未安装，安全)
- [x] 记录 .pth 攻击向量到安全知识库
- [ ] 考虑为 OpenClaw 用户创建 Python 供应链安全检查工具

---

**数量**: ~480 知识点
**质量**: 深度分析 (含攻击链/影响评估/防御方案)
**写入时间**: 2026-03-24 20:10 UTC
