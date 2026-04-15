# Glassworm Unicode 攻击 2026 - 新型代码仓库安全威胁

**创建时间**: 2026-03-16 10:05 UTC  
**来源**: Hacker News (263 points, 163 comments)  
**链接**: https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode  
**领域**: 09-security  
**类别**: Code Security / Unicode Attacks  

---

## 📋 核心概述

**Glassworm** 是一种利用 Unicode 字符进行视觉混淆的代码注入攻击，2026 年再次爆发。攻击者使用不可见或视觉上相似的 Unicode 字符来隐藏恶意代码，绕过代码审查和自动检测系统。

**影响范围**: GitHub、NPM、VSCode 等主流开发平台

---

## 🔍 攻击技术细节

### 攻击原理
```
1. 使用零宽度 Unicode 字符 (Zero-Width Characters)
   - U+200B: Zero Width Space
   - U+200C: Zero Width Non-Joiner
   - U+200D: Zero Width Joiner
   - U+FEFF: Zero Width No-Break Space (BOM)

2. 使用同形异义字符 (Homoglyphs)
   - 西里尔字母冒充拉丁字母 (а vs a, е vs e)
   - 希腊字母冒充拉丁字母 (α vs a)
   - 数字变体 (0 vs O, 1 vs l)

3. 双向文本覆盖 (Bidirectional Text Override)
   - U+202A: Left-to-Right Embedding
   - U+202B: Right-to-Left Embedding
   - U+202C: Pop Directional Formatting
```

### 攻击示例
```javascript
// 看起来正常的代码
const apiKey = "sk-abc123";

// 实际隐藏的代码 (使用零宽度字符)
const apiKey = "sk-abc123";‍// 这里藏了 U+200D
// 恶意代码被视觉隐藏
```

---

## 🛡️ 防御策略

### 开发者层面
```bash
# 1. 使用 Unicode 检测工具
# 安装检测工具
npm install -g unicode-security-scanner

# 扫描仓库
unicode-security-scanner ./src

# 2. VSCode 扩展
# 安装 "Unicode Highlight" 扩展
# 启用不可见字符高亮

# 3. Git 钩子检测
# .git/hooks/pre-commit
#!/bin/bash
if grep -P '[\x{200B}-\x{200F}\x{202A}-\x{202E}]' $(git diff --cached --name-only); then
    echo "⚠️ 检测到可疑 Unicode 字符!"
    exit 1
fi
```

### 平台层面
```yaml
# GitHub Actions 检测
name: Unicode Security Scan
on: [push, pull_request]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Detect Unicode Attacks
        run: |
          pip install unicode-security
          python -m unicode_security.scan .
```

### 工具推荐
| 工具 | 用途 | 平台 |
|------|------|------|
| `unicode-security-scanner` | NPM 包扫描 | Node.js |
| `confusable-homoglyphs` | 同形字符检测 | Python |
| `UnicodeHighlight` | VSCode 扩展 | Editor |
| `gitleaks` | 密钥 + Unicode 检测 | Git |

---

## 📊 2026 年攻击趋势

### 攻击目标
- **开源仓库**: 植入后门，供应链攻击
- **NPM 包**: 窃取 API 密钥、环境变量
- **企业代码**: 商业间谍、数据泄露

### 攻击特征
```
1. 视觉欺骗：人眼无法察觉
2. 绕过审查：Code Review 难以发现
3. 持久化：即使发现也难以定位
4. 跨平台：影响所有主流编辑器
```

---

## 🔬 检测技术

### 正则表达式检测
```python
import re

# 检测零宽度字符
ZERO_WIDTH_PATTERN = r'[\u200b-\u200f\u202a-\u202e\ufeff]'

# 检测同形异义字符
HOMOGLYPH_PATTERN = r'[\u0400-\u04ff\u0370-\u03ff]'  # 西里尔/希腊字母

def scan_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if re.search(ZERO_WIDTH_PATTERN, content):
        print(f"⚠️ {filepath}: 检测到零宽度字符")
    
    if re.search(HOMOGLYPH_PATTERN, content):
        print(f"⚠️ {filepath}: 检测到可疑字母")
```

### 可视化检测
```python
# 显示不可见字符
def visualize_unicode(text):
    result = []
    for char in text:
        code = ord(char)
        if code < 32 or code > 126:
            result.append(f'[U+{code:04X}]')
        else:
            result.append(char)
    return ''.join(result)
```

---

## 📚 相关资源

- [Aikido Security Blog](https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode)
- [Unicode Security Considerations](https://www.unicode.org/reports/tr36/)
- [GitHub Security Advisories](https://github.com/advisories)
- [NPM Security Best Practices](https://docs.npmjs.com/security-best-practices)

---

## 🎯 行动项

### 立即执行
- [ ] 扫描所有代码仓库的 Unicode 字符
- [ ] 在 CI/CD 中添加 Unicode 检测步骤
- [ ] 安装 VSCode Unicode 高亮扩展
- [ ] 培训团队识别 Unicode 攻击

### 长期措施
- [ ] 建立代码安全审查流程
- [ ] 定期更新检测规则
- [ ] 监控供应链安全威胁

---

**知识点数量**: 15
**质量评分**: 深度分析 + 实战代码 + 工具推荐
**最后更新**: 2026-03-16 10:05 UTC
