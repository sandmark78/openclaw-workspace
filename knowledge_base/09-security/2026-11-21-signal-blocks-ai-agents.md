# Signal 屏蔽操作系统级 AI Agent 截屏

**日期**: 2026-11-21
**来源**: Signal 官方博客

## 核心事件
Signal 屏蔽了 iOS 27 和 Android 的 AI Agent 截屏功能，防止 Apple 的 Onscreen Awareness 和 Google 的 Gemini Intelligence 抓取 Signal 聊天记录。

## 关键数据
- 受影响系统：iOS 27、Android、Windows 11（去年已屏蔽 Microsoft Recall）
- 三大操作系统（苹果/谷歌/微软）全部集成了系统级 AI Agent
- Signal 覆盖率：99% 智能手机用户

## 核心观点
1. **操作系统是海洋，应用是鱼**：OS 级 AI Agent 改变了应用生态的生存条件
2. **应用层隐私承诺被绕过**：端到端加密被操作系统级的"看"功能绕过
3. **措施不完整**：屏蔽截屏只挡住一种方式，Agent 还可通过文件系统、通知、API 获取数据
4. **无障碍权限被滥用**：Meta Muse 等第三方 Agent 把为残障人士设计的无障碍权限当成"万能钥匙"

## Signal 的诉求
- 开发者应有简单方式退出 AI 数据访问（截屏、文件系统、通知、API）
- OS 公司应提供更好的 AI Agent 文档和技术规范

## 实操保护措施
1. Signal 设置 → 隐私 → 开启"屏蔽截屏"
2. iOS: 设置 → Apple Intelligence → 关闭不需要的权限；Android: 设置 → Google → Gemini → 关闭"屏幕感知"
3. 检查无障碍权限：设置 → 无障碍 → 移除不需要的应用权限

## 教训
- 当操作系统本身成为"第三方"时，应用层的加密承诺变得脆弱
- 隐私应用被迫与操作系统"自卫"，说明行业缺乏标准化的 Agent 权限控制
- 长期方案需要细粒度权限（类似浏览器沙箱），而非"全开/全关"
