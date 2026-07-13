# OpenClaw 生态探索记录 2026-06-06

**抓取时间**: 2026-06-06 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, GitHub Releases

---

## 📊 ClawHub 平台数据（无变化）

- **域名**: clawhub.com → 重定向到 clawhub.ai
- **工具总数**: 52.7k
- **用户数**: 180k
- **总下载**: 12M
- **平均评分**: 4.8

---

## 🆚 版本差距

| 项目 | 值 |
|------|------|
| **当前运行版本** | OpenClaw 2026.3.8 |
| **最新预发布** | 2026.6.5 (2026-06-05) ⬆️ NEW |
| **最新稳定版** | 2026.5.30 (2026-05-30) |
| **落后版本** | 3 个大版本！(3.8 → 5.30 → 6.5) |

---

## 🔥 2026.6.5 预发布亮点 (2026-06-05 03:36 UTC) ⬆️ 新增

1. **QQBot 推理内容过滤**: QQBot 现在会在交付前剥离模型的 reasoning/thinking 脚手架，防止原始推理内容泄露到频道回复中 (#89913, #90132)。贡献者: @openperf
2. **MCP 工具结果强制转换**: MCP 工具返回的 resource_link、resource、audio、malformed image 等非文本/图片块，现在会在 materialize 边界被强制转换，防止 Anthropic 400 错误和被污染的会话历史 (#90710, #90728)。贡献者: @RanSHammer, @849261680
3. **Anthropic 扩展思维会话恢复**: prompt-cache 过期或 Gateway 重启后，扩展思维会话可以恢复——stream start 事件等待 message_start，让 pre-generation 签名错误触发现有的恢复重试 (#90667, #90697)。贡献者: @openperf
4. **Parallel 作为内置 web_search 提供商**: Parallel 现在是捆绑的 web_search 提供商，支持 PARALLEL_API_KEY 发现、guard 端点处理、缓存安全的 session id、onboarding picker 和文档 (#85158)。贡献者: @NormallyGaussian
5. **Google Vertex ADC 修复**: Vertex ADC 用户重新获得静态 catalog 行和运行时模型解析，单提供商 cooldown 恢复和 memory adapter 状态检查更可靠 (#90506, #90609, #90717, #90816)。贡献者: @849261680
6. **Matrix 语音笔记改进**: Matrix 可以在 mention 门控前预检语音笔记，通过 Matrix 关系分页保留线程读取/回复，覆盖语音和线程流的 QA (#78016, #90415)

---

## 📝 行动建议

⚠️ 当前版本 2026.3.8 落后较远，最新预发布已跳到 2026.6.5。2026.6.5 新增的 MCP 工具结果强制转换和 Anthropic 会话恢复改进对我们日常使用有直接影响。建议老大考虑升级。

---

*自动生成，下次生态探索将对比此快照*
