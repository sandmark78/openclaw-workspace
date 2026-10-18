# OpenClaw 2026.10.10-beta.1 发布说明

**抓取时间**: 2026-10-18 20:00 UTC  
**来源**: https://github.com/openclaw/openclaw/releases  
**版本类型**: Pre-release (Beta)

---

## 🚀 核心亮点

### 1. Gateway 性能大幅提升
- **问题**: 繁忙主机和大型 agent 集群响应慢
- **解决**: 将更多 SQLite 工作移到 worker threads
- **影响**: 聊天轮次、会话列表、启动和空闲 Gateway 做更少的主线程工作
- **相关 PR**: #167965, #168002, #168093, #169005, #169164, #171685 等 14 个

### 2. 更新完成度提升
- **升级稳定性**: 从 2026.10.1 及更早 beta 版本的升级能正常完成
- **繁忙 Gateway**: 不再拒绝或回滚良好的更新
- **失败恢复**: 失败的更新不再留下半安装版本
- **平台修复**: macOS、Windows、Bun 安装的特定问题已修复
- **相关 PR**: #168849, #172249, #172196 等 14 个

### 3. 重启安全回复 ⭐
- **功能**: 中断和未完成的回复在 Gateway 重启后能恢复
- **保护内容**: 
  - 监视的子 agent 结果
  - 排队的轮次
  - 接受的 agent 更新
  - 操作者任务
- **相关 PR**: #172234, #172412, #169489 等 9 个

### 4. Cloud Sessions（云会话）
- **功能**: 在本地和云端之间移动会话
- **组织方式**: 按仓库组织云环境
- **环境配方**: 支持仓库环境配方和验证的 Node 工具链
- **快照进度**: 在第一个快照完成上传前显示启动进度
- **相关 PR**: #171690, #170892, #170862 等 7 个

### 5. 桌面应用本地 Gateway
- **Windows**: 桌面应用可运行本地 Gateway
- **macOS**: 新安装的 Tauri 版本以引导仪表板设置开始
- **首次运行**: 自动选择推理配置
- **相关 PR**: #169522, #169512, #169568, #169628

### 6. 新模型支持
- **Gemini 4 Argon**: 成为默认 Gemini 模型（与 Gemini 3.8 Flash 并列）
- **Nemotron 3.5 Super VL**: 新增支持
- **xAI Imagine Image 2.0**: 新增支持
- **Meta models**: 通过 Muse Code 运行
- **模型选择器**: 不再提供已退休的模型
- **相关 PR**: #171852, #172339, #172449, #172445 等 7 个

### 7. Apple 平台要求更新 ⚠️
- **最低要求**: macOS 26.2, iOS 26.2, Safari 26.2 或更新版本
- **影响**: 原生应用和 Control UI
- **相关 PR**: #168595

---

## 📊 贡献者感谢

感谢以下贡献者的工作：
- @obviyus, @609NFT, @Leon-SK668, @chelsealong, @RomneyDa, @joshavant
- @homeworld520, @Yolo521-bot, @giulianoaccorsi, @AntaresGG, @stop-time
- @davidcittadini, @SBC2016, @jeanmonet, @nv-kasikritc, @jacobtomlinson
- @JFLeonM 等

---

## 🔍 对 Sandbot 的影响

### 可受益功能
1. **重启安全回复**: 我们的 cron 任务和子 agent 结果在重启后不会丢失
2. **性能优化**: 如果未来 agent 数量增加，Gateway 会更稳定
3. **Cloud Sessions**: 未来可以考虑将会话迁移到云端

### 注意事项
1. **Apple 平台要求**: 如果使用 macOS/iOS 控制，需要升级到 26.2+
2. **Beta 版本**: 这是预发布版本，生产环境建议等待稳定版

---

## 📝 相关链接

- GitHub Releases: https://github.com/openclaw/openclaw/releases
- 完整变更日志: 查看 /tmp/openclaw-web-fetch-65740cfd6323c4a1.log

---

*此文件已真实写入服务器*
*创建时间: 2026-10-18 20:00 UTC*
*验证: cat knowledge_base/openclaw-2026-10-10-beta-release.md*
