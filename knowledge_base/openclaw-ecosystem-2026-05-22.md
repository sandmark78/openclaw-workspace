# OpenClaw 生态快照 - 2026-05-22

**抓取时间**: 2026-05-22 20:00 UTC  
**来源**: clawhub.ai, docs.openclaw.ai, GitHub Releases

---

## 🔴 重要：OpenClaw 版本更新

| 项目 | 值 |
|------|-----|
| **当前安装版本** | `2026.3.8` |
| **最新可用版本** | `2026.5.20`（2026-05-21 发布） |
| **差距** | ⚠️ 落后约 2 个月，建议升级 |

### 2026.5.20 关键变更

#### 新功能
- **Discord 语音会话增强**: 语音会话可跟随用户进入语音频道，支持多用户交接、DAVE 恢复
- **Policy 插件**: 新增策略驱动的频道一致性检查、doctor lint 修复、可选工作区修复
- **Exec 审批安全加固**: 移除旧的 `cat SKILL.md && printf` 兼容路径，技能文件必须通过 read 工具加载
- **xAI device-code OAuth**: 支持远程/无头模式授权 xAI，无需本地浏览器回调
- **OpenRouter 路由策略**: 支持 provider 级别 params.provider 路由策略
- **Codex harness 升级**: `@openai/codex` 升级到 0.132.0
- **本地模型精益模式**: `agents.list[].experimental.localModelLean` 可为单个 Agent 启用

#### 重要修复
- WhatsApp Baileys 升级到 7.0.0-rc12
- 浏览器截图遵循图片消毒限制
- Cron 分页修复（#83856）
- Doctor 移除无效模型配置（#77803）
- Doctor 新增明文密钥警告（#84718）
- 密钥加载 fail-closed 恢复（防符号链接攻击）
- WebChat 清理过时 typing 指示器
- macOS Peekaboo 桥升级到 3.2.1
- 多个 CLI/Doctor 修复

---

## ClawHub 统计

| 指标 | 数值 |
|------|------|
| 工具总数 | **52,700** |
| 用户数 | **180,000** |
| 下载量 | **12,000,000** |
| 平均评分 | **4.8** |

**注意**: 域名已从 `clawhub.com` 重定向到 `clawhub.ai`

---

## Docs 更新

- **Node.js 要求**: Node 24 推荐，Node 22 LTS（22.19+）兼容
- 文档结构全面更新，包含更清晰的入门指南
- 新增 DAVE 语音恢复、Policy 插件等文档

---

## 建议操作

```bash
# 检查当前版本
openclaw --version          # 当前: 2026.3.8

# 升级到最新版
npm install -g openclaw@latest

# 升级后运行 doctor
openclaw doctor --fix
```
