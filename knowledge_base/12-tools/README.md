# 12-tools 知识库索引

## 核心主题
- 脚本体系完善 → 2026-08-tools-evolution.md
- API调用优化 → 2026-08-tools-evolution.md#API优化
- 工具使用规范 → 2026-08-tools-evolution.md#规范

## 关键数据
- 发布脚本：4个（publish/update/generate/update-index）
- 质量脚本：3个（score/check-duplicate/get-improvements）
- 音频脚本：3个（edge-tts/extract-text/regenerate）
- 素材脚本：2个（aihot-scraper/news-aggregator）
- 安全脚本：2个（input-validator/decision-gate-wrapper）
- 总脚本数：14个

## 重要教训
- AIHOT必须用API（2026-08-03）：数据源有API就用API，禁止网页解析
- 文章生成流水线5个bug（2026-08-03）：改了模板必须更新脚本
- 验证循环浪费token（2026-08-03）：验证一次就够
- 中文引号导致JavaScript语法错误（2026-07-12）：必须转义
- TTS播客问题（2026-07-12）：必须过滤UI元素和结构性内容

## 最近更新
- 2026-08-09: 工具系统进化总结
- 2026-08-05: 音频脚本修复
- 2026-07-12: TTS文本提取优化
