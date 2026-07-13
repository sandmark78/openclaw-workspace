# OpenClaw 生态监控记录

**最后更新**: 2026-06-19 20:00 UTC
**监控范围**: ClawHub、docs.openclaw.ai、GitHub Releases

---

## ClawHub 平台数据
- 域名：clawhub.com → 重定向到 clawhub.ai
- 52.7k 工具 | 180k 用户 | 12M 下载 | 4.8 平均评分
- 三大板块：Skills（技能包）、Plugins（网关插件）、Publishers（构建者/组织）

## Docs 更新
- docs.openclaw.ai 正常访问，内容无明显变更
- 标准文档首页，覆盖 Get Started / Onboarding / Control UI

## GitHub Releases — 🆕 Pre-release (2026-05-17 17:59 UTC)

### 新技能 (Skills)
| 技能 | 说明 |
|------|------|
| **meme-maker** | 模板搜索 + 本地 SVG/PNG 渲染 + Imgflip 托管 + Know Your Meme 来源链接 |
| **node inspector debugging** | Node.js 调试、融合图表生成、一次性 spike 工作流 |
| **python-debugging** | pdb、breakpoint()、事后检查、debugpy 远程附加 |
| **autoreview** | Codex closeout review 重命名为 autoreview，保留 Codex-first fallback |
| **Obsidian 更新** | 改用官方 obsidian CLI，要求注册的二进制文件 |

### CLI/插件系统
- **defineToolPlugin** — 新增 typed simple tool plugins 支持
- `openclaw plugins build/validate/init` — 插件构建工具链
- 生成 manifest metadata + 可选 tool declarations + context factories

### 代理/工具优化
- 缩短内置工具描述和 schema hints（media/messaging/sessions/cron/Gateway/web/image/PDF/TTS/nodes/plan）
- 保留路由护栏
- 收紧 bundled skill prompts 和 metadata
- 更新嵌入式 sherpa-onnx runtime 下载

### 消息渲染
- 通道渲染器新增 presentation capability limits
- 原生渲染前自适应 rich message 控制
- 标记 legacy interactive/Slack directive producer API 为 deprecated

