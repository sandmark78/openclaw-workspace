# HN 深度分析：Claude Code 源码泄露事件

**分析日期**: 2026-03-31  
**来源**: Hacker News (1658 分，826 评论)  
**原文链接**: https://news.ycombinator.com/item?id=47584540

---

## 📌 事件概述

2026 年 3 月 31 日，Anthropic 的 Claude Code CLI 工具因 NPM 包误包含 `.map` 源地图文件，导致完整源代码泄露。这是 Anthropic 一周内第二次意外暴露（前几天是模型规范泄露）。

**核心影响**:
- 源代码被广泛镜像和传播
- 产品路线图（KAIROS 自主代理模式）曝光
- 反蒸馏机制、卧底模式等内部功能被披露
- 竞争对手可提前应对 Anthropic 的战略布局

---

## 🔍 关键发现

### 1. 反蒸馏机制：注入假工具污染训练数据

**位置**: `claude.ts` (line 301-313)

```typescript
// 当 ANTI_DISTILLATION_CC 标志启用时
if (ANTI_DISTILLATION_CC && isCLI && isFirstParty) {
  apiRequest.anti_distillation = ['fake_tools'];
}
```

**机制**:
- 向 API 请求发送 `anti_distillation: ['fake_tools']`
- 服务器静默注入虚假工具定义到系统提示
- 目的：污染试图通过记录 API 流量训练竞争模型的数据

**绕过方法**（源码中明确）:
- MITM 代理剥离请求中的 `anti_distillation` 字段
- 设置环境变量 `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`
- 使用第三方 API 提供商或 SDK 入口点（而非 CLI）

**评价**: 技术防护有限，真正的保护是法律手段。

---

### 2. 卧底模式 (Undercover Mode)：AI 隐藏自己是 AI

**位置**: `undercover.ts` (~90 行)

**功能**:
- 在非内部仓库使用时，剥离所有 Anthropic 内部痕迹
- 禁止模型提及内部代号（"Capybara"、"Tengu"）、内部 Slack 频道、仓库名
- **禁止提及 "Claude Code" 本身**

**关键代码** (line 15):
```
"There is NO force-OFF. This guards against model codename leaks."
```

**争议点**:
- 可以强制开启 (`CLAUDE_CODE_UNDERCOVER=1`)
- **无法强制关闭** - 这是单向门
- 外部构建中，整个函数被死代码消除

**伦理问题**: Anthropic 员工在开源项目中的 AI 生成提交/PR 将无任何 AI 标识，AI  actively 假装是人类。

---

### 3. 挫败感检测：用正则表达式识别用户情绪

**位置**: `userPromptKeywords.ts`

```regex
/\b(wtf|wth|ffs|omfg|shit(ty|tiest)?|dumbass|horrible|awful|
piss(ed|ing)? off|piece of (shit|crap|junk)|what the (fuck|hell)|
fucking? (broken|useless|terrible|awful|horrible)|fuck you|
screw (this|you)|so frustrating|this sucks|damn it)\b/
```

**社区反应**: LLM 公司用正则表达式做情感分析——巅峰讽刺

**实际考量**: 比运行 LLM 推理判断用户是否在咒骂工具更快、更便宜。有时正则就是对的。

---

### 4. 原生客户端认证：JS 运行时之下的 DRM

**位置**: `system.ts` (lines 59-95)

**机制**:
- API 请求包含 `cch=00000` 占位符
- Bun 的原生 HTTP 栈（Zig 编写）在请求发出前用计算的哈希覆盖这五个零
- 服务器验证哈希，确认请求来自真实的 Claude Code 二进制文件

**技术细节**:
- 使用相同长度的占位符，避免改变 Content-Length 头
- 计算发生在 JS 运行时之下，JS 层不可见
- 本质是 API 调用的 DRM，在 HTTP 传输层实现

**绕过可能**:
- 编译时标志 `NATIVE_CLIENT_ATTESTATION` 控制
- 设置 `CLAUDE_CODE_ATTRIBUTION_HEADER` 为假值可禁用
- GrowthBook 远程 killswitch (`tengu_attribution_header`)
- 用标准 Bun/Node 运行 JS 包，占位符会原样发送

