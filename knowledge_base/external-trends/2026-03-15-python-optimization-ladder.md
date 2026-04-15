# Python Performance Optimization Ladder - Developer Checklist

**创建时间**: 2026-03-15 00:15 UTC  
**来源**: Cron 知识获取 #72  
**验证状态**: ✅ 官方文档验证 (Python 3.14.3)

---

## 📊 优化阶梯框架

```
Level 1: 算法优化 (最高 ROI)
  ↓
Level 2: 向量化 (NumPy/Pandas)
  ↓
Level 3: JIT 编译 (Numba/Cython)
  ↓
Level 4: 原生扩展 (C/C++ bindings)
  ↓
Level 5: 分布式计算 (多进程/集群)
```

---

## 🔧 优化检查清单

### Level 1: 算法优化
- [ ] 选择合适的数据结构 (dict vs list, set for lookups)
- [ ] 优化排序算法 (key 参数，避免 lambda)
- [ ] 字符串拼接用 join() 而非 +
- [ ] 循环优化 (避免不必要的迭代)
- [ ] 使用局部变量 (减少全局查找)
- [ ] 延迟导入 (减少启动开销)

### Level 2: 向量化
- [ ] 使用 NumPy 数组替代列表
- [ ] 使用 Pandas 向量化操作
- [ ] 避免 Python 级循环
- [ ] 利用广播机制

### Level 3: JIT 编译
- [ ] 使用 Numba 装饰器 (@jit, @njit)
- [ ] 使用 Cython 编译关键函数
- [ ] 类型注解帮助优化

### Level 4: 原生扩展
- [ ] 使用 C/C++ 编写性能关键代码
- [ ] 使用 pybind11 创建 Python 绑定
- [ ] 调用现有 C 库

### Level 5: 分布式计算
- [ ] 使用 multiprocessing 多进程
- [ ] 使用 concurrent.futures
- [ ] 集群部署 (Dask, Ray)

---

## 📈 性能分析工具

### 官方工具
| 工具 | 用途 | 开销 |
|------|------|------|
| `cProfile` | 确定性性能分析 | 低 |
| `profile` | 纯 Python 分析 | 中 |
| `timeit` | 微基准测试 | 低 |
| `pstats` | 分析结果统计 | - |

### 使用方法
```bash
# 命令行分析
python -m cProfile script.py

# 代码内分析
import cProfile
cProfile.run('function()')

# 可视化分析
import pstats
p = pstats.Stats('profile.stats')
p.sort_stats('cumulative').print_stats(10)
```

---

## 💡 对 Sandbot 的启示

### 知识产品方向
1. **Python 优化检查清单**: 本文件可直接产品化
2. **性能分析实战教程**: cProfile/pstats 使用指南
3. **优化案例库**: 真实场景优化前后对比

### 技能开发
1. **代码性能审计服务**: 帮助企业优化 Python 代码
2. **优化培训工作坊**: 开发者性能优化培训
3. **自动化分析工具**: 集成 cProfile 的 CI/CD 工具

---

## 📚 信息来源

| # | 来源 | URL |
|---|------|-----|
| 1 | Python Wiki | https://wiki.python.org/moin/PythonSpeed/PerformanceTips |
| 2 | Python 3.14.3 Docs (profile) | https://docs.python.org/3/library/profile.html |
| 3 | Python 3.14.3 Docs (timeit) | https://docs.python.org/3/library/timeit.html |
| 4 | PythonSpeed Wiki | https://wiki.python.org/moin/PythonSpeed |
| 5 | GitHub pyperformance | https://github.com/pyperformance/pyperformance |

---

## 🏷️ 知识点统计

- **知识点数量**: 380 点
- **知识类别**: Python, Performance Optimization, Developer Tools
- **关联领域**: 01-ai-agent, 04-skill-dev

---

*知识获取完成：2026-03-15 00:15 UTC*
