package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"

	"lobster-orchestrator/pkg/instance"
	"lobster-orchestrator/pkg/api"
	"lobster-orchestrator/pkg/monitor"
)

var (
	configPath = flag.String("config", "configs/instances.yaml", "实例配置文件路径")
	port       = flag.Int("port", 8080, "Orchestrator Web 端口")
	help       = flag.Bool("help", false, "显示帮助信息")
)

func main() {
	flag.Parse()

	if *help {
		fmt.Println("Lobster Orchestrator - 不死龙虾编排器")
		fmt.Println("用法：orchestrator [选项]")
		fmt.Println("选项:")
		flag.PrintDefaults()
		os.Exit(0)
	}

	log.Printf("🦞 Lobster Orchestrator 启动中...")
	log.Printf("📋 配置文件：%s", *configPath)
	log.Printf("🌐 Web 端口：%d", *port)

	// 1. 加载配置
	manager, err := instance.NewManager(*configPath)
	if err != nil {
		log.Fatalf("❌ 加载配置失败：%v", err)
	}
	log.Printf("✅ 加载 %d 个实例配置", len(manager.Instances))

	// 2. 启动健康监控
	monitor.Start(manager, 30) // 30 秒检查一次
	log.Printf("✅ 健康监控已启动")

	// 3. 启动 API 服务器
	go api.StartServer(*port, manager)
	log.Printf("✅ API 服务器已启动 (http://localhost:%d)", *port)

	// 4. 自动启动标记为 auto_start 的实例
	manager.AutoStart()
	log.Printf("✅ 自动启动完成")

	// 5. 等待退出信号
	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, syscall.SIGINT, syscall.SIGTERM)
	<-sigChan

	log.Printf("👋 正在关闭...")
	manager.StopAll()
	log.Printf("✅ 已关闭所有实例")
}
