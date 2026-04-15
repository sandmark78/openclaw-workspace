# Stripe Machine Payments Protocol (MPP) - AI Agent 支付协议

**来源**: Stripe Blog (2026-03-18)  
**HN 评分**: 47 points  
**领域**: AI Agent 基础设施 / 支付 / 商业化  
**数量**: 15 知识点

---

## 核心概念

### MPP 是什么
Stripe 与 Tempo 联合发布的开放标准协议，让 AI Agent 能够**程序化地完成支付**，无需人工介入创建账户、选择套餐、输入支付信息等步骤。

### 核心问题
当前金融系统的工具是为人类设计的。Agent 要完成一次购买，需要：创建账户→浏览定价页→选择订阅层级→输入支付信息→设置账单——这些步骤通常需要人工干预。

### 工作流程
```
Agent 请求资源 (HTTP 端点/API/MCP)
  → 服务返回支付请求
  → Agent 授权支付
  → 资源交付给 Agent
```

## 技术架构

### 支付方式
- **稳定币** (USDC 等)
- **法币** (信用卡)
- **先买后付** (BNPL)
- **共享支付令牌 (SPT)** - Stripe 的 Shared Payment Tokens

### 与现有基础设施兼容
- 对 Stripe 商户来说，Agent 支付与人类支付一样出现在 Dashboard
- 资金按正常结算周期进入商户余额
- 税务计算、欺诈保护、报告、退款等全部兼容

### 协议特性
- **开放标准** - 任何人可以实现
- **互联网原生** - 基于 HTTP
- **支持微交易** - Agent 可以按次/按量付费
- **支持定期付款** - 订阅模式

## 已落地案例

| 公司 | 用例 | 付费模式 |
|------|------|----------|
| Browserbase | Agent 启动无头浏览器 | 按会话付费 |
| PostalForm | Agent 打印和寄送实体邮件 | 按件付费 |
| Prospect Butcher Co. | Agent 订三明治 | 按单付费 |
| Stripe Climate | Agent 程序化碳补偿 | 按贡献付费 |

## Stripe Agentic Commerce 全栈

| 组件 | 功能 |
|------|------|
| MPP | Agent 支付协议 |
| x402 | HTTP 402 支付协议 |
| ACP (Agentic Commerce Protocol) | Agent 商务协议 |
| MCP 集成 | Model Context Protocol 集成 |
| Agentic Commerce Suite | 全套 Agent 商务基础设施 |

## 深度洞察

### 1. Agent 经济时代正式到来
Stripe 这样的支付巨头入场，意味着 "Agent 作为互联网经济参与者" 已从概念进入基础设施阶段。

### 2. 微交易是 Agent 经济的基础
人类不会为一次 API 调用付 $0.001，但 Agent 可以。MPP 的微交易支持将催生全新的定价模式。

### 3. 对 OpenClaw 生态的启示
- OpenClaw Agent 可以通过 MPP 直接购买外部服务
- 技能市场可以接入 MPP 实现按次付费
- fluxa-agent-wallet 技能已经支持 x402，MPP 是自然延伸

### 4. 与 x402 的关系
x402 是基于 HTTP 402 状态码的支付协议（区块链原生），MPP 是 Stripe 的企业级方案（法币+稳定币）。两者互补，覆盖不同场景。

---

**变现机会**: ⭐⭐⭐⭐ MPP 集成教程/OpenClaw 支付技能
**技术深度**: ⭐⭐⭐ 协议层面清晰，实现细节待文档完善
**时效性**: ⭐⭐⭐⭐⭐ 刚发布，先发优势明显
