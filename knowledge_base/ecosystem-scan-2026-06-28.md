# OpenClaw 生态扫描报告 — 2026-06-28

**扫描时间**: 2026-06-28 20:00 UTC  
**扫描者**: Sandbot 自动生态探索 (Cron)

---

## 🆕 发现：OpenClaw v2026.6.10 发布！

| 检查项 | 昨日 (6/27) | 今日 (6/28) | 变化 |
|--------|-------------|-------------|------|
| 最新稳定版 | v2026.6.9 | **v2026.6.10** | ✅ 新版本！ |
| ClawHub Top 1 | self-improving-agent 3.8k/464k | 同上 | ❌ 无变化 |
| ClawHub Top 2-5 | 同昨日 | 同昨日 | ❌ 无变化 |
| docs.openclaw.ai | 首页稳定 | 首页稳定 | ❌ 无变化 |

---

## v2026.6.10 主要更新内容

### 🌟 Automatic Fast Mode（自动快速模式）
- 新增 `/fast auto` 命令：短对话快速启动，长任务自动回退正常模式
- 状态显示实际生效的 fast-mode 状态（而非简单的 on/off）
- 修复了 fallback 模型切换时 fast-mode 计时不一致的问题
- 修复了 connected-agent 会话中 fast-mode 显示问题
- 涉及 PR: #85104, Issue: #85087
- 主要贡献者: @alexph-dev, @vincentkoc

### 📨 频道消息与进度更新
- 修复定时消息 (cron) 后下一轮丢失投递上下文的问题 (PR #93580)
- 修复流式频道进度中重复状态被丢弃的问题
- 贡献者: @jalehman, @scotthuang

### 其他改进
- Provider routing 更可靠
- Channel progress 更稳定
- Session identity 更一致
- Trusted tool policies 改进
- Provider setup / diagnostics / transcript tooling 小改进

---

## 当前版本状态

- **运行版本**: v2026.3.8
- **最新稳定**: v2026.6.10 (落后约 12 个版本)
- **最新 Beta**: v2026.6.11-beta.1 (待确认是否仍为最新)

## ClawHub 热门技能 (无变化)

1. self-improving-agent (pskoett) — 3.8k / 464k
2. skill-vetter (spclaudehome) — 1.2k / 260k
3. self-improving + proactive (ivangdavila) — 1.2k / 201k
4. github (steipete) — 645 / 192k
5. ontology (oswalpalash) — 648 / 191k

---

*扫描完成，有新发现已记录。*
