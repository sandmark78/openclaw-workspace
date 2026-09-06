# OpenClaw 2026.8.2 版本发布笔记

**抓取时间**: 2026-09-01 20:00 UTC  
**版本**: 2026.8.2  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🆕 主要新功能

### 1. Home Agent 侧边栏
- 快捷键：Cmd/Ctrl+Shift+H
- 可在右侧或底部 dock 打开 Home agent
- 支持预览/移除工作上下文快照
- 支持附加选中文本到消息
- 相关 PR: #133676

### 2. Linux 桌面伴侣应用 ⭐
- **格式**: .deb 和 AppImage (x86-64)
- **功能**: 
  - 连接本地或远程 Gateway
  - 从系统托盘打开 Quick Chat
  - X11 键盘快捷键支持
- **更新机制**: AppImage 支持签名验证
- **文档**: https://docs.openclaw.ai/platforms/linux

### 3. 后台会话
- 从 New Session 创建并运行后台会话
- 支持选择本地、云端或配对设备 placement
- 完成通知中可直接打开会话
- 相关 PR: #128050

### 4. 更安全的升级机制
- 保留更新的配置
- 在不完整的 session 迁移前停止
- 失败更新后可恢复停止的 Gateway
- 相关 Issues: #118244, #90551, #134206

### 5. 回复改进
- 工具工作完成后返回最终答案
- 修复停在工具输出或初始确认的对话
- 相关 PR: #133520, #133979

### 6. 语音功能增强
- 内部推理不进入语音
- 保留工具生成的音频
- 修复浏览器 Talk turns 问题
- 相关 PR: #133615, #133324, #134170, #134138

### 7. 浏览器控制改进
- macOS 和 Linux Chrome 扩展可唤醒配对的本地 relay
- 不需要运行 Gateway 即可使用
- 需要更新的原生主机和支持 relay wake-up 的扩展
- 相关 PR: #128379

### 8. 4 个新 Control UI 主题 🎨
- **CRT** - 复古 CRT 显示器风格
- **Manuscript** - 手稿/文档风格
- **Rosé** - 玫瑰色调
- **Miami** - 迈阿密风格
- 主题选择离线保存，重载时不会闪烁错误主题
- 相关 PR: #133495

---

## 📊 对 Sandbot 的影响

### 可能受益的功能
1. **Linux 桌面应用** - 如果老大用 Linux，可以直接从托盘快速聊天
2. **后台会话** - 可以在不中断当前工作的情况下运行长任务
3. **更安全的升级** - 减少升级失败风险
4. **新主题** - 可以让 WebUI 更好看 😎

### 建议行动
- [ ] 检查当前版本是否已经是 2026.8.2
- [ ] 如果是旧版本，考虑升级
- [ ] 测试 Linux 桌面应用（如果适用）
- [ ] 尝试新主题

---

## 🔗 相关链接
- 完整 Release Notes: https://github.com/openclaw/openclaw/releases/tag/2026.8.2
- Linux 指南: https://docs.openclaw.ai/platforms/linux
- 控制 UI 文档: https://docs.openclaw.ai/web/control-ui

---

*此文件由生态探索 cron 任务自动创建*
*最后更新: 2026-09-01 20:00 UTC*
