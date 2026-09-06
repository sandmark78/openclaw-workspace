# OpenClaw 生态探索 - 2026-08-04

## ClawHub 热门技能 (新发现)

| 技能 | 作者 | 用途 | 热度 |
|------|------|------|------|
| daily-trending | enchograph | 获取今日热榜 (tophub.today) | 79 |
| humor-up | kimmyplusli | 提升文案幽默感 | 18 |
| word-docx | ivangdavila | 创建/编辑 Word 文档 | 140 |
| agent-browser | matrixy | 无头浏览器自动化 | 124 |
| email-compat | shbernal | HTML 邮件兼容性 | 31 |
| 倪海厦skill | jangviktor-web | 经方中医 AI | 58 |
| self-improvement | mike5230odense | 自我学习改进 | 35 |
| prisma-database-setup | prisma | Prisma 数据库配置 | 7.2k |
| nemesis-c2-bridge | mightypi | WiFi 攻击代理控制 | 56 |
| baoyu-post-to-wechat | jimliu | 宝玉发帖到微信 | - |

## GitHub Releases 更新

### 最新修复 (稳定版)
- **npm 插件更新**: 修复单例数组元数据问题，官方插件可正常安装更新
- **Codex 进度回复**: 修复 GPT/Codex 在进度消息后停止的问题
- **Memory Core 启动修复**: 从数据库损坏中恢复，避免重启循环
- **WSL 状态权限**: 容忍 EROFS chmod 操作
- **遗留迁移恢复**: 迁移残留不再阻塞启动
- **托管插件更新**: 修复 npm lock 元数据过期问题

### Pre-release 2026.7.2 (实验性)
- **状态安全与恢复**: 
  - 隔离存储 (quarantine store) 在主数据库损坏时保护数据
  - SQLite 崩溃可恢复快照
  - 文件系统发布崩溃持久化
  - Schema 升级数据丢失拒绝
  - 回滚写入器快照恢复

## 评估

**值得关注的技能**:
1. `daily-trending` - 适合新闻聚合场景
2. `word-docx` - 文档生成实用
3. `self-improvement` - 自我学习机制值得研究

**系统更新**:
- Memory Core 修复对稳定性很重要
- 2026.7.2 的状态安全特性值得升级 (但需等稳定版)
