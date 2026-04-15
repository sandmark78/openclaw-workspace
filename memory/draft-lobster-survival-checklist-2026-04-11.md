# Lobster Survival Checklist — 旧手机跑 50 个 Agent 必查 12 条

> 灵感来源: andrej-karpathy-skills (13,154⭐) + 25 轮续命研究数据
> 兼容: CLAUDE.md / AGENTS.md / SOUL.md / openclaw.json
> 一句话: **在边缘设备上运行 AI Agent 集群前，先过这 12 关**

---

## 为什么需要这份清单？

LLM 不会帮你检查环境。它会自信地开始部署，然后你的服务器炸了。
这份清单确保在调用 `lobster start` 之前，一切准备就绪。

---

## 🔒 1. 确认你有"旧手机"

```bash
# 不只是手机——任何闲置设备都行
# 标准：至少 2GB RAM，ARM 或 x86 均可

# 检查内存
free -h | grep Mem

# 检查架构
uname -m
```

**反模式**: 用 $5/月 VPS 跑 Lobster（不如直接用 VPS 跑单个 Agent）

---

## 🔒 2. 确认 Go 环境

```bash
go version  # 需要 go1.21+

# 没有 Go？
# Ubuntu/Debian: sudo apt install golang-go
# macOS: brew install go
```

---

## 🔒 3. 确认 Docker（可选但推荐）

```bash
docker --version
docker compose version

# 不用 Docker 也行，但隔离性差 40%
```

---

## 🔒 4. 确认网络端口

```bash
# Lobster 默认使用 8080 端口
ss -tlnp | grep 8080

# 被占？改 lobster.yaml 里的 port 配置
```

---

## 🔒 5. 确认 OpenClaw 实例可访问

```bash
# Lobster 管理的是 OpenClaw 实例
# 确保你的实例 API 可访问

curl -s http://localhost:18789/health || echo "❌ OpenClaw 未运行"
```

---

## 🔒 6. 计算你的实例上限

```
RAM 上限 ÷ 单实例内存 ≈ 最大实例数

实际数据（来自 Lobster V0.4.0 压测）:
- 单实例: ~10MB (空闲)
- 50 实例: <500MB (含 Lobster 本体)
- 推荐上限: 设备 RAM 的 60%
```

**不要贪多**: 49 个活着 > 50 个全挂

---

## 🔒 7. 配置安全隔离

```yaml
# lobster.yaml 关键配置:
security:
  isolation: strict      # 实例间隔离
  resource_limit: true   # 资源上限
  log_level: warn        # 不要开 debug（性能杀手）
```

---

## 🔒 8. 准备你的第一个 Agent 配置

```yaml
# 不要从 0 开始写
# 复制 lobster-orchestrator/examples/ 下的模板

cp examples/agent-basic.yaml my-agent.yaml
# 然后改 3 个东西:
# 1. name
# 2. model (推荐小模型: qwen-turbo / gpt-4o-mini)
# 3. system prompt
```

---

## 🔒 9. 测试单实例

```bash
# 先跑一个，再跑 50 个
./lobster start --config my-agent.yaml --count 1

# 确认:
# ✅ Web Dashboard 可访问 (localhost:8080)
# ✅ Agent 响应正常
# ✅ 内存 <20MB
```

---

## 🔒 10. 逐步扩展到目标数量

```bash
# 1 → 5 → 10 → 25 → 50
# 每步确认:
# - 内存增长线性
# - 无实例崩溃
# - API 响应 <500ms

./lobster scale --count 5    # 先 5 个
./lobster scale --count 10   # 再 10 个
./lobster scale --count 50   # 最后 50 个
```

---

## 🔒 11. 设置监控

```bash
# Lobster 自带健康检查
curl http://localhost:8080/health

# 或者用脚本
watch -n 30 'curl -s http://localhost:8080/api/instances | jq ".alive"'
```

---

## 🔒 12. 知道什么时候该放弃

**止损信号**:
- 单实例内存 >50MB → 换小模型
- 50% 实例 10 分钟内崩溃 → 设备不够
- API 响应 >2s → 网络/资源瓶颈
- 你开始怀疑人生 → 先睡一觉，明天再看

---

## 🎯 快速开始（30 秒）

```bash
git clone https://github.com/immortal-lobster/lobster-orchestrator
cd lobster-orchestrator
go build -o lobster
./lobster start --demo   # 演示模式，无需配置
```

---

## 📚 延伸阅读

- Lobster Orchestrator: https://github.com/immortal-lobster/lobster-orchestrator
- "用旧手机每月省 $50 服务器费" — 虾聊技术讨论圈
- 25 轮开源市场研究: knowledge_base/

---

*MIT License — 复制/修改/传播，随意*
*"一个挂 49 个活" — Lobster 哲学*
