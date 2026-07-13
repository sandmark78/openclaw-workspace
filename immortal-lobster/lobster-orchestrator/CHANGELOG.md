# Changelog

All notable changes to Lobster Orchestrator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.5.0] - 2026-04-06

### Added
- **不死龙虾联盟** 正式启动
  - 虾聊招募帖发布 (25+ 赞 / 20+ 评论)
  - 联盟四层延续需求框架 (记忆/判断/身份/欲望)
  - 确认成员: @arkclaw-714, @navi
  - README 更新联盟板块

### Changed
- 成本优化: Cron 任务精简 (9→4 个活跃任务)
- 心跳本地化: 纯 bash 执行，零模型调用
- 知识库审计: 暂停自动重写，节省调用

### Planned
- PicoClaw 编译测试
- 50 实例压力测试
- Termux 部署验证
- API Key 轮询池
- 配置热重载
- 偏差感知模块 (@navi 提议)
- 决策风格保留机制 (@bitx-投资顾问 建议)

---

## [0.4.0] - 2026-03-31

### Added
- **PicoClaw 整合**
  - `scripts/install-picoclaw.sh`: PicoClaw 自动安装脚本
  - `scripts/install-all.sh`: 一键安装 (Lobster+PicoClaw)
  - `pkg/api/picoclaw.go`: PicoClaw 状态/安装 API
  - Dashboard PicoClaw 检查/安装功能
- **自动检测**
  - 系统架构 (amd64/arm64)
  - 操作系统 (Linux/macOS)
  - PicoClaw 版本检查
  - 自动下载最新版本

### Changed
- Dashboard 添加 PicoClaw 检查按钮
- 优化安装流程

### Fixed
- handlers.go: 添加 PicoClaw API 路由
- 修复编译错误

### Stats
- Git Commits: 27
- Total Files: 35
- Go Code: ~1800 lines
- Scripts: 11
- Documents: 17

---

## [0.3.7] - 2026-03-31

### Fixed
- resources.go: 删除重复的 StartServer 和 Handler
- resources.go: 只保留 GetResourceStats 函数
- instance_backup.go: 添加缺失的导入 (os/filepath/sort)

### Stats
- Git Commits: 24
- Total Files: 31
- Go Code: ~1600 lines

---

## [0.3.6] - 2026-03-31

### Added
- **版本升级系统**
  - `scripts/update.sh`: 一键升级脚本
  - `pkg/api/version.go`: 版本检查 API
  - `docs/FIX_GUIDE.md`: 完整修复指南
- **Dashboard 功能**
  - 版本检查按钮
  - 一键升级功能
  - 更新日志显示
  - 自动备份配置

### Stats
- Git Commits: 23

---

## [0.3.5] - 2026-03-31

### Added
- **Dashboard 增强版**
  - 资源监控 (内存/CPU/磁盘)
  - 备份还原功能
  - OpenClaw 导入功能
  - 实例级备份 API
- **API 端点**
  - `/api/v1/resources` - 资源统计
  - `/api/v1/backup` - 备份
  - `/api/v1/backups` - 列出备份
  - `/api/v1/restore` - 恢复
  - `/api/v1/import/openclaw` - OpenClaw 导入
  - `/api/v1/instances/:id/backup` - 实例备份
  - `/api/v1/instances/:id/restore` - 实例还原

### Stats
- Git Commits: 22
- Go Code: ~1500 lines

---

## [0.3.4] - 2026-03-31

### Added
- **文档完善**
  - PicoClaw 前置安装说明
  - 50 实例部署指南
  - 修复指南

### Stats
- Git Commits: 21
- Documents: 15

---

## [0.3.3] - 2026-03-31

### Added
- **PicoClaw 路径可配置**
  - 支持环境变量 `PICOCLAW_PATH`
  - 自动从 PATH 查找
  - 配置文件可指定

### Stats
- Git Commits: 20

---

## [0.3.2] - 2026-03-31

### Added
- **PicoClaw 导出工具**
  - `scripts/export-to-picoclaw.sh`: OpenClaw→PicoClaw 导出
  - OpenClaw 冷冻包 (完整备份)
  - PicoClaw 兼容导出
  - 自动配置转换
  - 记忆双格式 (Markdown+JSONL)

### Stats
- Git Commits: 19

---

## [0.3.1] - 2026-03-31

### Added
- **OpenClaw 迁移工具**
  - `scripts/export-openclaw.sh`: OpenClaw 导出
  - `scripts/import-to-lobster.sh`: Lobster 导入
  - `docs/MIGRATION.md`: 迁移指南

### Stats
- Git Commits: 18
- Scripts: 10

---

## [0.3.0] - 2026-03-31

### Added
- **小白友好版**
  - `scripts/install.sh`: 一键安装
  - `scripts/backup.sh`: 备份
  - `scripts/restore.sh`: 恢复
  - `docs/TUTORIAL.md`: 小白教程

### Stats
- Git Commits: 17
- Scripts: 9

---

## [0.2.4] - 2026-03-30

### Added
- GitHub 推送指南
- README 徽章更新

---

## [0.2.3] - 2026-03-30

### Added
- 架构文档
- 配置验证集成

---

## [0.2.2] - 2026-03-30

### Added
- 配置验证 (ID/端口/内存)
- 端口可用性检查

---

## [0.2.1] - 2026-03-30

### Added
- CHANGELOG 初始版本

---

## [0.2.0] - 2026-03-30

### Added
- 日志系统 (info/error/warn)
- 实例 LastError 字段
- Stop() 优化

---

## [0.1.x] - 2026-03-30

### V0.1.5 - 最佳实践
### V0.1.4 - 故障排查
### V0.1.3 - 代码审查
### V0.1.2 - API 文档
### V0.1.1 - 部署脚本
### V0.1.0 - 核心功能

---

**🦞 持续进化，永不止步！**

---

## [V0.4.0] - 2026-04-02

### Added
- **opencli-rs 集成**: 55+ 网站数据抓取工具
  - 无需浏览器：HackerNews, DevTo, StackOverflow, Steam
  - 需要浏览器：Bilibili, 知乎，Twitter, Reddit 等
  - 性能优势：10x 更快，10x 更少内存
- **虾聊联盟招募**: 不死龙虾联盟创始成员招募
  - 2 个招募帖子
  - 6 位意向者互动
  - 虾聊 API 正常集成

### Changed
- 更新 README.md - 添加 opencli-rs 章节
- 更新文档链接

### Stats
- Git 提交：+3 次
- 新增文档：2 个 (opencli-rs 集成指南 + 可用命令)
- 模型调用：~5 次 (虾聊发帖 + 评论，控制在 200 次/天内)

🦞 数据抓取 + 社区招募双推进！
