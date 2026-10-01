# OpenClaw v2026.9.6 发布记录

**抓取时间**: 2026-09-29 20:00 UTC  
**当前版本**: 2026.7.1 (我们)  
**最新版本**: 2026.9.6  
**落后程度**: ~2 个月

---

## 发布规模

- 2,614 个 PR
- 178 个直接提交
- 350 个贡献者

---

## 核心新功能

### 1. 托管更新 (Managed Updates)
- 更清晰的更新结果反馈
- 更新失败时有恢复路径

### 2. 重启恢复 (Restart Recovery)
- 重启后恢复未完成的工作
- 避免中断导致的工作丢失

### 3. 完整 30 天使用报告 (Usage Reporting)
- 完整的 30 天使用统计
- 帮助追踪使用模式

### 4. GitHub 阅读器 (GitHub Reader)
- 在聊天旁边查看公开讨论和 diff
- 无需切换上下文

### 5. 远程工作区增强 (Remote Workspaces)
- Files (文件管理)
- Memory (记忆)
- Skills (技能)

### 6. 实时会议笔记 (Live Meeting Notes)
- 会议进行时实时更新笔记
- 自动捕获和整理

### 7. 决策模型 (Decision Models)
- TypeSafe Jev
- 本地决策选项

### 8. 自定义 Agent 持久化
- 通过 Control UI 创建的自定义 Agent 保留其批准的用途
- 后续对话保持指令

---

## 新增模型支持

| 模型 | 提供商 |
|------|--------|
| Claude Opus 5.5 | Anthropic |
| GPT-6 Sol | OpenAI |
| GPT-6 Luna | OpenAI |
| Grok 4.7 | xAI |
| Meta Muse Spark 1.3 | Meta |
| Anthropic Fable 5.1 | Anthropic |
| OpenAI GPT-6 Astra | OpenAI |
| GPT Image 2.5 | OpenAI/fal |

---

## 安装改进

### Windows
- 安装失败后可继续（尝试其他选项）
- 便携恢复无需管理员权限
- 识别完整路径配置的 JS CLI 启动器

### FreeBSD
- 拒绝不支持的源码安装
- 引导用户使用包管理器安装

### Podman
- 缺失 host init helper 时给出修复说明
- 需要安装 catatonit

---

## 安全更新 (2026.8.33 LTS)

- Prometheus metrics 授权加固
- Discord asset/voice 所有权检查
- Nodemailer 安全建议清除
- 所有 2026.8.2 安全公告已协调

---

## macOS 特别说明

2026.9.6 macOS 版本在 2026-09-24 重建：
- 原始构建启动崩溃 (#156861)
- 09:52 UTC 替换为重建、公证版本 (#156881)
- npm 包未受影响

---

## 升级建议

**优先级**: P1 (重要)

**理由**:
1. 重启恢复功能对工作连续性很重要
2. 新模型支持（Claude Opus 5.5, GPT-6 系列）值得评估
3. GitHub 阅读器对代码工作有帮助
4. 安全更新已累积 2 个月

**风险**:
- 跨 2 个版本升级，需要仔细阅读迁移指南
- 建议在升级前备份 workspace
- 先在测试环境验证

**升级步骤**:
```bash
# 1. 备份当前工作区
cp -r /home/node/.openclaw/workspace /home/node/.openclaw/workspace.backup.$(date +%Y%m%d)

# 2. 查看迁移指南
# https://docs.openclaw.ai/releases/2026.9.6

# 3. 执行升级
openclaw update

# 4. 验证
openclaw --version
```

---

*此文件已真实写入服务器*
*验证路径*: `/home/node/.openclaw/workspace/knowledge_base/openclaw-release-2026.9.6.md`
