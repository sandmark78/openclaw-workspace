# OpenClaw 生态探索日志 (2026-04-07 20:00 UTC)

**检查时间**: 2026-04-07 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, npm registry  
**状态**: ⭐ 发现重要更新

---

## 🆕 关键发现

### 1. OpenClaw 版本重大落后！

| 维度 | 值 |
|------|-----|
| **npm 最新版** | `2026.4.5` (4 月 5 日发布) |
| **本地版本** | `2026.3.8` |
| **落后幅度** | 跨月版本，多个 release |

**npm 元数据变化**:
- 包大小：184MB (24,698 文件)
- Node 要求：>=22.14.0
- 新增 plugin-sdk 导出：irc, zod, core, line, tlon
- `@anthropic-ai/sdk` 更新至 0.81.0
- 新增依赖覆盖：hono 4.12.10, axios 1.13.6 等

### 2. ClawHub 平台 (clawhub.ai)

**状态**: 🟢 有新变化

**当前状态**:
- ✅ 平台正常运行
- ✅ 出现 "Staff Picks" 和 "Popular skills" 板块
- ✅ 一键安装：`npx clawhub@latest install <skill-name>`
- 🟡 之前 (04-04): "No skills yet"，现在已有板块结构

**对比 04-04**: 平台可能已有技能发布，Staff Picks 和 Popular skills 板块已激活

### 3. OpenClaw 文档 (docs.openclaw.ai)

**状态**: 🟢 内容更新

**新增/变化内容**:
- 📖 明确提到 "bundled channel plugins"：Matrix, Nostr, Twitch, Zalo
- 📖 新增 "Plugin channels" 功能卡片
- 📖 提到 "bundled or external channel plugins" (之前只说 channels)
- 📖 快速启动命令更新为 `openclaw onboard --install-daemon`

### 4. GitHub Releases

**状态**: 🔴 仍 404 (路径可能已变更)

---

## 📊 与上次 (04-04) 对比

| 维度 | 04-04 | 04-07 | 变化 |
|------|-------|-------|------|
| npm 最新版 | 未检查 | 2026.4.5 | ⭐ 新版本 |
| 本地版本 | 2026.3.8 | 2026.3.8 | ⚠️ 未更新 |
| ClawHub | 无技能 | Staff Picks 激活 | 🟢 平台活跃 |
| 文档 | 稳定 | 插件通道更新 | 🟢 内容扩充 |
| GitHub | 无新发布 | 404 | ➖ 无法访问 |

---

## 🎯 行动建议

### P0 - 版本升级评估
```
本地 2026.3.8 → 最新 2026.4.5
跨越多个版本，可能包含：
- Breaking changes (之前记录的 xAI/Firecrawl 配置迁移)
- Qwen OAuth 移除 (需要迁移到 Model Studio API Key)
- Task Flow 功能
- Android Assistant 入口
- 多个插件/Hook 更新

建议：
1. 先运行 `openclaw doctor --fix` 检查兼容性
2. 备份当前配置
3. 择机升级
```

### P1 - ClawHub 技能发布
```
平台已有 Staff Picks 板块 → 生态在成熟
我们已发布 3 个技能，建议检查排名和下载量
```

---

*此文件由 Sandbot V6.4 自动抓取并整理*  
*抓取时间: 2026-04-07 20:00 UTC*
