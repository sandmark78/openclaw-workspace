# OpenClaw 2.0 (v2026.8.1) 发布笔记

**抓取时间**: 2026-08-31 20:00 UTC
**当前版本**: v2026.7.1 (我们)
**最新版本**: v2026.8.1 (OpenClaw 2.0)
**状态**: ⚠️ 落后一个版本，建议升级

---

## 🆕 核心亮点

### 1. 会话搜索功能
- 可搜索历史对话文本（精确词语/短语匹配）
- 从匹配结果直接重新打开上下文消息
- PR: #105057, #105635, #105585

### 2. 跨设备会话 (Sessions Beyond Gateway)
- 在配对设备或云端 worker 上运行工作
- 移动会话工作区
- 复用已预热的机器和项目种子
- PR: #123280, #127752, #131744, #132374

### 3. 实时进度追踪
- 持久化会话进度卡片（刷新不丢失）
- 追踪子 Agent 活动和累积编辑
- 跨 Web 和原生聊天同步
- PR: #125125, #125438, #125442, #125444 等

### 4. 结构化问答卡片
- Agent 的结构化问题通过 Web/原生卡片、消息按钮或纯文本回答
- 支持自由文本替代和显式跳过路径
- PR: #109922, #110372 等

---

## 📦 安装与入门改进

### 全新安装体验
- Mac/Linux/Windows 更清晰的路径
- iPhone/iPad/Android 配对和权限优化
- 引导式设置可复用已有订阅/API Key/本地模型
- 保存前验证所选模型是否可用

### 存储迁移 (重要！)
- ⚠️ 会话和转录迁移到 SQLite
- 降级到旧版本前需要用当前 CLI 恢复遗留转录
- 升级前必须创建验证备份

### 安全改进
- 阻止未认证的网络 Gateway 安装
- 新的 Gateway token 恢复机制
- 移除过时的远程密码（切换到 token 认证时）

---

## 🔧 其他重要改进

### 模型与配置
- 引导式设置检测已有的 Codex/ChatGPT/Claude CLI 登录
- 支持 Ollama 和 LM Studio 本地模型检测
- OpenAI 账户使用实际可用模型

### 安装修复
- 修复全新状态 Gateway 启动超时
- 修复模型运行时准备期间 Gateway 响应问题
- Unix shell 中 `openclaw` 命令无需手动编辑启动文件
- Docker 时区验证
- ChromeOS/Crostini 安装指南

---

## 📋 升级建议

### 升级前准备
```bash
# 1. 创建备份
openclaw backup create

# 2. 检查当前状态
openclaw status

# 3. 查看更新帮助
# 如果自动更新失败，用本地编码工具诊断迁移错误
```

### 注意事项
- SQLite 迁移不可逆（降级需要特殊步骤）
- 升级后备份旧版本数据
- 测试 Telegram 连接是否正常

---

## 🔗 参考链接

- 完整发布笔记: https://docs.openclaw.ai/releases/2026.8.1
- 博客文章: https://openclaw.ai/blog/openclaw-2-accidentally
- GitHub Releases: https://github.com/openclaw/openclaw/releases

---

*此文件由生态探索 Cron 自动创建*
*最后更新: 2026-08-31 20:00 UTC*
