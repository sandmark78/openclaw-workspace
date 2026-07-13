# OpenClaw 生态探索记录 — 2026-06-17

**探索时间**: 2026-06-17 20:00 UTC
**触发**: 定时任务 🌐 生态探索

---

## 📦 版本差距

| 项目 | 版本 | 备注 |
|------|------|------|
| 当前安装 | `2026.3.8` | 容器内 `openclaw --version` |
| 最新 Release | `v2026.6.8` | 2026-06-16 发布，昨天 |
| 差距 | **3 个月 / ~3 个版本** | ⚠️ 建议升级 |

---

## 🆕 v2026.6.8 核心更新 (2026-06-16)

### 1. 更丰富的通道消息渲染
- **Telegram**: 支持结构化文本渲染（表格、列表、可折叠引用块、保留换行、CLI 回复）
- **WhatsApp**: 现在支持配置的 ACP 绑定
- 影响：我们的 Telegram 通道发送格式会更漂亮

### 2. 更可靠的 Agent 运行
- 账户级 DM 发送
- 生成媒体补全
- 自动回复 message-tool 最终回复
- 重启时优雅关闭中止
- 子 Agent 暂停恢复
- 会话身份提示保持正确恢复路径

### 3. 新模型支持
- **GLM-5.2** 支持
- **Claude Haiku 4.5** 目录支持
- 规范化 provider ID（OpenRouter/Google Vertex 路径）
- 更安全的工具 schema 恢复

### 4. 使用量脚注改进
- `/usage` 命令原生完整页脚渲染器
- 默认脚脚模板
- 凭证感知限制
- 固定小数格式化
- 模板错误警告（而非静默输出错误）

### 5. Web 搜索默认值变更
- 无 Key 提供者（Parallel Free、DuckDuckGo、Ollama、Codex Hosted Search）改为**显式选择**而非自动降级
- 影响：如果没有配置 API 搜索，不会再自动 fallback 到免费源

### 6. UI 和移动端改进
- 工作区文件默认折叠
- WebChat 回滚支持流式
- 桌面会话选择器交互修复
- iOS 重连过时前台 Gateway

### 7. 内存和状态弹性
- 超大 OpenAI embedding 批次自动拆分（避免 431 错误）
- QMD 搜索在瞬态模式下可用
- SQLite 避免在 NFS 卷上使用 WAL
- 全量重建索引保留回滚/缓存恢复

### 8. 其他修复
- Discord 自动线程标题 60 秒超时 + 4096 token 预算
- Feishu 动态 Agent 路由修复（绑定复用后）
- Slack 出站消息钩子
- Gemini CLI OAuth/密钥认证隔离

---

## 🌐 ClawHub 变化

- 域名从 `clawhub.com` 重定向到 `clawhub.ai`
- 页面定位：Skills / Plugins / Publishers 三大分类
- 标语：「EquipInstallUnleash.Ship.Build.Create.Unleash.」
- 「Tools built by thousands, ready in one search.」
- 无其他显著变化

---

## 📚 docs.openclaw.ai

- 标准文档首页，无明显结构变化
- 推荐 Node 版本更新为 **Node 24**（推荐）或 Node 22 LTS（22.19+）
- 当前模型运行在 `qwen3.6-plus`

---

## ⚡ 建议行动

1. **升级 OpenClaw**: `npm install -g openclaw@latest` → 从 2026.3.8 升级到 2026.6.8
   - 主要收益：Telegram 渲染改善、Agent 可靠性提升、新模型支持
   - 风险：中等，需重启 Gateway

2. **关注 Node 24**: 如果升级 OpenClaw，考虑同时升级 Node.js

3. **检查搜索配置**: 新版搜索默认值变更，确认 Brave API 或备用搜索正常
