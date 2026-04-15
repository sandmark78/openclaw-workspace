# 用 Orange Pi 6 Plus + Lobster 搭建你的边缘 AI 编排平台

> HN 热度信号: Orange Pi 6 Plus 98pts/66c（讨论密度 0.67）
> 反云叙事窗口: Backblaze 559c + "Fuck the Cloud" 复活 + WP 后门 6 天核爆

## 为什么是 Orange Pi 6 Plus？

- RK3588 8 核 ARM，8GB/16GB RAM
- 价格 ~$50-80，性能远超树莓派 5
- 支持 NPU 加速（6 TOPS）
- 社区活跃，Linux 支持完善

## 为什么是 Lobster？

- 专为旧手机/SBC 设计的多实例编排器
- 每实例 <10MB 内存
- Go 单二进制部署，零依赖
- RESTful API + Web Dashboard

## 30 分钟部署指南

### 硬件准备
1. Orange Pi 6 Plus（8GB 版本推荐）
2. 32GB+ microSD 卡
3. 电源（5V/3A USB-C）
4. 网络连接

### 系统安装
```bash
# 1. 刷入 Armbian（推荐 Ubuntu 24.04）
# 2. SSH 登录
ssh root@orangepi.local

# 3. 安装 Docker（可选，如果用容器模式）
curl -fsSL https://get.docker.com | sh

# 4. 或直接下载 Lobster 二进制
wget https://github.com/immortal-lobster/lobster-orchestrator/releases/latest/download/lobster-linux-arm64
chmod +x lobster-linux-arm64
```

### 运行 Lobster
```bash
# 启动编排器
./lobster-linux-arm64 --port 8080

# 访问 Web Dashboard
# http://orangepi.local:8080

# 创建第一个 PicoClaw 实例
curl -X POST http://localhost:8080/api/v1/instances \
  -d '{"name": "my-agent", "memory_limit": "50MB"}'
```

### 成本对比
| 方案 | 月成本 | 性能 | 隐私 |
|------|--------|------|------|
| 云服务器 (VPS) | $5-20 | 中等 | 低 |
| Orange Pi + Lobster | **$0**（一次性 $60） | 高（NPU） | **完全本地** |

## 下一步

- GitHub: https://github.com/immortal-lobster/lobster-orchestrator
- 文档: /docs/ 目录下的完整部署指南
- 社区: 加入不死龙虾联盟

---

*草稿: 2026-04-15*
*目标发布: GitHub Discussion + Orange Pi 论坛*
