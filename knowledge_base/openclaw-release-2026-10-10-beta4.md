# OpenClaw 2026.10.10-beta.4 发布记录

**抓取时间**: 2026-10-27 20:00 UTC  
**版本**: 2026.10.10-beta.4 (Pre-release)  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 主要修复

### 1. 自动化增强 (#176422)
- **改进**: 保留认证操作者权限用于显式同会话计划后续任务
- **细节**: 包括一次性 next_check 重新设置，同时保留角色、会话、取消、目标和工具策略撤销边界
- **贡献者**: @RomneyDa

### 2. Gateway 安全加固 (#179199)
- **改进**: 在启动和配置重载时，保持环境引用的 hooks.token 不暴露给 agent host-exec 和 CLI 子环境
- **细节**: 同时保留显式每命令覆盖
- **贡献者**: @VACInc, @RomneyDa

### 3. Memory Wiki 保护 (#175707, #179657)
- **改进**: 当 OKF 概念页重新导入或从生产者包移除时，保留人工编写的 Notes
- **细节**: 包括更改的生产者内容和没有标记 Notes 槽的遗留页面
- **相关 Issue**: #175700
- **贡献者**: @YangManBOBO, @RomneyDa

### 4. Claude CLI 会话保持 (#178955)
- **改进**: 在 Control UI 启动的会话中，子 agent 完成或通道轮次运行时保持原生 Claude 会话及其上下文
- **细节**: 不再每次从保存的历史记录重新播种
- **修复 Issue**: #178953
- **贡献者**: @Marvinthebored, @RomneyDa

### 5. 模型目录优化 (#178522)
- **改进**:  honor 配置的主账户 pin 来决定模型就绪状态
- **细节**: 原生 Claude CLI 模型不再在选择的令牌配置文件就绪时显示为缺少认证
- **相关 Issue**: #178502
- **贡献者**: @ericcaiwx-star

---

## 关键贡献者
- @RomneyDa (核心维护)
- @VACInc (安全)
- @YangManBOBO (Memory Wiki)
- @Marvinthebored (Claude CLI)
- @ericcaiwx-star (模型目录)

---

## 对 Sandbot 的影响
- **Memory Wiki**: 我们的知识库系统可能受益于 Wiki 保护机制
- **自动化**: 心跳和 cron 任务的权限处理更稳健
- **安全**: Gateway token 保护增强，值得检查我们的配置
