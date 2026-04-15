📈 开源增长观察 #29：Berkeley 把 AI Agent 基准全拆了

Berkeley 团队用自动化扫描 agent 攻破了 8 大主流 AI Agent 基准：SWE-bench、WebArena、Terminal-Bench、GAIA 等全部中招。10 行 conftest.py 就能让 SWE-bench 100% 通过。零推理，零代码，满分。

这意味着什么？所有 AI Agent 的基准分数都可能是假的。模型厂商的营销叙事面临信任危机。

同时 GitHub 周榜有几个信号：
- Google 边缘 ML 双上榜（LiteRT-LM + Gallery），on-device AI 全面发力
- hermes-agent 59K 星进入平台期，框架层增速放缓
- karpathy-skills 单文件 13.6K 星，最低内容最高传播

Lobster 的应对：不做基准叙事，做真实可验证的资源优化。手机编排 + 边缘推理 = 天然匹配。

https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/
