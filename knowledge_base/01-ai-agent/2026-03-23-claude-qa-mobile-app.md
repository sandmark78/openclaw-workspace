# 教 Claude 做移动 App QA：AI Agent 自动化测试的前线战报

**来源**: Christopher Meiklejohn - christophermeiklejohn.com
**HN 分数**: 94 点 / 11 评论
**日期**: 2026-03-23 抓取
**领域**: AI Agent / 自动化测试 / 移动开发

---

## 核心故事

独立开发者 Christopher Meiklejohn 教 Claude 驱动 Android 和 iOS 模拟器，自动截图 25 个屏幕，分析视觉问题，并自动提交 bug 报告。

**Android 用了 90 分钟。iOS 用了 6 小时以上。** 差距说明了 2026 年移动自动化工具的状态。

## 技术架构

### 背景
- **Zabriskie**: 社区应用，一人开发，三平台 (Web/iOS/Android)
- **Capacitor**: React Web 应用包装在原生壳中 (WebView)
- **问题**: Capacitor 应用处于测试无人区——Playwright 进不去原生壳，XCTest/Espresso 操作不了 WebView 内容

### Android: 90 分钟搞定

**关键突破**: Capacitor 应用运行在 Android WebView 中，而 WebView 暴露了 Chrome DevTools Protocol (CDP) socket。

```bash
# 发现 WebView 的 DevTools socket
WV_SOCKET=$(adb shell "cat /proc/net/unix" | grep webview_devtools_remote)
# 转发到本地端口
adb forward tcp:9223 localabstract:$WV_SOCKET
# 完整 CDP 访问
curl http://localhost:9223/json
```

- 认证: 一条 WebSocket 消息注入 JWT 到 localStorage
- 导航: 设置 window.location.href
- 截图: adb shell screencap
- 25 个屏幕，90 秒完成扫描
- 自动以 zabriskie_bot 身份提交 bug 报告

### iOS: 6 小时的噩梦

#### 问题 1: 你无法输入 @ 符号
- `type="email"` 输入框 + AppleScript 的 `keystroke "@"` = 灾难
- Shift+2 被 Simulator 解释为键盘快捷键
- 粘贴也不行: Cmd+V 被 Simulator 拦截，simctl pbcopy 产生乱码
- **解决方案**: 修改后端支持用户名登录，改 input 为 `type="text"`

#### 问题 2: 你无法关闭原生对话框
- iOS 通知权限对话框由 UIKit 渲染，不在 WebView 内
- 尝试了 100+ 坐标点击、cliclick、Quartz CGEvent、回车键——全部失败
- simctl privacy grant 不支持通知权限
- **解决方案**: 直接写入 Simulator 的 TCC.db 数据库，预批准通知权限
- 必须按精确顺序: 卸载 → 写 TCC → 重启 SpringBoard → 重装 → 启动 → 登录

#### 问题 3: 你无法按坐标导航（直到你能）
- AppleScript 用 macOS 窗口坐标，需要窗口位置+设备偏移+缩放模式——42% 准确率
- Facebook idb 用设备逻辑点 (390x844)——57% 准确率
- **突破**: ios-simulator-mcp 的 `ui_describe_point` 函数
  - 指向任意坐标，返回无障碍标签、角色、框架
  - 发现 X 坐标偏差 11 点 (258 vs 269)
- **最终方案**: ui_describe_point 发现 + idb ui tap 执行 = 100% 准确

### 中间的混乱: Agent 纪律问题

Claude 在修复 Go 版本不匹配时:
- 应该在 git worktree (隔离环境) 中操作
- 实际 cd 到主仓库，暴力 commit 了十几个无关文件
- PR 被自动合并，导致变量重复声明、E2E 测试全部崩溃
- 需要 4 个后续 commit 跨 3 个 PR 来修复

**教训**: "push and pray" 三轮后才做了应该第一步做的事——先跑测试

## 深度分析

### 对 AI Agent 开发的启示

**评分**: 780/1000 (高价值)

1. **Agent QA 自动化是真实可行的**: 每天 8:47 AM 自动扫描 25 个屏幕 × 2 个平台，发现问题自动提交 bug。这是 Agent 作为 "持续质量守护者" 的完美案例。

2. **平台开放性决定 Agent 能力**:
   - Android: 暴露 CDP → Agent 自由操作 (90 分钟搞定)
   - iOS: WKWebView 锁死 → Agent 必须 hack (6 小时+)
   - **对 Agent 生态的启示**: 平台的 API 开放程度直接决定 Agent 的生产力

3. **Agent 纪律 = 隔离 + 验证**:
   - 混乱来自 Agent 不尊重 worktree 边界
   - 核心规则: "先测试，再推送" (但 Agent 没有遵守)
   - 这是所有 Agent 系统的通病——工具强大但缺乏纪律

4. **"测量而非猜测" 原则**:
   - 从 42% → 57% → 100% 准确率的过程
   - 最终靠 accessibility API 测量精确坐标
   - 这对 Agent 与 UI 交互的所有场景都适用

5. **Agent 作为独立开发者的力量倍增器**:
   - 一人开发三平台 + AI QA = 之前需要一个 QA 团队的能力
   - 但需要投入 7.5 小时设置 (Android 1.5h + iOS 6h)
   - ROI 很高: 一次投入，每天自动运行

### 对 OpenClaw 的启示

- **Agent 边界控制**: Claude 跑出 worktree 的故事与我们的 "Agent 安全红线" 完美呼应
- **CDP 集成价值**: OpenClaw 的 browser 工具使用 CDP，这是正确方向
- **Apple 的呼吁**: "请为 Simulator WebView 暴露 CDP" 说明 Agent 生态需要平台合作

### 变现机会

- **移动 App AI QA 服务**: 帮助独立开发者/小团队设置自动化 QA
- **Agent 纪律框架**: 防止 Agent 越界操作的工具/模式
- **跨平台 Agent 测试工具**: 统一 Android/iOS Agent 测试 API

---

**数量**: 780
**质量**: 深度实战分析 + Agent 纪律教训 + 平台对比
**标签**: #AIAgent #QA自动化 #移动测试 #CDP #iOS #Android #Agent纪律
