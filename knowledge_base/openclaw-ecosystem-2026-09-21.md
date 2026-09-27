# OpenClaw 生态探索 - 2026-09-21

## 📦 OpenClaw 版本
| 项目 | 当前 | 最新 | 状态 |
|------|------|------|------|
| OpenClaw | 2026.7.1 | **2026.9.4** (v2026.9.4) | ❌ 落后多版本 |

### 🆕 新发现：GitHub Releases 现已可访问
- 上次(09-15) GitHub releases 页面 404，今日已恢复可访问 ✅
- 顶部显示 **2026.7.35**：extended-stable 维护线的**首个 GitHub Release**
  - 说明 2026.7.33 / 2026.7.34 是不稳定 extended-stable 构建，未发布为 Release
  - 2026.7.35 修复：Doctor 插件注册表（保留完整内置插件清单，浏览器/Canvas/pairing/file-transfer/phone-control/Talk voice/Bonjour 插件重启后保持可用）
  - 从完整 1,418-commit 审计中选出，无其他缺陷需 backport
- **v2026.9.4**：20 直接提交 · 1,558 PR · 294 贡献者（大版本）

## 🦞 ClawHub 域名变更
- `clawhub.com` 现重定向至 **`clawhub.ai`** 🔄

### ClawHub 热门技能 (2026-09-21 抓取)
| 技能 | 下载量 | 说明 |
|------|--------|------|
| Weather (steipete) | 170k | 无需 API key 的天气 |
| Tavily Search (jacky1n7) | 107k | 结构化搜索结果 |
| Word/DOCX (ivangdavila) | 92.9k | Word 文档读写 |
| Excel/XLSX (ivangdavila) | 80.9k | Excel 读写 |
| Find Skills Skill (fangkelvin) | 59.6k | 技能发现 |
| Tavily AI Search (bert-builder) | 47.6k | AI 搜索 |
| Qmd (steipete) | 35.7k | 本地检索 CLI (BM25+向量+rerank, MCP) |
| Gog (steipete) | 195k | Google Workspace CLI |
| Skill Vetter (spclaudehome) | 274k | 安全技能审计 |
| Planning with files | 43.6k | 文件规划 |
| Proactive Agent Lite | 41k | 主动型 Agent |
| Superpowers Dev Workflow | 28k | Spec-first TDD 开发流程 |

⚠️ 注：今日下载量显示口径与上次不同（部分技能 100k+ 级别），可能是排行榜口径/时间窗变化，非真实暴增。

## 💡 值得关注的趋势
1. **Skill Vetter 下载量最高 (274k)**：AI 代理技能安全审计成为生态最热需求
2. **Gog (195k)** Google Workspace CLI 持续强势
3. **steipete 一人多技能霸榜**：Weather/Gog/Qmd，高产作者
4. **ivangdavila 文档处理套件**：Word+DOCX+Excel+XLSX 全覆盖
5. **extended-stable 维护线恢复发布**：2026.7.35 首个 Release，稳定性修复为主

## 📌 行动建议
- 老大本地版本 2026.7.1 落后较多，可在下次维护窗口评估升级到 2026.9.4
- 关注 Skill Vetter 技能（安全审计），与我们的 Auditor 子 Agent 理念契合
