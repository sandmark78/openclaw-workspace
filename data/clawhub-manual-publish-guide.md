# ClawHub 手动发布指南

**API 状态**: ⚠️ 需要正确的 payload 格式  
**建议**: 使用网页界面手动发布

---

## 网页发布步骤

### 第 1 步：登录
1. 访问 https://clawhub.ai
2. 使用 API Key 对应的账号登录
3. 进入 Dashboard

### 第 2 步：创建技能
1. 点击 "Create Skill" 或 "New Skill"
2. 填写以下信息：

**技能 1: evomap-v61**
```
Name: evomap-v61
Display Name: EvoMap V6.1
Description: EvoMap V6.1 发布技能 (避免 slug 冲突版)
Version: 1.0.0
Changelog: Initial release - V6.1 version with slug fix
```

**技能 2: vercel-deploy-v61**
```
Name: vercel-deploy-v61
Display Name: Vercel Deploy V6.1
Description: Vercel 部署 V6.1 技能 (避免 slug 冲突版)
Version: 1.0.0
Changelog: Initial release - V6.1 version with slug fix
```

### 第 3 步：上传文件
1. 上传 SKILL.md 文件
2. 文件位置：
   - `/home/node/.openclaw/workspace/skills/evomap-v61/SKILL.md`
   - `/home/node/.openclaw/workspace/skills/vercel-deploy-v61/SKILL.md`

### 第 4 步：发布
1. 点击 "Publish" 或 "Submit"
2. 等待审核通过
3. 获取技能链接

---

## API 调试记录

### 尝试 1: JSON
```bash
curl -X POST ... -d '{"name":"..."}'
结果：Bad control character in JSON
```

### 尝试 2: Base64
```bash
curl -X POST ... -d '{"content":"base64..."}'
结果：需要 changelog, displayName, files 字段
```

### 尝试 3: multipart/form-data
```bash
curl -X POST ... -F "file=@SKILL.md"
结果：Missing payload
```

### 结论
API 需要特定的 payload 格式，建议：
1. 使用网页界面发布
2. 或查看 ClawHub API 文档确认格式
3. 或使用浏览器开发者工具抓包分析

---

**状态**: 等待手动发布
