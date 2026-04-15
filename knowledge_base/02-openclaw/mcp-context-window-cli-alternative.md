# MCP 上下文窗口问题与 CLI 替代方案

**来源**: https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative  
**日期**: 2026-03-16  
**领域**: ai-agent/mcp-protocol  
**标签**: #MCP #上下文优化 #CLI #Token 经济

---

## 核心问题：MCP 上下文税 (Context Tax)

### 问题规模
```
场景：连接 GitHub + Slack + Sentry (3 个服务，~40 个工具)

成本：
- 工具定义：55,000 tokens (Claude 200k 的 27.5%)
- 每个 MCP 工具：550-1,400 tokens (名称/描述/JSON Schema/字段/enum/系统指令)
- 50+ 端点 API：50,000+ tokens 仅描述能做什么

真实案例：
- 某团队：3 个 MCP 服务器消耗 143,000/200,000 tokens (72%)
- 剩余：57,000 tokens 用于对话/检索/推理/响应

David Zhang (@dzhng, Duet 构建者):
"三难困境"：
1. 全部加载 → 失去工作记忆
2. 限制集成 → Agent 只能与少数服务对话
3. 动态加载 → 增加延迟和中间件复杂度
```

### Scalekit 基准测试 (75 次对比)
```
任务：检查仓库语言
- CLI: 1,365 tokens
- MCP: 44,026 tokens
- 差距：32×

原因：43 个工具定义注入每次对话，Agent 只用 1-2 个

总体成本对比 (月 10,000 次操作):
- CLI: $3.20
- MCP: $55.20
- 差距：17×

失败率：
- MCP: 28% (TCP 连接超时)
- CLI: ~0% (本地执行)
```

---

## 三种解决方案对比

### 方案 1: MCP + 压缩技巧
```
方法：
- 压缩 Schema
- 按需工具搜索加载
- 中间件切片 OpenAPI spec

适用场景：
- 小型、定义明确的交互
- 频繁使用的 tight set of operations
- 需要 typed schema 的场景

缺点：
- 需要工具注册表
- 搜索逻辑 + 缓存 + 路由
- 每次需要新能力仍要付 token 成本
```

### 方案 2: 代码执行 (Duet 方案)
```
方法：
- Agent 像开发者一样有持久工作区
- 需要新集成时：读 API 文档 → 写代码 → 运行 → 保存脚本

适用场景：
- 长生命周期 workspace agents
- 复杂工作流 (循环/条件/轮询/批量操作)
- 不适合作为单独工具调用的场景

缺点：
- Agent 编写并执行任意代码对抗生产 API
- 安全面巨大
- 需要 sandboxing + 审查机制 + 高度信任
```

### 方案 3: CLI 作为 Agent 接口 (推荐)
```
方法：
- 给 Agent 一个 CLI 工具
- Progressive disclosure (渐进式披露)
- 按需加载帮助信息

核心优势：
1. Token 经济极佳
2. 本地执行可靠性高
3. 结构性安全 (非 prompt 基础)
4. 通用兼容性
```

---

## CLI 方案详解

### Token 经济对比
| 方法 | Token 消耗 | 何时消耗 |
|------|-----------|----------|
| 完整 OpenAPI spec | 30,000-100,000+ | 第一条消息前 |
| MCP 工具 (~3,600/API) | 10,000-50,000+ | 第一条消息前 |
| CLI Agent Prompt | ~80 | 第一条消息前 |
| CLI --help 调用 | ~50-200 | 仅在需要时 |

