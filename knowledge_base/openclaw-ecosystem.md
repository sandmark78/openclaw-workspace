# OpenClaw 生态追踪

**最后更新**: 2026-08-25 20:00 UTC

---

## 当前版本状态

| 项目 | 版本 | 日期 |
|------|------|------|
| 本地安装 | 2026.7.1 | - |
| 最新稳定版 | v2026.8.1-beta.3 | 2026-08-25 |
| 最新预发布 | 2026.8.1-beta.3 | 2026-08-25 |

---

## v2026.8.1-beta.3 预发布版 (2026-08-25) ⭐ 重大更新

### 核心亮点

1. **GPT-5.6 系列支持**
   - Sol, Terra, Luna, Ultra 推理模型支持
   - 跨 OpenClaw 和 Codex 运行时

2. **Control UI 改进**
   - 首次运行设置流程优化
   - 验证模型设置进入 Custodian
   - 可选通道设置

3. **浏览器自动化**
   - Puppeteer 兼容 CDP 中继支持
   - 配对 Chrome 会话

4. **Gateway 生命周期**
   - 显式外部 Gateway 生命周期监控
   - 验证重启交接

5. **数据库**
   - 紧凑、验证的 SQLite 备份命令
   - 新目标恢复命令

6. **通道插件**
   - 共享持久入口监控器

### 发布证据
- npm: https://www.npmjs.com/package/openclaw/v/2026.8.1-beta.3
- 89 个官方 npm 插件已同步到 v2026.8.1-beta.3
- @openclaw/codex@2026.8.1-beta.3 搭载 @openai/codex@0.149.1

### 安全特性 (2026.8.1)
- **Secret egress host binding**: 每个共享存储密钥绑定到精确 HTTPS 目标主机
- 未绑定哨兵替换在明文出口前失败关闭

---

## ClawHub 生态观察 (2026-08-25 快照)

热门技能：
- Planning with Files (othmanadi) - 194 安装 - Manus 风格持久文件规划
- Grilling (mattpocock) - 面试式深度理解
- Remotion Best Practices (am-will) - 191 安装 - React 视频创作
- ClawCall (clawcall-dev) - 164 安装 - AI 电话拨打
- Self-Improving Agent (pskoett) - 136 安装 - 持续学习
- Homeassistant Skill (anotb) - 133 安装 - 智能家居控制
- 缠论引擎 (adsorgcn) - 100 安装 - A股缠论分析
- Neural Memory - 关联记忆系统

**观察**: 
- 技能生态持续增长
- 出现更多垂直领域技能（股票分析、智能家居）
- 中文技能：缠论引擎是新出现的

---

## 升级建议

**当前状态**: 本地 v2026.7.1 → 新预发布版 v2026.8.1-beta.3 可用

**重大变化**:
- GPT-5.6 系列模型支持（Sol/Terra/Luna/Ultra）
- 安全增强（Secret egress host binding）
- 浏览器自动化改进（CDP 中继）

**建议**:
- 这是重大版本更新，GPT-5.6 支持是重要功能
- 但仍是 beta 版，建议等稳定版发布
- 如需 GPT-5.6 支持可考虑升级

**升级命令**（需老大确认）:
```bash
openclaw update
```

---

## 历史版本

### v2026.7.2 预发布版 (2026-08-04)
- 隔离存储 (Quarantine Store)
- 崩溃可恢复 SQLite 快照
- Schema 升级数据丢失拒绝

### v2026.7.1-2 补丁 (2026-08-04)
- Memory Core 启动修复
- WSL 状态权限修复

---

*下次检查: 2026-08-26*
