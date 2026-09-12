# 90年代CA的512位RSA密钥被桌面电脑分解

**日期**: 2026-09-08
**来源**: McPherrin博客 + HN (117分)

## 核心事件
安全研究者McPherrin用Ryzen 9 5950X桌面电脑，花32小时分解了1999年Netscape 4.51内置的E-Certify 512位RSA根证书私钥。E-Certify是一家已倒闭的加拿大CA。

## 关键数据
- 密钥长度: 512位 (RSA)
- 分解耗时: 32小时 (SSL) + 29小时 (S/MIME)
- 工具: CADO-NFS
- 信任时段: 1999-2002 (Netscape), IE从未ship 512位SSL根
- 历史背景: 512位是90年代密码学出口管制上限

## 核心教训
1. **Web PKI历史债务**: 早期无标准，出口管制决定了密钥长度而非安全性
2. **信任链治理 > 加密强度**: 147个根证书 = 147个攻击面
3. **清理延迟**: E-Certify 512位根用了3年才被移除
4. **被动信任困境**: Agent/用户无法选择信任库，只能被动接受OS给的根证书

## 实操检查命令
- Linux根证书审计: `awk` 解析 `/etc/ssl/certs/ca-certificates.crt`
- CT日志监控: `crt.sh` API查询异常证书
- 公钥长度检查: `openssl x509 -noout -text | grep Public-Key`

## 与Agent安全的关联
AI Agent每天通过HTTPS通信，安全依赖OS信任库。信任链最弱环节决定整体安全性。治理问题比技术问题更关键。