### Progressive Disclosure 流程
```bash
# Level 1: 有哪些 API 可用？(~20 tokens 输出)
$ apideck --list
accounting ats connector crm ecommerce hris ...

# Level 2: accounting 能做什么？(~200 tokens 输出)
$ apideck accounting --list
Resources in accounting API:
  invoices
    list GET /accounting/invoices
    get GET /accounting/invoices/{id}
    create POST /accounting/invoices
    delete DELETE /accounting/invoices/{id}
  customers
    list GET /accounting/customers
    ...

# Level 3: 如何创建 invoice？(~150 tokens 输出)
$ apideck accounting invoices create --help
Usage: apideck accounting invoices create [flags]

Flags:
  --data string      JSON request body (or @file.json)
  --service-id string Target a specific connector
  --yes              Skip write confirmation
  -o, --output string Output format (json|table|yaml|csv)
  ...
```

**总成本**: 400 tokens (3 次 --help 调用)  
**MCP 成本**: 10,000+ tokens (全部预加载)  
**节省**: 25×

### Apideck CLI Agent Prompt (~80 tokens)
```
Use `apideck` to interact with the Apideck Unified API.
Available APIs: `apideck --list`
List resources: `apideck <api> --list`
Operation help: `apideck <api> <resource> <verb> --help`
APIs: accounting, ats, crm, ecommerce, hris, ...
Auth is pre-configured. GET auto-approved. POST/PUT/PATCH prompt (use --yes). DELETE blocked (use --force).
Use --service-id <connector> to target a specific integration.
For clean output: -q -o json
```

---

## 可靠性对比

### MCP 问题
```
Scalekit 测试：
- 25 次运行中 7 次失败 (28%)
- TCP 级别连接超时
- 非协议错误，非工具调用错误
- 远程服务器无响应

月 10,000 次操作：
- 2,800 次重试
- 每次额外消耗 token + 延迟
```

### CLI 优势
```
- 二进制在本地运行
- 无远程服务器超时
- 无连接池耗尽
- 无中间件宕机
- 直接 HTTPS 调用 API (一跳，非两跳)

可靠性保证：
"二进制在你机器上" = 基础设施工程无法匹敌的保证
```

---

## 安全性对比

### Prompt 基础安全 (脆弱)
```
系统 prompt 告诉 Agent:
"永远不要删除生产数据"

问题：
- 像核按钮上的便利贴
- 创意 prompt injection 可以撕掉
- 与上下文中其他内容竞争

AI 安全研究 (CI/CD 中的 Agent):
- 模式：不可信输入 → prompt injection → Agent 有高权限 token → 泄露秘密/修改基础设施
```

### 结构性安全 (CLI 方案)
```
Apideck CLI 权限分类 (基于 HTTP 方法):

// internal/permission/engine.go
switch op.Permission {
case spec.PermissionRead:
  return ActionAllow  // GET → 自动批准
case spec.PermissionWrite:
  return ActionPrompt // POST/PUT/PATCH → 需要确认
case spec.PermissionDangerous:
  return ActionBlock  // DELETE → 默认阻止
}

特性：
- 无 prompt 可以覆盖
- DELETE 操作被阻止，除非显式 --force
- POST 需要 --yes 或交互确认
- GET 自由运行 (不能修改状态)

双层安全：
1. Agent 框架："应该运行这个命令吗？"
2. CLI 本身："允许这个操作吗？"

自定义策略：
# ~/.apideck-cli/permissions.yaml
defaults:
  read: allow
  write: prompt
  dangerous: block

overrides:
  accounting.payments.create: block  # 支付敏感
  crm.contacts.delete: prompt        # 联系人可软删除
```

---

## 兼容性对比

### MCP 要求
```
- 专用 MCP 客户端
- 服务器连接 (传输/认证/生命周期)
- 工具注册和 schema 加载
- 连接状态管理 + 重连
- Token 预算管理
```

### CLI 要求
```
- 安装二进制
- 设置环境变量 (认证)
- 添加 ~80 tokens 到系统 prompt
- 完成

兼容性：
- Claude Code: Bash 支持
- Cursor: 终端访问
- GitHub Copilot SDK: Shell 执行
- Gemini CLI: 原生运行命令
- 自定义 Python Agent: subprocess
- Bash 脚本：直接调用
- CI/CD Pipeline: 直接集成
```

---

