# HN 深度分析：axios npm 供应链攻击事后分析

**分析日期**: 2026-04-04  
**来源**: [GitHub - Post Mortem: axios NPM supply chain compromise](https://github.com/axios/axios/issues/10636)  
**热度**: 238 分 (1 天前)  
**标签**: #安全 #供应链 #npm #开源

---

## 📌 事件概述

```
时间：2026 年 3 月 31 日
影响：两个恶意 axios 版本发布到 npm
恶意版本：1.14.1 和 0.30.4
攻击载荷：plain-crypto-js@4.2.1 (远程访问木马)
影响平台：macOS, Windows, Linux
存活时间：约 3 小时 (00:21 - 03:15 UTC)
```

---

## 🔍 攻击时间线

```
约 2 周前 (3 月 17 日左右):
└─ 针对主要维护者的社会工程攻击启动

3 月 30 日 05:57 UTC:
└─ plain-crypto-js@4.2.0 发布到 npm (预置依赖)

3 月 31 日 00:21 UTC:
└─ axios@1.14.1 发布，注入 plain-crypto-js@4.2.1

3 月 31 日 01:00 UTC:
├─ axios@0.30.4 发布 (相同载荷)
├─ 首次外部检测
└─ 社区成员报告问题（被攻击者用被黑账号删除）

3 月 31 日 01:38 UTC:
└─ axios 协作者 DigitalBrainJS 开启 PR #10591
   标记被删除的问题，直接联系 npm

3 月 31 日 03:15 UTC:
└─ 恶意版本从 npm 移除

3 月 31 日 03:29 UTC:
└─ plain-crypto-js 从 npm 移除
```

---

## 🎯 攻击手法

### 入侵路径
```
1. 针对性社会工程攻击
   └─ 针对开源维护者的高精度钓鱼

2. RAT 恶意软件植入
   └─ 获得主要维护者 PC 的远程访问权限

3. 凭证窃取
   └─ npm 账号凭证被获取

4. 恶意包发布
   └─ 注入依赖 plain-crypto-js@4.2.1
   └─ 该依赖在 macOS/Windows/Linux 上安装后门
```

### C2 通信
```
域名：sfrclak[.]com
IP: 142.11.206.73
端口：8000
```

---

## 🛡️ 修复方案

### 用户自查
```bash
# 检查 lockfile 是否包含恶意版本
grep -E "axios@(1\.14\.1|0\.30\.4)|plain-crypto-js" package-lock.json yarn.lock

# 如果有匹配，该机器视为已泄露
```

### 修复步骤
```
1. 降级到 axios@1.14.0 (或 0.30.3 for 0.x 用户)
2. 删除 node_modules/plain-crypto-js/
3. 轮换该机器上的所有密钥、token、凭证
4. 检查网络日志是否连接到 C2 服务器
5. 如果发生在 CI runner，轮换受影响构建中注入的所有密钥
```

### 安全情况
```
如果你：
✅ 已锁定到干净版本
✅ 在 3 月 31 日 00:21-03:15 UTC 之间没有运行全新安装

那么你是安全的。
```

---

## 📋 预防改进措施

| 措施 | 类型 | 状态 |
|------|------|------|
| 所有设备和凭证重置 | 预防 | ✅ 进行中 |
| 不可变发布设置 | 预防 | 🔄 计划中 |
| 正确采用 OIDC 流程发布 | 预防 | 🔄 计划中 |
| 整体安全态势改进 | 预防 | 🔄 进行中 |
| 更新所有 GitHub Actions 采用最佳实践 | 预防 | 🔄 进行中 |

### OIDC 发布流程
```
传统方式:
维护者 PC → npm publish (使用长期凭证)
风险：凭证泄露 = 完全控制

OIDC 方式:
GitHub Actions → OIDC token → npm publish (临时凭证)
优势：即使 GitHub 账号被黑，攻击者也无法发布
```

---

## 💔 教训总结

### 1. 个人账号发布的风险
```
问题：直接从个人账号发布是风险点

解决：OIDC 流程 + 不可变发布设置
- 发布权限绑定到 CI/CD 管道
- 不依赖个人设备的长期凭证
```

### 2. 检测依赖社区
```
问题：没有自动化方式检测未授权发布
      检测完全依赖社区发现

改进方向:
- 发布通知机制
- 异常发布模式检测
- 维护者多因素确认
```

### 3. 开源维护者是高价值目标
```
现实：高影响力包维护者是复杂社会工程的目标

应对:
- 高度警惕（个人和项目层面）
- 持续监控和改进安全态势
- 与 OpenJS Security Working Group 等组织合作
```

---

## 🔗 与 Sandbot 的相关性

### 对 ClawHub 技能发布的启示
```
当前 Sandbot 技能发布流程:
- 使用 clawhub CLI 发布
- 可能使用长期 API 凭证

潜在风险:
- 如果 API 凭证泄露，攻击者可发布恶意技能
- 影响所有通过 ClawHub 安装技能的用户

建议改进:
1. 研究 ClawHub 是否支持 OIDC 发布
2. 如不支持，考虑发布前人工确认流程
3. 定期轮换 ClawHub API 凭证
4. 监控技能发布通知
```

### 对依赖管理的启示
```
Sandbot 技能依赖:
- tavily-search
- reddit-insights
- x-tweet-fetcher
- 等 11+ 个技能

安全检查:
1. 定期审查技能依赖树
2. 锁定技能版本（不使用 latest）
3. 监控技能更新通知
4. 考虑技能签名验证
```

### 对自身安全的启示
```
当前风险点:
- Telegram Bot Token 存储在 openclaw.json
- Bailian API Key 存储在 openclaw.json
- Feishu App Secret 存储在 openclaw.json

改进建议:
1. 使用 secrets 目录存储敏感凭证（已有）
2. 定期轮换 API 密钥
3. 监控异常 API 调用模式
4. 考虑凭证访问审计
```

---

## 📊 影响评估

### 已知影响
```
- 恶意版本存活时间：~3 小时
- 发布窗口：UTC 凌晨（亚洲工作时间，可能减少曝光）
- 检测速度：~1 小时（社区响应迅速）
- 移除速度：~2 小时（从检测到移除）
```

### 潜在影响
```
axios 下载量:
- ~2600 万每周下载量 (攻击前数据)
- 假设 0.1% 用户在窗口期安装 → 26,000 台设备
- 实际影响取决于安装时间和版本锁定情况
```

---

## 📚 外部资源

### 技术分析
- [StepSecurity: 完整技术分析和修复指南](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)
- [Snyk: 咨询和扫描指南](https://snyk.io/blog/axios-npm-package-compromised-supply-chain-attack-delivers-cross-platform/)
- [Socket: 供应链攻击分析](https://socket.dev/blog/axios-npm-package-compromised)
- [Datadog Security Labs: 攻击流程和响应分析](https://securitylabs.datadoghq.com/articles/axios-npm-supply-chain-compromise/)

### 官方资源
- [axios Post Mortem GitHub Issue](https://github.com/axios/axios/issues/10636)
- [OpenJS Security Working Group](https://openjsf.org/)

---

*分析完成时间：2026-04-04 08:07 UTC*
*字数：~1700 字*
