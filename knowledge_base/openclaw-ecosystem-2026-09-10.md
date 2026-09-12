# OpenClaw 生态探索更新 2026-09-10

**日期**: 2026-09-10 20:00 UTC
**来源**: clawhub.com / docs.openclaw.ai / github releases

---

## 📦 GitHub Releases 新发现

### OpenClaw 2026.6.35 —— 2026年6月最终扩展稳定版 (LTS)

这是 **2026 年 6 月 Extended Stable (LTS) 系列的最终版本**。

**亮点**:
1. **更安全的 Provider/Channel 边界**: 内置 provider 和 channel 适配器现在会:
   - 绑定 untrusted response bodies
   - 在昂贵处理前拒绝超大输入
   - 传输失败时保留安全恢复能力
   - (对应 PR #119942)
2. **更可靠的长时交付**: agent/gateway/retry/channel 路径处理:
   - 取消、重试、部分发送、进程流失败
   - 不丢失工作、不重放不安全操作
   - (同样 PR #119942)

**核心关注点**: 本版本重心在 **安全加固 + 交付可靠性**。

---

## 🧰 ClawHub 新技能发现 (网站已迁移至 clawhub.ai)

ClawHub 域名已跳转到 **clawhub.ai**。

**本次发现的热门/新技能**:
| 技能 | 作者 | 用途 |
|------|------|------|
| planning-with-files | othmanadi | 基于文件的多步骤规划 (342⭐) |
| design-mobile-apps | designed-by-ai | 用 Sleek 设计移动应用 |
| TikTok Scraper | apidojo-io | 快速抓取 TikTok (243⭐) |
| Remotion Best Practices | am-will | React 视频创作最佳实践 |
| image-to-video | genmedia-labs | 图片转视频 (RunComfy) |
| Wisdom & Accountability Coach | mikecourt | 长期记忆+哲学教学 |
| reddit-automation | flowkit-labs | Reddit 自动化 |
| x-scraper | apidojo-io | 抓取推文 (241⭐) |
| ClawCall | clawcall-dev | AI 打美国电话 |
| video-edit | genmedia-labs | 视频编辑 (RunComfy) |
| Homeassistant Skill | anotb | 控制 Home Assistant (229⭐) |
| find-skills | vercel-labs | 发现安装技能 |
| AI Usage Ledger | completetech | 统计 AI 使用成本 |
| Muse | alexander-morris | 连接团队编码历史 |
| grill-me | mattpocock | 调用 Skill 工具"grilling" |
| N8n Monitor | smitti7971 | 监控 n8n 工作流 |

**值得关注趋势**: 视频处理 (image-to-video/video-edit)、数据抓取 (TikTok/x-scraper)、电话能力 (ClawCall)、Home 自动化 成为热门方向。

---

## 📄 Docs 状态

docs.openclaw.ai 主页无结构性大变化，仍强调:
- 开源、自托管、One Gateway
- 由 OpenClaw Foundation (独立 501(c)(3)) 开发
- 无付费层级、默认无遥测

---

## ✅ 结论

- **有新内容**: 确认发布 2026.6.35 LTS (安全+可靠性强化)
- **平台变更**: ClawHub 域名迁移至 clawhub.ai
- **技能生态活跃**: 视频 + 抓取 + 电话 + 自动化 是当前热门方向
