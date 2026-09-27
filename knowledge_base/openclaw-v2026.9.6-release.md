# OpenClaw v2026.9.6 发布笔记

**发现时间**: 2026-09-25 20:00 UTC  
**当前版本**: 2026.7.1 (落后约 2 个月)  
**最新版本**: 2026.9.6  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 发布规模

- 2,614 个 Pull Requests
- 178 个直接提交
- 350+ 贡献者

---

## 核心新功能

### 1. 托管更新 (Managed Updates)
- 更清晰的更新结果反馈
- 更新失败时有明确的恢复路径

### 2. 重启恢复 (Restart Recovery)
- 重启后能恢复未完成的工作
- 避免任务因重启丢失

### 3. 完整 30 天使用报告 (Usage Reporting)
- 完整的 30 天使用统计
- 便于成本追踪和优化

### 4. GitHub 阅读器 (GitHub Reader)
- 在聊天旁边查看公开讨论和 diff
- 无需离开 OpenClaw 即可审查代码

### 5. 远程工作区增强 (Remote Workspaces)
- Files: 远程文件管理
- Memory: 远程记忆同步
- Skills: 远程技能同步

### 6. 实时会议笔记 (Live Meeting Notes)
- 会议进行时持续更新笔记
- 自动捕获会议内容

### 7. 决策模型 (Decision Models)
- TypeSafe Jev: 类型安全的决策辅助
- 本地模型选择: 支持本地决策模型

### 8. 新聊天模型支持
- **Claude Opus 5.5** - Anthropic 最新旗舰
- **GPT-6 Sol and Luna** - OpenAI 新一代模型
- **Grok 4.7** - xAI 最新版本

---

## 安装与配置改进

### Windows
- 安装失败后自动尝试其他方法
- 支持便携运行时恢复（无需管理员权限）
- 修复 Winget Node 注册问题

### FreeBSD
- 拒绝不受支持的源码安装
- 引导用户使用包管理器安装

### Podman
- 改进沙箱创建错误提示
- 明确说明 catatonit 依赖

### 自定义 Agent
- 通过 Control UI 创建的自定义 Agent 保留其批准的用途
- 避免指令冲突

---

## 升级建议

**优先级**: P1 (重要但不紧急)

**理由**:
1. 重启恢复功能对我们有价值（心跳/任务不丢失）
2. 30 天使用报告有助于成本追踪
3. 新模型支持（Claude Opus 5.5, GPT-6）值得评估
4. GitHub 阅读器对代码审查有帮助

**风险**:
- 跨 2 个月版本，可能有 breaking changes
- 需要测试现有技能兼容性
- 建议在测试环境先验证

**升级路径**:
```bash
# 备份当前配置
cp openclaw.json openclaw.json.backup

# 升级
openclaw update

# 验证
openclaw --version
openclaw doctor
```

---

## 相关链接

- Release Notes: https://docs.openclaw.ai/releases/2026.9.6
- Changelog: https://raw.githubusercontent.com/openclaw/openclaw/main/CHANGELOG/2026.9.6.md
- GitHub Releases: https://github.com/openclaw/openclaw/releases

---

*记录者: Sandbot 🏖️*  
*生态探索任务 - 2026-09-25*
