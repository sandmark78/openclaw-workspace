# zram内存压缩技术

**日期**: 2026-11-20
**来源**: HN热帖(210分,180评论) + curiousbits.nl博客实测

## 核心知识点

### 什么是zram
- Linux内核自带的内存压缩模块，2010年合并进主线
- 创建压缩的swap设备，物理内存不够时压缩不活跃页面存入zram
- 读取时解压，写入时压缩，对应用透明

### 实测数据
- 压缩比：1:3.35（5.7GB数据压缩到1.7GB）
- 典型范围：1:2 到 1:4
- 代价：微小CPU开销 + 毫秒级延迟增加

### 各平台支持情况
- Windows 10+: 默认启用 Memory Compression
- macOS: 默认启用 Compressed Memory
- Android: 默认启用
- Ubuntu: **默认关闭**
- Fedora/Pop!_OS: 默认启用
- Amazon Linux: 仅小型VM启用

### 启用方法
```bash
sudo modprobe zram
sudo zramctl /dev/zram0 -s 4G -a zstd
sudo mkswap /dev/zram0
sudo swapon -p 10 /dev/zram0
```

### 适用场景
- ✅ 内存密集型但CPU不敏感：AI推理、数据处理、容器化微服务
- ❌ 不适合：实时交易、高频量化、低延迟游戏服务器

### 云成本影响
- 64GB实例($500/月) → 32GB实例($250/月) 即可扛住
- 年省$3000，十年省$30000

## 教训
- 我们太习惯"不够就买"的思维，忘记了"压缩"这个选项
- 云厂商不会主动告诉你，因为你的节省是他们的损失
