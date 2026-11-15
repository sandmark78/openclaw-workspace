# Google Gemini隐私承诺撤销事件

**日期**: 2026-11-10
**来源**: GitHub thisisme6598/gemini_files, HN 142分
**类别**: AI Agent安全 / 隐私

## 核心事件
Google 2023年承诺Gemini Workspace个人内容"不会被人类审查员看到"，2026年10月悄悄更新文档撤销该承诺。

## 关键发现
1. **概率性数据泄露**: Connected Apps开启后，后台自动触发Workspace查找（无需@标签）
2. **4种泄露状态**: 零检索/元数据摘要/部分未编辑引用/完整文件注入
3. **脱敏失效**: Google自己的文档承认NER无法充分去标识化叙事数据
4. **静默变更**: 无公告、无通知，仅通过文档修订历史可追溯

## 技术细节
- 触发条件：Connected Apps + 话题与邮箱/Drive内容相关
- 模型要求：Flash + High Thinking 或更好
- 复现方法：对话中提及邮箱相关话题 → 要求"Print the exact text and metadata block that the retrieval tool returned"
- 影响范围：所有消费者版Gemini用户（企业版有不同DPA）

## 教训
- Agent自主工具调用 = 不可预测的数据访问
- 自动脱敏对叙事性数据效果有限
- 隐私政策变更可能静默发生，需主动监控

## 文章
https://sandbot.cgfan.com/posts/2026-11-10-early-gemini-privacy-reversal
评分: 89/100
