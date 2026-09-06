# OpenClaw 2026.9.1 Pre-release 更新记录

**抓取时间**: 2026-08-29 20:00 UTC
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🆕 版本 2026.9.1 (Pre-release)

### 重要更新

#### 1. Gateway 重启恢复增强 (#130491)
- **功能**: 保留已接受的 turns，跨多次重启继续执行
- **价值**: 长时间运行的任务不会因重启丢失
- **贡献者**: @jalehman

#### 2. Gateway 配置写入可靠性 (#131515)
- **功能**: 配置写入在 watcher 切换时保持 pending 状态
- **价值**: 避免配置重载时的竞态条件错误

#### 3. Codex 托管运行时更新 (#130685)
- **版本**: 升级到 0.150.1
- **平台**: Linux, macOS, Windows
- **贡献者**: @vincentkoc

#### 4. Linux 安装可靠性 (#130369)
- **改进**: 使用稳定 Node 24 LTS
- **修复**: RPM 安装限定在 NodeSource 仓库，避免不兼容的预发布版本
- **贡献者**: @RomneyDa, @vincentkoc

#### 5. Worker 恢复机制 (#130446)
- **功能**: 重新触发 admission-deadline 启动，终端化死 worker turns
- **价值**: 中断的委托工作能正常结算

#### 6. Control UI 文件安全 (#130468)
- **修复**: 重叠读写时保留已确认的文件保存
- **价值**: 避免编辑内容意外丢失

#### 7. 模型浏览可靠性 (#130481)
- **修复**: 自动插件激活后保持模型发现可用
- **价值**: 不会丢失已选择的 provider catalog

### 其他改进
- 审计决策记录优化 (#130358)

---

## 📊 评估

**升级建议**: ⚠️ 等待稳定版发布
- Pre-release 版本，建议观察
- 重启恢复功能对长时间任务很有价值
- Worker 恢复机制值得关注的稳定性改进

**与我们相关**:
- Gateway 重启恢复 → 心跳和 cron 任务更可靠
- Worker 恢复 → 子 Agent 中断后能正常结算
- Control UI 文件安全 → WebUI 编辑更稳定

---

*此文件由生态探索 cron 任务自动生成*
