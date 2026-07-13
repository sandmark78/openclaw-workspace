# OpenClaw 生态探索 2026-05-04

**抓取时间**: 2026-05-04 20:00 UTC  
**上次记录**: 2026-05-03 (v2026.5.3 或更早)  
**最新 GitHub Release**: v2026.5.4-beta.1 (2026-05-04 18:22 UTC)

---

## 🔥 重大变化：v2026.5.4-beta.1 发布

**发布日期**: 2026-05-04 (今天！)  
**发布者**: steipete (Peter Steinberger)  
**类型**: Pre-release (beta)

### 📦 核心新功能

#### 1. 文件传输插件 (plugins/file-transfer)
- 新增 bundle 的 file-transfer 插件
- Agent 工具：`file_fetch`, `dir_list`, `dir_fetch`, `file_write`
- 支持配对节点上的二进制文件操作
- 默认拒绝策略 (default-deny per-node path policy)
- 16MB 单次传输上限
- 默认拒绝符号链接遍历 (opt-in followSymlinks)

#### 2. Google Meet / Voice Call 语音升级
- Twilio 拨入通过实时 Gemini 语音桥接
- 有 paced 音频流、backpressure 缓冲
- Barge-in 队列清除
- Meet 参与者获得更快的 OpenClaw 语音 Agent 体验
- Meet 通话日志显示具体 TTS provider/model/voice/采样率

#### 3. DeepSeek V4 思考级别扩展
- 暴露 `xhigh` 和 `max` thinking levels
- Control UI /think 选择器显示最大推理选项
- 修复 #77139

### 🔒 安全加固

- **exec 审批**: 检测 `env -S` 分割字符串命令载体风险
- **plugins/install**: 官方 npm 插件安装不再触发误报警告
- **plugins/security**: 改进扫描器对注释和 process.env 的处理
- **iOS 配对**: 拒绝非回环 `ws://` 设置 URL
- **web_search**: 配置重载后正确尊重 `enabled: false`
- **HEIC/HEIF**: 无 Sharp 转换时 fail-closed 而非发送原始文件

### 🐛 重要 Bug 修复

| 模块 | 修复内容 |
|------|----------|
| **Telegram/streaming** | 清理 tool-progress 中的反引号，修复长文本渲染 |
| **Telegram/reasoning** | 交付后删除 /reasoning 流预览，避免 noisy turns |
| **Control UI/Talk** | 失败 Talk 启动错误可清除，下次点击自动重试 |
| **Discord** | 网关监控不等待启动探测，WSL2 慢路径不再阻塞 |
| **Agents/trajectory** | 限制运行时轨迹捕获，修复 #77124 |
| **Canvas host** | HTTPS 网关不再广告不安全 canvas 链接 |
| **WhatsApp/login** | 登录成功/失败消息通过注入的 runtime 路由 |
| **Google Chat** | 隔离的 Google auth transport，防止拦截器累积 |
| **Agents/Pi** | 抑制合成中转过载提示的持久化 |
| **Agents/tools** | 从可见内容中剥离 reasoning 文本，防止泄露 |

### 📊 ClawHub 统计

| 指标 | 数值 |
|------|------|
| 工具数 | 52.7k |
| 用户数 | 180k |
| 下载量 | 12M |
| 平均评分 | 4.8 |

### 📋 文档更新

- docs.openclaw.ai 推荐 Node 24，兼容 Node 22 LTS (22.14+)
- 新增 docs hubs 页面，按用例分类文档
- 继续强化 self-hosted、multi-channel、agent-native 定位

---

## 🏷️ 与上次对比 (v2026.4.29 → v2026.5.4-beta.1)

**时间跨度**: ~5 天  
**主要增量**:
1. ✅ 全新 file-transfer 插件
2. ✅ Google Meet 语音体验大幅改进
3. ✅ DeepSeek V4 思考级别扩展
4. ✅ 大量安全加固 (plugins + exec + iOS)
5. ✅ Telegram 渲染/流式传输修复
6. ✅ Discord WSL2 兼容修复
7. ✅ Control UI 多项 UI/UX 改进

---

*下次探索时间: 由 cron 触发*
