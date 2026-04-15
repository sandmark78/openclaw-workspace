# OpenClaw 生态探索报告

**探索时间**: 2026-04-02 20:00 UTC  
**状态**: ✅ 发现最新更新

---

## 🦞 ClawHub (clawhub.ai)

**状态**: 正常运行  
**Slogan**: "Lobster-light. Agent-right."

**当前状态**:
- 技能上传系统就绪
- 支持技能版本管理（类似 npm）
- 支持向量搜索
- 暂无高亮技能
- 暂无热门技能

**安装命令**:
```bash
npx clawhub@latest install <skill-name>
```

---

## 📚 OpenClaw 文档 (docs.openclaw.ai)

**状态**: 正常  
**核心定位**: 自托管 AI Agent 网关

**关键特性**:
- 多通道支持：WhatsApp, Telegram, Discord, iMessage
- 插件扩展：Mattermost 等
- 多 Agent 路由
- 媒体支持（图片/音频/文档）
- Web 控制面板
- 移动端节点（iOS/Android）

**快速启动**:
```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

---

## 🚀 GitHub Releases - ⭐ **今日更新 (2026-04-02 18:30)**

### Breaking Changes

1. **xAI 搜索配置迁移** (#59674)
   - 从 `tools.web.x_search.*` 迁移到 `plugins.entries.xai.config.xSearch.*`
   - 统一认证方式：`plugins.entries.xai.config.webSearch.apiKey` / `XAI_API_KEY`
   - 迁移命令：`openclaw doctor --fix`

2. **Firecrawl web_fetch 配置迁移** (#59465)
   - 从 `tools.web.fetch.firecrawl.*` 迁移到 `plugins.entries.firecrawl.config.webFetch.*`
   - 新的 fetch-provider 边界回退机制
   - 迁移命令：`openclaw doctor --fix`

### 重要更新

3. **Task Flow 核心恢复** (#58930)
   - 管理 vs 镜像同步模式
   - 持久化流状态/修订追踪
   - `openclaw flows` 检查/恢复原语

4. **Task Flow 子任务管理** (#59610)
   - 添加管理型子任务生成
   - 粘性取消意图（sticky cancel intent）
   - 外部编排器可立即停止调度

5. **Task Flow 插件接口** (#59622)
   - 添加 `api.runtime.taskFlow` 接口
   - 插件可创建和管理 Task Flow

6. **Android Assistant 入口** (#59596)
   - 添加 Assistant 角色入口点
   - Google Assistant App Actions 元数据
   - 可从 Assistant 触发器启动 OpenClaw

7. **Exec 默认模式**
   - Gateway/Node 主机 exec 默认 YOLO 模式
   - `security=full` + `ask=off`
   - 无需提示的默认行为

8. **Provider 回放钩子** (#59143)
   - 转录策略
   - 回放清理
   - 推理模式分发

9. **插件钩子** (#20067)
   - 添加 `before_agent_reply`
   - 插件可在内联操作后用合成回复短路 LLM

10. **Feishu 评论事件流** (#58497)
    - 专用 Drive 评论事件流
    - 评论线程上下文解析
    - 线程内回复

11. **Matrix 提及元数据** (#59323)
    - 符合规范的 `m.mentions` 元数据
    - 支持文本发送、媒体标题、编辑、投票回退

12. **Diffs 查看器基础 URL** (#59341)
    - 插件拥有的 `viewerBaseUrl`
    - 稳定代理/公共来源

13. **Agent 压缩模型** 
    - 统一 `agents.defaults.compaction.model`
    - 支持手动 `/compact`

---

## 📋 行动建议

### 立即执行
```bash
# 运行配置迁移和修复
openclaw doctor --fix
```

### 关注重点
1. **配置迁移** - xAI 和 Firecrawl 配置路径变更
2. **Task Flow** - 核心功能恢复，适合复杂编排
3. **Android Assistant** - 新的移动端入口

### 版本检查
```bash
# 检查当前版本
openclaw --version

# 更新到最新版
npm install -g openclaw@latest
```

---

## 🔍 下次探索

**建议频率**: 每周一次  
**监控重点**:
- GitHub Releases 更新
- ClawHub 新技能发布
- 文档新增功能

---

*报告生成时间：2026-04-02 20:00 UTC*  
*下次自动探索：2026-04-09 20:00 UTC*
