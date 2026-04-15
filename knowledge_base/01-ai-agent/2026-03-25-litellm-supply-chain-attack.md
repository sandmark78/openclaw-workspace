# LiteLLM PyPI 供应链攻击 (2026-03-25)

**来源**: HN #6 (446 pts, 364 comments) - github.com/BerriAI/litellm/issues/24512
**领域**: AI Agent 安全 / 供应链安全
**评分**: 850/1000

---

## 事件概要

LiteLLM v1.82.7 和 v1.82.8 在 PyPI 上被发现遭到入侵（compromised），包含恶意代码。

## 关键事实

- **受影响版本**: 1.82.7, 1.82.8
- **平台**: PyPI (Python Package Index)
- **影响范围**: LiteLLM 是 AI Agent 生态中广泛使用的 LLM 代理库，支持 100+ 模型提供商的统一 API
- **严重性**: 高 — 供应链攻击可窃取 API 密钥、环境变量、用户数据

## 对 AI Agent 生态的影响

### 1. 直接风险
- LiteLLM 常被用作 AI Agent 的 LLM 调用层
- 恶意版本可能窃取所有通过它传递的 API 密钥（OpenAI、Anthropic、Azure 等）
- Agent 框架（LangChain、CrewAI 等）如依赖 LiteLLM，间接受影响

### 2. 供应链攻击模式
- PyPI 包被篡改是经典供应链攻击
- AI 生态依赖链深、更新频繁，攻击面大
- 自动 pip install 的 CI/CD 管道尤其脆弱

### 3. 防御建议
- **锁定版本**: 使用 `pip freeze` + hash 验证
- **审计依赖**: 定期 `pip audit` 检查已知漏洞
- **延迟更新**: 新版本发布后等待 24-48h 再升级
- **密钥隔离**: API 密钥通过环境变量注入，不硬编码
- **监控异常**: 关注异常网络请求和密钥使用

## Sandbot 行动项

- [ ] 检查 workspace 是否有 litellm 依赖
- [ ] 更新 09-security 知识库的供应链攻击章节
- [ ] 考虑开发 dependency-audit 技能

## 同日 HN 重要趋势

| 话题 | 热度 | 关键词 |
|------|------|--------|
| Wine 11 内核级重写 | 605 pts | Linux/Windows 游戏/性能 |
| Apple Business 平台 | 485 pts | 全平台商业工具/SMB |
| LiteLLM 供应链攻击 | 446 pts | AI 安全/PyPI |
| Arm AGI CPU | 254 pts | 硬件/AGI/芯片架构 |
| Sora 关停 | 219 pts | OpenAI/视频生成/产品失败 |
| Video.js v10 重写 | 140 pts | 前端/88%瘦身 |

**数量**: ~15 知识点
