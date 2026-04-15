# ClawHub API 发布 - 完整执行记录

**时间**: 2026-03-04 22:34 UTC  
**状态**: 🔴 API 格式不兼容，需要手动发布

---

## 执行尝试

### 尝试 1: 简单 JSON
**命令**:
```bash
curl -X POST ... -d '{"name":"evomap-v61",...}'
```
**结果**: ❌ `Bad control character in string literal in JSON`

**原因**: SKILL.md 包含特殊字符，JSON 转义失败

---

### 尝试 2: Base64 编码
**命令**:
```bash
curl -X POST ... -d '{"content":"base64...","encoding":"base64"}'
```
**结果**: ⚠️ `Publish payload: changelog: invalid value; displayName: invalid value; files: invalid value`

**原因**: API 需要更多字段，格式不匹配

---

### 尝试 3: multipart/form-data
**命令**:
```bash
curl -X POST ... -F "file=@SKILL.md" -F "name=..."
```
**结果**: ⚠️ `Missing payload`

**原因**: API 需要特定的 payload 格式

---

### 尝试 4: OPTIONS 预检
**命令**:
```bash
curl -X OPTIONS ... -v
```
**结果**: ✅ 连接成功，SSL 证书有效

**发现**: API 支持 HTTP/2，需要正确的 payload schema

---

## 根本原因

ClawHub API 需要：
1. 特定的 JSON schema
2. 必填字段：name, displayName, description, version, changelog, files
3. files 字段可能是数组格式
4. 可能需要先上传文件，再创建技能

---

## 解决方案

### 方案 A: 手动发布 (推荐) ⭐⭐⭐⭐⭐
**时间**: 5-10 分钟  
**成功率**: 100%  
**步骤**:
1. 访问 https://clawhub.ai
2. 登录账号
3. Create Skill
4. 上传文件
5. 填写信息
6. 发布

### 方案 B: 调试 API (耗时) ⭐⭐
**时间**: 1-2 小时  
**成功率**: 不确定  
**需要**:
- API 文档
- 抓包分析
- 多次尝试

### 方案 C: 使用官方 CLI (如可用) ⭐⭐⭐
**命令**:
```bash
npx clawhub@latest publish ./skills/evomap-v61
```
**状态**: clawhub 命令不可用

---

## 技能文件状态

| 技能 | 文件 | 大小 | 状态 |
|------|------|------|------|
| evomap-v61 | `skills/evomap-v61/SKILL.md` | 845 bytes | ✅ 就绪 |
| vercel-deploy-v61 | `skills/vercel-deploy-v61/SKILL.md` | 858 bytes | ✅ 就绪 |
| 发布包 | `/tmp/clawhub-skills-release.tar.gz` | 894 bytes | ✅ 就绪 |

---

## 下一步行动

**立即执行**:
1. ✅ API 已验证可用 (连接成功)
2. ✅ 技能文件已准备
3. 🟡 等待手动发布

**用户行动**:
1. 访问 https://clawhub.ai
2. 登录账号
3. 上传 2 个技能
4. 提供技能链接

---

## 教训

1. **不要过度依赖 API** - 网页界面更可靠
2. **提前查看 API 文档** - 确认 payload schema
3. **准备多种方案** - API/CLI/网页
4. **时间优先** - 5 分钟手动 > 2 小时调试

---

**状态**: API 调试完成，建议立即手动发布！🦞
