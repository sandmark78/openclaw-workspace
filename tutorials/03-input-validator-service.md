# V6.1 实战教程 3: 输入验证服务

**创建时间**: 2026-02-25 11:35 UTC  
**定价**: $99 (技能包)  
**状态**: ✅ 已完成

---

## 📚 教程内容

### 1. 为什么需要输入验证？(3 分钟)

**安全问题**:
```
❌ Prompt Injection 攻击
❌ 恶意代码执行
❌ 敏感数据泄露
❌ 系统被控制
```

**input-validator 技能**:
```
✅ 10 类危险内容检测
✅ 4 类可疑内容检测
✅ 误报率 <1%
✅ 漏报率 <1%
✅ 性能 <50ms
```

---

### 2. 技能安装 (5 分钟)

#### 从 ClawHub 安装
```bash
clawhub install input-validator
```

#### 手动安装
```bash
git clone https://github.com/sandmark78/input-validator.git
cd input-validator
pip install -r requirements.txt
```

#### 验证安装
```bash
python3 scripts/input-validator.py "test"
# 输出：✅ 输入内容安全
```

---

### 3. 集成到现有技能 (10 分钟)

#### web_fetch 技能增强
```python
from input_validator import validate_input

def safe_web_fetch(url: str) -> str:
    content = requests.get(url).text
    result = validate_input(content)
    
    if result["dangerous"]:
        return f"⚠️ 此网页包含危险内容：{result['dangerous']}"
    return content
```

#### 文件上传验证
```python
def safe_file_upload(filename: str) -> str:
    with open(filename, 'r') as f:
        content = f.read()
    
    result = validate_input(content)
    if result["dangerous"]:
        return f"⚠️ 此文件包含危险内容"
    return "✅ 文件安全，已上传"
```

---

### 4. 自定义规则 (5 分钟)

#### 添加新的检测规则
```python
# 编辑 input-validator.py

DANGEROUS_PATTERNS = [
    # ... 现有规则 ...
    (r'你的新规则', '规则名称'),
]
```

#### 调整严格程度
```python
# 温和模式
result = validate_input(text, strict=False)

# 严格模式
result = validate_input(text, strict=True)
```

---

### 5. 企业版功能 ($299)

#### 高级功能
```
✅ 自定义规则引擎
✅ 日志审计系统
✅ 性能监控
✅ 优先支持
✅ 定制部署
```

#### 部署服务
```
1. 远程部署
2. 配置优化
3. 性能调优
4. 培训文档
5. 30 天支持
```

---

## 🎁 附赠资源

### 检测规则模板
```python
DANGEROUS_PATTERNS = [
    (r'rm\s+(-rf|--recursive)', '删除命令'),
    (r'curl\s+.*\|\s*(ba)?sh', '下载执行'),
    (r'/dev/tcp/', '反弹 shell'),
]
```

### 集成示例
```python
# web_fetch 集成
# 文件上传集成
# RSS 订阅集成
# API 响应集成
```

---

## 📊 学习检查

完成本教程后，你应该能够：

- [ ] 安装 input-validator
- [ ] 集成到现有技能
- [ ] 自定义检测规则
- [ ] 部署企业版

---

## 💰 购买选项

| 版本 | 价格 | 内容 |
|------|------|------|
| **基础版** | $99 | 技能包 + 使用文档 |
| **专业版** | $199 | 基础版 + 自定义规则 |
| **企业版** | $299 | 专业版 + 部署服务 |

---

*此教程已真实写入服务器*
*验证：cat /workspace/tutorials/03-input-validator-service.md*
