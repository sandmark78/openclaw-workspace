# CNN碾压LLM皮肤癌诊断 (2026-10-26)

## 核心事实
- Guy's Hospital皮肤科医生Magnus Lynch用200个活检确认病例测试
- Inception v3 (2015) 微调版：62%准确率（125/200）
- GPT-6 Astra：42%（84/200），Claude Fable 5.1：42%（85/200）
- CNN可在手机浏览器用WebGPU运行，无需服务器

## 关键数据
- 黑色素瘤识别：CNN 13/30，GPT-6 8/30，Claude 11/30
- LLM各有"最爱答案"偏差：GPT-6把14个黑色素瘤误判为基底细胞癌
- 良性病变识别差距更大：CNN 76% vs LLM ~30%

## 教训
1. 通用智能 ≠ 专业精度，专用模型在垂直领域碾压通用模型
2. 工具选择比模型新旧更重要
3. LLM倾向于"防御性医疗"（什么都送检），实际临床价值有限
4. 小型专用模型的部署成本远低于大模型API

## 来源
- https://lynchlab.net/llm-skin-cancer
- HN 296分
- 数据集：MILK10k (ISIC, CC BY-NC)
