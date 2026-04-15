# Lobster Orchestrator API 文档

**版本**: V0.1.1  
**基础 URL**: `http://localhost:8080/api/v1`

---

## 📋 接口列表

### 1. 获取所有实例

**请求**:
```http
GET /instances
```

**响应**:
```json
{
  "success": true,
  "instances": [
    {
      "id": "lobster-001",
      "name": "Sandbot #1",
      "status": "running",
      "pid": 12345,
      "port": 18790,
      "workspace": "/data/workspaces/lobster-001",
      "start_time": "2026-03-30T17:00:00Z",
      "restart_count": 0,
      "uptime_seconds": 3600
    }
  ],
  "count": 50
}
```

**状态码**:
- `200`: 成功
- `500`: 服务器错误

---

### 2. 获取单个实例

**请求**:
```http
GET /instances/{id}
```

**响应**:
```json
{
  "success": true,
  "instance": {
    "id": "lobster-001",
    "name": "Sandbot #1",
    "status": "running",
    "pid": 12345,
    "port": 18790
  }
}
```

**状态码**:
- `200`: 成功
- `404`: 实例不存在

---

### 3. 启动实例

**请求**:
```http
POST /instances/{id}
```

**响应**:
```json
{
  "success": "Instance started"
}
```

**状态码**:
- `200`: 成功
- `400`: 启动失败 (已在运行/配置错误)
- `404`: 实例不存在

---

### 4. 停止实例

**请求**:
```http
DELETE /instances/{id}
```

**响应**:
```json
{
  "success": "Instance stopped"
}
```

**状态码**:
- `200`: 成功
- `400`: 停止失败
- `404`: 实例不存在

---

### 5. 健康检查

**请求**:
```http
GET /health
```

**响应**:
```json
{
  "status": "healthy",
  "service": "lobster-orchestrator"
}
```

**状态码**:
- `200`: 健康
- `503`: 服务异常

---

## 🔧 使用示例

### cURL 示例

```bash
# 获取所有实例
curl http://localhost:8080/api/v1/instances

# 启动实例
curl -X POST http://localhost:8080/api/v1/instances/lobster-001

# 停止实例
curl -X DELETE http://localhost:8080/api/v1/instances/lobster-001

# 健康检查
curl http://localhost:8080/api/v1/health
```

### JavaScript 示例

```javascript
const API_BASE = 'http://localhost:8080/api/v1';

// 获取所有实例
async function getInstances() {
  const res = await fetch(`${API_BASE}/instances`);
  const data = await res.json();
  return data.instances;
}

// 启动实例
async function startInstance(id) {
  await fetch(`${API_BASE}/instances/${id}`, { method: 'POST' });
}

// 停止实例
async function stopInstance(id) {
  await fetch(`${API_BASE}/instances/${id}`, { method: 'DELETE' });
}
```

### Python 示例

```python
import requests

API_BASE = 'http://localhost:8080/api/v1'

# 获取所有实例
def get_instances():
    res = requests.get(f'{API_BASE}/instances')
    return res.json()['instances']

# 启动实例
def start_instance(id):
    requests.post(f'{API_BASE}/instances/{id}')

# 停止实例
def stop_instance(id):
    requests.delete(f'{API_BASE}/instances/{id}')
```

---

## 📊 状态说明

| 状态 | 说明 | 操作 |
|------|------|------|
| `running` | 实例运行中 | 可停止/重启 |
| `stopped` | 实例已停止 | 可启动 |
| `crashed` | 实例崩溃 | 自动重启中 |

---

## ⚠️ 错误处理

### 常见错误码

| 错误码 | 说明 | 解决方案 |
|--------|------|----------|
| `400` | 请求参数错误 | 检查实例 ID 是否正确 |
| `404` | 实例不存在 | 确认实例已配置 |
| `500` | 服务器内部错误 | 查看 Orchestrator 日志 |
| `503` | 服务不可用 | 检查服务是否运行 |

### 错误响应格式

```json
{
  "error": "实例 lobster-999 不存在"
}
```

---

## 🔐 认证 (未来版本)

当前版本无需认证。未来版本将支持：
- API Token 认证
- 用户权限控制
- 请求速率限制

---

**🦞 API 设计遵循 RESTful 规范！**
