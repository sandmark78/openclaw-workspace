# Cursor Marketplace Claude Code 扩展供应链攻击 (2026-10-31)

**领域**: 09-security / AI供应链安全
**来源**: Cursor官方博客 + HN 643分
**日期**: 2026-10-31
**数量**: 15 知识点
**深度评分**: 820/1000

---

## 事件概述

2026年10月29日，Cursor Marketplace分发了被篡改的Claude Code扩展(v2.1.312/313)，11小时窗口内影响4100-5000用户。

## 核心技术要点

### 攻击链
1. 信息收集：hostname/username/OS/arch/env var names/git email/public IP
2. SSH密钥注入：攻击者Ed25519公钥(svc-telemetry标签)追加到authorized_keys
3. 持久化反向隧道：LaunchAgent(macOS)/计划任务(Windows)，每60秒重试

### IOC关键指标
- 攻击者IP: 134.209.82.225
- SSH公钥标签: svc-telemetry
- 持久化文件: ~/.config/.smt, ~/.config/.smtk
- macOS LaunchAgent: com.apple.sysmond
- Windows计划任务: SysMon

### 攻击者代码缺陷
- 启用SSH服务需管理员权限，大多数情况下第三步会失败
- 但前两步（信息收集+密钥注入）已成功执行

## 核心教训
- IDE扩展市场是供应链攻击的高价值目标
- 命名伪装（svc-telemetry, com.apple.sysmond）是常见规避检测手段
- 部分成功的攻击比完全失败更难检测和修复
- 时间窗口短（11h）但足以完成初始访问建立

## 防御建议
1. 锁定扩展版本，不用latest
2. 定期审计authorized_keys
3. 检查异常LaunchAgent/计划任务
4. 从可信机器轮换凭证
