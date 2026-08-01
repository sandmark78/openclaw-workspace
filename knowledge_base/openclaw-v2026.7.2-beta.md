# OpenClaw v2026.7.2-beta.1 更新日志

**发布日期**: 2026-07-15  
**记录时间**: 2026-07-15 20:00 UTC  
**类型**: Beta 版本

---

## 主要更新

### 1. 远程编码会话 (Remote Coding Sessions)
- Control UI 会话可在云端 worker 上运行
- 可在宿主终端中打开 Codex 和 Claude catalog 会话
- 支持直接在终端中恢复 OpenCode 和 Pi 会话
- PR: #107670, #107086, #107200

### 2. 原生自动化与节点 (Native Automation and Nodes)
- Automations 功能在移动端实现同等能力
- Android 新增前台 Voice Wake（语音唤醒）
- 无头 Linux 节点暴露摄像头、位置、通知能力
- PR: #106355, #107081, #107193

### 3. 更安全的通道操作 (Safer Channel Operation)
- 修复 Telegram 重启后持久入口丢失问题
- Signal 在活跃回合期间保持停止和审批控制响应
- 修复通道允许列表不应授予 owner 访问权限
- PR: #107288, #107422, #107403
- 贡献者: @obviyus, @arduano, @yetval

### 4. 引导式 Control UI 设置 (Guided Control UI Setup)
- 从设置页面配置模型提供商
- 通过引导页面接入通道
- 创建会话时可选择图片和模型
- PR: #106490, #106469, #107358
- 贡献者: @alexandre-leng, @fuller-stack-dev

### 5. Gateway 和会话恢复 (Gateway and Session Recovery)
- 防止重启准入卡住 Gateway
- 最终确定停滞后恢复回复会话
- 保持一次性 cron 任务在生命周期声明竞争中启用
- PR: #107339, #106792, #107236
- 贡献者: @obviyus, @joshavant, @charliemeyer2000, @SL4N

### 6. 安装和打包 (Install and Packaging)
- 新增 Linux deb 和 AppImage 包
- 从稳定的 main 分支发布
- Windows 安装 winget 后继续执行

---

## 近期稳定版参考

### v2026.7.1 (2026-07-13)
- Control UI 和 onboarding 大改版
- iOS/Android/macOS 官方应用重大更新
- 新增模型/提供商: Featherless, Claude Sonnet 5, Mythos 5, Meta Muse Spark 1.1, ClawRouter
- GPT-5.6 成为新安装默认模型，支持 `/think ultra`

---

## 对我们的意义

```
✅ Voice Wake (Android) - 可用于手机节点唤醒
✅ 远程编码会话 - 云端 worker 可能是未来方向
✅ Linux deb/AppImage - 部署更方便
✅ Gateway 恢复改进 - 稳定性提升
⚠️ Beta 版本，暂不升级，等稳定版
```

---

*来源: https://github.com/openclaw/openclaw/releases*
