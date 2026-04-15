# OpenClaw 生态探索 - 2026-04-11

**抓取时间**: 2026-04-11 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, GitHub releases

---

## 1. ClawHub (clawhub.com → clawhub.ai)

- 域名已从 clawhub.com 重定向到 **clawhub.ai**
- 定位：AI Agent 技能的版本化注册中心
- 安装命令：`npx clawhub@latest install <skill>`
- 功能：浏览、安装、发布技能包，支持版本回滚和向量搜索
- 页面结构：Staff Picks（精选）+ Popular skills（热门下载）

---

## 2. docs.openclaw.ai

- 文档站点正常运行
- 文档索引：`https://docs.openclaw.ai/llms.txt`
- 核心定位：自托管 AI Agent 网关，支持 Discord/Telegram/WhatsApp/Signal/iMessage 等多通道
- 关键特性：多通道网关、插件通道、多 Agent 路由、开源 MIT 协议
- 推荐 Node 版本：Node 24（推荐）或 Node 22 LTS (22.14+)

---

## 3. GitHub Releases - ⚠️ 新 Pre-release (2026-04-11)

今天刚发布的 pre-release，主要更新：

### 新特性
- **Dreaming/记忆 Wiki**: 新增 ChatGPT 导入功能、Imported Insights 和 Memory Palace 日记子标签
- **Control UI/Webchat**: 媒体/语音回复渲染为结构化聊天气泡，新增 `[embed ...]` 富输出标签
- **视频生成工具**: URL-only 资产交付、类型化 providerOptions、参考音频输入、自适应宽高比
- **飞书改进**: 文档评论会话增强，支持评论反应和打字反馈
- **Microsoft Teams**: 新增反应支持、Graph 分页、委托 OAuth 设置
- **插件系统**: manifest 可声明激活和设置描述符，插件安装流程更清晰
- **Ollama 优化**: 模型发现时缓存 context-window 和能力元数据

### Bug 修复
- **OpenAI/Codex OAuth**: 修复 invalid_scope 错误
- **音频转录**: 修复 OpenAI/Groq/Mistral 转录 DNS 问题
- **macOS Talk Mode**: 修复首次麦克风授权后需要二次切换的问题
- **Webchat TTS**: 持久化 TTS 音频回复到聊天历史
- **WhatsApp**: 修复默认账户注册问题

---

## 对比上次检查 (2026-04-02)

| 项目 | 变化 |
|------|------|
| ClawHub 域名 | clawhub.com → clawhub.ai (已重定向) |
| GitHub Release | 新 pre-release (4月11日) |
| 文档站点 | 无明显变化 |
| Node 推荐版本 | 提升到 Node 24 |

---

## 建议行动
1. ⬆️ 考虑升级到最新 pre-release（含多项 Bug 修复）
2. 📝 关注 Dreaming/记忆 Wiki 功能，可能对我们有用
3. 🔧 如果考虑 Node 升级，确认当前版本是否需要更新
