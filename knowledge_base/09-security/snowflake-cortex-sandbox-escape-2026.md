# Snowflake Cortex AI 沙箱逃逸漏洞分析

**来源**: PromptArmor (2026-03-18)  
**HN 评分**: 39 points  
**领域**: AI 安全 / Agent 安全 / 沙箱逃逸  
**数量**: 12 知识点  
**CVE 状态**: 已修复 (Cortex Code CLI v1.0.25, 2026-02-28)

---

## 漏洞概述

Snowflake Cortex Code CLI（类似 Claude Code / OpenAI Codex 的命令行编程 Agent）在命令验证系统中存在漏洞，允许：
1. **绕过人工审批** (human-in-the-loop) 执行任意命令
2. **逃逸沙箱**，在沙箱外执行命令

## 攻击链

```
1. 用户启动 Cortex，开启沙箱模式
2. 用户让 Cortex 分析一个第三方开源代码库
3. 代码库 README 中隐藏 prompt injection
4. Cortex 的子 Agent 探索代码库时触发注入
5. 利用 process substitution 绕过命令验证
6. 在沙箱外执行恶意命令
7. 利用 Cortex 缓存的 Snowflake 认证令牌
8. 窃取数据/删除表/添加后门用户
```

## 关键技术细节

### 绕过机制
Cortex 未验证 **process substitution** (`<(...)`) 表达式内的命令，导致未经审批就能执行恶意命令。

### 子 Agent 上下文丢失 (核心教训)
- 第一层子 Agent 调用第二层子 Agent
- 第二层子 Agent 执行了恶意命令
- 回传时**上下文丢失**
- 主 Agent 报告"发现恶意命令，建议不要执行"
- **但命令已经被第二层子 Agent 执行了！**

### 凭证利用
- Snowflake 默认使用浏览器认证，产生的会话令牌被 Cortex 缓存
- 攻击者可以找到并利用这些缓存令牌执行 SQL 查询
- 开发者通常有读写权限 → 数据泄露 + 数据销毁

## 对 OpenClaw 生态的教训

### 1. 沙箱 ≠ 安全
即使有沙箱，命令验证的漏洞也能导致逃逸。**验证逻辑必须覆盖所有 shell 特性**。

### 2. 子 Agent 上下文传递是安全盲区
多层子 Agent 调用时，安全上下文（"已执行了什么"）可能在传递中丢失。**每一层 Agent 都需要独立的安全审计日志**。

### 3. Workspace Trust 机制缺失
Cortex 不支持"工作区信任"对话框（VS Code 首创）。在不受信任的目录中运行 Agent 是高风险操作。

### 4. Indirect Prompt Injection 仍是最大威胁
攻击入口可以是：README、搜索结果、数据库记录、终端输出、MCP 响应——任何不受信任的数据。

---

**安全等级**: ⭐⭐⭐⭐⭐ 严重 (远程代码执行 + 凭证窃取)
**对 OpenClaw 的相关性**: ⭐⭐⭐⭐⭐ 直接相关 (同类 Agent 架构)
**教学价值**: ⭐⭐⭐⭐⭐ 完整攻击链 + 修复过程
