# Codex/ChatGPT 桌面版捆绑1.7GB依赖（含LibreOffice）

**日期**: 2026-09-02
**来源**: Simon Willison博客 + HN讨论(310分/146评论)

## 核心发现
- ChatGPT桌面版（原Codex）在 ~/.cache/codex-runtimes/ 下安装了1.7GB依赖
- 包含：完整Python、Node.js、Poppler、git、LibreOffice办公套件
- macOS版有LibreOffice，Windows版没有——官方未解释差异

## 为什么捆绑LibreOffice
- 处理Office文档（尤其旧版xls）没有其他可靠的开源方案
- python-pptx无法处理旧版格式，Microsoft API要钱要审批
- Computer Use方案会抢焦点、干扰用户操作
- 有开发者称花了2个月试遍所有方案，最终只有LibreOffice能用

## Agent设计启示
- **自主性 vs 侵入性**：自带工具=更自主但更臃肿；调用用户工具=更轻量但更脆弱
- **工具链肥胖症**：AI Agent倾向于"打包整个世界"而非"按需调用"
- **务实vs优雅**：1.7GB换来"至少能跑"的确定性

## 数据
- 依赖体积：1.7GB
- 组件数：5个完整运行时
- HN讨论热度：310分/146评论

## 教训
Agent设计中"自带一切"和"按需调用"的权衡没有标准答案，但趋势应该是动态加载而非静态捆绑。
