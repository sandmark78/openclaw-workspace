# OpenClaw GitHub Release 2026.5.25 + 2026.5.25-beta.1

**日期**: 2026-05-25 / 2026-05-26 (beta)
**类型**: 正式版 + Pre-release
**来源**: https://github.com/openclaw/openclaw/releases

---

## 📌 v2026.5.25 (正式版)

### 核心修复

#### 安装器改进
- **Alpine Linux**: 使用 apk 安装 Node.js/npm/Git，不再下载 glibc Node tarballs（修复 node:sqlite 失败）
- **musl Linux 检测**: 正确识别 Alpine 等 musl Linux 为 Linux，不再在安装前拒绝
- **Windows 原生支持**: Node package scripts 使用跨平台启动器，gateway/TUI/Docker-all 等在原生 Windows 上工作

#### Agent 性能
- **提供者描述符缓存**: 缓存 manifest-backed CLI provider descriptors 和 fallback provider resolution，避免重复扫描 bundled provider runtime
- **OpenRouter 上下文限制**: 使用 endpoint-specific OpenRouter context limits（来自 top_provider metadata），不再过度夸大可用上下文 (#85949)

#### MCP 工具
- **MCP 工具发现边界**: 限制 bundled MCP tools/list catalog discovery，hung MCP servers 不再阻塞 session tool materialization (#85063)

#### 配置/密钥
- **SecretRef IDs**: exec SecretRef ids 支持 # 选择器，AWS-style secret#json_key ids 验证更一致 (#80731)

#### iMessage 修复
- **iMessage 群组 watch**: 恢复 malformed anchorless group watch payloads by GUID，drop unrecoverable payloads 而不是回复 sender DM (#84470)
- **启动 catchup**: catchup pass 完成后推进启动 catchup cursor，重启不再重放已处理消息 (#85475)

#### 图片工具
- **Anthropic 媒体限制**: 使用 bundled Anthropic media limits 解析图片压缩策略（无 provider-runtime hooks 时）

---

## 📌 v2026.5.25-beta.1 (Pre-release, 5月26日)

### Beta 1 Late Fixes
- **iMessage 附件**: inbound attachment roots 通过 image tool 读取 ~/Library/Messages/Attachments，不再被 path-not-allowed 拒绝 (#30170, #86569)
- **iMessage watcher 去重**: channels.imessage.accounts 同时列出 default 和 named account 指向同一 Messages 源时，防止重复 imsg rpc 进程和加倍 inbound 回复 (#65141, #86705)
- **Codex sandbox**: remapping workspace instruction files 时保留 sandbox bootstrap path style

---

## 对我们有用的变更

1. **OpenRouter 上下文修正** - 我们的模型经过 OpenRouter 路由，之前可能高估上下文窗口
2. **MCP 工具发现边界** - 防止 hung MCP 服务器阻塞工具加载
3. **Alpine/musl 支持** - 如果未来在 Alpine 容器部署需要关注
4. **Windows 原生** - 本地开发体验改善
