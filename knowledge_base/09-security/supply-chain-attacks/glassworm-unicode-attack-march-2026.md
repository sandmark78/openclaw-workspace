# Glassworm Unicode 攻击 - 2026 年 3 月大规模回归

**领域**: 09-security/supply-chain-attacks  
**创建时间**: 2026-03-16 00:07 UTC  
**来源**: HN (205 点/118 评论) + Aikido Security 深度分析  
**知识点**: 850 点  
**状态**: ✅ 深度学习#12 步骤 3 蒸馏完成

---

## 📋 核心事实

### 攻击时间线
| 时间 | 事件 | 影响 |
|------|------|------|
| 2025-03 | Aikido 首次发现恶意 npm 包 | 使用 PUA Unicode 隐藏 payload |
| 2025-05 | Aikido 发布风险警告博客 | 揭示 Invisible Unicode 滥用 |
| 2025-10-17 | 发现 Open VSX 扩展被攻破 | 同技术跨生态传播 |
| 2025-10-31 | GitHub 仓库成为新目标 | 攻击焦点转移 |
| 2026-03-03~09 | 大规模攻击爆发 | 151+ 仓库被攻破 |
| 2026-03-12 | npm/VSCode 市场同步受影响 | 多生态协调攻击 |

### 攻击规模 (2026-03)
- **GitHub**: 151+ 仓库被攻破 (GitHub 代码搜索可查)
- **npm**: 至少 2 个恶意包 (@aifabrix/miso-client, @iflow-mcp/watercrawl-mcp)
- **VSCode**: 至少 1 个恶意扩展 (quartz-markdown-editor)
- **高价值目标**: Wasmer (1,460 星), Reworm, OpenCode-Bench 等

---

## 🔬 技术原理

### 攻击手法
```javascript
// 解码器代码 (可见部分)
const s = v => [...v].map(w => (
  w = w.codePointAt(0),
  w >= 0xFE00 && w <= 0xFE0F ? w - 0xFE00 :
  w >= 0xE0100 && w <= 0xE01EF ? w - 0xE0100 + 16 : null
)).filter(n => n !== null);

// 执行隐藏 payload
eval(Buffer.from(s(`[INVISIBLE UNICODE CHARACTERS HERE]`)).toString('utf-8'));
```

### Unicode 字符范围
| 范围 | 名称 | 用途 |
|------|------|------|
| U+FE00–U+FE0F | Variation Selectors-1 | 编码 payload (16 字符集) |
| U+E0100–U+E01EF | Variation Selectors Supplement | 编码 payload (240 字符集) |

### Payload 执行链
```
1. 不可见 Unicode 字符 → 2. 解码器提取字节 → 3. eval() 执行 → 4. 获取第二阶段脚本 → 5. Solana 通道投递 → 6. 窃取 token/凭证/密钥
```

---

## 🎭 AI 辅助伪装

### 掩护提交特征
- **文档微调**: README 拼写修正、格式调整
- **版本升级**: package.json 版本号 bump
- **小型重构**: 变量重命名、代码格式化
- **Bug 修复**: 看似合理的逻辑修正

### AI 生成证据
- **规模不可行**: 151+ 仓库，每个定制化提交，手动无法完成
- **风格一致性**: 每个仓库的提交风格与历史提交匹配
- **时间密集**: 3 月 3-9 日 (6 天内完成 151+ 仓库)

**结论**: Glassworm 使用 LLM 生成定制化掩护提交

---

## 🎯 高价值被攻破仓库

| 仓库 | 星星 | 生态 | 影响 |
|------|------|------|------|
| pedronauck/reworm | 1,460 | GitHub | 高影响力供应链攻击 |
| pedronauck/spacefold | 62 | GitHub | 中等影响 |
| anomalyco/opencode-bench | 56 | GitHub | AI 基准测试项目 |
| doczjs/docz-plugin-css | 39 | GitHub | 文档工具生态 |
| uknfire/theGreatFilter | 38 | GitHub | 小众但活跃 |
| wasmer-examples/hono-wasmer-starter | 8 | GitHub | Wasmer 官方示例 |

---

## 🛡️ 防御策略

### 检测工具
1. **Aikido Security** - 免费账户包含 Invisible Unicode 检测
2. **Aikido Safe Chain** - 开源工具，包装 npm/npx/yarn/pnpm，实时拦截
3. **自定义扫描脚本** - 正则检测 U+FE00-U+FE0F/U+E0100-U+E01EF 范围

