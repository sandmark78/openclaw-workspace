# 🌐 OpenClaw 生态快照 - 2026-08-15

**抓取时间**: 2026-08-15 20:00 UTC  
**下次检查**: 2026-08-16 或下次 cron 触发

---

## 1️⃣ OpenClaw 核心 — 新版本发布

**版本**: `v2026.8.1-beta.2`  
**发布时间**: 2026-08-15 05:36 UTC  
**发布者**: @steipete  
**标签**: Prerelease  
**链接**: https://github.com/openclaw/openclaw/releases/tag/v2026.8.1-beta.2

### Highlights
- 🔐 **Secret egress host binding** — 每个共享存储 secret 绑定到精确 HTTPS 目标主机，未绑定的 sentinel 替换失败闭合，防止明文外泄
- 🤖 **GPT-5.6 Ultra + runtime 切换** — 支持 Sol/Terra/Luna 三种 OpenClaw 和 Codex 引擎 runtime，通过 `/model` 保持模型/runtime/thinking 原子切换
- 📡 **Channel plugin ingress monitors** — 共享插件 SDK 监控实现稳定准入、轮询、清理、身份验证、接管，IRC/Synology Chat/Google Chat 已迁移
- 💾 **SQLite snapshots** — `openclaw backup sqlite create|list|verify|restore` 命令，支持紧凑的可验证数据库快照
- 🖥️ **macOS app profiles** — 隔离命名实例的状态、偏好、Keychain、Gateway 服务
- ⚠️ **Plugin install provenance warnings** — 任意可执行插件源需要 `--force` 确认，ClawHub/官方目录保持无障碍
- 🔄 **Control UI 更新恢复** — "新版本可用"Reload 按钮现在等待 Gateway 重启完成后再加载

### 其他重要修复
- Codex 子 Agent fan-out 完成终端 yield 立即收尾
- Telegram 实时位置支持（初始/移动/停止位置更新）
- Control UI 浏览器标签页身份保持、附件暂存、浏览器标注、头像刷新、无障碍改进
- 浏览器扩展 relay 安全：要求 64 字符 relay secret 和安全 WebSocket URL
- 引导式 onboarding 跳过 UI 路由修复
- 大量 Control UI 权限/会话/操作修复

---

## 2️⃣ ClawHub 市场状态

**URL**: https://clawhub.ai/ (已重定向)  
**热点技能**（按安装量排序）:
| 排名 | 技能 | 作者 | 安装量 |
|------|------|------|--------|
| 1 | self-improving agent | pskoett | 157 |
| 2 | 倪海厦skill·经方中医AI | jangviktor-web | 80 |
| 3 | Tavily AI Search | bert-builder | 62 |
| 4 | OOXML Lookup | shbernal | 62 |
| 5 | Word/DOCX | ivangdavila | 61 |
| 6 | Find Skills Skill | fangkelvin | 50 |
| 7 | 中国专利Skill | handsomestwei | 40 |
| 8 | frontend-design-ultimate | aiepco | 33 |
| 9 | Business Strategy | ivangdavila | 11 |
| 10 | Caveman Commit | seanford | 7 |

**新出现技能**:
- `treg` by superdesigndev — 外部/实时数据 SEO/SERP 查询 (23 installs)
- `gitea` by wei840222 — Gitea CLI 交互 (6 installs)

**注意**: 部分技能链接指向 `skills.sh`（belt CLI 生态），非纯 ClawHub 托管

---

## 3️⃣ 文档状态

**URL**: https://docs.openclaw.ai  
**内容**: 文档结构稳定，无重大变化。主要章节：
- 快速开始 / 安装 / 通道 / Agent / 能力 / ClawHub / 模型 / 平台 / Gateway 运维 / 参考 / 帮助
- 文档域名未变，内容与上次抓取一致

---

## 4️⃣ 关联项目

- **Lobster Orchestrator**: GitHub repo 无新 release（空列表）
- **nicepkg/openclaw**: 404 (不存在此 repo)

---

## 5️⃣ 总结

| 项目 | 状态 | 变化 |
|------|------|------|
| 🔥 OpenClaw 核心 | **有更新** | v2026.8.1-beta.2 (2026-08-15) |
| 🏪 ClawHub 市场 | 活跃 | 多技能更新，belt CLI 生态技能数量增长 |
| 📖 文档站 | 无变化 | 结构稳定 |
| 🦞 Lobster Orchestrator | 无变化 | 无新 release |