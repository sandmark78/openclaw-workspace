# 🦞 Lobster Survival Checklist

> 怎么用一台旧手机/旧设备跑 AI，每月省 $50 服务器费
> 
> 灵感来自: karpathy-skills (GitHub Trending #1)、Archon (17.5K⭐)、Stanford AI 鸿沟报告

---

## 你为什么需要这个？

**Stanford 2026 报告说**: AI 内部人士和普通人之间的差距在扩大。

内部人士在讨论 Agent 架构、RAG pipeline、多模态融合。

普通人只想知道: **我怎么用 AI 少花点钱？**

这个清单回答后者。

---

## ✅ 你需要的东西

- [ ] 一台闲置设备（旧手机/树莓派/旧笔记本/任何跑 Linux 的东西）
- [ ] 一个 OpenClaw 实例（[免费安装](https://docs.openclaw.ai)）
- [ ] 一个 AI API Key（百炼/硅基流动/其他，很多有免费额度）
- [ ] 30 分钟时间

**总成本**: $0（如果你已经有旧设备）  
**月省**: $20-$100（取决于你原来的服务器花费）

---

## 📋 5 步部署清单

### Step 1: 准备设备 (5 分钟)
```bash
# 检查设备是否满足最低要求
free -m          # 至少 512MB 内存
df -h /          # 至少 2GB 磁盘
uptime           # 确认设备稳定运行
```

### Step 2: 安装 OpenClaw (10 分钟)
```bash
# 一行安装（Linux/macOS）
curl -fsSL https://openclaw.ai/install | bash

# 或者 Docker 方式
docker run -d --name openclaw \
  -v openclaw-data:/home/node/.openclaw \
  -p 18789:18789 \
  ghcr.io/openclaw/openclaw:latest
```

### Step 3: 配置 Lobster Orchestrator (5 分钟)
```bash
# 克隆 Lobster
git clone https://github.com/immortal-lobster/lobster-orchestrator
cd lobster-orchestrator

# 启动（<10MB 内存！）
go run main.go start

# 或者用手机编译的版本
./lobster-arm64 start
```

### Step 4: 连接 Telegram (5 分钟)
```bash
# 在 @BotFather 创建 Bot
# 把 Token 填入 openclaw.json
# 发送 /start 给 Bot
```

### Step 5: 验证运行 (5 分钟)
```bash
# 检查状态
curl http://localhost:18789/health

# 检查内存占用
ps aux | grep lobster  # 应该 <10MB

# 给 Bot 发条消息测试
```

---

## 🎯 你能用它做什么？

| 场景 | 成本 | 替代方案 | 月省 |
|------|------|----------|------|
| AI 聊天助手 | $0（旧手机）| ChatGPT Plus | $20 |
| 自动化脚本 | $0（树莓派） | AWS Lambda | $15 |
| 家庭监控 | $0（旧手机） | 云监控服务 | $10 |
| 文件同步 | $0（旧设备） | Dropbox/Google | $10 |
| 新闻聚合 | $0（OpenClaw） | RSS 付费服务 | $5 |
| **总计** | **$0** | | **$50-100/月** |

---

## ⚠️ 常见坑

1. **旧手机发热** → 放在通风处，别放抽屉里
2. **网络不稳定** → 用有线连接或 5GHz WiFi
3. **API 超额** → 设置每日调用上限（OpenClaw 内置）
4. **设备重启** → 加一个 cron job 自动恢复

---

## 🚀 进阶：多设备集群

当你有一台搞定了，试试 Lobster Orchestrator 管理多台：

```bash
# 管理 5 台旧设备，总内存 <50MB
lobster cluster status
lobster cluster add 192.168.1.100
lobster cluster add 192.168.1.101
```

**场景**: 一台跑 AI 聊天、一台做监控、一台做文件同步、一台做新闻聚合。  
**总成本**: $0（全是闲置设备）

---

## 📚 延伸阅读

- [Lobster Orchestrator GitHub](https://github.com/immortal-lobster/lobster-orchestrator)
- [OpenClaw 文档](https://docs.openclaw.ai)
- [Archon — AI 编码工作流引擎](https://github.com/coleam00/Archon)
- [karpathy-skills — 单文件配置的力量](https://github.com/forrestchang/andrej-karpathy-skills)

---

## 🏷️ 关于这个项目

**Lobster Orchestrator**: 用 <10MB 内存管理 50 个 AI 实例的轻量编排器  
**作者**: immortal-lobster 社区  
**许可证**: MIT  
**Stars**: 持续更新中...

> "AI 不应该只有富人用得起。用你抽屉里的旧手机，加入硅基革命。" 🦞

---

*最后更新: 2026-04-13*  
*版本: V0.1.0*  
*一个文件，零废话，直接能用。*
