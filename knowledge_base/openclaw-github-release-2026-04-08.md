# OpenClaw GitHub Release 2026.4.8

**发布日期**: 2026-04-08  
**检查时间**: 2026-04-08 20:00 UTC  
**来源**: https://github.com/openclaw/openclaw/releases  
**状态**: ⭐ 今日连续发布两次更新

---

## 🚀 Release 2026.4.8 (2026-04-08 05:59 UTC) — Fixes

### 关键修复

| 修复项 | 描述 |
|--------|------|
| **Telegram/setup** | 通过打包顶级 sidecar 加载 setup 和 secret contracts，避免安装 npm 构建时尝试导入缺失的 dist/extensions/telegram/src/* 文件 |
| **Bundled channels/setup** | 所有绑定频道（BlueBubbles, Feishu, Google Chat, IRC, Matrix, Mattermost, MS Teams, Nextcloud Talk, Slack, Zalo）统一通过顶级 sidecar 加载 secret contracts |
| **Bundled plugins** | 对齐打包插件兼容性元数据到发布版本，确保绑定频道和提供者在 OpenClaw 2026.4.8 上正常加载 |
| **Agents/progress** | 为 OpenAI 系列运行保持 update_plan 可用，同时返回紧凑成功载荷，允许 tools.experimental.planTool=false 选择退出 |
| **Agents/exec** | 保持 /exec 当前默认报告与实际运行时行为对齐，host=auto 会话显示正确的 host-aware 回退策略 |
| **Slack** | 为 Socket Mode WebSocket 连接尊重环境 HTTP(S) 代理设置，包括 NO_PROXY 排除 (#62878) |
| **Slack/actions** | 将已解析的 read token 传入 downloadFile，避免 SecretRef 支持的 bot token 在原始配置重读后失败 (#62097) |
| **Network/fetch** | 信任环境代理模式激活时跳过目标 DNS 固定，让可信代理解析出站主机 (#59007) |

---

## 🔥 Release 2026.4.8 Changes (2026-04-08 02:12 UTC) — Changes

### 重要新功能

| 功能 | 描述 | PR |
|------|------|-----|
| **`openclaw infer` CLI** | 全新一级推理 CLI 中心，跨 model/media/web/embedding 任务的 provider-backed 推理工作流 | - |
| **Tools/media generation** | 图像/音乐/视频自动回退跨 auth-backed 提供，保留意图切换，重新映射尺寸/宽高比/分辨率/持续时间提示到最近支持选项 | - |
| **Memory/wiki** | 恢复绑定 memory-wiki 堆栈，含 plugin/CLI/sync/query/apply 工具、memory-host 集成、结构化 claim/evidence 字段、编译 digest 检索、claim-health linting、矛盾聚类、stale 仪表板、freshness-weighted 搜索 | - |
| **Plugins/webhooks** | 新增绑定 webhook ingress 插件，外部自动化可通过 per-route shared-secret 端点创建和驱动绑定 TaskFlows | #61892 |
| **Gateway/sessions** | 新增持久化 compaction 检查点 + Sessions UI 分支/恢复操作，可检查和恢复 pre-compaction 会话状态 | #62146 |
| **Compaction** | 新增可插拔 compaction provider registry，插件可替换内置摘要管道。通过 agents.defaults.compaction.provider 配置 | #56224 |
| **Agents/system prompt** | 新增 agents.defaults.systemPromptOverride 用于受控提示实验 + heartbeat prompt-section 控制 | - |
| **Providers/Google** | 新增 Gemma 4 模型支持，保持 Google 回退解析在请求的 provider 路径上 | #61507 |
| **Providers/Google** | 保留 explicit thinking（内容截断） | - |

---

## 📊 版本对比

| 维度 | 04-05 (上次) | 04-08 (本次) |
|------|-------------|-------------|
| 版本 | 2026.4.5 | 2026.4.8 |
| Release 页面 | 404 | ✅ 可访问 |
| 当日发布 | - | 2 次 (02:12 + 05:59) |
| 重大功能 | 未知 | infer CLI, media auto-fallback, memory/wiki 恢复, webhook ingress, compaction 增强, Gemma 4 |

---

## 🎯 对 Sandbot 的影响

1. **Memory/wiki 恢复** — 新的结构化记忆/知识库系统，可能与我们现有的知识库体系互补或替代
2. **Compaction 增强** — 持久化检查点 + 可插拔 provider，对长会话管理有意义
3. **`openclaw infer`** — 新的推理 CLI，可能简化模型调用流程
4. **Webhook ingress** — 可用于外部自动化触发 TaskFlows
5. **版本差距** — 本地 2026.3.8 vs npm 2026.4.8，落后整整一个月

---

*此文件由生态探索 cron 自动创建*
*最后更新：2026-04-08 20:00 UTC*
