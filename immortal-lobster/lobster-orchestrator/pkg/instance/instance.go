package instance

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"sync"
	"syscall"
	"time"
)

var (
	// 日志记录器
	infoLog  = log.New(os.Stdout, "🦞 INFO [orchestrator] ", log.Ldate|log.Ltime)
	errorLog = log.New(os.Stderr, "❌ ERROR [orchestrator] ", log.Ldate|log.Ltime)
	warnLog  = log.New(os.Stderr, "⚠️  WARN [orchestrator] ", log.Ldate|log.Ltime)
)

// Instance 表示一个 PicoClaw 实例
type Instance struct {
	ID            string `yaml:"id"`
	Name          string `yaml:"name"`
	Workspace     string `yaml:"workspace"`
	Port          int    `yaml:"port"`
	Model         string `yaml:"model"`
	APIKeyEnv     string `yaml:"api_key_env"`
	MemoryLimitMB int    `yaml:"memory_limit_mb"`
	AutoStart     bool   `yaml:"auto_start"`

	// 运行时状态
	PID          int       `json:"pid"`
	Status       string    `json:"status"` // running, stopped, crashed
	StartTime    time.Time `json:"start_time"`
	RestartCount int       `json:"restart_count"`
	LastError    string    `json:"last_error,omitempty"`

	// 内部字段
	cmd   *exec.Cmd
	mutex sync.RWMutex
}

// Manager 管理所有实例
type Manager struct {
	Instances  map[string]*Instance
	ConfigPath string
	mutex      sync.RWMutex
}

// NewManager 创建实例管理器
func NewManager(configPath string) (*Manager, error) {
	infoLog.Printf("加载配置文件：%s", configPath)
	
	config, err := LoadConfig(configPath)
	if err != nil {
		errorLog.Printf("加载配置失败：%v", err)
		return nil, err
	}

	// 验证配置
	if err := ValidateConfig(config); err != nil {
		errorLog.Printf("配置验证失败：%v", err)
		return nil, err
	}
	infoLog.Printf("✅ 配置验证通过")

	// 验证工作目录
	if err := ValidateAllWorkspaces(config); err != nil {
		warnLog.Printf("工作目录验证警告：%v", err)
		// 不阻断启动，继续执行
	}

	instances := make(map[string]*Instance)
	for _, cfg := range config.Instances {
		instances[cfg.ID] = &Instance{
			ID:            cfg.ID,
			Name:          cfg.Name,
			Workspace:     cfg.Workspace,
			Port:          cfg.Port,
			Model:         cfg.Model,
			APIKeyEnv:     cfg.APIKeyEnv,
			MemoryLimitMB: cfg.MemoryLimitMB,
			AutoStart:     cfg.AutoStart,
			Status:        "stopped",
		}
	}

	infoLog.Printf("✅ 加载 %d 个实例配置", len(instances))
	return &Manager{
		Instances:  instances,
		ConfigPath: configPath,
	}, nil
}

// Start 启动单个实例
func (m *Manager) Start(id string) error {
	m.mutex.Lock()
	defer m.mutex.Unlock()

	inst, exists := m.Instances[id]
	if !exists {
		return fmt.Errorf("实例 %s 不存在", id)
	}

	if inst.Status == "running" {
		warnLog.Printf("实例 %s 已在运行 (PID: %d)", inst.Name, inst.PID)
		return nil
	}

	infoLog.Printf("🚀 启动实例：%s (端口：%d)", inst.Name, inst.Port)

	// 确保 workspace 目录存在
	if err := os.MkdirAll(inst.Workspace, 0755); err != nil {
		inst.Status = "crashed"
		inst.LastError = fmt.Sprintf("创建工作目录失败：%v", err)
		errorLog.Printf("实例 %s 工作目录创建失败：%v", inst.Name, err)
		return fmt.Errorf("创建工作目录失败：%v", err)
	}

	// 构建 PicoClaw 启动命令
	// 优先使用环境变量 PICOCLAW_PATH，否则使用默认路径
	picoclawPath := os.Getenv("PICOCLAW_PATH")
	if picoclawPath == "" {
		// 尝试从 PATH 中查找
		path, err := exec.LookPath("picoclaw")
		if err != nil {
			// 默认路径
			picoclawPath = "/usr/local/bin/picoclaw"
		} else {
			picoclawPath = path
		}
	}
	
	cmd := exec.Command(picoclawPath, "serve", "--port", fmt.Sprintf("%d", inst.Port))
	cmd.Dir = inst.Workspace
	cmd.Env = append(os.Environ(),
		fmt.Sprintf("PORT=%d", inst.Port),
		fmt.Sprintf("WORKSPACE=%s", inst.Workspace),
		fmt.Sprintf("PICOCLAW_PATH=%s", picoclawPath),
	)

	// 设置进程组 (便于后续杀死整个进程树)
	cmd.SysProcAttr = &syscall.SysProcAttr{Setpgid: true}

	// 启动进程
	if err := cmd.Start(); err != nil {
		inst.Status = "crashed"
		inst.LastError = fmt.Sprintf("启动失败：%v", err)
		inst.RestartCount++
		errorLog.Printf("实例 %s 启动失败 (第 %d 次): %v", inst.Name, inst.RestartCount, err)
		return fmt.Errorf("启动失败：%v", err)
	}

	inst.cmd = cmd
	inst.PID = cmd.Process.Pid
	inst.Status = "running"
	inst.StartTime = time.Now()
	inst.LastError = ""

	infoLog.Printf("✅ 实例 %s 已启动 (PID: %d, Port: %d)", inst.Name, inst.PID, inst.Port)
	return nil
}

