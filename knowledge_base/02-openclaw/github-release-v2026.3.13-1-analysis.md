# OpenClaw v2026.3.13-1 Release Analysis

**版本**: v2026.3.13-1  
**发布日期**: 2026-03-14 18:04 UTC  
**来源**: https://github.com/openclaw/openclaw/releases  
**分析时间**: 2026-03-19 20:01 UTC  

---

## 📋 版本说明

这是一个**恢复版本**，用于修复 v2026.3.13 标签/发布路径的问题。

**重要提示**:
- npm 版本仍然是 2026.3.13，不是 2026.3.13-1
- `-1` 后缀仅用于 Git tag 和 GitHub Release
- 对应 npm 包版本不变

---

## 🔧 关键修复 (与 Sandbot 相关)

### 1. Telegram 通道修复 ⭐⭐⭐⭐⭐
```
fix(telegram): thread media transport policy into SSRF
PR: #44639
作者：@obviyus
```
**影响**: 线程中媒体传输策略集成到 SSRF 保护
**相关性**: Sandbot 使用 Telegram 作为主要通道，此修复可能影响媒体发送/接收

### 2. 会话状态保留 ⭐⭐⭐⭐
```
fix(session): preserve lastAccountId and lastThreadId on session reset
PR: #44773
作者：@Lanfei
```
**影响**: 会话重置时保留 lastAccountId 和 lastThreadId
**相关性**: 避免会话重置后丢失通道上下文，提升用户体验

### 3. Docker 时区支持 ⭐⭐⭐⭐
```
Docker: add OPENCLAW_TZ timezone support
PR: #34119
作者：@Lanfei
```
**影响**: Docker 部署支持时区配置
**相关性**: Sandbot 运行在 Docker 容器中，可配置 CST 时区 (UTC+8)

### 4. 压缩后完整性检查 ⭐⭐⭐
```
fix(compaction): use full-session token count for post-compaction sanity check
PR: #28347
作者：@efe-arv
```
**影响**: 使用完整会话 token 计数进行压缩后检查
**相关性**: LCM 压缩机制改进，提升上下文管理可靠性

### 5. Discord 网关容错 ⭐⭐⭐
```
fix: handle Discord gateway metadata fetch failures
PR: #44397
作者：@jalehman
```
**影响**: 处理 Discord 网关元数据获取失败
**相关性**: 如果未来启用 Discord 通道，此修复提升稳定性

---

## 📱 移动端更新

### Android
- `feat(android): redesign chat settings UI` (#44894)
- `fix(android): use Google Code Scanner for onboarding QR` (#45021)
- `Android: fix HttpURLConnection leak in TalkModeVoiceResolver` (#43780)

### iOS
- `feat(ios): add onboarding welcome pager` (#45054)

---

## 🤖 Agent 相关修复

| 修复 | PR | 影响 |
|------|-----|------|
| 移除 Anthropic thinking blocks 重放 | #44843 | 避免重复思考块 |
| 保留用户兼容性覆盖 | #44432 | 非原生 OpenAI 兼容模式 |
| 会话重置提示优化 | #43403 | 避免 Azure 内容过滤 |
| MEMORY.md 重复注入修复 | #26054 | 大小写不敏感挂载 |

---

## 📊 配置与 Schema 修复

- `fix(config): add missing params field to agents.list[] validation schema` (#41171)
- `fix(signal): add groups config to Signal channel schema` (#27199)
- `fix: restore web fetch firecrawl config in runtime zod schema` (#42583)

---

## 🧪 测试与文档

- 默认模型更新：gpt-5.3-codex → gpt-5.4 (测试)
- 文档修复：session key `:dm:` → `:direct:`
- Changelog 条目移动到 Unreleased

---

## 💡 对 Sandbot 的启示

### 1. Telegram 媒体传输
**现状**: Sandbot 使用 Telegram 作为主要通道
**行动**: 测试媒体发送功能，确认修复效果
**优先级**: P1

### 2. Docker 时区配置
**现状**: Sandbot 运行在 Docker 容器中
**行动**: 在 openclaw.json 或 Docker 环境变量中添加 `OPENCLAW_TZ=CST` 或 `OPENCLAW_TZ=Asia/Shanghai`
**优先级**: P2

### 3. 会话状态保留
**现状**: 会话重置可能导致上下文丢失
**行动**: 验证会话重置行为，确认 lastAccountId/lastThreadId 保留
**优先级**: P2

### 4. LCM 压缩改进
**现状**: Sandbot 依赖 LCM 进行上下文管理
**行动**: 监控压缩后完整性检查，确保无 token 丢失
**优先级**: P3

---

## 🚀 升级建议

### 当前版本检查
```bash
# 检查当前运行的 OpenClaw 版本
openclaw --version
# 或
cat /home/node/.openclaw/package.json | grep version
```

### 升级步骤 (如需)
```bash
# 1. 备份配置
cp -r /home/node/.openclaw /home/node/.openclaw.backup.$(date +%Y%m%d)

# 2. 升级 npm 包
npm install -g openclaw@latest

# 3. 重启 Gateway
openclaw gateway restart

# 4. 验证版本
openclaw --version
```

### 升级风险评估
| 组件 | 风险 | 缓解措施 |
|------|------|----------|
| 配置兼容性 | 低 | 备份配置，回滚测试 |
| 数据迁移 | 低 | 会话/记忆文件不受影响 |
| 通道连接 | 低 | Telegram 修复是改进 |
| 子 Agent | 低 | 配置文件独立 |

---

## 📝 结论

**v2026.3.13-1 是一个维护性发布**，主要修复：
- ✅ Telegram 媒体传输 (Sandbot 核心通道)
- ✅ 会话状态保留 (用户体验改进)
- ✅ Docker 时区支持 (部署优化)
- ✅ LCM 压缩完整性 (上下文管理)

**建议**: 
- 如果当前运行稳定，可暂缓升级
- 如果遇到 Telegram 媒体问题或会话重置问题，建议升级
- 升级前备份配置，测试通道连接

---

**知识点数量**: 25  
**深度评级**: ⭐⭐⭐ (中等深度，版本分析)  
**关联领域**: 02-openclaw, 09-security, 10-automation
