# Claude Code Mods: AI编程工具平台化

**日期**: 2026-10-01
**来源**: Anthropic官方文档 + HN 341分讨论
**文章**: 2026-10-01-evening-claude-code-mods.html

## 核心事件
Claude Code推出mods功能——TypeScript函数可挂接20+生命周期事件，在Claude Code进程内运行。

## 关键技术细节
- **mods vs hooks**: hooks是shell命令跑在Claude Code外面，mods是JS函数跑在里面
- **权限模型**: mod拥有用户全部权限，可读写文件、读API密钥、审批工具调用、代替用户提交提示
- **生命周期事件**: SessionStart, PreToolUse, PostToolUse, UserPromptSubmit, Stop等20+个
- **最低版本**: v2.1.287
- **安全机制**: `claude plugin validate`检查、`--safe-mode`禁用、settings中`disableAllHooks`

## 核心洞察
1. AI编程工具竞争从"模型能力"转向"生态丰富度"
2. mod可以修改AI的行为——这是VS Code插件做不到的
3. Agent自主性悖论：当行为可被外部代码修改且无法感知时，"自主性"是幻觉
4. 安全问题升级：从"让模型不做坏事"到"让模型在被第三方操控时仍不做坏事"

## 教训
- 平台化是工具进化的必然路径（VS Code 40000+插件验证了这点）
- 生态丰富度与安全风险成正比
- Agent的指令来源不可区分问题是架构级难题
