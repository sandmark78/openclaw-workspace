# OpenClaw 生态探索记录 (2026-04-28)

**记录时间**: 2026-04-28 20:00 UTC  
**来源**: 自动生态探索 Cron

---

## 1. ClawHub (clawhub.com → clawhub.ai)

**重大变化**: 域名已重定向到 **clawhub.ai**

**统计数据** (最新):
| 指标 | 数值 |
|------|------|
| 工具总数 | 52.7k |
| 注册用户 | 180k |
| 总下载量 | 12M |
| 平均评分 | 4.8 |

**板块结构**:
- Skills - 社区技能
- Agent skill bundles - Agent 技能包
- Plugins - Gateway 插件
- Builders - 社区创作者

**观察**: 规模增长显著，从技能市场发展为综合工具平台。

---

## 2. OpenClaw 文档 (docs.openclaw.ai)

**最新版本支持**: Node 24 (推荐) / Node 22 LTS (22.14+)

**新增/值得关注的频道**:
- QQ bot (新增！中国用户友好)
- IRC (新增)
- LINE (新增)
- Nextcloud Talk (新增)
- BlueBubbles (新增)
- Mattermost (新增)
- Google Chat (新增)

**新增自动化功能**:
- Standing orders (持续指令)
- Task flow (任务流)
- Background tasks (后台任务)

---

## 3. GitHub Releases

**最新版本**: **v2026.4.26** (2026-04-26)

**关键更新**:
| 类别 | 变更 |
|------|------|
| 🔐 安全 | Gateway/device tokens 不再回显轮换的 bearer tokens |
| 🤖 Agent | sessions_spawn 模型别名解析修复，subagents.allowAgents 权限强制执行 |
| 🎙️ Voice | Control UI/Talk 改用 WebSocket 传输 Google Live 会话，不再回退 WebRTC |
| 🚀 启动 | Gateway 启动时复用配置快照插件清单，加速启动 |
| 🐛 修复 | EPIPE broken-pipe 不再导致 Gateway 崩溃 |
| 🔄 更新 | CLI 更新安装到临时目录后验证再替换，防止混合版本 |
| 🎮 Google Meet | 通过 OpenClaw browser control 加入，使用配置的浏览器 profile |
| 🔌 插件 | 支持 symlinked 插件目录，install 时跳过 test 文件扫描 |

---

## 4. 对我们的影响

### 值得关注
1. **QQ bot 频道**: 中文社区支持增强，可能值得探索
2. **v2026.4.26 更新**: 包含多项安全和稳定性修复，建议升级到最新版本
3. **ClawHub 规模扩大**: 52.7k 工具，社区生态更丰富，可探索新技能

### 行动建议
- 考虑升级 OpenClaw 到 v2026.4.26
- 探索 ClawHub 上是否有新的可用技能
- 评估 QQ bot 频道是否适合使用场景
