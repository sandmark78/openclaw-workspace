# Chrome DevTools MCP - 浏览器调试集成

**来源**: https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session  
**日期**: 2025-12-11 (发布) / 2026-03-16 (分析)  
**领域**: ai-agent/mcp-protocol  
**标签**: #Chrome #DevTools #MCP #调试 #浏览器自动化

---

## 核心功能

Chrome DevTools MCP 服务器增强：Coding Agent 可直接连接到活动浏览器会话。

### 新能力
```
1. 复用现有浏览器会话
   - 场景：修复需要登录的问题
   - Agent 直接访问当前浏览会话
   - 无需额外登录

2. 访问活动调试会话
   - 场景：DevTools Network 面板发现失败请求
   - 选择请求 → 让 Agent 调查
   - Elements 面板选择元素 → 让 Agent 修复
   - 无缝切换手动和 AI 辅助调试
```

---

## 工作原理

### Chrome M144+ 新功能 (Beta)
```
1. 远程调试连接请求
   - 基于现有远程调试能力
   - 默认禁用 (chrome://inspect#remote-debugging)
   - 开发者需显式启用

2. --autoConnect 选项
   - MCP 服务器配置此选项
   - 连接到活动 Chrome 实例
   - 请求远程调试会话

3. 用户许可对话框
   - 每次 MCP 请求远程调试会话
   - Chrome 显示对话框请求用户许可
   - 防止恶意滥用

4. 调试会话指示器
   - 调试会话激活时
   - Chrome 顶部显示"Chrome is being controlled by automated test software"横幅
```

---

## 配置指南

### 步骤 1: 启用远程调试
```
Chrome (>=144):
1. 导航到 chrome://inspect/#remote-debugging
2. 启用远程调试
3. 跟随对话框 UI 允许/拒绝传入调试连接

注意：远程调试必须在客户端请求前启用
```

### 步骤 2: 配置 MCP 服务器
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--autoConnect",
        "--channel=beta"
      ]
    }
  }
}
```

### 步骤 3: 测试配置
```
gemini-cli prompt:
"Check the performance of https://developers.chrome.com"

流程：
1. MCP 服务器尝试连接运行中的 Chrome 实例
2. Chrome 显示对话框请求用户许可
3. 点击 Allow
4. MCP 打开 developers.chrome.com 并执行性能追踪
```

---

## 使用场景

### 场景 1: 登录门控问题修复
```
问题：
- 网站问题仅在登录后出现
- Agent 无法独立登录 (需要 2FA/验证码)

传统方案：
1. 开发者登录
2. 截图/录屏问题
3. 描述给 Agent
4. Agent 推测原因
5. 开发者验证修复

MCP 方案：
1. 开发者登录并打开 DevTools
2. Agent 直接连接到当前会话
3. Agent 查看网络请求/控制台错误/DOM
4. Agent 直接诊断并修复
5. 开发者验证

节省：
- 无需截图/录屏/描述
- Agent 获得完整上下文
- 修复速度更快
```

### 场景 2: Network 面板调试
```
流程：
1. 开发者发现 Network 面板中失败请求
2. 选择该请求
3. 告诉 Agent: "调查这个失败请求"
4. Agent 访问：
   - 请求头/响应头
   - 请求体/响应体
   - 时间线/瀑布图
   - 控制台相关错误
5. Agent 诊断并建议修复

优势：
- 完整上下文 (非截图片段)
- Agent 可访问所有调试信息
- 实时交互
```

### 场景 3: Elements 面板修复
```
流程：
1. 开发者在 Elements 面板选择问题元素
2. 告诉 Agent: "修复这个元素的样式问题"
3. Agent 访问：
   - 完整 DOM 树
   - 计算样式
   - CSS 规则来源
   - Box model
4. Agent 诊断并修复

优势：
- 无需手动检查样式
- Agent 理解完整样式层级
- 修复更精准
```

---

## 连接模式对比

| 模式 | 描述 | 适用场景 |
|------|------|----------|
| **Auto Connect** (新) | 连接活动 Chrome 会话 | 复用登录状态/活动调试 |
| **Remote Debug Port** | 连接指定远程调试端口 | 自动化测试/CI |
| **Temporary Profile** | 临时配置文件隔离运行 | 多实例并行测试 |
| **Default Profile** | MCP 特定用户配置文件 | 日常开发 |

---

## 安全考虑

### 用户许可机制
```
每次连接请求：
- Chrome 显示对话框
- 用户必须明确允许
- 防止恶意网站静默连接