// Stop 停止单个实例
func (m *Manager) Stop(id string) error {
	m.mutex.Lock()
	defer m.mutex.Unlock()

	inst, exists := m.Instances[id]
	if !exists {
		return fmt.Errorf("实例 %s 不存在", id)
	}

	if inst.Status != "running" {
		warnLog.Printf("实例 %s 未在运行 (状态：%s)", inst.Name, inst.Status)
		return nil
	}

	infoLog.Printf("⏹️  停止实例：%s (PID: %d)", inst.Name, inst.PID)

	// 杀死进程组
	if inst.cmd != nil && inst.cmd.Process != nil {
		// 先尝试优雅退出
		syscall.Kill(-inst.cmd.Process.Pid, syscall.SIGTERM)
		
		// 等待最多 5 秒
		for i := 0; i < 10; i++ {
			if inst.cmd.ProcessState != nil {
				break  // 已退出
			}
			time.Sleep(500 * time.Millisecond)
		}
		
		// 如果还没死，强制杀死
		if inst.cmd.ProcessState == nil {
			warnLog.Printf("实例 %s 未响应 SIGTERM，发送 SIGKILL", inst.Name)
			syscall.Kill(-inst.cmd.Process.Pid, syscall.SIGKILL)
			time.Sleep(1 * time.Second)
		}
	}

	inst.Status = "stopped"
	inst.PID = 0
	inst.cmd = nil

	infoLog.Printf("✅ 实例 %s 已停止", inst.Name)
	return nil
}

// Restart 重启实例
func (m *Manager) Restart(id string) error {
	infoLog.Printf("🔄 重启实例：%s", id)
	if err := m.Stop(id); err != nil {
		return err
	}
	time.Sleep(1 * time.Second)
	return m.Start(id)
}

// AutoStart 自动启动所有标记为 auto_start 的实例
func (m *Manager) AutoStart() {
	infoLog.Printf("🚀 开始自动启动...")
	count := 0
	for id := range m.Instances {
		inst := m.Instances[id]
		if inst.AutoStart {
			go func(id string) {
				if err := m.Start(id); err != nil {
					errorLog.Printf("自动启动 %s 失败：%v", id, err)
				}
			}(id)
			count++
			time.Sleep(200 * time.Millisecond) // 避免同时启动冲击
		}
	}
	infoLog.Printf("✅ 自动启动完成 (%d 个实例)", count)
}

// StopAll 停止所有实例
func (m *Manager) StopAll() {
	infoLog.Printf("👋 正在关闭所有实例...")
	for id := range m.Instances {
		m.Stop(id)
	}
	infoLog.Printf("✅ 所有实例已关闭")
}

// GetStatus 获取实例状态
func (m *Manager) GetStatus(id string) (map[string]interface{}, error) {
	m.mutex.RLock()
	defer m.mutex.RUnlock()

	inst, exists := m.Instances[id]
	if !exists {
		return nil, fmt.Errorf("实例 %s 不存在", id)
	}

	inst.mutex.RLock()
	defer inst.mutex.RUnlock()

	uptime := float64(0)
	if !inst.StartTime.IsZero() && inst.Status == "running" {
		uptime = time.Since(inst.StartTime).Seconds()
	}

	return map[string]interface{}{
		"id":             inst.ID,
		"name":           inst.Name,
		"status":         inst.Status,
		"pid":            inst.PID,
		"port":           inst.Port,
		"workspace":      inst.Workspace,
		"start_time":     inst.StartTime,
		"restart_count":  inst.RestartCount,
		"last_error":     inst.LastError,
		"uptime_seconds": uptime,
	}, nil
}

// GetAllStatus 获取所有实例状态
func (m *Manager) GetAllStatus() []map[string]interface{} {
	m.mutex.RLock()
	defer m.mutex.RUnlock()

	statuses := make([]map[string]interface{}, 0, len(m.Instances))
	for id := range m.Instances {
		if status, err := m.GetStatus(id); err == nil {
			statuses = append(statuses, status)
		}
	}
	return statuses
}

// CheckHealth 检查实例健康状态 (被 monitor 调用)
func (m *Manager) CheckHealth(id string) bool {
	m.mutex.RLock()
	inst, exists := m.Instances[id]
	m.mutex.RUnlock()

	if !exists || inst.Status != "running" {
		return false
	}

	// 检查进程是否还活着
	if inst.cmd != nil && inst.cmd.ProcessState != nil {
		// 进程已退出
		warnLog.Printf("实例 %s 崩溃 (PID: %d)", inst.Name, inst.PID)
		inst.Status = "crashed"
		inst.RestartCount++
		return false
	}

	return true
}

// ReloadConfig 重新加载配置 (未来功能)
func (m *Manager) ReloadConfig() error {
	infoLog.Printf("📋 重新加载配置...")
	// TODO: 实现配置热重载
	return fmt.Errorf("未实现")
}
