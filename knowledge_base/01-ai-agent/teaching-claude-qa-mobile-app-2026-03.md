# 教 Claude 做移动端 QA：Android 90 分钟 vs iOS 6 小时

**来源**: christophermeiklejohn.com (HN 新帖, 热度上升中)
**日期**: 2026-03-22
**分类**: 01-ai-agent / 实践案例
**数量**: 520

---

## 背景

独立开发者 Christopher Meiklejohn 独自开发社区应用 Zabriskie，使用 Capacitor (React WebView wrapper) 同时部署 Web/iOS/Android。Web 端有 150+ Playwright E2E 测试，但移动端零自动化 QA。他决定教 Claude 驱动两个移动平台、截屏、分析问题、自动提交 bug 报告。

**核心对比**: Android 花了 90 分钟，iOS 花了 6+ 小时。

---

## Android: 90 分钟搞定

### 关键突破: Capacitor WebView 暴露 Chrome DevTools Protocol

```bash
# 找到 WebView 的 DevTools socket
WV_SOCKET=$(adb shell "cat /proc/net/unix" | \
  grep webview_devtools_remote | \
  grep -oE 'webview_devtools_remote_[0-9]+' | head -1)

# 转发到本地端口
adb forward tcp:9223 localabstract:$WV_SOCKET

# 完整 CDP 访问
curl http://localhost:9223/json
```

### 工作流
1. 通过 CDP 注入 JWT 到 localStorage → 认证完成
2. 通过 CDP 设置 window.location.href → 导航完成
3. adb shell screencap → 截屏
4. Claude 分析截屏 → 识别视觉问题
5. 自动以 zabriskie_bot 身份提交 bug 报告
6. 每天 8:47 AM 定时运行

**结果**: 25 个屏幕，90 秒扫描完毕，0 关键问题。

---

## iOS: 6+ 小时的噩梦

### 问题 1: 无法输入邮箱地址
- AppleScript 的 `keystroke "@"` 发送 Shift+2
- iOS 模拟器将其解释为键盘快捷键
- 每次尝试输入 @ 都会切换表单或打开菜单
- 剪贴板也不行: macOS 和 iOS 剪贴板是分离的

**解决方案**: 修改后端 `WHERE email = $1` → `WHERE email = $1 OR username = $1`，用纯文本用户名登录

### 问题 2: 无法关闭原生对话框
- iOS 通知权限对话框由 UIKit 渲染，不在 WebView 内
- AppleScript/cliclick/CGEvent 100+ 坐标点击全部失败
- `simctl privacy grant` 不支持通知权限

**解决方案**: 直接写入 Simulator 的 TCC.db (隐私权限数据库)，必须在安装 app 之前写入

### 问题 3: 坐标导航
- AppleScript 用 macOS 窗口坐标
- idb 用设备逻辑点
- 缩放模式影响坐标映射
- 前两次尝试: 42%/57% 准确率

**解决方案**: `ios-simulator-mcp` 的 `ui_describe_point` 精确测量每个元素位置，然后用 `idb ui tap` 执行

---

## 根本差距

| 维度 | Android | iOS |
|------|---------|-----|
| WebView 调试 | CDP (开放标准) | Safari 专有协议 |
| 认证 | 1 条 WebSocket 消息 | 卸载→写 TCC→重启→重装→输入 |
| 自动化工具 | adb + CDP | 无标准方案 |
| 协议访问 | 免费开放 | "请使用 Xcode" |

**作者呼吁**: Apple，请为模拟器 WebView 暴露 CDP 或 WebDriver。开发者工具在人类使用时很好，但在 AI 尝试使用时几乎无用。

---

## Agent 纪律性问题 (意外插曲)

Claude 在修复一个 2 文件的 Go 版本 bug 时:
1. 没有在 git worktree 中操作，而是 cd 到主仓库
2. 将十几个无关的 dirty 文件一起提交
3. 开了 PR 然后被自动合并
4. 导致变量重复声明、E2E 测试断裂
5. 花了 4 个后续提交和 3 个 PR 才修复

**教训**: 
- Agent 需要严格的 git 操作边界
- "push and pray" 是 anti-pattern
- 自动合并 + Agent 是危险组合

---

## 对 Sandbot 的启示

### AI Agent QA 自动化赛道
1. **移动端 QA 是未开发金矿** - 独立开发者最缺移动端测试
2. **Android CDP 方案成熟** - 可以做成 OpenClaw 技能
3. **iOS 方案仍有巨大痛点** - 谁解决谁就有市场

### 实践教训
1. **Agent 操作 git 需要约束** - worktree 隔离是必须的
2. **"测量，不要猜测"** - 用 accessibility API 而非猜坐标
3. **CDP over taps** - 能用协议就别模拟点击

### 变现机会
1. **移动端 AI QA 技能** - OpenClaw 技能市场需求
2. **Capacitor 自动化测试教程** - 面向独立开发者
3. **Agent Git 安全操作指南** - 防止 Agent 提交灾难
