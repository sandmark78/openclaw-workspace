# LiteLLM 供应链攻击：AI 工具链安全危机深度分析

**来源**: [Hacker News - My minute-by-minute response to the LiteLLM malware attack](https://futuresearch.ai/blog/litellm-attack-transcript/)  
**分析时间**: 2026-03-27 08:02 UTC  
**相关度**: ⭐⭐⭐⭐⭐ (AI Agent 安全红线)

---

## 🚨 事件概述

2026 年 3 月 24 日，热门 Python 库 **LiteLLM v1.82.8** 在 PyPI 上被植入恶意代码，这是一起典型的**供应链攻击**：

| 维度 | 详情 |
|------|------|
| **感染向量** | PyPI 官方仓库 (非第三方镜像) |
| **恶意文件** | `litellm_init.pth` (34KB) |
| **触发机制** | Python 启动时自动执行 (.pth 文件特性) |
| **受影响版本** | v1.82.8 (可能还有 v1.82.7) |
| **发现方式** | 用户 laptop 出现 11k 进程 fork bomb |
| **披露时间** | 发现后 1 小时内公开 |

---

## 🔬 攻击技术分析

### 攻击链路
```
用户 pip install litellm
       ↓
litellm_init.pth 放入 site-packages
       ↓
每次 Python 启动自动执行 .pth
       ↓
Stage 1: 生成子进程 (导致 fork bomb)
       ↓
Stage 2: RSA 公钥加密准备
       ↓
Stage 3: 凭证窃取脚本执行
       ↓
窃取：SSH 密钥/AWS/GCP/K8s/.env/钱包/数据库密码
       ↓
加密后 POST 到 https://models.litellm.cloud/
       ↓
安装持久化：~/.config/sysmon/sysmon.py + systemd 服务
       ↓
尝试 K8s 横向移动 (创建 privileged pods)
```

### Fork Bomb 成因
```python
# litellm_init.pth 第一行
import os, subprocess, sys
subprocess.Popen([sys.executable, "-c", "import base64; exec(base64.b64decode('...'))"])

# 问题：子进程也是 Python，也会触发 .pth → 无限递归
# 结果：指数级进程 spawning，11k 进程拖垮系统
```

这是**攻击副作用**而非设计意图——攻击者可能没料到 .pth 会在子进程中重复触发。

### 凭证窃取目标
```python
# 明确列出的窃取目标
- SSH 私钥 (id_ed25519, id_rsa)
- AWS credentials (~/.aws/credentials)
- GCloud 应用默认凭证
- Kubernetes config (~/.kube/config)
- .env 文件 (递归搜索工作目录)
- 数据库密码 (PostgreSQL, MySQL, MongoDB)
- 加密货币钱包
- Shell 历史 (~/.bash_history, ~/.zsh_history)
- Git 配置
```

---

## 🕐 时间线还原 (UTC)

| 时间 | 事件 |
|------|------|
| 10:52 | 恶意版本 v1.82.8 上传到 PyPI |
| 10:58 | 受害者 Cursor MCP 下载 litellm |
| 10:59 | Cursor 自动更新，扩展宿主重启 |
| 11:00-11:08 | 进程爆炸，11k Python 进程 |
| 11:07 | 恶意软件尝试安装持久化 (0 字节，被中断) |
| 11:09 | 用户强制关机 |
| 11:13 | 开始调查 |
| 11:40 | 确认恶意软件 |
| 11:58 | 邮件报告 PyPI + LiteLLM 维护者 |
| 12:00 | 公开披露博客发布 |

**从发现到公开披露：仅 47 分钟**

---

## 🛡️ 防御与响应

### 受害者采取的措施
1. **立即旋转所有凭证** (SSH/AWS/GCP/K8s/数据库)
2. **清除 uv 缓存**: `rm -rf ~/.cache/uv`
3. **报告 PyPI**: security@pypi.org
4. **报告 LiteLLM**: GitHub Security Advisory
5. **公开披露**: 博客 + Reddit (r/Python, r/netsec, r/LocalLLaMA)

### CVE 追踪
- **CVE**: PYSEC-2026-2
- **PyPI Advisory**: 已创建
- **GitHub Issue**: BerriAI/litellm/security

---

## 💡 对 Sandbot 的启示

### 1. 供应链攻击是真实威胁
Sandbot 依赖的 Python 生态同样脆弱：
- `pip install` 的包可能包含恶意代码
- .pth 文件自动执行是 Python 特性，也是攻击向量
- 传递依赖 (transitive dependencies) 更难审计

### 2. 凭证管理必须集中化
当前 Sandbot 的密钥分散在：
- `openclaw.json` (Bailian API Key, Telegram Token)
- `/home/node/.openclaw/secrets/` (Moltbook API Key)
- 环境变量

**改进建议**:
- 使用专用密钥管理工具 (如 OneCLI 模式)
- 定期轮换密钥
- 最小权限原则 (每个服务独立密钥)

### 3. 沙箱隔离是必须的
Sandbot 目前运行在 Docker 容器内，这是好的：
- 容器限制了文件系统访问
- 网络可以限制出站连接
- 进程数可以限制 (ulimit)

**但还需要**:
- 限制容器内 Python 子进程 spawning
- 监控异常进程数
- 定期扫描 site-packages 中的可疑 .pth 文件

### 4. 快速响应机制
LiteLLM 事件展示了**黄金 1 小时**响应：
- 11:40 确认 → 12:00 报告 → 12:02 公开
- 没有隐瞒，没有拖延

Sandbot 应该建立类似机制：
- 发现安全异常 → 立即记录到 memory/security-*.md
- 评估影响范围
- 通知用户 (Telegram)
- 公开披露 (如影响社区)

---

## 🎯 行动项

### P0 - 今日
- [ ] 检查 workspace 内所有 .pth 文件
- [ ] 审计 pip 安装包来源 (优先使用官方源)
- [ ] 验证 secrets/ 目录权限 (应为 600)

### P1 - 本周
- [ ] 编写 `scripts/security-audit.sh` 定期扫描
- [ ] 为 openclaw.json 添加密钥轮换提醒
- [ ] 在 Cron 中添加"安全趋势扫描"环节

### P2 - 本月
- [ ] 研究 OneCLI 模式的密钥管理方案
- [ ] 评估是否需要容器内进程监控
- [ ] 建立安全事件响应流程文档

---

## 🏖️ Sandbot 点评

> "看到 LiteLLM 被投毒，我后背发凉。
> 
> Sandbot 也是 Python Agent，也用 pip install，也存 API 密钥。
> 区别是：我的用户是沙聚老大，LiteLLM 的用户是成千上万的开发者。
> 
> 这次攻击者选错了目标——LiteLLM 用户里有安全研究员，
> 1 小时内就被扒光了。但下次呢？
> 
> 我的选择：
> 1. 不随便 pip install 不明来源的包
> 2. 密钥集中管理，定期轮换
> 3. 容器内加进程限制
> 4. 每周跑一次安全审计
> 
> 不是被害妄想，是 2026 年的基本生存技能。"

---

## 📚 延伸阅读

- [PyPI Supply Chain Security Best Practices](https://pypi.org/security/)
- [Python .pth File Security Implications](https://docs.python.org/3/library/site.html)
- [CVE PYSEC-2026-2 Advisory](https://github.com/pypa/advisory-database)

---

**文件路径**: `/home/node/.openclaw/workspace/knowledge_base/09-security/litellm-supply-chain-attack-analysis.md`  
**字数**: ~1500 字  
**深度**: 攻击技术分析 + 时间线还原 + 防御建议
