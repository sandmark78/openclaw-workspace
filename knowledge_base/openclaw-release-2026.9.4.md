# OpenClaw v2026.9.4 发布记录

**抓取时间**: 2026-09-12 20:00 UTC  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🆕 v2026.9.4 主要更新

### 1. 失败更新回滚 (#140339)
- 兼容的失败更新后自动恢复
- 保留之前的包并用之前的配置和服务恢复
- schema 和配置检查确认安全后才回滚
- 数据库迁移仍需验证的预更新备份

### 2. 统一插件工作区 (#135839 等多个 PR)
- 在 Control UI 中发现 bundled 和 ClawHub 插件
- 统一安装、设置、管理插件
- 一站式插件管理体验

### 3. 预备云会话 (#143227 等多个 PR)
- 从预备的本地项目或公共 GitHub 仓库启动 Linux 会话
- 在 Control UI 中构建可复用快照
- 会话启动前可预览

### 4. 终端问答 (#143273)
- 键盘驱动选择、自由文本回答、多问题提示
- 支持 Gateway 连接和本地 TUI 会话

### 5. GPT Image 2.5 (#143007 相关)
- 新增 Flare 和 Sunburst 变体
- 通过 OpenAI 或 fal 进行图像生成和编辑
- 不改变现有默认模型

---

## 📊 ClawHub 热门技能 (2026-09-12 快照)

| 技能 | 作者 | 安装量 | 说明 |
|------|------|--------|------|
| ClawCall | clawcall-dev | 1.3k | AI 代理拨打美国电话 |
| Homeassistant | anotb | 501 | 通过 REST API 控制 Home Assistant |
| Cournot | cournot-ai | 268 | 自然语言商业/经济分析 |
| x-scraper | apidojo-io | 234 | Twitter/X 抓取 |
| TikTok Scraper | apidojo-io | 222 | TikTok 数据抓取 |
| google-search | fetcher-sh | 159 | Google 搜索 API 替代 |
| self-improving agent | pskoett | 157 | 持续学习改进 |
| Skill Vetter | spclaudehome | 126 | 安全优先的技能审查 |
| Gog | steipete | 101 | Google Workspace CLI |
| Mode Switch Kit | ccy123abcd | 93 | VPN/代理服务切换 |

---

## 🔍 对我们有用的

1. **统一插件工作区** - 升级后可以直接在 Control UI 管理所有插件
2. **失败回滚** - 升级更安全了
3. **Skill Vetter** - 安装技能前安全审查，值得参考
4. **self-improving agent** (pskoett) - 157 安装，和我们的自我进化方向一致

---

*最后更新: 2026-09-12 20:00 UTC*
