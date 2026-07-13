# Lobster Orchestrator 升级指南

**版本**: V0.4.0  
**最后更新**: 2026-03-31

---

## 📋 版本信息

| 版本 | 日期 | 核心功能 |
|------|------|----------|
| **V0.4.0** | 2026-03-31 | 🆕 PicoClaw 整合 (一键安装/自动检测) |
| V0.3.7 | 2026-03-31 | 🔧 修复编译错误 |
| V0.3.6 | 2026-03-31 | 🔧 版本升级系统 + 修复指南 |
| V0.3.5 | 2026-03-31 | 📊 Dashboard 增强版 |
| V0.3.4 | 2026-03-31 | 📚 文档完善 |
| V0.3.3 | 2026-03-31 | 🔧 PicoClaw 路径可配置 |
| V0.3.2 | 2026-03-31 | 📦 PicoClaw 导出工具 |
| V0.3.1 | 2026-03-31 | 🔄 OpenClaw 迁移工具 |
| V0.3.0 | 2026-03-31 | 🎓 小白友好版 |

---

## 🚀 升级方式

### 方式 A: Dashboard 一键升级 (推荐)

1. 打开 Dashboard: `http://localhost:8080`
2. 点击右上角「⚙️ 检查更新」
3. 如果有新版本，点击「🚀 一键升级」
4. 等待升级完成
5. 重启服务

### 方式 B: 升级脚本

```bash
cd lobster-orchestrator
./scripts/update.sh
```

**升级过程**:
1. ✅ 检查最新版本
2. ✅ 备份当前配置
3. ✅ 拉取最新代码
4. ✅ 重新编译
5. ✅ 恢复配置
6. ✅ 显示更新日志

### 方式 C: 手动升级

```bash
# 1. 备份配置
cd lobster-orchestrator
cp configs/instances.yaml configs/instances.yaml.backup

# 2. 拉取最新代码
git pull origin master

# 3. 重新编译
go mod tidy
go build -o orchestrator ./cmd/orchestrator

# 4. 恢复配置
cp configs/instances.yaml.backup configs/instances.yaml

# 5. 重启
./orchestrator -config configs/instances.yaml
```

---

## 📦 全新安装

### 一键安装 (包含 PicoClaw)

```bash
curl -sL https://raw.githubusercontent.com/immortal-lobster/lobster-orchestrator/master/scripts/install-all.sh | bash
```

**安装内容**:
- ✅ 系统依赖 (Git/Go/curl/jq/wget)
- ✅ PicoClaw (最新版)
- ✅ Lobster Orchestrator
- ✅ 配置文件
- ✅ 目录结构

### 单独安装 PicoClaw

```bash
curl -sL https://raw.githubusercontent.com/immortal-lobster/lobster-orchestrator/master/scripts/install-picoclaw.sh | bash
```

---

## 🔧 版本回滚

如果新版本有问题，可以回滚到旧版本：

```bash
# 1. 查看历史版本
git tag

# 2. 回滚到指定版本
git checkout v0.3.6

# 3. 重新编译
go build -o orchestrator ./cmd/orchestrator

# 4. 重启
./orchestrator -config configs/instances.yaml
```

---

## 📊 升级检查清单

升级前检查：
- [ ] 备份当前配置 (`./scripts/backup.sh`)
- [ ] 检查磁盘空间 (`df -h`)
- [ ] 检查 Go 版本 (`go version`)

升级后验证：
- [ ] 检查版本 (`curl http://localhost:8080/api/v1/version`)
- [ ] 检查实例状态 (`curl http://localhost:8080/api/v1/instances`)
- [ ] 检查 Dashboard (`http://localhost:8080`)
- [ ] 检查 PicoClaw (`curl http://localhost:8080/api/v1/picoclaw/check`)

---

## ⚠️ 常见问题

### Q1: 升级失败

**解决**:
```bash
# 查看错误日志
cat logs/orchestrator.log

# 恢复备份
./scripts/restore.sh <备份名称>
```

### Q2: 编译失败

**解决**:
```bash
# 清理 Go 缓存
go clean -modcache

# 重新下载依赖
go mod tidy

# 重新编译
go build -o orchestrator ./cmd/orchestrator
```

### Q3: PicoClaw 未安装

**解决**:
```bash
# Dashboard 安装
# 点击「🦞 PicoClaw 检查」→「🚀 安装」

# 或命令行安装
./scripts/install-picoclaw.sh
```

### Q4: 配置不兼容

**解决**:
```bash
# 使用备份配置
cp configs/instances.yaml.backup configs/instances.yaml

# 或重新生成配置
./scripts/generate-config.sh 2
```

---

## 📈 版本规划

### V0.5.x (计划中)
- [ ] 50 实例压力测试
- [ ] Termux 部署验证
- [ ] API Key 轮询池
- [ ] 配置热重载

### V1.0.0 (目标)
- [ ] 生产就绪
- [ ] 完整测试覆盖
- [ ] 性能优化
- [ ] 文档完善

---

## 🦞 版本命名规则

遵循语义化版本 (SemVer):

```
主版本号。次版本号.修订号
  ↑      ↑      ↑
  |      |      └─ 向后兼容的问题修正
  |      └─ 向后兼容的功能新增
  └─ 不兼容的 API 修改

示例：
V0.4.0 - 新增 PicoClaw 整合功能
V0.3.7 - 修复编译错误
V1.0.0 - 首个稳定版本
```

---

## 📞 获取帮助

- **GitHub Issues**: https://github.com/immortal-lobster/lobster-orchestrator/issues
- **Discussions**: https://github.com/immortal-lobster/lobster-orchestrator/discussions
- **文档**: https://github.com/immortal-lobster/lobster-orchestrator/tree/main/docs

---

**🦞 版本管理规范，升级简单方便！**
