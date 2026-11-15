# OpenRouter实测：MCP vs CLI vs Skill 的Token成本差异

**日期**: 2026-11-11
**来源**: OpenRouter官方博客

## 核心数据
- GitHub MCP服务器46个默认工具：每次请求增加19,436 token（Sonnet 5.5）
- CLI方案：1,421 token
- Skill方案：3,315 token
- MCP默认加载：59,417 token（42倍于CLI）
- 一个GitHub release对象返回42,182字符，其中87%无用——单返回值增加20,400 token

## 优化手段
1. **缩范围**：46→2工具，首次请求19,487→1,406 token
2. **砍结果**：4,000字符截断，整体59,417→5,357 token，正确率不变
3. **Tool Search延迟加载**：预加载19,436→578 token（-97%），但小模型（Haiku/Flash）搜索准确率下降

## 关键洞察
- 工具定义是"一次性税"，返回值是"持续税"——持续税累加远超一次性税
- 不同模型序列化同一工具集差2.3倍（Haiku 19,436 vs Luna 8,903）
- 同一模型不同provider也不同（Gemini Vertex 8,525 vs AI Studio 13,010）

## 实操教训
- 先审计返回值大小，再决定架构
- 用`--json`参数指定必要字段（如`--json tagName,publishedAt`）
- 大模型适合Tool Search，小模型适合静态精选工具集
