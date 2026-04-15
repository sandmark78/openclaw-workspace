package monitor

import (
	"fmt"
	"log"
	"time"

	"lobster-orchestrator/pkg/instance"
)

// Start 启动健康监控
func Start(manager *instance.Manager, intervalSeconds int) {
	go func() {
		ticker := time.NewTicker(time.Duration(intervalSeconds) * time.Second)
		defer ticker.Stop()

		for range ticker.C {
			checkAndRecover(manager)
		}
	}()
}

// checkAndRecover 检查实例健康并自动恢复
func checkAndRecover(manager *instance.Manager) {
	statuses := manager.GetAllStatus()

	for _, status := range statuses {
		id, _ := status["id"].(string)
		currentStatus, _ := status["status"].(string)

		// 检查运行中的实例
		if currentStatus == "running" {
			if !manager.CheckHealth(id) {
				// 实例崩溃，尝试重启
				restartCount, _ := status["restart_count"].(int)
				log.Printf("⚠️  实例 %s 崩溃，尝试重启 (第 %d 次)...", id, restartCount+1)

				if err := manager.Restart(id); err != nil {
					log.Printf("❌ 重启 %s 失败：%v", id, err)
				} else {
					log.Printf("✅ 实例 %s 重启成功", id)
				}
			}
		}
	}

	fmt.Printf("🔍 健康检查完成 (%d 个实例)\n", len(statuses))
}
