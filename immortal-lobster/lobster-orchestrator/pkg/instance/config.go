package instance

import (
	"os"

	"gopkg.in/yaml.v3"
)

// Config 配置结构
type Config struct {
	Instances []InstanceConfig `yaml:"instances"`
	Global    GlobalConfig     `yaml:"global"`
}

// InstanceConfig 单个实例配置
type InstanceConfig struct {
	ID            string `yaml:"id"`
	Name          string `yaml:"name"`
	Workspace     string `yaml:"workspace"`
	Port          int    `yaml:"port"`
	Model         string `yaml:"model"`
	APIKeyEnv     string `yaml:"api_key_env"`
	MemoryLimitMB int    `yaml:"memory_limit_mb"`
	AutoStart     bool   `yaml:"auto_start"`
}

// GlobalConfig 全局配置
type GlobalConfig struct {
	OrchestratorPort      int    `yaml:"orchestrator_port"`
	HealthCheckIntervalS  int    `yaml:"health_check_interval_s"`
	LogLevel              string `yaml:"log_level"`
	MaxInstances          int    `yaml:"max_instances"`
}

// LoadConfig 从 YAML 文件加载配置
func LoadConfig(path string) (*Config, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}

	var config Config
	if err := yaml.Unmarshal(data, &config); err != nil {
		return nil, err
	}

	// 设置默认值
	if config.Global.OrchestratorPort == 0 {
		config.Global.OrchestratorPort = 8080
	}
	if config.Global.HealthCheckIntervalS == 0 {
		config.Global.HealthCheckIntervalS = 30
	}
	if config.Global.MaxInstances == 0 {
		config.Global.MaxInstances = 50
	}

	return &config, nil
}

// SaveConfig 保存配置到 YAML 文件
func SaveConfig(path string, config *Config) error {
	data, err := yaml.Marshal(config)
	if err != nil {
		return err
	}
	return os.WriteFile(path, data, 0644)
}
