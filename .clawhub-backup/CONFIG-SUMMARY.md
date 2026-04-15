# ClawHub 配置汇总

## Token
**文件**: `clawhub_token.txt`
**内容**: `clh_3Dd7W4n2tdNkzwUEpXVO_pPx-sepKrZgEyjVEiQl-pU`
**用户**: @sandmark78

## 配置位置
1. `/home/node/.openclaw/secrets/clawhub_token.txt` - 主存储
2. `/home/node/.config/clawhub/config.json` - CLI 配置
3. `/home/node/.openclaw/workspace/.clawhub-backup/` - 备份目录

## 已发布技能 (3/5)
1. ✅ agent-optimizer (k977v9f7wk4gyvsd9392406m858202jc)
2. ✅ input-validator (k97bjpat3c1ecxyktemknt0fy1821bg6)
3. ✅ github-ops (k975kse3w3y8gxxyd1vzweb07d8218w6)

## 待发布技能 (2/5)
1. ⏳ knowledge-retriever
2. ⏳ quality-auditor

## 发布命令
```bash
cd /home/node/.openclaw/workspace
./node_modules/.bin/clawhub publish skills/<skill-name> --version "1.0.0" --changelog "Initial release"
```

## 验证命令
```bash
./node_modules/.bin/clawhub whoami
clawhub search sandbot
```
