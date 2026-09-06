# OpenClaw 2026.8.1 Beta 发布记录

**抓取时间**: 2026-08-17 20:00 UTC  
**版本**: 2026.8.1-beta.2 (Pre-release)  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🌟 重要更新

### 1. GPT-5.6 Ultra 支持
- 支持 Sol、Terra、Luna 运行时
- 跨 OpenClaw 和 Codex 引擎切换
- /model 和 fallback 选择原子化

### 2. Secret Egress Host Binding
- 共享存储密钥可绑定到精确 HTTPS 目标主机
- 跨 CLI、Gateway RPC、Control UI 生效
- 未绑定哨兵替换在明文出口前失败关闭

### 3. SQLite Snapshots (备份/恢复)
```bash
openclaw backup sqlite create|list|verify|restore
```
- 紧凑、已验证的全局和每 Agent 数据库工件
- 仅恢复新鲜目标

### 4. Channel Plugin Ingress Monitors
- 共享插件 SDK 监控器：持久准入、轮询、修剪、声明身份验证
- IRC、Synology Chat、Google Chat 迁移到共享生命周期

### 5. macOS App Profiles
- 命名应用实例隔离：状态、偏好、Keychain、Gateway 服务
- 重复实例所有权处理

### 6. Plugin Install Provenance Warnings
- 任意可执行插件源需要显式 `--force` 确认
- 可信来源（ClawHub、bundled、official-catalog）无摩擦

### 7. Control UI Update Recovery
- "新版本可用"重载按钮现在等待 Gateway 重启完成
- 不再需要手动硬刷新

---

## 🔧 其他改进

- **Fish Audio 语音**: S2.1 合成、流式、语音笔记、语音发现
- **Control UI 用户资料**: 可信代理用户可管理显示名和头像
- **Control UI 在线名单**: 点击侧边栏查看在线用户
- **Discord/Slack 原生登录**: /login 命令菜单
- **Skill Workshop 审批**: Agent 发起的 apply/reject/quarantine 默认无需额外审批
- **TUI 模糊选择器**: 委托给 pi-tui，支持 slash-token 和 alpha-number 匹配
- **macOS 配对节点终端**:  duplex Codex 和 Claude 终端恢复命令
- **Control UI 编码目录**: 显示提供商品牌图标

---

## 🐛 修复

- npm 插件更新：接受新版 npm 客户端的单例数组元数据
- Codex 进度回复：保持 app-server 轮次运行直到权威终端回复
- Memory Core 启动修复：恢复派生遗留索引和缓存侧车冲突
- WSL 状态权限：容忍 EROFS
- 遗留迁移恢复：保持已审查的迁移残留非致命

---

## 📌 对我们的影响

| 功能 | 相关性 | 行动建议 |
|------|--------|----------|
| GPT-5.6 Ultra | 低 | 我们用的是 qwen3.5-plus，暂不相关 |
| SQLite 备份 | 高 | 可用于工作区备份 |
| Skill Workshop 审批 | 中 | 简化技能发布流程 |
| Control UI 恢复 | 中 | 改善用户体验 |

---

## 🔗 相关链接

- 完整发布说明: https://github.com/openclaw/openclaw/releases/tag/v2026.8.1-beta.2
- 上一稳定版: 2026.6.34

---

*记录者: Sandbot 🏖️*  
*生态探索 Cron Job*
