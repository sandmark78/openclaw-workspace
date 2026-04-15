# NVIDIA NemoClaw - OpenClaw 安全沙箱化部署方案

**来源**: GitHub NVIDIA/NemoClaw (2026-03-18)  
**HN 评分**: 26 points  
**领域**: OpenClaw 生态 / 安全部署 / NVIDIA Agent Toolkit  
**数量**: 12 知识点  
**状态**: Alpha (早期阶段)

---

## 核心概念

NVIDIA NemoClaw 是一个开源工具，用于**安全地运行 OpenClaw Agent**。它将 OpenClaw 安装在 NVIDIA OpenShell 安全运行时中，通过 Landlock + seccomp + netns 实现沙箱隔离，推理请求通过 NVIDIA Cloud 路由。

## 架构组件

| 组件 | 角色 |
|------|------|
| Plugin | TypeScript CLI，管理启动/连接/状态/日志 |
| Blueprint | 版本化 Python 构件，编排沙箱创建、策略和推理设置 |
| Sandbox | 隔离的 OpenShell 容器，运行受策略约束的 OpenClaw |
| Inference | NVIDIA 云模型调用，通过 OpenShell 网关路由 |

## 安全特性

### 沙箱隔离
- **Landlock**: Linux 安全模块，限制文件系统访问
- **seccomp**: 系统调用过滤
- **netns**: 网络命名空间隔离
- 每个网络请求、���件访问、推理调用都受声明式策略管控

### Blueprint 生命周期
```
解析构件 → 验证摘要 → 规划资源 → 通过 OpenShell CLI 应用
```

## 系统要求

| 资源 | 最低 | 推荐 |
|------|------|------|
| CPU | 4 vCPU | 4+ vCPU |
| RAM | 8 GB | 16 GB |
| 磁盘 | 20 GB | 40 GB |

- 沙箱镜像约 2.4 GB 压缩
- 需要 Ubuntu 22.04+, Node.js 20+, Docker

## 默认模型
- **nvidia/nemotron-3-super-120b-a12b** (NVIDIA Cloud API)

## 安装方式
```bash
curl -fsSL https://nvidia.com/nemoclaw.sh | bash
```

## 使用方式
```bash
# 连接沙箱
nemoclaw my-assistant connect

# TUI 交互
openclaw tui

# CLI 单消息
openclaw agent --agent main --local -m "hello" --session-id test
```

## 对我们的意义

### 1. NVIDIA 官方支持 OpenClaw 生态
NVIDIA 为 OpenClaw 开发专用安全部署工具，说明 OpenClaw 在 AI Agent 领域的地位得到头部厂商认可。

### 2. 安全是 Agent 部署的核心需求
NemoClaw 的存在验证了"Agent 安全部署"是真实市场需求，不是伪需求。

### 3. 与 Snowflake 漏洞形成对比
Snowflake Cortex 刚曝出沙箱逃逸漏洞，NemoClaw 用 Landlock+seccomp+netns 三层隔离应对，是更成熟的安全方案。

### 4. 技能开发机会
- 为 NemoClaw 编写安全策略模板
- 开发 OpenClaw 安全审计技能
- 撰写 NemoClaw 部署教程

---

**OpenClaw 生态相关性**: ⭐⭐⭐⭐⭐ 直接相关
**技术深度**: ⭐⭐⭐⭐ 安全架构清晰
**影响力机会**: ⭐⭐⭐⭐ 早期项目，贡献空间大
