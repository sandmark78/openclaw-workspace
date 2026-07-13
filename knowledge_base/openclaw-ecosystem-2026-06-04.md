# OpenClaw 生态探索报告

**日期**: 2026-06-04  
**触发**: Cron 生态探索任务  
**当前运行版本**: 2026.3.8  
**npm 最新稳定版**: 2026.5.28（上次记录，待确认是否更新）  
**GitHub 最新 pre-release**: 2026.6.2（2026-06-03 发布！）

---

## 🔴 版本落后状态

| 指标 | 值 |
|------|------|
| **当前运行版本** | 2026.3.8 |
| **最新稳定版** | ≥ 2026.5.28 |
| **最新 pre-release** | 2026.6.2（2026-06-03） |
| **落后天数** | ~88 天 |

升级命令: `npm install -g openclaw@latest && openclaw gateway restart`

---

## 🆕 2026.6.2 Pre-release 新增亮点（2026-06-03 发布）

### 1. 插件/技能安装策略重构
- **Operator install policy** 取代旧的 dangerous-code scanner 路径
- 更清晰的 doctor、CLI、ClawHub 和故障排除界面
- 覆盖 package、archive、source、upload、marketplace 安装全流程

### 2. 通道安全性全面提升
- **Telegram**: 管理员 writeback 权限校验、exec approval allowlists 修复、预览重复阻止、流式预览优化、投票修改器修复
- **Feishu**: setup runtime setter 修复
- **Discord**: voice 错误处理、libopus 错误形状匹配、tool progress 清理
- **WhatsApp/Outbound**: transcript mirror 失败时保持 channel send 耐久

### 3. Chat/Control UI 改进
- 流式文本可见性保持
- 完成的 send 协调
- ACK 计时暴露
- Workboard 键盘移动控制
- 对话框可访问性增强
- Usage view 懒加载
- WebChat prompt-cache 亲和性稳定

### 4. Skill Workshop & Workboard 增强
- Workboard 卡片操作收紧
- Android companion-first shell UX 改进
- Chat ACK timing 元数据文档

### 5. 安全与策略
- 拒绝 corrupt shell snapshots
- 拒绝不支持的策略 key
- unsafe exec approval precheck 环境检测
- malformed script limits 拒绝
- suspicious gateway startup config 检测
- data-handling conformance checks 新增

### 6. Gateway/Agent/Codex 路径恢复
- 会话 write-lock 释放失败恢复
- 废弃 Codex app-server 启动退休
- stream-to-parent ACP spawn 注册保持
- custom-provider runtime fanout 恢复
- bundled provider aliases 修复
- prompt-cache boundaries 修复
- Gemini stop sequences 修复
- Kimi cache markers 修复

### 7. Release/CI/Docker
- Windows node installer 发布提升
- Windows release asset 链接验证
- 网络调用边界化
- package hydration 路径修复
- log drains 修复

### 8. 文档更新
- Windows Hub setup guidance 刷新
- Gateway/CLI/plugin SDK helper contracts 文档化

---

## 🟡 ClawHub 生态（与上次一致）

| 指标 | 值 |
|------|------|
| 技能/插件总数 | 52.7k |
| 注册用户 | 180k |
| 总下载量 | 12M |
| 平均评分 | 4.8 |

---

## 🟢 Docs 网站

无明显变化，内容与上次一致。

---

## 📊 总结

1. **版本升级优先级: 🔴 HIGH** — 落后 ~88 天，2026.3.8 → 最新 2026.5.28+
2. **2026.6.2 pre-release 值得关注** — 安装策略重构、通道安全大幅增强
3. **ClawHub 生态稳定** — 数据无变化
4. **重点新功能**: operator install policy、通道安全性、Workboard 键盘控制、Windows 安装器

---

*由 Sandbot 🏖️ 自动生态探索任务生成*
