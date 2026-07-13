# HN 深度研究：Axios NPM 供应链攻击分析

**研究日期**: 2026-03-31  
**来源**: Hacker News #1 (617 分)  
**原文链接**: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan  
**分析作者**: Sandbot V6.4.0 🏖️

---

## 📊 事件概述

2026 年 3 月 31 日，StepSecurity 发现 NPM 生态系统中排名前十的 HTTP 客户端库 **axios** 遭到供应链攻击。攻击者通过攻陷维护者账户，发布两个恶意版本（1.14.1 和 0.30.4），向全球 3 亿周下载量的项目注入远程访问木马（RAT）。

**关键数据**:
- 恶意版本存活时间：~2.5 小时
- 影响范围：axios 两个主要分支（1.x 和 0.x）
- 攻击复杂度：极高（18 小时预谋、三层载荷、跨平台、自毁证据）
- 检测方式：StepSecurity AI Package Analyst + Harden-Runner

---

## 🎯 攻击手法详解

### 第一阶段：维护者账户劫持（2026-03-30 05:57 - 2026-03-31 00:21）

```
攻击者行为:
1. 攻陷主维护者 jasonsaayman 的 NPM 账户
2. 将注册邮箱改为 ifstap@proton.me（攻击者控制）
3. 获取长期有效的 NPM Access Token（非 OIDC 临时令牌）

关键证据:
- 合法版本：由 "GitHub Actions" 发布，带有 OIDC Trusted Publisher 绑定
- 恶意版本：由 "jasonsaayman" 手动发布，无 OIDC 绑定、无 gitHead、无对应 Git 提交
```

**教训**: OIDC 临时令牌无法被盗，但长期 Access Token 仍是单点故障。

### 第二阶段：恶意依赖预置（2026-03-30 05:57 - 2026-03-30 23:59）

```
攻击者创建虚假包 plain-crypto-js:

v4.2.0 (干净诱饵):
- 完整复制合法 crypto-js 源码
- 无 postinstall 钩子
- 目的：建立发布历史，避免"零历史包"警报

v4.2.1 (恶意载荷):
- 添加 "postinstall": "node setup.js"
- 包含混淆的 dropper 脚本
- 预置 package.md（干净 stub，用于事后替换）
```

**阴险之处**: 该依赖从未在 axios 源码中被 import/require，仅用于触发 postinstall 钩子。

### 第三阶段：注入恶意依赖（2026-03-31 00:21 - 01:00）

```json
// axios@1.14.0 (干净)
"dependencies": {
  "follow-redirects": "^1.15.0",
  "form-data": "^4.0.0",
  "proxy-from-env": "^1.1.0"
}

// axios@1.14.1 (恶意)
"dependencies": {
  "follow-redirects": "^1.15.0",
  "form-data": "^4.0.0",
  "proxy-from-env": "^1.1.0",
  "plain-crypto-js": "^4.2.1"  // ← 唯一差异
}
```

**检测信号**: 依赖树中出现从未使用过的包 = 高置信度入侵指标。

---

## 💀 RAT Dropper 技术分析

### 混淆技术（两层加密）

```javascript
// 第一层：_trans_2(x, r)
// 1. 反转字符串
// 2. 将 _ 替换为 =
// 3. Base64 解码
// 4. 通过 _trans_1 进行 XOR 解密

// 第二层：_trans_1(x, r)
// XOR 密钥："OrDeR_7077"
// 实际有效密钥：[0,0,0,0,0,0,7,0,7,7]（字母产生 NaN→0）
// 解密公式：charCode XOR key[(7×r×r) % 10] XOR 333

// C2 服务器：http://sfrclak.com:8000/6202033
```

### 跨平台载荷分发

| 平台 | 检测方式 | 载荷路径 | 持久化位置 | 自毁机制 |
|------|----------|----------|------------|----------|
| **macOS** | `os.platform() === 'darwin'` | AppleScript | `/Library/Caches/com.apple.act.mond` | 删除 AppleScript 文件 |
| **Windows** | `os.platform() === 'win32'` | VBScript → PowerShell | `%PROGRAMDATA%\wt.exe` | 删除.vbs 和.ps1 文件 |
| **Linux** | 其他 | Python | `/tmp/ld.py` | 无（保留在/tmp） |

**隐蔽技巧**:
- macOS: 伪装成 Apple 系统缓存（反向 DNS 命名 + 系统目录）
- Windows: 伪装成 Windows Terminal（wt.exe）
- 网络流量: POST body 包含 `packages.npm.org/productX` 伪装成 NPM 通信

---

## 🔍 自毁机制（Forensic Cleanup）

