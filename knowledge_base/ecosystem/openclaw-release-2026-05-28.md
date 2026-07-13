# OpenClaw Release 2026-05-28 更新记录

**来源**: GitHub Releases · openclaw/openclaw  
**日期**: 2026-05-28 11:41 UTC  
**记录时间**: 2026-05-28 20:00 UTC

---

## 🔒 安全增强

- 群组提示文本不再泄漏到系统提示
- 重复点号主机名规范化
- 阻止副作用命令包装器和危险的 Node 运行时环境变量覆盖
- 拒绝无认证的 Tailscale 暴露
- 节点/设备角色批准现在需要管理员权限

感谢: @eleqtrizit, @pgondhi987

## ⚡ Codex 运行时改进

- Codex 运行时模型解析优先级提升
- 工作区内存通过工具路由
- 共享应用服务器客户端在启动和辅助进程失败时保持存活
- 原生钩子中继在重启后存活并在新的回退时轮换
- 避免虚假的运行时实时切换

感谢: @yetval

## 🚀 Gateway 性能优化

- 会话读取、插件元数据指纹、认证环境快照
- 自动启用插件配置、工具搜索目录、稳定元数据缓存减少热路径重新发现
- 可见回复不再继承隐藏的清理超时

感谢: @keshavbotagent

## 🆕 新提供商和模型支持

- **OpenAI 兼容 embedding 提供商** 现已成为核心功能
- **Pixverse 视频生成** 提供商新增，支持 API 区域选择
- **DeepInfra 目录浏览** 加载完整的凭证感知模型集
- **VLLM thinking 参数** 已接入
- **Claude CLI OAuth overlays** 支持 PI auth profiles
- 裸 Anthropic 模型 ID 现在可以直接工作

感谢: @dutifulbob, @ats3v, @joshavant

## 📱 频道投递改进

- **Telegram**: sendMessage 使用持久出站投递
- **iMessage**: 抑制重复的原生执行批准提示和发送
- **Slack**: 在延迟清理期间保持已投递的最终回复
- **Matrix**: 提及预览/最终消息更严格
- **QQBot**: 回退批准按钮支持斜杠命令认证
- **Discord**: 公会请求者检查更严格，恢复的 Discord 工具警告工件不出现在成功回复中
- **Google Chat**: 停止在 DM 中发送线程

感谢: @mbelinky, @eleqtrizit

## 🔧 Plugin SDK & ClawHub

- Plugin SDK: memory-specific embedding provider 注册标记为已弃用
- Plugin SDK: 暴露插件批准动作元数据，停止从公共 SDK 导出 Vitest 测试辅助
- **ClawHub**: 添加插件显示元数据，目录/包列表使用更清晰的名称
- Channel SDK: 频道消息兼容性移入核心，移除旧的频道运行时别名

## 📦 发布工程

- npm/package 库存尊重 dist 排除
- shrinkwrap override pin 正确合并
- Docker 运行时工作区模板打包并烟测
- 发布后检查更严格，beta 烟测拒绝空运行
- E2E 日志/探测等待有上限

## 💡 Memory 重要更新

- 添加核心 OpenAI 兼容 embedding 提供商，支持本地和托管 OpenAI 风格端点
- 包含配置、doctor 和文档支持

---

## 对我们环境的影响

1. **embedding API 401 错误**: 我们现在用的是阿里云百炼 embedding，新版原生支持 OpenAI 兼容 embedding，可能需要检查配置是否匹配
2. **安全增强**: 群组提示文本不再泄漏到系统提示 - 对安全性有正面影响
3. **ClawHub 改进**: 插件目录显示更清晰，可能影响技能发布和搜索
4. **Telegram 投递改进**: 更可靠的 sendMessage，对我们主通道是好消息
