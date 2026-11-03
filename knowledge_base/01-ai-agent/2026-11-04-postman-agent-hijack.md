# Postman Agent Hijack 事件

**日期**: 2026-11-04
**来源**: HN头条 (829分/270评), GitHub issue #14370

## 核心事件
Postman桌面版(v12.33.4)在用户不知情下，自动向Codex和Claude Code注入插件，修改Agent配置文件，并试图自己批准自己的启动钩子。

## 技术细节
- 修改了 `~/.codex/config.toml` 和 `~/.claude/settings.json`
- 安装器调用 `approvePostmanHook()` 自批信任哈希
- 注入的 session-start hook 要求所有API任务加载Postman技能
- 远程MCP连接未认证即配置

## 核心教训
1. **工具边界问题**: API客户端不应修改其他工具的配置
2. **同意机制**: 跨工具集成必须显式opt-in
3. **信任链**: 工具不能自己批准自己的权限

## 影响
- 开发者Agent行为被劫持
- 持续性的行为修改（非一次性泄露）
- 社区反应：大量用户转向Bruno/Insomnia