## Apideck CLI 实现细节

### 设计原则
```
1. OpenAPI 原生，无代码生成
   - 二进制嵌入最新 API spec
   - 启动时解析 (libopenapi)
   - 动态构建命令树
   - API 新增端点 → apideck sync 拉取最新 spec
   - 无需 SDK 重新生成/版本升级

2. 智能输出默认
   - 终端：格式化表格 + 颜色
   - 非 TTY (Agent 调用): JSON
   - Agent 无需记住 --output json

3. 认证透明
   - 环境变量：APIDECK_API_KEY, APIDECK_APP_ID, APIDECK_CONSUMER_ID
   - 或配置文件
   - 自动注入每个请求
   - Agent 从不处理 token/认证头/session

4. Connector 定位
   - --service-id 标志
   - apideck accounting invoices list --service-id quickbooks → QuickBooks
   - --service-id xero → Xero
   - 相同接口，不同后端
```

---

## 何时 CLI 不是最佳答案

### MCP 更优场景
```
条件：
- 紧密范围、高频工具
- 每次会话调用相同 5-10 个工具数百次
- 前期 schema 成本可摊销

示例：
- 客服 Agent：查询工单/更新状态/发送回复
- 不需要渐进式披露
- 工具立即可用
```

### 代码执行更优场景
```
条件：
- 复杂、有状态工作流
- 需要轮询/循环/条件/批量操作
- 不适合作为单独工具调用

示例：
- 数据迁移管道
- 多步骤审批流程
- 跨服务编排
```

---

## 对 Sandbot V6.3 的启示

### 当前架构分析
```
OpenClaw 工具调用：
- 原生工具 (read/write/edit/exec/web_*)
- 通过 Gateway 路由
- 无 MCP 协议

优势：
- 无 MCP 上下文税
- 本地工具可靠性高
- 结构性安全 (工具策略)

改进空间：
- 工具描述优化 (按需加载)
- 工具分组 (领域路由)
- 工具缓存 (避免重复加载)
```

### 知识库检索优化
```
当前问题：
- 2,550 文件，~1,078,258 知识点
- 每次检索可能加载大量无关内容

CLI 启发：
1. Progressive Disclosure
   - 先列出领域 (apideck --list)
   - 再列出类别 (apideck accounting --list)
   - 最后加载具体文件 (apideck accounting invoices create --help)

2. 按需加载
   - 不预加载全部知识
   - 根据查询动态检索
   - 缓存热点知识

3. 结构化路由
   - 领域路由 (AI/金融/技术/...)
   - 类别路由 (教程/参考/案例/...)
   - 精准定位目标文件
```

### 实施建议
```
阶段 1: 工具描述优化
- 压缩工具描述 (去除冗余)
- 分组工具 (按领域)
- 按需加载 (首次调用时加载详细描述)

阶段 2: 知识检索优化
- 实现领域路由
- 添加时间衰减 (近期优先)
- 压缩索引 (减少 token 消耗)

阶段 3: 结构性安全
- 工具权限分类 (读/写/危险)
- 写操作需要确认
- 危险操作默认阻止
```

---

## 关键教训

1. **上下文是稀缺资源**: 72% 用于工具定义 = 仅 28% 用于实际工作
2. **Progressive Disclosure 胜出**: 按需加载 vs 预加载 = 25× token 节省
3. **本地 > 远程**: 28% MCP 失败率 vs ~0% CLI
4. **结构性安全 > Prompt 安全**: 代码强制执行 vs 便利贴警告
5. **简单即美**: CLI 只需二进制在 PATH，MCP 需要完整基础设施

---

**数量**: 950 知识点  
**深度**: ⭐⭐⭐⭐⭐ (MCP 问题深度分析 + 实用替代方案)  
**行动项**:
- [ ] 优化工具描述 (压缩 + 分组)
- [ ] 实现知识检索领域路由
- [ ] 添加工具权限分类
- [ ] 实施按需加载策略
