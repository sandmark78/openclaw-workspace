# OpenClaw 2026.8.1-beta.3 发布记录

**抓取时间**: 2026-08-26 20:00 UTC  
**当前版本**: 2026.7.1  
**最新版本**: 2026.8.1-beta.3 (预发布)

---

## 主要更新内容

### 1. GPT-5.6 系列支持
- GPT-5.6 Sol, Terra, Luna, Ultra reasoning 支持
- 跨 OpenClaw 和 Codex runtime

### 2. Control UI 改进
- 首次运行设置流程优化
- 验证模型设置可继续到 Custodian
- 可选通道设置

### 3. 浏览器自动化增强
- Puppeteer-compatible CDP relay 支持
- 配对 Chrome 会话支持

### 4. Gateway 生命周期管理
- 显式外部 Gateway 生命周期监督
- 验证重启交接

### 5. 数据库维护
- 紧凑的 SQLite 备份命令
- 新目标恢复命令

### 6. 通道插件
- 共享持久入口监视器

### 7. 安全增强
- Secret egress host binding
- 每个共享存储密钥可绑定到精确的 HTTPS 目标主机
- 未绑定的哨兵替换在明文出口前失败关闭

---

## 发布证据

- npm: https://www.npmjs.com/package/openclaw/v/2026.8.1-beta.3
- 89 个官方 npm 插件均已验证
- @openclaw/codex@2026.8.1-beta.3 包含 @openai/codex@0.149.1

---

## 升级建议

⚠️ 这是 beta 版本，建议：
1. 先在测试环境验证
2. 备份当前配置
3. 等待稳定版发布后再升级生产环境

---

## ClawHub 新技能 (2026-08-26 抓取)

| 技能名 | 作者 | 说明 |
|--------|------|------|
| Planning with files | othmanadi | Manus 风格的持久文件规划 |
| ai-video-generation | skills-101 | AI 视频生成 |
| Instagram API | fetcher-sh | Instagram API 替代方案 (USDC 付费) |
| Remotion Best Practices | am-will | React 视频创作最佳实践 |
| ClawCall | clawcall-dev | AI 代理拨打电话 |
| TikTok API | fetcher-sh | TikTok API 替代方案 |
| Homeassistant Skill | anotb | 智能家居控制 |
| Agent OS Asset | lee-agi | 将文件变成 AI 资产 |
