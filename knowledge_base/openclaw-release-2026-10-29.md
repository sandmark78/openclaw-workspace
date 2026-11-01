# OpenClaw 版本更新检查 (2026-10-29)

**检查时间**: 2026-10-29 20:00 UTC  
**当前版本**: 2026.7.1  
**最新稳定版**: 2026.10.9  
**最新预发布版**: 2026.10.10-beta.4  
**状态**: ⚠️ **落后 3+ 个月，建议升级**

---

## 📦 最新版本：2026.10.9

### 重点更新

#### 🔒 安全补丁
- **fast-uri 4.2.3**: 修复 MCP schema 验证中的 URI 方案/主机漏洞
- **nodemailer 10.1.4**: 修复 IMAP 发送者解析漏洞（防止伪造发送者）
- **MSAL Node 7.1.1**: Microsoft Teams 集成安全补丁
- **Zod collections**: A2UI 和 Discord 嵌入式应用 SDK 中的大集合提前拒绝

#### 🛡️ 工具安全
- `tools.fs.workspaceOnly` 现在应用于 Gateway 内置工具
- 委托变更仍需审批，媒体工具限制在工作区内

#### 🔐 凭据保护
- MCP CLI 检查不再暴露实时凭据
- Google OAuth 客户端密钥在日志中脱敏

#### 🔄 更新回滚安全
- Git 源回滚保留操作者编辑（不再重置 checkout）
- npm 回滚重试 Windows 瞬态拒绝，报告恢复步骤

#### 💾 数据恢复
- SQLite tokenizer 变更后恢复完整的 agent 数据库和过时全文索引
- 大文件转录归档迁移（不超 Node.js 字符串限制）
- 磁盘满后恢复（无需重启）

#### 🐛 其他修复
- Codex steering 消息中的本地媒体解析修复
- 进程清理报告改进
- 节点连接重新审批保持活跃
- macOS 停止时避免卸载服务
- CLI Node 运行时从文件系统根启动修复
- ACP 会话在请求的工作目录启动
- 模型刷新重叠防止失败
- SSH 端口 22 在 `openclaw gateway probe --ssh` 中正确处理
- 技能元数据（图标、主页）保留

### 发布验证
- npm: https://www.npmjs.com/package/openclaw/v/2026.10.9
- integrity: sha512-KbIl0/nKBO92FnJg7LFcEpFVQyOgSRfHNE9yxELg1Ebql7BjmBsdLL+1dDOLZnQtuwjt6Hy45CCrmYdJNA==
- release SHA: 8b18b5578f66eab1501cba4cef2310d88bfb9a41

---

## 🧪 预发布版本：2026.10.10-beta.4

- 状态：Beta 测试中
- 不建议生产环境使用

---

## 📊 版本对比

| 项目 | 当前 | 最新 | 差距 |
|------|------|------|------|
| 主版本 | 2026.7.1 | 2026.10.9 | 3 个月 |
| 安全补丁 | ❌ 缺失 | ✅ 已修复 | **高优先级** |
| 数据恢复 | ❌ 缺失 | ✅ 已改进 | 中优先级 |
| 回滚安全 | ❌ 缺失 | ✅ 已改进 | 中优先级 |

---

## 🎯 建议行动

### P0：立即升级（安全原因）
```bash
# 升级命令
openclaw update

# 或手动升级
npm install -g openclaw@2026.10.9

# 验证版本
openclaw --version
```

### 升级前准备
1. 备份配置：`cp openclaw.json openclaw.json.backup`
2. 备份工作区：`tar czf workspace-backup.tar.gz /home/node/.openclaw/workspace/`
3. 记录当前版本：`openclaw --version > version-before.txt`

### 升级后验证
1. 检查版本：`openclaw --version`
2. 检查服务状态：`openclaw gateway status`
3. 检查 Telegram 连接
4. 检查工作区完整性

---

## 📝 备注

- ClawHub 网站正常（clawhub.ai）
- 文档网站正常（docs.openclaw.ai）
- GitHub releases 页面正常
- 48 个 PR 合入 2026.10.9 版本
- 主要贡献者：@RomneyDa, @shakkernerd, @wr-web, @eleqtrizit

---

*此文件由生态探索任务自动创建*
*最后更新：2026-10-29 20:00 UTC*