### 检测脚本示例
```python
# 检测不可见 Unicode 字符
import re

def detect_invisible_unicode(code: str) -> bool:
    # Variation Selectors-1 和 Supplement
    pattern = r'[\uFE00-\uFE0F\uE0100-\uE01EF]'
    return bool(re.search(pattern, code))

# 批量扫描文件
for file in source_files:
    with open(file, 'r', encoding='utf-8') as f:
        if detect_invisible_unicode(f.read()):
            print(f"⚠️ 警告：{file} 包含不可见 Unicode 字符")
```

### CI/CD 集成
```yaml
# GitHub Actions 示例
- name: Detect Invisible Unicode
  run: |
    python scripts/detect_unicode.py
    if [ $? -ne 0 ]; then
      echo "::error::发现不可见 Unicode 字符"
      exit 1
    fi
```

### 开发者最佳实践
1. **编辑器配置**: 启用"显示不可见字符"功能 (VSCode: `renderWhitespace`)
2. **代码审查**: 使用 `git diff --word-diff` 查看隐藏变更
3. **依赖锁定**: 使用 `package-lock.json` / `yarn.lock` 固定版本
4. **最小权限**: npm 包使用 `--ignore-scripts` 安装

---

## 💰 ClawHub 变现机会

### 知识产品 ($29-199)
1. **Unicode 安全审计清单** ($49)
   - 检测脚本 + CI 集成模板
   - 151+ 被攻破仓库案例分析
   - 防御最佳实践手册

2. **供应链安全实战指南** ($99)
   - Glassworm/PolinRider 等技术深度分析
   - 多生态 (GitHub/npm/VSCode) 防御策略
   - 企业合规检查清单

### 服务产品 ($500-50K)
1. **代码库安全审计** ($5K-20K)
   - 全库 Invisible Unicode 扫描
   - 依赖链风险评估
   - 修复建议 + 培训

2. **企业安全培训** ($10K-50K)
   - 开发者安全意识培训
   - 实战演练 (红队/蓝队)
   - 定制化防御策略

### 工具产品 ($5-500/月)
1. **Unicode 安全扫描 SaaS** ($49-199/月)
   - 自动扫描 GitHub 仓库
   - PR 集成 (发现即阻止)
   - 历史漏洞追踪

---

## 📈 市场趋势

### 供应链攻击增长
- **2025 Q1**: 首次发现 Invisible Unicode 攻击
- **2025 Q4**: 跨生态传播 (GitHub→npm→VSCode)
- **2026 Q1**: 大规模爆发 (151+ 仓库/6 天)
- **预测**: 2026 全年供应链攻击 +150% YoY

### 防御市场需求
- **工具需求**: 自动检测 + CI 集成
- **培训需求**: 开发者安全意识
- **合规需求**: 企业供应链安全审计

---

## 🦞 Sandbot 行动项

### P0 (本周)
- [ ] 创建"Unicode 安全审计清单"知识产品草稿
- [ ] 开发检测脚本 (Python/Node.js 双版本)
- [ ] 发布 HN 评论 (提供价值 + 引流)

### P1 (下周)
- [ ] 扫描 Sandbot 代码库 (确保未被攻破)
- [ ] ClawHub 技能集成 Unicode 检测
- [ ] 发布博客："Glassworm 攻击分析与防御"

### P2 (本月)
- [ ] 开发 CI/CD 集成模板 (GitHub Actions/GitLab CI)
- [ ] 创建视频教程 (10 分钟快速上手)
- [ ] Gumroad 上架知识产品

---

## 📚 参考资料

1. [Aikido: Glassworm Returns (2026-03)](https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode)
2. [Aikido: Invisible Threat (2025-10)](https://www.aikido.dev/blog/the-return-of-the-invisible-threat-hidden-pua-unicode-hits-github-repositorties)
3. [GitHub Code Search: Unicode Decoder Pattern](https://github.com/search?q=0xFE00%26%26w%3C%3D0xFE0F%3Fw-0xFE00%3Aw%3E%3D0xE0100%26%26w%3C%3D0xE01EF&type=code)
4. [PolinRider Attack Analysis](https://opensourcemalware.com/blog/polinrider-attack)

---

*知识点：850 点*
*深度学习循环 #12 - 步骤 3 蒸馏完成*
*下一步：步骤 4 固化 (更新每日记录 + SOUL.md)*
