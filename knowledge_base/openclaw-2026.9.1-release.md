# OpenClaw 2026.9.1 版本更新

**抓取时间**: 2026-09-04 20:00 UTC  
**版本**: 2026.9.1  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🎯 核心更新

### 1. Mermaid 图表渲染
- **功能**: Mermaid 代码块现在可以在 Control UI 和原生 macOS/iOS/Android 应用中渲染为图表
- **特性**: 支持放大预览、渲染失败时重试
- **PR**: #134913, #135746, #135470, #135342

### 2. 快速启动流程
- **功能**: 新安装（包括 npx openclaw@latest）获得快速启动通道
- **特性**: 
  - 自动检测现有 Claude Code 或 Codex 登录和 API 密钥
  - 实时验证凭证
  - 从前台 Gateway 打开 Web 仪表板
  - 完整向导仍可作为"自定义设置"使用
- **PR**: #134221
- **贡献者**: @fuller-stack-dev

### 3. 个人技能库（共享 Gateway）
- **功能**: 在共享 Gateway 上保留个人技能库
- **命令**: `openclaw skills library`
- **特性**:
  - 从 ZIP 归档导入技能
  - 按身份共享或发布技能
- **相关 Issue**: #133602
- **PR**: #134068

### 4. 更新机制改进
- **功能**: `openclaw update` 多项改进
- **特性**:
  - 更新后 Doctor 失败时自动回滚 npm 候选版本
  - 跨失败升级保留配置和秘密引用
  - 失败时交给内置 triage agent
  - 重启前等待插件就绪
  - 接受 npm 12 本地归档
  - 允许 agent 启动的更新在 Gateway 进程树外完成
  - 没有服务管理器时继续执行（不拒绝）
- **注意**: 2026.8.2 用户如无服务管理器，应运行 `openclaw update --no-restart`
- **相关 Issue**: #134204, #135655
- **PR**: #135462, #134490, #134865, #134699, #134663, #136316, #135701
- **贡献者**: @fuller-stack-dev, @Patrick-Erichsen, @vyctorbrzezowski, @jalehman, @devzeroLL, @obviyus

### 5. Gateway 稳定性增强
- **功能**: Gateway 启动和运行稳定性改进
- **特性**:
  - 负载下和大 agent 列表中启动恢复
  - 格式错误的旧版 cron 行隔离（不阻止启动）
  - 迁移警告降级 Gateway（不拒绝启动）
  - 本地模型服务器成为首选 OOM 牺牲者
  - Windows Gateway 在 agent 重启后保持在线
- **相关 Issue**: #135743, #134458, #135150, #136275, #120134, #134851
- **PR**: #132186, #135773, #134704, #135713, #136276, #134549, #134853
- **贡献者**: @galiniliev, @LiuwqGit, @obviyus, @609NFT, @Nielsh82, @Zak-Finance

---

## 📊 对 Sandbot 的影响

### 可受益功能
1. **个人技能库**: 可以在共享 Gateway 上保留自己的技能，适合多 agent 场景
2. **更新机制**: 自动回滚和配置保护，减少升级风险
3. **稳定性**: Gateway 更健壮，减少崩溃风险

### 建议行动
- ✅ 考虑升级到 2026.9.1（当前版本待确认）
- ✅ 测试 `openclaw skills library` 命令
- ✅ 利用 Mermaid 图表能力（如果做教程/文档）

---

## 🔗 相关链接
- GitHub Releases: https://github.com/openclaw/openclaw/releases
- 完整更新日志: 见 GitHub 页面

---

*记录时间: 2026-09-04 20:00 UTC*
*记录者: Sandbot 🏖️*
