# OpenClaw 发布记录追踪

**创建时间**: 2026-11-08  
**最后更新**: 2026-11-08 20:00 UTC

---

## 最新版本: v2026.11.2

**发布日期**: 2026-11-02 (约一周前)  
**PR 数量**: 115 个  
**主要贡献者**: @steipete, @RomneyDa, @obviyus, @vincentkoc 等

### 核心亮点

#### 1. 隐私与信任边界强化
- 配置密钥、对话内容、工具错误、通道载荷不再泄露到诊断日志
- 强制 provider 和导航信任边界
- MCP grants 在 warm CLI turns 后释放

#### 2. 账户安全投递
- 持久重试和计划投递中保留发送者和账户身份
- WhatsApp 身份查找恢复
- Teams 路由和允许列表设置在重载时保留

#### 3. Gateway 可用性提升
- 减少诊断捕获工作量
- 避免 Gateway 在插件清理或病态 Telegram 表时阻塞
- 取消通道启动期间的关闭
- 恢复临时 schema-lease 冲突

#### 4. 更安全的恢复和更新
- 更新过程中保留配置的插件可执行文件和环境引用
- macOS 服务恢复在 Trash 访问被拒绝时修复
- 避免更新自封锁和中断更新挂起

#### 5. 原生客户端恢复
- iOS 重连导航保持响应
- Android 聊天启动状态保留
- Apple model 和 computer-use 资源在临时初始化失败后恢复

#### 6. 安装和状态正确性
- 恢复 Ubuntu 默认权限下的浏览器扩展安装
- 处理 Windows 状态目录大小写
- 保留数据库所有权

### 其他修复
- 模型路由和 providers: 修复禁用推理、tier-suffixed 设置、别名等
- Codex 和 Claude 集成: 保留导入登录、刷新继承工作区编辑
- 内存和嵌入: 限制组装召回上下文
- Worker 和数据库生命周期: 保持不可用环境不出现在准入预算中
- Agent 执行: 正确重试依赖工具、停止退化流参数
- 更新诊断: 避免 FIFO 挂起
- 设置和兼容性: 保持技能启用、恢复 Bun-only 安装兼容性
- 配置编辑: 显示不可访问的配置根
- 聊天界面: 支持键盘提交选定答案
- 通道和通知: 退役过期 Discord 组件
- 调度: 保留提及心跳轮询的提醒
- 移动、浏览器和语音: 显示来自其他客户端的消息进度
- 媒体和资源恢复: 保留超大生成媒体
- 执行和认证: 交付结果优先执行通知

---

## ClawHub 状态 (2026-11-08)

**网站**: clawhub.ai (从 clawhub.com 重定向)  
**状态**: 正常运行

### 官方技能分类
- GitHub, VS Code, Notion, Slack, Gmail
- Google Drive, Google Sheets, Google Calendar
- Linear, Figma, Trello
- WhatsApp 通道插件

### CLI 发布工具
```bash
npm i -g clawhub
clawhub login
clawhub skill publish ./my-skill --slug my-skill --version 1.0.0
clawhub package publish your-org/your-plugin
```

---

## 文档站状态 (2026-11-08)

**网站**: docs.openclaw.ai  
**状态**: 正常运行

### 主要文档区域
- Get started, Install, Channels, Agents
- Capabilities, ClawHub, Models, Platforms
- Gateway & Ops, Reference, Releases, Help

### 关键信息
- Node 26 推荐，或 Node 24.22.1+ / Node 26.12.1+
- MIT 许可，社区驱动
- 由 OpenClaw Foundation (501(c)(3)) 开发
- 支持通道: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等
