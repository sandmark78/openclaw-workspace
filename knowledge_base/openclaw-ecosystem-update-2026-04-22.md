# OpenClaw 生态探索 - 2026-04-22

**抓取时间**: 2026-04-22 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, GitHub releases

---

## 1. ClawHub (clawhub.com → clawhub.ai)

- 域名重定向持续有效
- 最新数据：**52.7k tools / 180k users / 12M downloads / 4.8 avg rating**
- 定位不变：社区驱动的 AI Agent 技能市场

---

## 2. docs.openclaw.ai

- 文档站点正常运行
- 核心定位不变：自托管 AI Agent 网关，多通道支持
- 无显著结构性变化

---

## 3. GitHub Releases - ⚠️ 两个新 Release (4/20 + 4/21)

### Release 2026.4.21 (4月21日发布)

**变更：**
- **OpenAI/images**: 默认图像生成 provider 改为 `gpt-image-2`，支持 2K/4K 尺寸提示
- **Image generation**: 图像生成失败时在回退前记录 warn 级别日志，方便排查

**修复：**
- **Plugins/doctor**: 修复 doctor 路径下捆绑插件运行时依赖问题
- **Auth/commands**: 🔒 安全修复 — 严格 owner 身份验证，防止非 owner 通过宽松回退访问 owner 专属命令（#69774）
- **Slack**: 保留线程别名，确保发送消息留在正确的 Slack 线程（#62947）
- **Browser**: 立即拒绝无效的 ax 无障碍引用，不再等待超时（#69924）
- **npm/install**: 修复 node-domexception 别名链，避免废弃依赖被拉入

### Release 2026.4.20 (4月20日发布)

**变更：**
- **Onboard/wizard**: 🎨 重新设计安全免责声明 — 黄色警告横幅、分区标题、加载旋转器、API key 占位符（#69553）
- **Agents/prompts**: 强化默认系统提示和 GPT-5 覆盖层，增加完成偏差检查、弱结果恢复、验证后最终输出指导
- **Models/costs**: 支持分层模型定价，新增 Moonshot Kimi K2.6/K2.5 成本估算（#67605）
- **Moonshot/Kimi**: 默认捆绑 Kimi K2.6，保留 K2.5 兼容（#69477）
- **Cron**: 🔧 运行状态拆分到 `jobs-state.json`，保持 `jobs.json` 稳定用于 git 追踪（#63105）
- **Agents/compaction**: 上下文压缩期间发送开始/完成通知（#67830）
- **Plugins/tests**: 复用插件 loader 别名和 Jiti 配置解析，减少重复加载开销（#69316）

**修复：**
- **Sessions/Maintenance**: 默认强制执行 entry cap 和 age prune，加载时修剪超大存储，防止 OOM（#69404）

---

## 对比上次检查 (2026-04-11)

| 项目 | 变化 |
|------|------|
| ClawHub 数据 | 52.7k tools, 180k users, 12M downloads |
| GitHub Release | 新增 2 个 release（4/20 + 4/21） |
| 文档站点 | 无显著变化 |
| 关注点 | 安全修复(owner命令)、OOM防护、Cron状态分离、Kimi K2.6 默认化 |

---

## 与我们相关的重点

1. 🔒 **Owner 命令安全修复** — 严格身份验证，防止权限绕过
2. 💥 **OOM 防护** — session 存储自动修剪，减少网关崩溃风险
3. 🔧 **Cron jobs-state.json** — 运行状态与配置分离，更利于 git 管理
4. 🖼️ **gpt-image-2 默认化** — 如果后续需要图像生成，成本/质量可能变化
5. 🤖 **系统提示强化** — GPT-5 覆盖层改善默认行为

---

*生态探索记录 - 2026-04-22*