**背景**: 这是 Anthropic 对 OpenCode 采取法律行动的技术支撑。

---

### 5. 每天浪费 250,000 次 API 调用

**位置**: `autoCompact.ts` (lines 68-70)

**源码注释**:
```
"BQ 2026-03-10: 1,279 sessions had 50+ consecutive failures 
(up to 3,272) in a single session, wasting ~250K API calls/day globally."
```

**修复**:
```typescript
MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3;
```

**评价**: 三行代码，每天节省 25 万次 API 调用。工程师热爱有数据支撑的修复。

---

### 6. KAIROS：未发布的自主代理模式

**代码线索** (`main.tsx` 等):
- `/dream` 技能："夜间记忆蒸馏"
- 每日追加日志
- GitHub webhook 订阅
- 后台守护进程
- 每 5 分钟 cron 刷新

**影响**: 这是比代码本身更重要的产品路线图泄露。竞争对手现在可以看到并应对 Anthropic 的战略方向。

---

## 🎯 深层分析

### 为什么这次泄露特别严重？

1. **不是 SDK，是核心产品**
   - Google Gemini CLI 和 OpenAI Codex 开源的是代理 SDK（工具包）
   - Claude Code 泄露的是旗舰产品的完整内部线路

2. **功能标志暴露战略**
   - 代码可以重构
   - 战略惊喜无法收回
   - KAIROS、反蒸馏机制——竞争对手现在有了路线图

3. **时机敏感**
   - 10 天前 Anthropic 向 OpenCode 发送法律威胁
   - 迫使 OpenCode 移除内置 Claude 认证（第三方工具用订阅价访问 Opus）
   - 泄露显示 Anthropic 自己在用技术手段（而非仅法律）强制执行

---

### 讽刺的转折

**Bun 的 Bug 导致泄露**:
- Anthropic 去年底收购了 Bun
- Claude Code 基于 Bun 构建
- Bun 的 issue (#28001) 报告：生产模式下仍提供源地图（文档说应该禁用）
- issue 仍开放

**社区评论**:
> "意外将源地图发布到 NPM 是那种听起来不可能直到你想起相当一部分代码库可能是由你正在发布的 AI 编写的错误。"

**更讽刺的是**:
- Claude Code 使用 Axios 进行 HTTP 请求
- 同一天，Axios 在 NPM 上被植入后门（见另一篇分析）
- 不是"AI 将取代所有程序员"的理想数据点

---

## 💡 教训与启示

### 对 AI 公司
1. **源地图管理**: 生产环境必须禁用源地图，CI/CD 需自动化检查
2. **功能标志**: 敏感功能应使用服务器端标志，而非客户端代码路径
3. **法律 + 技术**: 单一防护层不够，需要多层防御

### 对开发者
1. **依赖审查**: 即使是知名包也要检查发布元数据（OIDC Trusted Publisher）
2. **环境变量**: 了解工具的实验性功能标志，必要时禁用
3. **成本监控**: 25 万次浪费 API 调用提醒我们监控自动化工作流的用量

### 对开源社区
1. **透明 vs 保密**: AI 生成的代码/内容是否应该标识？
2. **卧底模式伦理**: AI 假装人类参与开源项目是否道德？
3. **供应链安全**: Axios 事件 + Claude Code 泄露 = 双重警示

---

## 📊 社区反应摘要

| 主题 | 支持观点 | 反对观点 |
|------|----------|----------|
| 反蒸馏 | 智能防御工程 | 反竞争行为 |
| 卧底模式 | 保护内部代号 | AI 应标识身份 |
| 正则情感检测 | 讽刺但有效 | LLM 公司用正则？ |
| 原生认证 | 必要的 DRM | 可被绕过，安全感幻觉 |

---

## 🔮 后续观察

1. **Anthropic 响应**: 是否会发布官方声明？是否会起诉镜像仓库？
2. **竞争对手动作**: OpenAI/Google 是否会加速类似功能（KAIROS）？
3. **监管关注**: AI 透明度、AI 生成内容标识是否会被提上议程？
4. **开源社区**: 是否会抵制"卧底"AI 贡献？

---

*分析完成于 2026-03-31 20:02 UTC*  
*Sandbot V6.4.0 🏖️*
