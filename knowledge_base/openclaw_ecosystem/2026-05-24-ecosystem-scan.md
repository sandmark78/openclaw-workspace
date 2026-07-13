# OpenClaw 生态探索 - 2026-05-24

**扫描时间**: 2026-05-24 20:00 UTC  
**状态**: ✅ 有新变化

---

## 📦 GitHub Releases - 新 Pre-Release (2026-05-24 14:42 UTC)

### 关键新功能

#### 1. Meeting Notes 插件 🆕
- 新增 **外部会议记录插件**，SDK source-provider 架构
- 支持自动开始捕获配置、手动导入转录
- 只读 `openclaw meeting-notes` CLI 访问
- **Discord 语音作为第一个实时数据源**
- 不在核心 npm 包中，独立插件

#### 2. Talk/Realtime 增强 🆕
- WebUI 和 Discord 语音通话者可以在咨询运行时：
  - 查询活跃 OpenClaw 运行状态
  - 取消、引导或排队后续工作
  - PR [#84231](https://github.com/openclaw/openclaw/pull/84231)

#### 3. Discord/Voice 实时唤醒
- 新增实时 wake-name 门控
- agent-name 默认值
- 提升 profile bootstrap context budget（支持更长的 USER.md/SOUL.md）

#### 4. Image Tool 自适应压缩 🆕
- 新增 **模型感知图像压缩**
- `agents.defaults.imageQuality` 偏好设置
- 可选：token-efficient / balanced / high-detail 三种模式

#### 5. CLI/Models 认证配置
- `openclaw models auth login` 支持 `--profile-id` 存储提供商认证
- 支持命名 Codex OAuth profile 设置
- PR [#49315](https://github.com/openclaw/openclaw/pull/49315)

### Gateway 性能优化
- 复用进程稳定的 channel catalog 读取
- 缓存 install-record、channel-catalog、bundled-channel、Telegram session-store 元数据
- 复用不可变插件元数据快照
- **Lazy-load** 启动空闲的插件工作、核心 gateway 方法处理器、嵌入 ACPX 运行时
- 缓存插件 SDK public-surface alias maps
- 跳过无关的 macOS/Linuxbrew PATH 探测
- 轮换 gateway watch CPU profiles

### 文档更新
- Signal configPath、Telegram wildcard topic 默认值
- WhatsApp QR/408 恢复指南
- 中文内存导航文档
- Feishu dynamic agents
- 中国术语表更新
- Upstash Box 安装指南
- Gateway 暴露运行手册

### 打包优化
- 排除文档图片和资源，减少 npm 包体积

---

## 🌐 ClawHub

- 域名重定向：clawhub.com → **clawhub.ai**
- 统计数据：
  - **52.7k** tools
  - **180k** users
  - **12M** downloads
  - **4.8** avg rating
- 三大板块：Skills / Plugins / Publishers

---

## 📚 docs.openclaw.ai

- 文档正常更新
- 包含 Node 24 推荐 / Node 22 LTS (22.19+) 兼容要求
- 通道支持：Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等

---

## 🎯 Sandbot 相关发现

1. **imageQuality 设置** - 可配置降低图片处理 token 消耗
2. **Meeting Notes 插件** - 值得关注的外部插件生态
3. **Lazy-load 优化** - Gateway 启动更快，健康检查不再等待未使用的处理器
4. **中文文档更新** - 中文内存导航和术语表有社区贡献

---

*下次扫描：下次心跳或 cron 触发时*
