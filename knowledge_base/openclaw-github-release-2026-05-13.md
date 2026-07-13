# OpenClaw GitHub Release 2026.5.13 (Pre-release)

**抓取时间**: 2026-05-13 20:00 UTC  
**发布时间**: 2026-05-13 18:06 UTC  
**版本**: Pre-release  
**上次记录版本**: 2026.5.11 (Pre-release)

---

## 🔒 安全与配对增强（重点）

| 类别 | 内容 |
|------|------|
| **Node 配对** | 隐藏待处理的 Node 配对命令/能力/权限，直到审批通过；配对变更后实时刷新已批准界面 (#80741) |
| **Setup Code 配对** | 要求审批才能进行 setup-code 设备配对 (#81292) |
| **浏览器配对** | 要求显式浏览器设备配对 (#81289) |
| **Control UI 代理** | 代理范围访问前必须先进行 Control UI 配对 (#81288) |
| **可信代理** | 加固 trusted-proxy 来源验证 (#81290) |

## 📡 协议与通信

- **Gateway Protocol v4**: 要求 v4 客户端，流式传输显式 chat deltaText/replace 帧，SDK 客户端无需本地 diff 即可消费助手更新 (#80725)
- **Talk 会话**: Gateway 传递 Talk 会话 scope 给 resolver (#81379)
- **Agent 子代理**: 同进程子代理完成交接通过进程内 agent dispatcher 传递，不再走 Gateway RPC 回环

## 🛡️ 媒体与插件

- **入站媒体大小限制**: Feishu/WhatsApp/Line 插件在下载流中强制实施媒体大小上限，避免完整缓冲超大附件 (#81044, #81050)
- **插件安装**: 后续插件安装/更新时保留第三方 peer 依赖 (#81105)
- **插件卸载**: 移除插件后修剪第三方 peer 依赖，失败不阻塞清理
- **WeCom**: 更新到 @wecom/wecom-openclaw-plugin@2026.5.7

## 🔧 配置与构建

- **配置序列化**: 集中序列化 + 重试语义化配置变更，并发命令可 rebase 安全变更而非覆盖 (#76601)
- **Docker**: 固定 setup-time 容器路径，防止宿主机 .env 泄漏到 Linux 容器 (#81105)
- **安装器**: --version 参数支持 git 安装，从锁文件安装防止 pnpm minimum-release-age 问题

## 🤖 Agent & 模型

- **Claude CLI**: 会话旋转后从 OpenClaw 转录历史中重新种子重试，防止对话失忆 (#80934)
- **GitHub Copilot**: OAuth token 交换用于 Copilot API token，Gemini 图像负载通过 Chat Completions 路由 (#80393, #80442)
- **工具 Schema**: Agent 工具参数添加 permissive item schema，防止 OpenAI 兼容 provider 因缺少 items 拒绝插件工具 (#81175)

---

## 总结

本次 Pre-release 核心主题是 **安全加固 + 协议升级**：
1. 设备配对全面要求显式审批（Node/浏览器/Setup Code/Control UI）
2. Gateway Protocol 升级到 v4，支持显式帧流
3. 入站媒体安全加固（大小限制）
4. 子代理通信优化（进程内交接）
