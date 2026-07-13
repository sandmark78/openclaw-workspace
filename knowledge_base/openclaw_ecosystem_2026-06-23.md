# OpenClaw 生态探索记录 — 2026-06-23

**探索时间**: 2026-06-23 20:00 UTC
**触发**: 定时任务 🌐 生态探索

---

## 📦 版本动态

| 项目 | 版本 | 备注 |
|------|------|------|
| 当前安装 | `2026.3.8` | 容器内 `openclaw --version` |
| 最新 Release | `v2026.6.10-beta.2` | 2026-06-22 发布，昨天 |
| 上次扫描 | `v2026.6.8` | 2026-06-16 |
| 差距 | **3 个月+ / ~3 个版本** | ⚠️ 持续建议升级 |

---

## 🆕 v2026.6.10-beta.2 核心更新 (2026-06-22, Pre-release)

### 1. 🚀 对话自动 Fast Mode（新功能）
- **自动 Fast Mode**: OpenClaw 现在能自动为短对话回合启用 fast mode，长对话自动回正常模式
- 带有限制的 fallback 和交付行为
- Fast-mode 状态能在重试、fallback 转换、进度事件、嵌入/CLI/ACP 规范化中存活
- **影响**: 短回复更快，成本更低；对心跳类任务有好处

### 2. 🔄 模型路由更可靠
- **Zai 模型合成**: 提供更准确的 Zai base URL
- **GLM 过载故障转移**: 过载分类使用正确的运行时元数据
- **原生推理级选择**: 遵循活跃模型目录更一致
- 相关 PR: #94461, #93241, #94067, #94136
- **影响**: 我们用的百炼/bailian 提供商可能间接受益

### 3. 🛡️ 会话与通道状态更安全
- **通道切换时重置陈旧的 origin 字段**: 防止状态泄漏
- **Cron 交付感知**: 保持附着到目标会话
- 陈旧通道 origin 状态不再跨会话变更泄漏
- 相关 PR: #95328, #93580
- **影响**: 多通道环境下更稳定

### 4. 🔐 Hook 组合下策略保持
- 组合 Hook 注册表保留授信工具策略
- 审批敏感流程不再丢失策略
- PR: #94545

### 5. 🔧 其他修复
- Fallback 截止和重置通知有界化
- 重复进度事件保持可见
- Codex 服务级状态规范化
- Zai/GLM 故障转移路径使用正确的运行时元数据

---

## 🌐 ClawHub 动态

- 域名 `clawhub.com` → `clawhub.ai`（延续上次发现）
- 热门技能排行变化不大，Top 技能：
  - `self-improving-agent` (pskoett, 3.8k installs)
  - `skill-vetter` (spclaudehome, 1.2k)
  - `self-improving` (ivangdavila, 1.2k)
  - `github` (steipete, 640)
  - `ontology` (oswalpalash, 643)
  - `gog` (steipete, 929 - Google Workspace)
  - `proactive-agent` (halthelobster, 808)
  - `weather` (steipete, 419)
  - `tavily-search` (jacky1n7, 264 - 中文版)
  - `auto-updater` (maximeprades, 433)
- 新增/值得注意:
  - **SkillScan** (tokauthai, 381): 技能安全门禁 — "每个新技能必须通过 SkillScan"
  - **Multi Search Engine** (gpyangyoujun, 735): 16 引擎集成（7 中国 + 9 全球）
  - **Agent Browser** (matrixy): Agent 专用无头浏览器 CLI
  - **AdMapix** (fly0pants): 广告创意数据层
  - **PollyReach** (pollyreach): 给 AI Agent 分配电话号码

---

## 📚 docs.openclaw.ai

- 文档结构稳定，无重大变更
- 快速入门流程不变: `npm install -g openclaw@latest` → `openclaw onboard --install-daemon`
- 要求: Node 24 (推荐) 或 Node 22 LTS (22.19+)
- 强调: "使用最强最新一代模型以获得最佳质量和安全"

---

## 📊 与我们相关的变化

| 变化 | 对我们的影响 | 优先级 |
|------|-------------|--------|
| Fast Mode 自动切换 | 短回复更快更省钱 | ⭐⭐ |
| 模型路由改进 | bailian 提供商可能间接受益 | ⭐ |
| 通道状态安全修复 | 多通道更稳定（目前只用 Telegram） | ⭐ |
| SkillScan 新技能 | 技能安全审核新思路 | ⭐⭐ |
| 版本差距 3 个月 | 建议考虑升级 | ⭐⭐⭐ |

---

*自动生成，下次探索: 2026-06-25 左右*
