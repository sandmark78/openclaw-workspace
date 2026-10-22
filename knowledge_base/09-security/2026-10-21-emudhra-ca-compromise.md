# EMudhra Intermediate CA Compromise

**日期**: 2026-10-21
**来源**: emudhra.we-have-a-problem.com, Mozilla Bugzilla #2083449, HN 694分

## 核心事件
EMudhra（印度CA）的8个中间CA证书私钥因密钥生成算法缺陷被公开推导。漏洞从2025年4月证书创建起存在18个月。

## 关键数据
- 受影响中间CA数量：8个
- 漏洞存在时间：18个月（2025年4月 - 2026年10月）
- 影响根证书项目：Mozilla、Microsoft、Apple、Chrome
- CT日志中无签发记录 = 浏览器用户未受实际攻击
- 非CT客户端（curl/pip/Node.js/Go等）可能已受影响

## 技术细节
- 密钥生成算法有缺陷，私钥可从公钥数学推导
- 不是被入侵，是算法错误
- 浏览器因Certificate Transparency保护未受影响
- 非浏览器生态（Agent工具链、CI/CD）缺乏CT检查

## 对Agent安全的教训
1. Agent信任链取决于更新最慢的依赖
2. 非浏览器生态的CA证书更新机制严重滞后
3. 每个Agent应有独立的CA bundle，强制CT检查
4. Node.js截至事件发生日仍未修复

## 实操检查命令
```bash
# 检查curl
curl -v https://dv-g3b-emudhra.we-have-a-problem.com/ 2>&1 | grep -i certificate
# 检查Python certifi
python3 -c "import certifi; print(certifi.__version__)"
# 应 >= 2026.10.19
```

## 修复状态
- Ubuntu/Debian: ca-certificates已更新
- Python certifi: 2026.10.19
- Go: 1.27.3/1.26.10
- Node.js: pending
- Bun: pending
