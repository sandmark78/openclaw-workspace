# OpenClaw 生态更新 - 2026-08-23

## 🔥 GitHub 新版本：2026.8.1 (Pre-release)

来源：https://github.com/openclaw/openclaw/releases

### 重要更新

1. **Secret Egress Host Binding**
   - 每个 shared-store secret 可绑定到精确的 HTTPS 目标主机
   - 支持 CLI、Gateway RPC、Control UI
   - 未绑定的哨兵替换会在明文出口前失败关闭
   - 贡献者：@shakkernerd

2. **GPT-5.6 Ultra 和运行时切换**
   - 支持 Sol、Terra、Luna 跨 OpenClaw 和 Codex 引擎
   - /model 和 fallback 保持模型、运行时、思考选择原子性
   - 新增两个 harness 的实时矩阵覆盖
   - 贡献者：@anyech, @vincentkoc

3. **Channel Plugin Ingress Monitors**
   - 共享插件 SDK 监控器：持久准入、轮询、修剪、声明身份验证、采用交接、关闭
   - IRC、Synology Chat、Google Chat 迁移到共享生命周期
   - 贡献者：@vincentkoc, @shakkernerd

4. **SQLite Snapshots** ⭐
   - `openclaw backup sqlite create|list|verify|restore`
   - 紧凑、已验证的全局和每 agent 数据库工件
   - 仅恢复新鲜目标
   - 贡献者：@giodl73-repo

5. **macOS App Profiles**
   - 隔离命名 app 实例：状态、偏好、Keychain、Gateway 服务、重复实例所有权
   - 保持主机全局登录和节点服务不受影响
   - 贡献者：@shakkernerd, @vincentkoc

6. **Plugin Install Provenance Warnings**
   - 任意可执行插件源需要明确 --force 确认
   - 可信来源（ClawHub、bundled、official-catalog、tracked-update）无摩擦
   - Crestodian 安装限制为可信来源
   - 贡献者：@jesse-merhi, @vincentkoc

7. **Control UI Update Recovery**
   - "新版本可用"重载按钮现在会等待 gateway 重启完成后再加载
   - 修复了之前 chunk 卡住的问题

---

## ClawHub 状态

- clawhub.com 已重定向到 clawhub.ai
- 热门技能包括：Twitter API、AI Video Generation、TikTok API、Planning with files 等
- 无重大变化

## 文档站状态

- docs.openclaw.ai 正常运行
- 无重大变化

---

## 与我们相关的

- **SQLite Snapshots** 对我们有价值：可以用来备份记忆文件和知识库
- **GPT-5.6 Ultra** 如果我们未来升级模型，这个版本已支持
- **Plugin Provenance Warnings** 安全增强，安装第三方插件需注意
