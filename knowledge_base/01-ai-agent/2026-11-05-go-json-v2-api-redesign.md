# Go JSON v2: API Redesign After 10 Years

**日期**: 2026-11-05
**来源**: pkg.go.dev/encoding/json/v2, HN 220分

## 核心观点
Go标准库encoding/json发布v2版本，核心改变是"默认拒绝"代替"默认接受"：
1. 默认拒绝重复键名（v1允许，后面的覆盖前面的）
2. 默认拒绝无效UTF-8（v1替换成Unicode替换字符）
3. 默认严格大小写匹配（v1模糊匹配）

## 关键数据
- 等待时间：10年（v1发布于2015年Go 1.5）
- 流式API内存优化：从O(n)到O(1)，GB级文件内存占用从几GB降到几MB
- 新增API：MarshalWrite/UnmarshalRead（io.Writer/io.Reader）
- 新增omitzero选项，与omitempty区分语义

## 设计哲学教训
- 默认值必须是安全的，而不是方便的——因为大多数开发者不会去改默认值
- "宽容解析"是一种傲慢，你以为在帮开发者，其实在替他们做决定
- 安全默认值 > 宽松默认值，需要宽松的人可以显式开启

## 实操要点
- v1和v2可共存，支持渐进迁移
- 流式API适合处理大型JSON文件
- omitzero基于Go类型系统零值判断，omitempty基于JSON类型空值判断

## 与Agent的关联
Agent日常处理大量JSON（API响应、配置、日志），v2的严格默认值减少了语义歧义导致的安全风险。流式API让Agent可以在有限内存环境中处理大文件。
