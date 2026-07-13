# Rate Limit Tester 🔬

**功能**: 测试百炼/DashScope 模型的速率限制（并发数、每分钟调用次数、Token 上限）
**模型**: qwen3.6-plus（通过 coding.dashscope.aliyuncs.com）
**依赖**: Python3（标准库，无需 pip install）

## 使用方法

```bash
python3 /home/node/.openclaw/workspace/skills/ratelimit-tester/test_ratelimit.py
```

## 测试内容

| 测试项 | 说明 |
|--------|------|
| 1. 单次调用延迟 | 基础响应时间和 token 消耗 |
| 2. 连续调用上限 | 连续 N 次调用，检测何时开始报错 |
| 3. 并发调用上限 | N 路并发，检测并发限制 |
| 4. Token 消耗速率 | 每分钟的总 token 消耗上限 |

## 配置

API Key 和模型在脚本顶部配置，默认使用 workspace 中的百炼 key。
