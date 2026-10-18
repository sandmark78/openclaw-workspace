# OpenClaw 2026.10.5-beta.2 更新日志

**记录时间**: 2026-10-12 20:00 UTC
**当前本地版本**: 2026.7.1
**最新 Beta**: 2026.10.5-beta.2

## 主要更新

### 1. Update 流程改进
- `openclaw update` 现在能自动处理 stale handoff leases、completed receipts、legacy 2026.9.8 recovery records
- 不再因 update-recovery-pending 而卡住
- 保留 service heap limit 和 webhook listeners
- 修复 Windows short-name paths 问题
- 不再把 accepted handoffs 或 successful updates 报告为 failures

### 2. Doctor 命令增强
- Doctor 在 path safety checks 阻止插件时，保留已安装插件的配置
- 遇到 malformed UTF-8 root memory files 时不修改，保持原样
- Recovery copies 在 migrations 前捕获 Canvas 和 Memory Core 文件
- 支持无 configured agents 的 installs

### 相关 PR
#169038, #169027, #168388, #168889, #169035, #169292, #168927, #168993, #169037, #169454, #168905, #168111, #169029, #169436, #169516

## ClawHub 生态
- 新增集成：GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello
- WhatsApp Web channel plugin 可用
- CLI 发布流程：`clawhub skill publish` / `clawhub package publish`

## 行动建议
- 考虑升级到 2026.10.5-beta.2（需评估稳定性）
- 利用 Doctor 命令检查系统健康
- 探索 ClawHub 新技能集成机会
