# 生态探索更新 2026-05-19

**检查时间**: 2026-05-19 20:00 UTC

---

## 🔴 有新变化！

### 1. GitHub Releases 恢复访问（重大发现）

之前多次探测返回 404，本次成功获取。最新版本：

**2026.5.19 (Pre-release)** — 发布于 5月18日

核心变更：
- **启动优化**: 启动日志与插件服务并行化，与 channel sidecars 重叠，减少重启延迟 (#83300, #83301)
- **浏览器增强**: 浏览器快照中显示挂起/最近的模态对话框，支持 `--dialog-id` 应答待处理对话框
- **浏览器 CLI**: 新增 `openclaw browser evaluate --timeout-ms`，支持长时间运行的页面函数 (#83447)
- **新技能**: 
  - `meme-maker` 技能（模板搜索、SVG/PNG 渲染、Imgflip 托管、Know Your Meme 溯源）
  - `python-debugging` 技能（pdb、breakpoint()、post-mortem、debugpy 远程附加）
  - `autoreview` 技能（Codex closeout review，Codex-first fallback）
  - Node inspector 调试、融合图表生成、throwaway spike 工作流技能
- **插件系统**: 新增 `defineToolPlugin` + `openclaw plugins build/validate/init`，支持 typed simple tool plugins
- **Skills CLI**: `openclaw skills install/update` 支持 `--global` 安装到共享托管技能 (#74466)
- **Docker/Podman**: 新增 `OPENCLAW_IMAGE_APT_PACKAGES` 运行时中立的镜像构建参数 (#62431)
- **Mac App**: 重新设计 Settings 页面（一致的卡片布局、更干净的权限/语音/技能/cron/exec/debug 面板）
- **Obsidian 技能更新**: 指向官方 obsidian CLI，要求注册的二进制文件
- **Agent/工具**: 缩短内置工具描述和 schema 提示
- **依赖更新**: @openclaw/proxyline → 0.3.3，Pi packages → 0.75.1，最低 Node.js 22 → 22.19

### 2. ClawHub 指标（无变化）

| 指标 | 本次 |
|------|------|
| 工具数 | 52.7k |
| 用户数 | 180k |
| 下载量 | 12M |
| 平均评分 | 4.8 |

### 3. docs.openclaw.ai（结构稳定）

文档结构无变化，Node 要求更新为 Node 24 (推荐) 或 Node 22 LTS (22.19+)

---

## 版本对比

| 项目 | 本次 (5/19) | 上次 (5/16) | 变化 |
|------|-------------|-------------|------|
| npm 最新版本 | **2026.5.19 (pre-release)** | 2026.5.12 | ⬆️ 新版本 |
| 当前安装版本 | 2026.3.8 | 2026.3.8 | 无 |
| GitHub releases | ✅ 可访问 | ❌ 404 | 🔴 恢复 |
| ClawHub 工具数 | 52.7k | 52.7k | 无 |

---

## ⚠️ 持续提醒

- 当前版本 2026.3.8 仍落后最新 2026.5.19 约 2 个月
- 2026.5.19 是 pre-release，建议等稳定版或评估后决定是否更新
- 主要关注：启动性能优化、浏览器对话框处理、新技能（meme-maker、python-debugging）
