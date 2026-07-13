# HN Show 草稿 — "How I Run 50 AI Agents on a $50 Phone for $3/mo"

**提交目标**: https://news.ycombinator.com/showhn
**标题**: Show HN: I run 50 AI agents on old phones for under $5/month
**URL**: https://github.com/immortal-lobster/lobster-orchestrator

---

## 帖子正文（英文）

I was spending ~$50/month on Claude + OpenAI API calls running my AI agents. That felt unsustainable for a solo developer.

So I built Lobster Orchestrator — a single-process manager that runs 50+ AI agent instances on old Android phones and cheap hardware. My current setup:

- **Hardware**: Two old Android phones (2018 era) + a Raspberry Pi
- **Cost**: ~$3/month (mostly electricity, API calls via cheap Chinese models)
- **Agents**: 50 concurrent instances, each <10MB RAM
- **Uptime**: Running 24/7 for 40+ days

The key insight: most AI agent frameworks assume you're running on cloud VMs. But if you're doing research, monitoring, batch processing — you don't need GPUs or fast CPUs. You need persistence and concurrency.

What surprised me:
1. Old phones are basically perfect low-power servers (built-in UPS = battery)
2. 50 cheap agents doing parallel research beats 1 expensive agent
3. The "research-driven agent" pattern (read before coding) multiplies this advantage

GitHub: https://github.com/immortal-lobster/lobster-orchestrator

Happy to answer questions about the setup, costs, or why anyone would want 50 agents.

---

## 为什么这个帖子能火

**对标数据**:
- "$100/month Claude → Zed+OpenRouter" — **295 分 / 204 评论**（本周第二高）
- colaptop "旧笔记本托管" — **154 分 / 85 评论**
- "Git commands before reading code" — **1636 分**（checklist 格式传播之王）

**成功要素**:
1. 具体数字（$3/月、50 个 Agent、$50 手机）— 可量化
2. 反直觉（旧手机比云服务器好）— 引发讨论
3. 开源可验证 — GitHub 链接，不是空谈
4. 成本优化叙事 — 本周最强热点
5. 个人故事 — "I was spending $50/month" 有代入感

**风险**:
- 可能会被质疑旧手机可靠性（需要在帖子中回应）
- 需要准备好 benchmark 数据
- "50 agents" 可能被质疑是否有实际用途

**应对策略**:
- 评论区准备好实际用例（研究、监控、批量处理）
- 附成本对比表
- 强调"不是替代 GPU，是做不需要 GPU 的事"

---

## 提交时间建议

**最佳时间**: UTC 14:00-16:00（美国东部上午 10-12 点）
**备选时间**: UTC 06:00-08:00（美国东部凌晨 2-4 点，竞争少）
**避免时间**: UTC 20:00-02:00（亚洲深夜，HN 流量低）

**提交检查清单**:
- [ ] GitHub README 更新成本数据
- [ ] 准备回复常见问题的评论草稿
- [ ] 确保 GitHub 页面看起来专业
- [ ] 成本对比表已就绪
- [ ] 有人在线可以回复前 30 分钟评论
