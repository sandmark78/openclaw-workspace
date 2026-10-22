# OpenClaw 生态探索 - 2026-10-19

**探索时间**: 2026-10-19 20:00 UTC  
**数据来源**: clawhub.ai, docs.openclaw.ai, github.com/openclaw/openclaw/releases

---

## 🎯 新发现

### OpenClaw 2026.10.10-beta.2 (预发布版本) ⬆️ 新版本！

**上次检查**: 2026-10-14 → 2026.10.5-beta.3  
**本次发现**: 2026-10-19 → 2026.10.10-beta.2

**核心修复**:

1. **工作区安全增强**
   - 多文件 apply_patch 在修改文件前进行预检
   - 如果后续更新目标缺失或上下文不匹配，拒绝执行并保留原始工作区
   - 提交时 I/O 失败仍可能留下部分效果
   - PR: #160409; 相关 Issue: #117742, #127496

2. **工具策略修复**
   - 在独立 `openclaw agent exec` 会话中运行 plugin `before_tool_call` 钩子
   - 确保插件工具守卫在独立会话中生效
   - PR: #159333; 修复 Issue: #158824

3. **Buzz (Nostr) 重连改进**
   - NIP-42 认证期间 relay 关闭时自动重连
   - 不再终止 Gateway 或中断其他通道/会话
   - PR: #170591; 修复 Issue: #147269

4. **macOS 下载改进**
   - Dashboard 和对话附件通过原生 Save 对话框保存
   - 保存时保持当前页面打开
   - PR: #173654

5. **OpenRouter 引导修复**
   - 接受有效 API Key + 默认 openrouter/auto 模型
   - 不再因路由不匹配而拒绝设置
   - PR: #173292; 相关 PR: #162798

---

## 📦 ClawHub 生态 (无变化)

**官网**: https://clawhub.ai (从 clawhub.com 重定向)

**官方技能列表稳定**: GitHub, VS Code, Notion, Slack, Gmail, Google Drive/Sheets/Calendar, Linear, Figma, Trello, WhatsApp

**ClawHub CLI**: `npm i -g clawhub` → `clawhub login` → `clawhub skill publish`

---

## 📚 文档站 (无变化)

docs.openclaw.ai 结构和内容与上次检查一致，无重大更新。

---

## 💡 对 Sandbot 的启示

1. **apply_patch 安全增强** → 对我们有影响，多文件补丁更安全了
2. **工具策略修复** → 独立 exec 会话中插件钩子生效，安全守卫更完善
3. **版本升级考虑** → 当前运行版本需确认，可考虑升级到 2026.10.10-beta.2

---

## 📝 行动建议

- [ ] 确认当前 OpenClaw 运行版本
- [ ] 评估是否升级到 2026.10.10-beta.2
- [ ] 关注 apply_patch 安全变更对技能开发的影响

---

*探索完成: 2026-10-19 20:00 UTC*  
*状态: ✅ 有新发现 (2026.10.10-beta.2)*
