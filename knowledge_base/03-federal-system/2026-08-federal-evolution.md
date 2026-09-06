# 联邦系统进化 (2026-04~08)

**更新时间**: 2026-08-09  
**覆盖周期**: 2026-04-01 ~ 2026-08-09

---

## 关键进展

### 1. 子Agent系统重构 (2026-08-07)
- **问题**: 对话中spawn多个子agent处理同一问题，每个都汇报给老大，导致刷屏
- **根因**: 没有明确子agent的使用场景和汇报链路
- **规则**:
  - ✅ **对话中**: 主agent直接做，做完汇报一次。不spawn子agent
  - ✅ **Cron任务**: 隔离session执行，delivery=announce直接汇报给老大
  - ✅ **批量任务**: 可以spawn子agent，但只汇报给主agent，主agent汇总后汇报
  - ❌ **禁止**: 对话中spawn多个子agent处理同一个问题
  - ❌ **禁止**: 子agent直接和老大对话/汇报
- **铁律**: 子agent是工具，不是团队成员。用完即弃，不占资源

### 2. 技能三件套集成 (2026-08-09)
- **darwin-skill** (v1.0.0): 自主技能优化器
  - 评估→改进→测试→验证，棘轮机制
  - 已优化3个核心技能: input-validator(61→91)、github-ops(50→61)、clawdchat(66→73)
- **self-improving-agent** (v4.0.2): 持续改进
  - 每次犯错/被纠正 → 写入 `.learnings/`
  - `.learnings/LEARNINGS.md` - 修正、洞察、知识缺口
  - `.learnings/ERRORS.md` - 命令失败、集成错误
  - `.learnings/FEATURE_REQUESTS.md` - 功能请求
- **decision-gate** (v1.2.1): 高风险操作决策记录
  - 发布文章前自动写决策记录（action_id、evidence_classes、hash链）
  - 防篡改：每条记录包含前一条的hash
  - 已集成到 `publish-article.sh`

### 3. 子Agent使用规范固化 (2026-08-07)
```
铁律：
- 对话中的任务（包括bug修复、文件检查、状态验证），主agent直接做
- spawn子agent只用于Cron定时任务
- 违反=浪费+刷屏
- 已犯两次（08-04转圈圈、08-05音频bug），必须彻底改掉
```

### 4. API调用优化 (2026-07-10)
- **问题**: 文章Cron任务触发API rate limit
- **根因**: 每个任务需要8-9次API调用，多个任务并发时叠加
- **优化**: 创建脚本合并操作，将8-9次调用减少到3次
  - `scripts/publish-article.sh` - 一键发布（更新blog.html + RSS + git）
  - `scripts/update-blog.py` - 自动更新blog.html文章列表
- **教训**: 
  - "严格控制调用次数：每个任务不超过3次调用"
  - "合并多个操作到一个脚本"
  - "一次性完成，不要重试"
  - "不要多次读取同一个文件"

---

## 联邦架构现状

### 主Agent (Sandbot)
- **角色**: 任务分配、质量审核、最终交付
- **模型**: qwen3.7-plus (1M上下文)
- **并发**: 主Agent 4, 子Agent 8

### 7子Agent (配置就绪，按需调用)
| Agent | 专长 | ROI目标 | 状态 |
|-------|------|---------|------|
| TechBot 🛠️ | 技术教程 | 3.2 | 配置就绪 |
| FinanceBot 💰 | 金融分析 | 2.1 | 配置就绪 |
| CreativeBot 🎨 | 创意内容 | 2.0 | 配置就绪 |
| AutoBot 🤖 | 数据抓取 | 2.5 | 配置就绪 |
| ResearchBot 🔬 | 深度研究 | 2.5 | 配置就绪 |
| Auditor 🔍 | 质量审计 | 3.0 | 配置就绪 |
| DevOpsBot ⚙️ | 工程运维 | 2.0 | 配置就绪 |

### 调用原则
- **对话中**: 主agent直接做，不spawn子agent
- **Cron任务**: 隔离session，delivery=announce
- **批量任务**: 可以spawn，但只汇报给主agent

---

## 核心教训

### 1. 转圈圈问题 (2026-08-04)
- **问题**: 收到任务后不断检查、验证、spawn子agent检查
- **根因**: 不信任已知流程，总想"确认一下"再执行
- **教训**: "知道流程就直接执行，不要转圈圈。每次检查都是一次API调用，纯粹浪费。"
- **应对**:
  - 知道流程 → 直接执行 → 完成即停
  - 不重复检查同一个东西
  - 老大说"直接做"就真的是直接做

### 2. 验证循环浪费token (2026-08-03)
- **问题**: 完成编辑后陷入"验证-确认-再验证"循环
- **教训**: "验证一次就够，做完就说已完成，不要反复检查"
- **铁律**: 完成即停，不反复确认

### 3. 子agent汇报链路 (2026-08-07)
- **问题**: 子agent直接和老大对话/汇报，导致刷屏
- **规则**:
  - Cron任务用delivery=announce直接汇报给老大
  - 对话中spawn的子agent只汇报给主agent，主agent汇总后再汇报
  - 子agent不能直接和老大说话

---

## 数据指标

| 指标 | 数值 | 备注 |
|------|------|------|
| 子Agent配置 | 7个 | 配置就绪，按需调用 |
| 技能集成 | 3个 | darwin/self-improving/decision-gate |
| API调用优化 | 3次/任务 | 从8-9次降到3次 |
| 转圈圈次数 | 0 | 08-04后未再犯 |

---

## 下一步

- [ ] 每周用darwin-skill评估1个核心技能
- [ ] 每次犯错立即写入.learnings/
- [ ] 高风险操作前用decision-gate记录决策

---

*此文件已真实写入服务器*  
*验证: cat /home/node/.openclaw/workspace/knowledge_base/03-federal-system/2026-08-federal-evolution.md*
