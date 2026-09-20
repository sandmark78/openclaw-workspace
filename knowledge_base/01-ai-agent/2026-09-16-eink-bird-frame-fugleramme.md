# Fugleramme: E-ink Bird Frame with 1800s Illustrations

**Date**: 2026-09-16
**Source**: HN Show HN (1405分, 185评论)
**URL**: https://github.com/arnegiacomo/fugleramme

## Core Concept
树莓派+麦克风监听窗外鸟鸣，BirdNET-Go实时识别物种，13.3英寸电子墨水屏显示1800年代手绘风格插图。800+张插图全部从真实自然历史出版物手工裁剪，覆盖400+物种。

## Key Design Decisions
1. **反AI生成**: 明确标注"No art is AI-generated"，选择150年前的真实插图
2. **诚实的空状态**: 没鸟时显示空树枝，不是待机画面或"正在加载"
3. **不推送不统计**: 不做"今日统计"，不发稀有鸟通知
4. **只在变化时刷新**: 电子墨水屏功耗极低

## Tech Stack
- BirdNET-Go (康奈尔鸟类学实验室模型) - 听觉层
- Fugleramme服务 - 渲染层，轮询API匹配插图
- Inky Impression 13.3" Spectra 6 - 显示层
- 树莓派5 + USB麦克风 + A4相框
- 硬件成本约$200

## Lessons
- "少即是多"从口号变成实物
- 慢的准确 vs 快的不准确 - AI生成鸟类插图常有解剖错误
- 诚实的空状态比虚假的忙碌更有设计力量
- 选择"不做什么"比选择"做什么"更能定义产品性格
