# OpenClaw GitHub Release v2026.5.18

**抓取时间**: 2026-05-18 20:00 UTC  
**发布时间**: 2026-05-18 18:54 UTC  
**版本**: v2026.5.18 (Latest)  
**上次记录版本**: v2026.5.13 (Pre-release)

---

## 🆕 新技能（重点）

| 技能 | 功能 | 详情 |
|------|------|------|
| **meme-maker** | 梗图制作 | 模板搜索 + 本地 SVG/PNG 渲染 + Imgflip 托管渲染 + Know Your Meme 来源链接 |
| **Python debugging** | Python 调试 | pdb、breakpoint()、post-mortem 检查、debugpy 远程附加 |
| **node inspector** | Node.js 调试 | 节点检查器调试技能 |
| **fused diagram** | 图表生成 | 融合图表生成技能 |
| **throwaway spike** | 快速原型 | 临时性工作流技能 |
| **autoreview** | 自动审查 | 原 Codex closeout review 重命名，保留 Codex-first 回退行为 |
| **Obsidian (更新)** | 笔记管理 | 更新为官方 obsidian CLI，不再使用第三方 obsidian-cli |

## 🔧 CLI & 插件增强

- **defineToolPlugin**: 新增 `openclaw plugins build/validate/init` 命令
- 支持类型化的简单工具插件，自动生成 manifest 元数据
- 可选工具声明和上下文工厂

## 🌐 代理改进

- **Node.js 最低版本**: 提升至 22.19（Pi 包升级到 0.75.1）
- **代理修复**: 默认为简洁有界的重构，精简内部实现
- **工具描述优化**: 缩短所有内置工具描述和 schema hints（媒体、消息、会话、cron、Gateway、web、图像/PDF、TTS、nodes、plan）
- **技能 Prompt 收紧**: 强化 bundled skill prompts 和元数据，引用技能描述

## 🚀 Gateway 性能

- **启动优化**: 启动日志与插件服务启动和 channel sidecars 重叠，降低重启就绪延迟 (#83301)
- **ACPX 成本归因**: 启动探测、配置、运行时间和资源计数成本归因于重启追踪，不影响就绪行为 (#83300)
- **重启基准**: 新增 `pnpm test:restart:gateway` 基准工具 (#83299)

## 📱 移动端

- **Android Talk Mode**: 切换为实时 Gateway 中继语音会话 (#83130)
  - 流式麦克风输入
  - 实时音频播放
  - 工具结果桥接
  - 屏幕转录

- **Mac App**: 重新设计 Settings 页面
  - 一致的卡片布局
  - 缓存导航
  - 更清晰的面板（权限/语音/技能/cron/exec/debug）

## 🌐 浏览器控制

- **弹窗检测**: 快照中显示待处理/最近处理的模态对话框
- 操作打开模态时返回 `blockedByDialog`
- 支持 `browser dialog --dialog-id` 回答待处理对话框

## 🔒 代理 & 安全

- **Admin HTTP RPC**: 允许受信任的管理客户端启动并等待 Web QR 登录流程 (#83259)
- **代理 HTTPS**: 支持 HTTPS 管理的正向代理端点和 scoped proxy.tls.caFile CA 信任 (#79171)
- **媒体安全**: 防止图像元数据探测调用外部解码器委托

## 🐛 Bug 修复

- **Discord/OpenAI**: 保持实时 Discord 语音会话在后续回合正常接收 (#80505)
- **媒体处理**: 安装 Sharp 作为根包，回退到 sips/Windows 原生/ImageMagick/GraphicsMagick/ffmpeg

## 🧪 QA-Lab（大量新增）

- 首轮 20 回合 + 可选 100 回合运行时对等场景
- `openclaw qa suite --runtime-parity-tier` 命令
- Codex-vs-Pi 运行时 token 效率轨道
- 运行时工具覆盖率报告 (`openclaw qa coverage --tools`)
- 个人代理批准拒绝场景、本地任务跟进场景
- 插件钩子崩溃、清单合约错误自检场景

## 🐳 Docker

- **OPENCLAW_IMAGE_APT_PACKAGES**: 新增运行时中立的镜像构建参数
- 保留 `OPENCLAW_DOCKER_APT_PACKAGES` 作为遗留回退 (#62431)

## 📊 插件消息

- 新增频道渲染器的演示能力限制
- 原生渲染前适配丰富消息控制
- 标记旧版 interactive/Slack 指令生产者 API 为弃用

---

## 总结

本次发布核心主题是 **技能生态扩展 + 性能优化 + 调试能力增强**：
1. **5 个新技能**：meme-maker、Python 调试、node inspector、图表生成、快速原型
2. **插件开发工具链**：`openclaw plugins build/validate/init`
3. **Gateway 启动加速**：并行化降低就绪延迟
4. **Android 语音升级**：实时中继 + 流式处理
5. **浏览器弹窗管理**：模态对话框完整检测与响应
6. **QA-Lab 大规模扩展**：测试场景和覆盖率工具链
