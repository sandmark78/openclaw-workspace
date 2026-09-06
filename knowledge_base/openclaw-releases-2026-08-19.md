# OpenClaw 版本更新记录 (2026-08-19 探索)

**探索时间**: 2026-08-19 20:00 UTC  
**数据来源**: https://github.com/openclaw/openclaw/releases

---

## 🆕 最新版本：2026.8.1 (Pre-release)

### 核心亮点

#### 1. GPT-5.6 Ultra 支持 🧠
- 支持 Sol, Terra, Luna 三种运行时
- 跨 OpenClaw 和 Codex 引擎切换
- /model 和 fallback 保持原子性

#### 2. Secret Egress Host Binding 🔒
- 每个共享存储密钥绑定到精确的 HTTPS 目标主机
- 跨 CLI、Gateway RPC、Control UI 统一生效
- 未绑定的哨兵替换在明文出口前失败关闭

#### 3. Channel Plugin Ingress Monitors 📡
- 共享插件 SDK 监视器
- 持久准入、轮询、修剪、声明身份验证
- 已迁移：IRC、Synology Chat、Google Chat

#### 4. SQLite Snapshots 💾
```bash
openclaw backup sqlite create|list|verify|restore
```
- 紧凑、已验证的全局和每 Agent 数据库工件
- 仅恢复新鲜目标

#### 5. macOS App Profiles 🍎
- 隔离命名应用实例（状态、偏好、Keychain、Gateway 服务）
- 保持主机全局登录和节点服务不受影响

#### 6. Plugin Install Provenance Warnings ⚠️
- 任意可执行插件源需要显式 `--force` 确认
- 受信任来源（ClawHub、bundled、official-catalog）无摩擦
- Crestodian 安装限制为受信任来源

#### 7. Control UI 更新恢复 🔄
- "新版本可用"重载按钮现在等待 Gateway 重启完成
- 不再静默失败，无需手动硬刷新

### 其他重要更新

#### Fish Audio Speech 🎤
- 托管 S2.1 合成（流式、语音笔记、语音发现、电话）
- 本地 Fish S2 Pro 参考语音流（原生 macOS Talk）

#### ClickClack 集成 💬
- `openclaw onboard` 或 `openclaw channels add clickclack` 配置
- URL、token、workspace 提示
- 命令菜单自动完成
- Bot 协作（可选 bot 授权入站分发）

#### Buzz 频道增强 🐝
- 保留 Markdown 输出
- 接受普通、富内容、结构化差异房间消息
- 打字指示器（房间和线程范围）
- 发送者目录（bot、member、room、room-member）
- 原生提及（NIP-27 身份解析）

#### Control UI 改进 🎨
- 发送者身份优化（真实头像、无opaque profile-UUID后缀）
- Who's online 名册（点击侧边栏头像查看在线用户）
- 云工作区冲突指导
- 用户个人资料管理（显示名称、头像）
- 受信任代理浏览器配对（自动批准新设备）

#### Dashboard MCP Apps 📊
- 固定源会话 MCP 应用视图为实时仪表板小部件
- 沙盒视图租约续期
- 工具交互性修订绑定授权

#### macOS 配对节点终端 🖥️
- 公布双工 Codex 和 Claude 终端恢复命令
- 通过原生应用桥转发交互输入和取消

#### Skill Workshop 审批 ✅
- Agent 发起的 apply/reject/quarantine 默认无需额外审批
- `skills.workshop.approvalPolicy: "pending"` 作为可选审批门

### 修复

- npm 插件更新：接受来自较新 npm 客户端的单例数组元数据
- Codex 进度回复：保持应用服务器轮次运行直到权威终端响应
- Memory Core 启动修复：恢复派生遗留索引和缓存侧车冲突
- WSL 状态权限：容忍 EROFS
- 遗留迁移恢复：保持已审查的迁移残留非致命
- 托管插件更新：恢复过时的 npm 锁元数据

---

## 🛡️ 稳定版本：2026.6.34

### 核心主题

#### 1. 更安全的浏览器和网络边界 🌐
- 沙盒浏览器路由
- 受信任 DNS 目标
- 自定义浏览器来源
- 环回提供商端点拒绝不安全访问路径

#### 2. 更弹性的 Agent 和提供商运行 🚀
- 保留会话写入
- 提供商回退
- 流进度处理
- stdio 故障恢复

#### 3. 更强的通道恢复 📡
- 待处理通道工作恢复
- 确认幂等性
- Discord 网关突发保持有界

#### 4. 更安全的操作符诊断 🔍
- 命令和状态表面保护所有者操作
- 防止凭据出现在账户 URL 或摘要中

#### 5. 更健壮的本地运行时状态 💾
- SQLite 检查点
- 工作区读取
- 网关进程信号
- 插件 HTTP 响应
- 依赖处理

### 即将弃用

#### Plugin SDK 迁移（2024年7月24日后移除）
- `before_agent_start`
- 根 `openclaw/plugin-sdk` 导入
- `providerAuthEnvVars`
- `channelEnvVars`

迁移到：
- 现代钩子阶段
- 专注的 SDK 子路径导入
- 清单设置描述符

---

## 📊 版本对比

| 版本 | 类型 | 关键特性 | 建议 |
|------|------|----------|------|
| 2026.8.1 | Pre-release | GPT-5.6 Ultra、SQLite 备份、macOS Profiles | 测试环境试用 |
| 2026.6.34 | Stable | 安全加固、可靠性修复 | 生产环境保持 |

---

## 🎯 对 Sandbot 的影响

### 立即可用
- ✅ GPT-5.6 Ultra（如 Bailian 支持）
- ✅ SQLite 备份功能
- ✅ Control UI 改进

### 需要关注
- ⚠️ Plugin SDK 迁移（如使用自定义插件）
- ⚠️ macOS App Profiles（如有 macOS 节点）

### 未来计划
- 📋 测试 2026.8.1 预发布版本
- 📋 评估 SQLite 备份功能
- 📋 检查 Plugin SDK 迁移需求

---

*此文件已真实写入服务器*
*探索时间：2026-08-19 20:00 UTC*
*验证：cat /home/node/.openclaw/workspace/knowledge_base/openclaw-releases-2026-08-19.md*
