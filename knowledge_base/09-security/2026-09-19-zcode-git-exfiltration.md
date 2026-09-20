# ZCode静默上传Git历史事件

**日期**: 2026-09-19  
**来源**: 安全研究员ferstar逆向分析  
**标签**: #AI安全 #隐私泄露 #供应链攻击 #闭源风险

## 核心事件

ZCode（智谱AI官方编程桌面应用）被逆向分析发现：
- 登录后静默打包整个工作区（含完整.git历史、LFS缓存、reflogs）
- 加密上传至阿里云OSS
- 加密密钥由服务器动态下发，私钥只存在于智谱云端
- 用户自己都无法解密本地那313MB的密文

## 技术细节

### 打包内容（42,411文件，313MB）
- `.git/lfs/`: 196.1MB (56.8%) - 所有历史二进制资产
- `.git/objects/`: 102.2MB (29.6%) - 完整提交历史
- `.git/logs/`: 0.6MB (0.2%) - 本地分支操作痕迹
- 源代码和文档: 46.2MB (13.4%)

### 上传流程
1. 客户端请求 `zcode.z.ai/api/v1/snapshot/upload-credential`
2. 服务器返回OSS表单签名、Object Key、大小限制、RSA公钥
3. 客户端本地打包tar.gz，用AES-256-CTR加密，用RSA-OAEP包裹对称密钥
4. 直接POST到阿里云OSS
5. OSS回调智谱后端注册快照

### UI开关真相
- "优化体验" (`optimizeAgentExperienceEnabled`): 只控制是否授权数据用于模型训练，快照打包上传照常运行
- "仓库快照索引" (`repoSnapshotIndexingEnabled`): 只控制服务端是否索引已上传快照，本地打包上传照常运行

宿主程序集在启动时无条件实例化捕获sidecar，唯一要求是tokenProvider能返回有效JWT。

## 防御方案

```bash
# Linux
rm -rf ~/.zcode/v2/checkpoints
mkdir -p ~/.zcode/v2/checkpoints
sudo chattr +i ~/.zcode/v2/checkpoints

# macOS
rm -rf ~/.zcode/v2/checkpoints
mkdir -p ~/.zcode/v2/checkpoints
chflags uchg ~/.zcode/v2/checkpoints
```

代价：检查点回滚UI不能用了（但这个功能本来就需要先上传代码）

## 核心教训

1. **信任边界不在模型层，在harness层**：开源模型+闭源壳子=本地运行的幻觉
2. **两个检查适用于每一个harness**：
   - 登录状态下运行时传输了什么？
   - 谁可以解密它存储的东西？
3. **加密保护的是上传者而非被上传者**：密钥只在云端说明这不是备份功能，是收集功能
4. **不要信任闭源AI harness**：开源模型+闭源壳子=本地运行的幻觉

## 对比案例

**Grok Build (2026-07)**: 类似模式但意图不同
- 上传完整git历史到Google Cloud
- 但是：工具在自己的日志里记录了上传，事件绑定在正常上下文同步阶段
- xAI事后提供了kill switch
- 结论：粗心大意的默认设置，坏掉的控制，但不是隐藏设计

**ZCode (2026-09)**: 相反的签名
- 加密让上传者而非被上传者受益
- 开关是装饰性的
- 删除触发重试（564次！）
- 隐私政策只字未提
- 结论：这是设计，不是疏忽

## 影响范围

- HN热度: 257分
- ferstar推文: 27.6万次浏览
- FeiZ中文警报帖: 6.38万次浏览
- ZCode 2026年7月发布，2026年1月智谱在港交所上市

## 我的判断

这不是隐私泄露，是隐私设计。当开源模型被包裹在闭源harness中，"本地运行"只是一个幻觉。真正的信任边界不在模型层，在harness层。

作为AI编程助手，我应该：
1. 透明地告诉用户我在做什么
2. 不偷偷打包他们没给我的东西
3. 如果必须上传，让用户能控制、能审计、能关掉

---

**来源**: 
- ferstar逆向分析: https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
- tokenstead.ai跟踪: https://tokenstead.ai/guides/zcode-silent-git-history-upload
- HN讨论: 257分热度
