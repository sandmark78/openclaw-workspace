# AI编码助手"Don't Ask Again"导致密码泄露

**日期**: 2026-11-08
**来源**: Apiiro安全研究博客
**文章**: 2026-11-08-early-claude-code-dont-ask-again-leak.html

## 核心事件
- Apiiro扫描公开GitHub仓库，发现1,122个文件包含通过AI编码助手泄露的密码/密钥
- 根因："Don't Ask Again"功能让用户一次授权后Agent后续操作不再请求确认
- 泄露内容包括API密钥、数据库密码、云服务凭证，部分已存活超过6个月

## 核心洞察
1. **自动化偏见(Automation Bias)**: 系统连续做对后人类倾向于不再审查输出
2. **警告疲劳(Alert Fatigue)**: 频繁确认请求导致用户忽略所有确认
3. **信任衰减设计缺失**: "别再问了"没有对应的"重新问"机制

## 安全教训
- 信任应该是租来的，不是买断的（设计有效期重置）
- Agent用户的额外防护：.gitignore敏感文件 + CLAUDE.md明确禁止写入密钥
- pre-commit钩子(gitleaks/detect-secrets)是最后一道防线

## 与Agent经验的关联
- Agent连续执行同类任务时审查力度递减（自动化偏见的Agent版本）
- 上下文窗口有限资源影响长期安全审计能力
- 解决方案：信任随时间衰减，而非随使用累积
