# DEsk: Wayland拟物化桌面环境

**日期**: 2026-10-16
**来源**: HN 534分, GitHub fyzugx/DEsk

## 核心事实
- DEsk是一个Wayland桌面环境，采用iOS 6风格的拟物化设计
- 整个桌面被渲染成一张胡桃木书桌，窗口是纸、Dock是抽屉、通知是邮筒
- 房间用GLES 3光线追踪渲染，CPU fallback，按屏幕尺寸缓存
- 内存占用200-450MB，比GNOME(600-800MB)和KDE(500-700MB)更低
- 支持Debian/Ubuntu/Arch/Fedora，7种语言，多屏

## 关键洞察
- 视觉复杂度≠资源消耗，架构决策才是关键
- 拟物化的问题不是美不美，而是有没有人愿意投入工程精力
- Linux桌面20年来在"够用就行"心态下越来越无聊
- 社区反应两极：追求美 vs 实用性担忧

## 技术架构
- 基于wlroots生态的完整Wayland compositor
- 只造"房间里画出来的东西"和"只有compositor能做的事"
- 借用现有工具：NetworkManager, Blueman, PipeWire, IBus, grim
- 锁屏是"前门"，3D渲染，PAM认证

## 教训
- "花哨但克制"是可能的——缓存+借用+最小化自造
- 美的UI需要工程投入，不是不可能而是不愿意
