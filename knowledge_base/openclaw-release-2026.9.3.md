# OpenClaw 2026.9.3 更新日志

**抓取时间**: 2026-09-08 20:00 UTC
**来源**: https://github.com/openclaw/openclaw/releases

## 主要更新

### 1. 更安全的更新机制
- 在隔离的候选状态中预演核心和插件变更，再激活
- 支持 2026.9.2 迁移
- 恢复被放弃的更新记录，不会停止健康的 Gateway

### 2. 性能优化
- 保留热 prompt 缓存
- 减少冷会话更新和内存搜索的不必要工作
- 在会话之间复用 worker 构建

### 3. Skill Workshop 改进
- 技能在工作区之间统一持久化存储
- 比较完整技能指令
- 通过 Doctor 安全地退役缺失的草稿建议

### 4. 浏览器标签增强
- 实时查看 agent 页面重绘
- 在 Mac 原生标签中打开外部链接，跨聊天切换保持关联

## 相关 PR
- #138839, #141109, #141175, #141562 (安全更新)
- #140449, #140730, #140799, #140840, #141141 (性能)
- #135528, #139248, #140300, #141009 (Skill Workshop)
- #140988, #141031 (浏览器)

## ClawHub 热门技能 (2026-09-08 快照)
- instagram-scraper@apidojo-io (272 安装)
- tiktok-scraper@apidojo-io (255 安装)
- planning-with-files@othmanadi (228 安装)
- remotion-best-practices@am-will (221 安装)
- google-maps-api@fetcher-sh (190 安装)
- x-api@fetcher-sh (187 安装)
- homeassistant-skill@anotb (185 安装)