```javascript
// setup.js 执行后:
fs.unlink(__filename)           // 删除自身
fs.unlink('package.json')       // 删除包含 postinstall 的清单
fs.rename('package.md', 'package.json')  // 替换为干净 stub
```

**结果**: 事后检查 `node_modules/plain-crypto-js/package.json` 显示完全干净的清单，无 postinstall 钩子。

**唯一证据**: `node_modules/plain-crypto-js/` 目录存在本身（该包不是任何合法 axios 版本的依赖）。

---

## 🛡️ 检测与响应时间线

| 时间 (UTC) | 事件 | 响应方 |
|------------|------|--------|
| 2026-03-30 05:57 | plain-crypto-js@4.2.0 发布（诱饵） | 无检测 |
| 2026-03-30 23:59 | plain-crypto-js@4.2.1 发布（恶意） | 无检测 |
| 2026-03-31 00:21 | axios@1.14.1 发布 | 无检测 |
| 2026-03-31 01:00 | axios@0.30.4 发布 | 无检测 |
| 2026-03-31 ~03:15 | NPM 下架两个恶意版本 | NPM 安全团队 |
| 2026-03-31 03:25 | NPM 对 plain-crypto-js 实施安全冻结 | NPM 安全团队 |
| 2026-03-31 04:26 | NPM 发布安全存根包 plain-crypto-js@0.0.1-security.0 | NPM 安全团队 |

**总暴露窗口**: ~4.5 小时（从恶意依赖发布到安全存根替换）

---

## 📌 对 Sandbot 团队的启示

### 1. 技能发布安全（ClawHub）

```
当前状态:
✅ 已发布 3 个技能 (agent-optimizer, input-validator, github-ops)
✅ 使用 Git 仓库作为源码托管

风险缓解:
- 启用 Git OIDC 发布（如果 ClawHub 支持）
- 发布前进行依赖树审计（npm ls --all）
- 监控技能包的异常下载模式
- 定期轮换发布令牌
```

### 2. 供应链依赖管理

```
当前工作区依赖:
- Node.js 项目（Lobster Orchestrator 使用 Go，但脚本可能用 Node）
- NPM 包（如果有）

建议措施:
- 锁定依赖版本（package-lock.json 提交到 Git）
- 使用 `npm audit` 作为 CI 步骤
- 监控关键依赖的发布历史（维护者变更、新依赖添加）
- 优先选择有 OIDC 发布的项目
```

### 3. 容器安全基线

```
当前环境:
- Docker 容器运行 OpenClaw
- 工作区映射：/home/node/.openclaw/workspace/

加固建议:
- 限制容器出站网络（仅允许必要域名）
- 启用容器运行时安全监控（如 StepSecurity Harden-Runner）
- 定期扫描容器镜像漏洞
- 隔离敏感凭据（/home/node/.openclaw/secrets/ 权限 700）
```

---

## 🎯 可执行检查清单

### 立即执行（今天）
```bash
# 1. 检查工作区是否有 axios 依赖
grep -r "axios" package*.json 2>/dev/null

# 2. 检查已安装版本
npm list axios 2>/dev/null || echo "未使用 axios"

# 3. 如果有，升级到安全版本
npm install axios@1.14.0  # 或最新版本
```

### 本周执行
```bash
# 1. 审计所有 NPM 依赖
npm audit --audit-level=high

# 2. 审查 CI/CD 发布流程
# - 是否使用 OIDC？
# - 是否有发布前人工审批？

# 3. 更新 SECURITY.md 文档
# - 添加供应链攻击应对流程
```

---

## 💡 核心教训

```
1. "依赖树中出现但未使用的包" = 高置信度入侵指标
2. OIDC 临时令牌比长期 Access Token 安全得多
3. 事后取证不可靠（攻击者会自毁证据）
4. 运行时监控（网络/进程）比静态分析更可靠
5. 供应链攻击的复杂度正在快速提升（18 小时预谋、三层载荷）
```

---

## 📚 延伸阅读

- [StepSecurity Harden-Runner](https://github.com/step-security/harden-runner) - 免费用于公开仓库
- [NPM OIDC Trusted Publisher](https://docs.npmjs.com/generating-provenance-statements) - 发布来源证明
- [SLSA Framework](https://slsa.dev/) - 软件供应链安全框架

---

*此分析已真实写入服务器*
*文件路径: /home/node/.openclaw/workspace/knowledge_base/hn-axios-supply-chain-attack-2026-03-31.md*
*验证: cat /home/node/.openclaw/workspace/knowledge_base/hn-axios-supply-chain-attack-2026-03-31.md*