### 网络/代理
- HTTPS 托管 forward-proxy 端点支持
- scoped proxy.tls.caFile CA 信任配置 ([#79171](https://github.com/openclaw/openclaw/pull/79171))

### QA-Lab 大量更新
- first-hour 20-turn + 100-turn 运行时奇偶校验场景
- `openclaw qa suite --runtime-parity-tier` — Codex-vs-Pi 标准层
- live-only Codex Pi-shaped Read 词汇 canary
- 插件 hook 崩溃 / manifest 合约错误 / WebChat 路由自健康场景
- runtime tool fixture 场景 + 覆盖率报告
- `openclaw qa coverage --tools` — 覆盖率暴露
- personal-agent approval-denial 场景

### 修复
- CLI/update: 按平台定制 Gateway 恢复提示 (systemd/LaunchAgent/Scheduled Task)
- 插件 before_agent_start hooks 默认 15s 超时，防止挂起阻塞

### Mac App
- Settings 页面重新设计：一致的卡片布局、缓存导航、更清晰的权限/语音/技能/cron/exec/debug 面板

---

## 值得关注的变化
1. **meme-maker 技能** — 有趣但对我们用处不大
2. **defineToolPlugin** — 可能对我们开发自定义插件有用
3. **Python debugging skill** — 如果我们要做 Python 项目会有帮助
4. **QA-Lab 大幅扩展** — 说明 OpenClaw 在大力提升稳定性和兼容性
5. **HTTPS 代理支持** — 企业部署友好

---

## 🔴 2026-06-19 重大发现：版本落后！

### 版本差距
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | `2026.3.8` | 旧版 |
| NPM 最新稳定版 | `2026.6.8` | 2026-06-16 |
| GitHub 最新 beta | `v2026.6.9-beta.1` | 2026-06-19 (今天!) |

**我们落后 3 个小版本！**

### v2026.6.9-beta.1 亮点（今天发布）

- **🎉 Telegram 富文本大幅增强**：发送富 HTML、保留 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及走正确投递路径
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布，Gateway 启动时自动发现 channel 插件
- **更有能力的 Web/原生客户端**：Control UI 会话工作区轨道、iOS Watch 控制、Android 聊天上下文
- **更有用的搜索和技能**：Codex Hosted Search 可用、免密钥搜索保持 opt-in、ClawHub 技能保留来源出处

### v2026.6.8 稳定版亮点（3 天前）

- **更丰富的频道投递**：Telegram 渲染结构化文本（表格、列表、可展开引用块、保留换行、CLI 支持的回复）；WhatsApp 遵守 ACP 绑定
- **更可靠的 Agent 运行**：账户范围 DM、生成媒体完成、自动回复最终回复、子 Agent 暂停
- **更安全的模型路由**：GLM-5.2 和 Claude Haiku 4.5 支持、规范化 provider ID
- **用量页脚改进**：`/usage` 原生完整页脚渲染器、固定小数格式化
- **弹性内存和状态**：OpenAI 嵌入批次拆分、SQLite 避免 NFS WAL、完整重索引保留回滚

### 建议
1. 建议考虑升级到 2026.6.8 稳定版
2. 2026.6.9-beta.1 是 beta 版，建议观望几天等正式版
3. 升级前务必备份 `openclaw.json`

---

## 🔴 2026-06-19 重大更新发现

### 版本差距
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | 2026.3.8 | — |
| NPM 最新稳定版 | 2026.6.8 | 2026-06-16 |
| GitHub 最新 beta | v2026.6.9-beta.1 | 2026-06-19 (今天!) |

### v2026.6.9-beta.1（今天发布）亮点

- **🎉 Telegram 富文本增强**：发送富 HTML、保留富 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及和 spooled handlers 走正确投递路径
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布，Gateway 启动时自动发现 channel 插件
- **更有能力的 Web/原生客户端**：Control UI 新增会话工作区轨道、iOS Watch 控制、Android 聊天上下文
- **更有用的搜索和技能**：Codex Hosted Search 可用、免密钥搜索保持 opt-in、ClawHub 技能保留已验证来源出处

### v2026.6.8 稳定版（3 天前发布）亮点

- **更丰富的频道投递**：Telegram 渲染结构化文本（表格、列表、可展开引用块、保留换行），WhatsApp 遵守 ACP 绑定
- **更可靠的 Agent 运行**：账户范围 DM、生成媒体完成、自动回复最终回复、子 Agent 暂停
- **更安全的模型路由**：GLM-5.2 和 Claude Haiku 4.5 支持、规范化 provider ID、SecretRef 认证
- **用量页脚改进**：`/usage` 原生渲染器、固定小数格式化
- **弹性内存和状态**：OpenAI 嵌入批次拆分、SQLite 避免 NFS WAL、完整重索引保留回滚

### 建议
1. 当前版本落后 3 个次版本，建议考虑升级到 2026.6.8 稳定版
2. 2026.6.9-beta.1 是 beta 版，可观望几天再决定是否升级
3. Telegram 富文本增强与我们直接相关！

---

## 🔴 2026-06-19 重大发现：版本落后 3 个小版本！

### 当前版本状态
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | `2026.3.8` | 旧版本 |
| NPM 最新稳定版 | `2026.6.8` | 2026-06-16 |
| GitHub 最新 beta | `2026.6.9-beta.1` | 2026-06-19 (今天!) |

### v2026.6.9-beta.1（今天发布）亮点

- **🎉 Telegram 富文本大幅增强**：发送富 HTML、保留 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及走正确投递路径
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布
- **Web/原生客户端增强**：Control UI 新增会话工作区轨道、iOS Watch 控制、Android 聊天上下文
- **搜索改进**：Codex Hosted Search 可用、免密钥搜索保持 opt-in

### v2026.6.8 稳定版（3 天前发布）亮点

- **更丰富的频道投递**：Telegram 结构化文本（表格、列表、可展开引用块、保留换行、CLI 支持的回复）；WhatsApp 遵守 ACP 绑定
- **更可靠的 Agent 运行**：账户范围 DM 发送、生成媒体完成、自动回复最终回复、子 Agent 暂停
- **更安全的模型路由**：GLM-5.2 和 Claude Haiku 4.5 目录、规范化 provider ID、SecretRef 认证管理
- **用量页脚改进**：`/usage` 原生完整页脚渲染器、固定小数格式化
- **可预测的 Web 搜索默认值**：免密钥搜索保持显式 opt-in 而非自动回退
- **更平静的 UI 和移动会话**：工作区文件默认折叠、WebChat 回滚存活、iOS 重连
- **弹性内存和状态**：OpenAI 嵌入批次拆分、SQLite 避免 NFS WAL、完整重索引保留回滚

---

## 🔴 2026-06-19 重大发现：版本落后 3 个小版本！

### 版本对比
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | 2026.3.8 | — |
| NPM 最新稳定版 | 2026.6.8 | 2026-06-16 |
| GitHub 最新 beta | 2026.6.9-beta.1 | 2026-06-19 (今天!) |

### v2026.6.9-beta.1 亮点（今天发布）
- **🎉 Telegram 富文本大幅增强**：发送富 HTML、保留 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及走正确投递路径
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布
- **Web/原生客户端增强**：Control UI 新增会话工作区轨道、iOS Watch 控制、Android 聊天上下文
- **搜索/技能改进**：Codex Hosted Search 可用、免密钥搜索保持 opt-in

### v2026.6.8 稳定版亮点（3 天前发布）
- **更丰富的频道投递**：Telegram 渲染结构化文本（表格、列表、可展开引用块、保留换行、CLI 回复）
- **更可靠的 Agent 运行**：账户范围 DM 发送、生成媒体完成、自动回复最终回复
- **新模型支持**：GLM-5.2、Claude Haiku 4.5、规范化 provider ID
- **用量页脚**：/usage 原生渲染器、固定小数格式化
- **内存/状态弹性**：OpenAI 嵌入批次拆分、SQLite 避免 NFS WAL

---

## 🔴 2026-06-19 重大发现：版本落后！

### 当前版本 vs 最新版
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | `2026.3.8` | — |
| NPM 最新稳定版 | `2026.6.8` | 2026-06-16 |
| GitHub 最新 beta | `2026.6.9-beta.1` | 2026-06-19 (今天!) |

**我们落后 3 个小版本！**

### v2026.6.9-beta.1 亮点（今天发布）

- **🎉 Telegram 富文本大幅增强**：发送富 HTML、保留 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及走正确投递路径
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布
- **Web/原生客户端增强**：Control UI 新增会话工作区轨道、iOS Watch 控制、Android 聊天上下文
- **搜索和技能改进**：Codex Hosted Search 可用、免密钥搜索保持 opt-in、ClawHub 技能保留来源

### v2026.6.8 稳定版亮点（3 天前发布）

- **更丰富的频道投递**：Telegram 渲染结构化文本（表格、列表、可展开引用块、保留换行）
- **更可靠的 Agent 运行**：账户范围 DM、自动回复最终回复、子 Agent 暂停
- **新模型支持**：GLM-5.2、Claude Haiku 4.5、规范化 provider ID
- **用量页脚**：`/usage` 原生渲染器、固定小数格式化
- **内存/状态弹性**：OpenAI 嵌入批次拆分、SQLite 避免 NFS WAL

---

## 🔴 2026-06-19 重大发现：版本落后 3 个次版本！

### 版本差距
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | 2026.3.8 | — |
| NPM 最新稳定版 | 2026.6.8 | 2026-06-16 |
| GitHub 最新 beta | 2026.6.9-beta.1 | 2026-06-19 (今天!) |

### v2026.6.9-beta.1 亮点 (今天发布)

- **🎉 Telegram 富文本大幅增强**：Telegram 现在发送富 HTML、保留富 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及和 spooled handlers 走正确投递路径（我们正用 Telegram！）
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布，Gateway 启动时自动发现 channel 插件
- **更有能力的 Web/原生客户端**：Control UI 新增会话工作区轨道、iOS Watch 控制、Android 显示聊天上下文
- **更有用的搜索和技能**：Codex Hosted Search 可用、ClawHub 技能保留已验证来源

### v2026.6.8 稳定版亮点 (3 天前发布)

- **更丰富的频道投递**：Telegram 渲染结构化文本（表格、列表、可展开引用块、保留换行、CLI 支持的回复），WhatsApp 遵守 ACP 绑定
- **更可靠的 Agent 运行**：账户范围 DM 发送、生成媒体完成、自动回复最终回复、子 Agent 暂停
- **更安全的模型路由**：GLM-5.2 和 Claude Haiku 4.5 支持、规范化 provider ID、SecretRef 认证管理
- **用量页脚改进**：/usage 原生完整页脚渲染器、固定小数格式化
- **可预测的 Web 搜索默认值**：免密钥搜索保持 opt-in 而非自动回退
- **弹性内存和状态**：超大 OpenAI 嵌入批次拆分、SQLite 避免 NFS 卷 WAL、完整重索引保留回滚

### 建议
1. **建议升级到 2026.6.8 稳定版**，获得 Telegram 富文本和 Agent 恢复改进
2. 2026.6.9-beta.1 是 beta 版，可观望几天等稳定
3. 升级前务必备份 openclaw.json

---

## 🔴 2026-06-19 重大更新发现

### 版本差距
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | 2026.3.8 | 落后! |
| NPM 最新稳定版 | 2026.6.8 | 2026-06-16 |
| GitHub 最新 beta | 2026.6.9-beta.1 | 2026-06-19 (今天!) |

### v2026.6.9-beta.1 (今天发布) 亮点
- **Telegram 富文本大幅增强**：发送富 HTML、保留富 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及和 spooled handlers 走正确投递路径
- **Agent 恢复更可靠**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **Codex 集成更强**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布
- **Web/原生客户端增强**：Control UI 会话工作区轨道、iOS Watch 控制、Android 聊天上下文
- **搜索/技能改进**：Codex Hosted Search 可用、ClawHub 技能保留来源出处

### v2026.6.8 (3 天前稳定版) 亮点
- **Telegram/WhatsApp 投递增强**：结构化文本（表格、列表、可展开引用块）、保留换行、CLI 回复
- **Agent 运行更可靠**：账户级 DM 发送、媒体完成、自动回复、子 Agent 暂停
- **新模型支持**：GLM-5.2、Claude Haiku 4.5
- **用量页脚改进**：/usage 原生渲染、固定小数格式化
- **内存/状态弹性**：OpenAI 嵌入批次拆分、SQLite NFS 修复、完整重索引保留回滚

---

## 🔴 2026-06-19：重大发现 — 版本落后 3 个次版本！

### 版本差距
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | `2026.3.8` | — |
| NPM 最新稳定版 | `2026.6.8` | 2026-06-16 |
| GitHub 最新 beta | `2026.6.9-beta.1` | 2026-06-19 (今天!) |

### v2026.6.9-beta.1 (今天发布)

**🎉 与我们直接相关：**
- **Telegram 富文本大幅增强**：发送富 HTML、保留富 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及和 spooled handlers 走正确投递路径

**其他重要变化：**
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布
- **Web/原生客户端增强**：Control UI 新增会话工作区轨道、iOS Watch 控制、Android 显示聊天上下文
- **搜索改进**：Codex Hosted Search 可用、免密钥搜索保持 opt-in

### v2026.6.8 稳定版 (3 天前)

- **更丰富的频道投递**：Telegram 结构化文本（表格、列表、可展开引用块、保留换行）
- **新模型支持**：GLM-5.2、Claude Haiku 4.5
- **用量页脚改进**：`/usage` 原生渲染器
- **内存/状态弹性**：OpenAI 嵌入批次拆分、SQLite 避免 NFS WAL
- **更可靠的 Agent 运行**：账户范围 DM 发送、自动回复最终回复、子 Agent 暂停

### 建议
1. 考虑升级到 `2026.6.8` 稳定版（获取 Telegram 富文本、Agent 恢复等新功能）
2. `2026.6.9-beta.1` 是 beta 版，建议观望几天等稳定
3. 升级前备份 openclaw.json

---

## 🔴 2026-06-19 重大发现：版本落后！

### 版本差距
| 来源 | 版本 | 日期 |
|------|------|------|
| **当前运行** | `2026.3.8` | 旧版本 |
| NPM 最新稳定版 | `2026.6.8` | 2026-06-16 |
| GitHub 最新 beta | `2026.6.9-beta.1` | 2026-06-19 (今天!) |

**落后 3 个次版本！**

### v2026.6.9-beta.1 亮点 (今天刚发布)

- **🎉 Telegram 富文本大幅增强**：发送富 HTML、保留富 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及和 spooled handlers 走正确投递路径（7 个 PR 合入）
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布，Gateway 启动时自动发现已安装 channel 插件
- **Web/原生客户端增强**：Control UI 新增会话工作区轨道、iOS Watch 控制、Android 显示聊天上下文
- **搜索和技能改进**：Codex Hosted Search 可用、免密钥搜索保持 opt-in、ClawHub 技能保留来源出处

### v2026.6.8 稳定版 (3 天前)

- **更丰富的频道投递**：Telegram 结构化文本（表格、列表、可展开引用块、保留换行）、CLI 支持的回复；WhatsApp 遵守 ACP 绑定
- **更可靠的 Agent 运行**：账户范围 DM 发送、自动回复最终回复、子 Agent 暂停
- **新模型支持**：GLM-5.2、Claude Haiku 4.5，规范化 provider ID
- **用量页脚改进**：`/usage` 原生渲染器、固定小数格式化
- **内存/状态弹性**：OpenAI 嵌入批次拆分、SQLite 避免 NFS WAL

### 📋 建议
1. **考虑升级到 2026.6.8 稳定版** — 获取 Telegram 富文本等核心改进
2. **2026.6.9-beta.1 是 beta** — 建议观望几天等正式版
3. 升级前务必备份 `openclaw.json`

---

## 🔴 2026-06-19 重大发现：版本落后 3 个次版本！

### 当前版本状态
| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | 2026.3.8 | 旧版本 |
| NPM 最新稳定版 | 2026.6.8 | 2026-06-16 |
| GitHub 最新 beta | 2026.6.9-beta.1 | 2026-06-19 (今天!) |

### v2026.6.9-beta.1 亮点 (今天发布)

**🎉 与我们直接相关：**
- **Telegram 富文本大幅增强**：发送富 HTML、保留富 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及和 spooled handlers 走正确投递路径 (#93286, #93164, #93124, #93364, #93130, #93088, #93281)

**其他亮点：**
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布，Gateway 启动时自动发现已安装 channel 插件
- **更有用的搜索和技能**：Codex Hosted Search 可用，ClawHub 技能保留已验证来源出处
- **Web/原生客户端增强**：Control UI 会话工作区轨道、iOS Watch 控制、Android 聊天上下文

### v2026.6.8 稳定版亮点 (3 天前发布)

- ** richer channel 投递**：Telegram 渲染结构化文本（表格、列表、可展开引用块、保留换行、CLI 支持的回复）
- **更可靠的 Agent 运行**：账户范围 DM 发送、生成媒体完成、自动回复最终回复、子 Agent 暂停
- **更安全的模型路由**：GLM-5.2 和 Claude Haiku 4.5 支持、规范化 provider ID、SecretRef 认证
- **用量页脚**：`/usage` 原生渲染器、固定小数格式化
- **Web 搜索默认值**：免密钥搜索保持 opt-in 而非自动回退
- **内存和状态弹性**：OpenAI 嵌入批次拆分、SQLite 避免 NFS WAL、完整重索引保留回滚

### 建议
1. **考虑升级到 2026.6.8 稳定版** — 获得 Telegram 富文本、更可靠 Agent 恢复等新功能
2. **2026.6.9-beta.1 是 beta** — 建议等正式版再升级
3. 升级前注意备份 openclaw.json 配置

---

## 🔴 2026-06-19 重大更新发现

### 版本差距

| 位置 | 版本 | 日期 |
|------|------|------|
| **当前运行** | `2026.3.8` | 旧版本 |
| NPM 最新稳定版 | `2026.6.8` | 2026-06-16 |
| GitHub 最新 beta | `2026.6.9-beta.1` | 2026-06-19 (今天!) |

**我们落后 3 个小版本！**

### v2026.6.9-beta.1 亮点 (今天发布)

- **Telegram 富文本大幅增强** 🎉 — 发送富 HTML、保留富 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及和 spooled 处理走正确的投递路径
- **Agent 恢复更可靠** — 重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation，让中断的回合能走到可见的最终结果
- **Codex 集成更强** — 自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 `exec` 作为动态工具、更可靠的应用服务器拆卸
- **独立官方 Provider 插件** — 外部 provider 包作为独立 npm 包发布，Gateway 启动时自动发现已安装的 channel 插件，StepFun 仅限 npm 安装
- **Web/原生客户端增强** — Control UI 新增会话工作区轨道和扩展健康状态、iOS 新增 Watch 控制、Android 显示聊天上下文
- **搜索和技能** — Codex Hosted Search 可用、免密钥搜索保持 opt-in、ClawHub 技能保留已验证来源出处

### v2026.6.8 稳定版 (3 天前发布)

- **Telegram/WhatsApp 投递增强** — 结构化文本（表格、列表、可展开引用块）、保留 intentional 换行、CLI 支持的回复
- **Agent 运行更可靠** — 账户级 DM 发送、生成媒体完成、自动回复最终回复、子 Agent 暂停
- **新模型支持** — GLM-5.2、Claude Haiku 4.5 目录，规范化 provider ID，SecretRef 认证管理
- **用量页脚改进** — `/usage` 原生渲染器、固定小数格式化、凭据感知限制
- **内存/状态弹性** — 超大嵌入批次拆分、SQLite 避免 NFS WAL、完整重索引保留回滚

### ClawHub & Docs
- clawhub.com → clawhub.ai，页面内容无显著变化
- docs.openclaw.ai 正常访问，无明显变更

### 📋 建议
1. **考虑升级到 2026.6.8 稳定版**（或等 2026.6.9 正式版）
2. **Telegram 富文本增强** 对我们直接有用（当前用的就是 Telegram 通道）
3. **Agent 恢复改进** 可能减少中断/卡死问题

---

## 🆕 2026-06-19 检查：有重大更新！

### 版本差距
| 来源 | 版本 | 发布日期 |
|------|------|----------|
| **当前运行** | 2026.3.8 | — |
| NPM 最新稳定版 | 2026.6.8 | 2026-06-16 |
| GitHub 最新 beta | 2026.6.9-beta.1 | 2026-06-19 (今天!) |

**⚠️ 我们落后 3 个次版本！**

### v2026.6.9-beta.1 亮点 (今天发布)
- **Telegram 富文本大幅增强**：发送富 HTML、保留富 Markdown 和贴纸路径、更忠实地渲染进度草稿和命令输出、@提及和 spooled 处理更可靠（7 个 PR 合入）
- **Agent 恢复更可靠**：重试、终端结果、压缩后用量、会话历史修复、回复 reconciliation
- **Codex 集成更强**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具
- **独立官方 Provider 插件**：外部 provider 包作为独立 npm 发布
- **Web/原生客户端增强**：Control UI 新增会话工作区轨道、iOS Watch 控制、Android 聊天上下文
- **搜索和技能**：Codex Hosted Search、免密钥搜索 opt-in、ClawHub 技能保留来源出处

### v2026.6.8 稳定版亮点 (3 天前发布)
- **Telegram/WhatsApp 投递增强**：结构化文本（表格、列表、可展开引用块）、保留换行、CLI 回复
- **Agent 运行更可靠**：账户范围 DM、媒体完成、自动回复、子 Agent 暂停
- **新模型支持**：GLM-5.2、Claude Haiku 4.5
- **用量页脚改进**：/usage 原生渲染、固定小数、凭据感知限制
- **内存和状态弹性**：嵌入批次拆分、SQLite NFS 修复、完整重索引回滚

### 📋 建议
1. **考虑升级到 2026.6.8 稳定版** — 特别是 Telegram 富文本增强，对咱们的 Telegram 通道直接受益
2. **2026.6.9-beta.1 刚出 beta** — 观望几天再考虑

### ClawHub 和 Docs
- clawhub.com → clawhub.ai 无变化
- docs.openclaw.ai 无显著变更

---

## 🆕 2026-06-19 检查：有重大更新！

### 版本差距
| 位置 | 版本 | 日期 |
|------|------|------|
| **我们当前运行** | 2026.3.8 | — |
| NPM 最新稳定版 | 2026.6.8 | 2026-06-16 |
| GitHub 最新 (beta) | v2026.6.9-beta.1 | 2026-06-19 (今天!) |

**差距：3 个次版本！建议尽快升级。**

---

### v2026.6.9-beta.1 (2026-06-19 发布)

#### 亮点
- **Telegram 富文本增强** 🎉：Telegram 现在发送富 HTML，保留富 Markdown 和贴纸路径，更忠实地渲染进度草稿和命令输出，保持 @提及 和 spooled 处理程序在正确的投递路径上
- **更可靠的 Agent 恢复**：重试、终端结果、压缩后用量跟踪、会话历史修复、回复 reconciliation，让中断的回合能继续到可见的最终结果
- **更强的 Codex 集成**：自动插件审批、GPT-5.3 Spark OAuth 路由、远程节点 exec 作为动态工具、更可靠的应用服务器拆卸和终端结果
- **独立官方 Provider 插件**：外部 provider 包现在是独立 npm 发布，外部安装的 channel 插件在 Gateway 启动时加载，StepFun 仅限 npm 安装
- **更有能力的 Web 和原生客户端**：Control UI 新增会话工作区轨道和扩展健康状态，iOS 新增 Watch 控制，Android 显示聊天上下文
- **更有用的搜索和技能**：Codex Hosted Search 可用，免密钥搜索提供商保持为 deliberate opt-ins，ClawHub 技能安装保留已验证来源出处

#### 变更
- 新增 Codex Hosted Search，改进 Gemini CLI OAuth 代理支持
- 外部化的官方 provider 作为独立 npm 包发布
- 会话工作区轨道、插件健康状态、紧凑 cron 列表、iOS Watch 控制
- 自动插件审批、保留 ClawHub 技能来源、暴露远程节点执行给 Codex

---

### v2026.6.8 (2026-06-16 稳定版)

#### 亮点
- **更丰富的频道投递**：Telegram 渲染结构化文本（表格、列表、可展开引用块、保留换行、CLI 支持的回复），WhatsApp 现在遵守配置的 ACP 绑定
- **更可靠的 Agent 运行**：账户范围的 DM 发送、生成媒体完成、自动回复消息工具最终回复、重置归档回退读取、重启关机中止、生成的子 Agent 暂停、会话身份提示
- **更安全的模型路由**：新增 GLM-5.2 和 Claude Haiku 4.5 目录支持，规范化 provider ID，管理的 SecretRef 认证，有界模型浏览，更安全的 OpenAI/Anthropic 工具 schema 恢复
- **有用的用量页脚**：`/usage` 和回复 payload 挂钩现在原生完整页脚渲染器，固定小数格式化，凭据感知限制
- **可预测的 Web 搜索默认值**：免密钥提供商 (Parallel Free、DuckDuckGo、Ollama、Codex Hosted Search) 保持显式 opt-in
- **更平静的 UI 和移动会话**：工作区文件默认折叠，WebChat 回滚流式传输保持，桌面会话选择器保持交互，iOS 重新连接过期前台 Gateway
- **弹性内存和状态**：超大 OpenAI 嵌入批次在 431s 前拆分，QMD 搜索在瞬态模式可用，SQLite 避免 NFS 卷上的 WAL，完整重索引保留回滚/缓存恢复

#### 变更
- 新增 GLM-5.2 支持、Claude Haiku 4.5 目录条目
- Mac App Settings 页面优化
- 多 Agent 和子 Agent 稳定性修复

---

## 建议
1. **升级到 2026.6.8 稳定版** — 获得 Telegram 富文本、GLM-5.2/Claude Haiku 4.5 支持、更好的 Agent 恢复
2. **关注 2026.6.9-beta.1** — 今天刚发布的 beta，等稳定后可升级
3. **Telegram 富文本增强** 与我们直接相关！升级后 Telegram 消息质量会显著提升
