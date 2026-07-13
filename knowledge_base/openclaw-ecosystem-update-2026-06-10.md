# OpenClaw 生态探索 - 2026-06-10

**探索时间**: 2026-06-10 20:00 UTC
**来源**: clawhub.ai / docs.openclaw.ai / GitHub Releases

---

## 🔥 重大发现：GitHub 预发布 2026.6.6（2026-06-10 发布）

**当前运行版本**: 2026.3.8
**最新预发布**: 2026.6.6 (Pre-release)
**差距**: 近 3 个月更新，大量安全与功能改进

### 核心更新亮点

#### 1. 安全性大幅收紧
- 转录、沙箱绑定、主机环境继承、MCP stdio、Codex HTTP 访问、本地搜索策略、高权限发送者检查、已删除 Agent ACP 绕过、回环工具、Discord 审核、Teams 群组操作等全链路安全强化
- exec 审批超时现在默认 fail-closed（安全失败）
- 涉及 PR: #91529, #91618, #91615, #91619, #91741-91763 等

#### 2. Telegram 投递更安全
- 账户级 topic 路由到正确 Agent
- 流式文本在工具调用中存活
- /compact 在通用入口生效
- 草稿分块共享
- 未授权 DM 文本不进入缓存和 prompt 上下文
- 涉及 PR: #91189, #88682, #89588, #90212, #91876, #91874 等

#### 3. iMessage 恢复与投递
- 持久入站重启覆盖
- 持久 echo 标记
- 空闲审批发现
- 加固出站传输

#### 4. 浏览器和 MCP 连接
- 现有会话 CDP 支持
- 默认 profile cdpUrl 处理
- 更安全的 browser-output 边界
- Streamable HTTP 回环传输
- 修正 OAuth/SSE 授权处理

#### 5. Control UI 性能优化
- 启动更快，首次回复延迟更低
- 缓存模型元数据
- 移除启动目录等待
- 懒加载斜杠命令
- 首次事件追踪 + 慢回复诊断

#### 6. 提供商支持扩展
- OpenRouter OAuth onboarding
- Claude Fable 5 自适应思维
- Codex 会话保持正确压缩所有权
- 本地模型跳过 guardian 审核
- Gemma 4 推理回放保留

#### 7. Plugins / ClawHub
- 可复用包发布
- dry run 跳过发布审批
- 声明安装受信任 hooks
- 报告托管插件版本漂移
- 废弃 Skill Workshop 配置改为警告而非报错

#### 8. 可观测性
- 允许受信任诊断通道捕获工具输入/输出内容
- 首次助手事件追踪
- 慢回复警告

#### 9. CLI 进度
- 发射 Claude CLI 注释进度事件
- 桥接工具间注释到通道进度

---

## 📊 ClawHub 统计

- 域名变更为 **clawhub.ai**（原 clawhub.com）
- 工具数: **52.7k**
- 用户数: **180k**
- 下载量: **12M**
- 平均评分: **4.8**

---

## 📚 文档更新

- 文档仍位于 docs.openclaw.ai
- 推荐 Node 24，兼容 Node 22 LTS (22.19+)
- 支持通道: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 等

---

## ⚠️ 建议行动

1. **考虑升级到 2026.6.6 预发布**：安全性大幅收紧，Telegram 投递改进直接相关
2. **域名注意**：ClawHub 域名已变更为 clawhub.ai
3. **版本差距大**：当前 2026.3.8 与最新差 3 个月，建议评估升级影响