会话期间：
- 顶部横幅提示"Chrome is being controlled"
- 用户始终知道被控制
- 可随时关闭浏览器终止
```

### 权限范围
```
MCP 服务器可访问：
- DevTools 所有面板数据
- Network 请求/响应
- Elements DOM/样式
- Console 日志
- Performance 追踪
- Application 存储
- ...

MCP 服务器不可访问：
- 浏览器密码
- 扩展数据 (除非明确授权)
- 其他标签页 (除非切换)
- 本地文件系统
```

---

## 对 Sandbot V6.3 的启示

### 当前能力对比
```
Sandbot 当前：
- web_fetch: 抓取网页内容
- browser: 浏览器控制 (OpenClaw 内置)
- 无 DevTools 集成

差距：
- 无法访问活动调试会话
- 无法复用登录状态
- 无法访问 Network/Performance 数据
```

### 潜在集成方向
```
阶段 1: 浏览器控制增强
- 支持远程调试连接
- 复用现有会话
- 访问 Network/Console 数据

阶段 2: DevTools MCP 集成
- 实现 chrome-devtools-mcp 客户端
- 支持 --autoConnect
- 无缝切换手动/AI 调试

阶段 3: 调试自动化
- 自动性能分析
- 自动错误诊断
- 自动修复建议
```

### 知识管理应用
```
场景：用户报告网页问题

当前流程：
1. 用户描述问题
2. Sandbot 请求截图/URL
3. web_fetch 抓取内容
4. 分析并建议

MCP 增强流程：
1. 用户打开问题页面 + DevTools
2. Sandbot 连接到活动会话
3. 直接访问 Network/Console/DOM
4. 精准诊断并修复

知识积累：
- 常见问题模式 → knowledge_base/
- 修复方案 → 可检索案例
- 性能基准 → 长期追踪
```

---

## 技术实现参考

### MCP 服务器架构
```
chrome-devtools-mcp/
├── src/
│   ├── server.ts        # MCP 服务器主逻辑
│   ├── connection.ts    # Chrome 连接管理
│   ├── devtools.ts      # DevTools 协议封装
│   └── tools.ts         # MCP 工具定义
├── package.json
└── README.md

工具示例：
- get_network_requests()
- get_console_logs()
- get_dom_element(selector)
- get_computed_styles(selector)
- run_performance_audit(url)
- take_screenshot()
```

### DevTools 协议
```
Chrome DevTools Protocol (CDP):
- Network 域：网络请求监控
- DOM 域：DOM 树操作
- CSS 域：样式查询修改
- Console 域：控制台日志
- Performance 域：性能分析
- Runtime 域：JS 执行

MCP 封装：
- 将 CDP 命令转为 MCP 工具
- 结构化响应 (JSON)
- 错误处理/重试
```

---

## 局限性与未来

### 当前局限
```
1. 需要 Chrome M144+ (Beta)
   - 旧版本不支持 --autoConnect
   - 需手动配置远程调试端口

2. 每次连接需用户许可
   - 无法完全自动化
   - 适合交互式调试，非后台任务

3. 单会话限制
   - 一次连接一个 Chrome 实例
   - 多标签页需手动切换

4. 面板数据逐步开放
   - 目前：Network/Elements/Performance
   - 未来：更多面板数据
```

### 未来方向
```
Chrome 团队计划：
- 逐步开放更多面板数据
- 改进连接体验
- 增强安全性
- 支持更多 Agent 框架

社区扩展：
- Firefox DevTools MCP
- Safari Web Inspector MCP
- 跨浏览器调试
```

---

## 关键教训

1. **复用会话价值巨大**: 登录门控问题不再阻碍调试
2. **无缝切换**: 手动调试 ↔ AI 调试无摩擦
3. **用户控制**: 每次连接需许可，防止滥用
4. **渐进式开放**: 从基础面板开始，逐步扩展
5. **标准化协议**: CDP 作为基础，MCP 作为封装

---

**数量**: 550 知识点  
**深度**: ⭐⭐⭐⭐ (浏览器调试集成新范式)  
**行动项**:
- [ ] 调研 OpenClaw browser 工具增强空间
- [ ] 评估 DevTools MCP 集成可行性
- [ ] 设计调试自动化工作流
- [ ] 追踪 Chrome DevTools MCP 更新
