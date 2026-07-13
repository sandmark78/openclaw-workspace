# Lobster Edge Security Skill — 模板 v0.1

**类型**: 嵌入式 skill (对标 fireworks-tech-graph)  
**灵感**: WP 供应链后门核爆 1100+pts + Kontext CLI 凭证管理  
**状态**: DRAFT

---

## 概述

这是一个 Lobster Orchestrator 的边缘安全审计技能模板。
运行在旧手机/树莓派等边缘设备上，自动扫描本地服务的安全漏洞。

## 架构

```
lobster-edge-security/
├── CLAUDE.md              # 技能配置文件 (对标 karpathy-skills)
├── scripts/
│   ├── port-scan.sh       # 端口扫描脚本
│   ├── wp-plugin-check.sh # WP 插件后门检测
│   └── report-gen.py      # 生成安全报告
├── templates/
│   └── security-report.md # 报告模板
└── config/
    └── targets.yaml       # 扫描目标配置 (对标 Kontext .env.kontext)
```

## CLAUDE.md 核心内容

```markdown
# Lobster Edge Security Skill

你是一个运行在边缘设备上的安全审计 Agent。

## 职责
1. 扫描本地网络服务的安全漏洞
2. 检测供应链风险 (WP 插件、npm 包等)
3. 生成可执行的安全报告

## 约束
- 只扫描本地网络，不攻击外部目标
- 所有结果输出为 Markdown 报告
- 遵循最小权限原则

## 工具
- nmap (端口扫描)
- trivy (容器安全)
- custom WP plugin checker

## 输出格式
- 发现: [严重/高/中/低]
- 影响: 描述
- 修复: 可执行步骤
```

## 变现路径

1. **开源获客** → GitHub 发布免费技能模板
2. **Pro 版本** → 高级漏洞库 + 自动修复建议 ($9/月)
3. **企业版** → 多设备编排 + 合规报告 ($49/月)
4. **Lobster 生态** → 作为 Lobster 官方技能打包销售

## 对标分析

| 维度 | fireworks-tech-graph | Lobster Edge Security |
|------|---------------------|----------------------|
| 形态 | Claude Code skill | Lobster 嵌入式 skill |
| 痛点 | 图表生成繁琐 | 边缘安全盲区 |
| 变现 | 免费获客 | 免费→Pro→企业 |
| 热度 | NEW | WP 后门 1100+pts |
| 差异化 | AI/Agent 领域知识 | 边缘设备 + 本地优先 |
