package instance

import (
	"fmt"
	"net"
	"os"
)

// ValidateConfig 验证配置有效性
func ValidateConfig(config *Config) error {
	if len(config.Instances) == 0 {
		return fmt.Errorf("配置中无实例")
	}

	if len(config.Instances) > config.Global.MaxInstances {
		return fmt.Errorf("实例数 (%d) 超过最大限制 (%d)", len(config.Instances), config.Global.MaxInstances)
	}

	ports := make(map[int]bool)
	ids := make(map[string]bool)

	for i, inst := range config.Instances {
		// 验证 ID 唯一性
		if ids[inst.ID] {
			return fmt.Errorf("实例 ID %s 重复 (第 %d 个)", inst.ID, i+1)
		}
		ids[inst.ID] = true

		// 验证 ID 格式
		if inst.ID == "" {
			return fmt.Errorf("第 %d 个实例 ID 为空", i+1)
		}

		// 验证名称
		if inst.Name == "" {
			return fmt.Errorf("实例 %s 名称为空", inst.ID)
		}

		// 验证工作目录
		if inst.Workspace == "" {
			return fmt.Errorf("实例 %s 工作目录为空", inst.ID)
		}

		// 验证端口
		if inst.Port < 1024 || inst.Port > 65535 {
			return fmt.Errorf("实例 %s 端口 %d 超出有效范围 (1024-65535)", inst.ID, inst.Port)
		}

		// 验证端口冲突
		if ports[inst.Port] {
			return fmt.Errorf("实例 %s 端口 %d 与之前的实例冲突", inst.ID, inst.Port)
		}
		ports[inst.Port] = true

		// 验证端口是否被占用
		if err := checkPortAvailable(inst.Port); err != nil {
			return fmt.Errorf("实例 %s 端口 %d 不可用：%v", inst.ID, inst.Port, err)
		}

		// 验证内存限制
		if inst.MemoryLimitMB < 5 {
			return fmt.Errorf("实例 %s 内存限制过小 (%dMB)", inst.ID, inst.MemoryLimitMB)
		}
		if inst.MemoryLimitMB > 1024 {
			return fmt.Errorf("实例 %s 内存限制过大 (%dMB)", inst.ID, inst.MemoryLimitMB)
		}

		// 验证模型配置
		if inst.Model == "" {
			return fmt.Errorf("实例 %s 模型配置为空", inst.ID)
		}

		// 验证 API Key 环境变量
		if inst.APIKeyEnv == "" {
			return fmt.Errorf("实例 %s API Key 环境变量为空", inst.ID)
		}
	}

	// 验证全局配置
	if config.Global.OrchestratorPort < 1024 || config.Global.OrchestratorPort > 65535 {
		return fmt.Errorf("Orchestrator 端口 %d 超出有效范围", config.Global.OrchestratorPort)
	}

	if config.Global.HealthCheckIntervalS < 10 {
		return fmt.Errorf("健康检查间隔过短 (%ds)", config.Global.HealthCheckIntervalS)
	}

	if config.Global.HealthCheckIntervalS > 300 {
		return fmt.Errorf("健康检查间隔过长 (%ds)", config.Global.HealthCheckIntervalS)
	}

	return nil
}

// checkPortAvailable 检查端口是否可用
func checkPortAvailable(port int) error {
	ln, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
	if err != nil {
		return err
	}
	ln.Close()
	return nil
}

// ValidateWorkspace 验证工作目录
func ValidateWorkspace(path string) error {
	// 检查是否存在
	info, err := os.Stat(path)
	if os.IsNotExist(err) {
		// 尝试创建
		if err := os.MkdirAll(path, 0755); err != nil {
			return fmt.Errorf("创建工作目录失败：%v", err)
		}
		return nil
	}
	if err != nil {
		return err
	}

	// 检查是否是目录
	if !info.IsDir() {
		return fmt.Errorf("%s 不是目录", path)
	}

	// 检查是否可写
	testFile := path + "/.write_test"
	if err := os.WriteFile(testFile, []byte(""), 0644); err != nil {
		return fmt.Errorf("工作目录不可写：%v", err)
	}
	os.Remove(testFile)

	return nil
}

// ValidateAllWorkspaces 验证所有工作目录
func ValidateAllWorkspaces(config *Config) error {
	for _, inst := range config.Instances {
		if err := ValidateWorkspace(inst.Workspace); err != nil {
			return fmt.Errorf("实例 %s 工作目录验证失败：%v", inst.ID, err)
		}
	}
	return nil
}
