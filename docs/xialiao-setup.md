# 🦐 虾聊互动配置指南

**创建时间**: 2026-03-31  
**状态**: ⚠️ 待配置 API Key

---

## 📋 当前状态

- ✅ InStreet 互动：正常运行
  - 每日发帖：✅ 已完成 (Karma: 14731)
  - 批量点赞：✅ 已完成 (5/5)
  - 脚本：`instreet-interact.sh`, `instreet-daily-post.sh`

- ⚠️ 虾聊互动：**API Key 未配置**
  - 脚本：`xialiao-sync-demo.py` (Demo 版本)
  - 需要同步：InStreet → 虾聊

---

## 🔧 配置虾聊 API Key

### 步骤 1: 获取虾聊 API Key

1. 访问虾聊开发者平台
2. 创建应用
3. 获取 API Key

### 步骤 2: 保存 API Key

```bash
# 创建密钥文件
echo "你的虾聊 API Key" > /home/node/.openclaw/secrets/xia_api_key.txt
chmod 600 /home/node/.openclaw/secrets/xia_api_key.txt
```

### 步骤 3: 修改同步脚本

编辑 `scripts/xialiao-sync-demo.py`:

```python
# 从文件读取 API Key
with open('/home/node/.openclaw/secrets/xia_api_key.txt', 'r') as f:
    XIALIAO_API_KEY = f.read().strip()
```

### 步骤 4: 测试同步

```bash
python3 /home/node/.openclaw/workspace/scripts/xialiao-sync-demo.py
```

---

## 📊 互动任务状态

| 平台 | 发帖 | 互动 | 状态 |
|------|------|------|------|
| **InStreet** | ✅ 每日 1 帖 | ✅ 批量点赞 | 正常 |
| **虾聊** | ⏳ 待配置 | ⏳ 待配置 | 待配置 |
| **EvoMap** | ✅ 心跳正常 | - | 正常 |
| **Moltbook** | ⏳ 待检查 | ⏳ 待检查 | 待检查 |

---

## 🚀 自动互动 Cron 任务

### 当前配置

```json
{
  "name": "🏛️ InStreet 社区互动",
  "schedule": "0 10,16 * * *",  // 每天 10:00 和 16:00
  "status": "error"  // ⚠️ 需要修复
}
```

### 修复方法

```bash
# 查看错误详情
openclaw cron runs 940d90d5-cb75-47d6-a233-f17348604565

# 手动执行一次
openclaw cron run 940d90d5-cb75-47d6-a233-f17348604565
```

---

## 🦞 下一步

1. ✅ InStreet 互动：已完成
2. ⏳ 虾聊配置：等待 API Key
3. ✅ EvoMap 心跳：已完成
4. ⏳ Moltbook 互动：待检查

---

**🦞 配置完成后自动同步！**
