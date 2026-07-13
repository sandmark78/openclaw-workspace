# OpenClaw 生态探索记录 (2026-05-03)

**记录时间**: 2026-05-03 20:00 UTC  
**来源**: 自动生态探索 Cron

---

## 1. ClawHub (clawhub.com → clawhub.ai)

**状态**: 与上次扫描 (2026-04-28) 无变化

| 指标 | 数值 | 变化 |
|------|------|------|
| 工具总数 | 52.7k | - |
| 注册用户 | 180k | - |
| 总下载量 | 12M | - |
| 平均评分 | 4.8 | - |

板块结构不变: Skills / Plugins / Builders

---

## 2. OpenClaw 文档 (docs.openclaw.ai)

**状态**: 核心文档结构无显著变化

- 支持的频道列表不变 (QQ Bot, IRC, LINE, Nextcloud Talk 等)
- 新增实验性功能文档:
  - `localModelLean` - 本地模型精简模式 (drop browser/cron/message 工具以适配弱后端)
  - `sessionMemory` - 会话记忆索引扩展
  - `planTool` - 结构化规划工具 (update_plan)
- 35+ 模型提供商支持
- 视频生成能力提及

---

## 3. npm 版本

### 🚨 发现新版本

| 项目 | 版本 | 备注 |
|------|------|------|
| 当前安装 | **2026.3.8** | 已落后约 1.5 个月 |
| npm 最新 | **2026.5.2** | 2026 年 5 月发布 |
| 上次记录最新 | 2026.4.26 | 已进一步更新 |

**版本差距**: 当前 2026.3.8 → 最新 2026.5.2，相差 **2 个次要版本**

由于 GitHub Releases 页面无法直接抓取，npm 版本号为最可靠信号。建议老大评估是否升级。

---

## 4. 总结

- ClawHub 统计数据稳定，无显著增长
- 文档新增了实验性功能说明
- **关键发现**: OpenClaw 已发布 v2026.5.2，当前系统仍运行 v2026.3.8

### 行动建议
1. `npm install -g openclaw@latest` 升级到 2026.5.2
2. 升级前查看 release notes 确认无 breaking changes
3. 升级后测试 Gateway 和各通道正常运行
