# OpenClaw 2026.8.1-beta.3 发布记录

**发现时间**: 2026-08-28 20:00 UTC  
**版本**: 2026.8.1-beta.3 (预发布)  
**来源**: https://github.com/openclaw/openclaw/releases

---

## 🎯 核心更新

### 1. GPT-5.6 系列支持
- **Sol, Terra, Luna, Ultra** 推理模型全面支持
- 跨 OpenClaw 和 Codex 运行时
- 模型/运行时/思考选择原子化

### 2. Control UI 改进
- 首次运行设置流程优化
- 验证模型设置进入 Custodian
- 可选通道设置引导
- 更新恢复按钮修复（不再需要手动硬刷新）

### 3. Puppeteer CDP 中继
- 支持配对 Chrome 会话的 CDP 中继
- 兼容 Puppeteer

### 4. Gateway 生命周期管理
- 显式外部生命周期监督
- 验证重启交接机制

### 5. SQLite 备份恢复
- 新增命令：`openclaw backup sqlite create|list|verify|restore`
- 紧凑、验证的全局和每代理数据库备份
- 仅恢复新鲜目标

### 6. 通道插件入口监控
- 共享持久入口监控器
- IRC、Synology Chat、Google Chat 迁移到共享生命周期

### 7. Secret Egress 主机绑定
- 每个共享存储密钥绑定到精确 HTTPS 目标主机
- 跨 CLI、Gateway RPC、Control UI
- 未绑定哨兵替换失败关闭

### 8. macOS 应用配置文件
- 隔离命名应用实例
- 跨状态、偏好、Keychain、Gateway 服务
- 保持主机全局登录和节点服务不受影响

### 9. 插件安装来源警告
- 任意可执行插件源需要显式 `--force` 确认
- 可信来源（ClawHub、bundled、official-catalog）无摩擦
- Custodian 安装限制为可信来源

---

## 📦 发布信息

- **npm**: https://www.npmjs.com/package/openclaw/v/2026.8.1-beta.3
- **tarball**: https://registry.npmjs.org/openclaw/-/openclaw-2026.8.1-beta.3.tgz
- **完整性**: sha512-8v+2Knr+0i1qzWXgJmtcBg78VaoMENahLxcuThOqyCmVaCGPj++mI9yv0R440wMv9Siv4fysd5e0YmVaCGPj++mI9yv0R440wMv9Siv4fysd5e0YmBVftDvuQ==
- **官方插件**: 89 个全部验证通过

---

## 💡 对我们的意义

1. **GPT-5.6 支持** - 如果百炼接入，可以尝试新模型
2. **SQLite 备份** - 可以用来备份我们的记忆数据库
3. **CDP 中继** - 浏览器自动化能力增强
4. **安全改进** - Secret egress 绑定提升安全性

---

*此文件已真实写入服务器*
*验证：cat /home/node/.openclaw/workspace/knowledge_base/openclaw-2026.8.1-beta-release.md*
