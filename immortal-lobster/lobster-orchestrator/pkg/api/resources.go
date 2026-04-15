package api

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"syscall"
	"time"
)

// ResourceStats 资源统计
type ResourceStats struct {
	Memory float64 `json:"memory"`
	CPU    float64 `json:"cpu"`
	Disk   float64 `json:"disk"`
}

// BackupInfo 备份信息
type BackupInfo struct {
	Name string `json:"name"`
	Size string `json:"size"`
	Date string `json:"date"`
}

// GetResourceStats 获取资源统计
func GetResourceStats() ResourceStats {
	stats := ResourceStats{}

	// 内存 (从 /proc/meminfo)
	if data, err := os.ReadFile("/proc/meminfo"); err == nil {
		lines := strings.Split(string(data), "\n")
		var total, available uint64
		for _, line := range lines {
			if strings.HasPrefix(line, "MemTotal:") {
				fields := strings.Fields(line)
				if len(fields) >= 2 {
					total, _ = strconv.ParseUint(fields[1], 10, 64)
				}
			} else if strings.HasPrefix(line, "MemAvailable:") {
				fields := strings.Fields(line)
				if len(fields) >= 2 {
					available, _ = strconv.ParseUint(fields[1], 10, 64)
				}
			}
		}
		if total > 0 {
			used := float64(total-available) / 1024 // KB to MB
			stats.Memory = used
		}
	}

	// CPU (简化版本，从 /proc/stat)
	if data, err := os.ReadFile("/proc/stat"); err == nil {
		lines := strings.Split(string(data), "\n")
		if len(lines) > 0 {
			fields := strings.Fields(lines[0])
			if len(fields) >= 5 {
				var idle, total uint64
				for i, f := range fields[1:] {
					val, _ := strconv.ParseUint(f, 10, 64)
					total += val
					if i == 3 { // idle
						idle = val
					}
				}
				if total > 0 {
					stats.CPU = float64(total-idle) / float64(total) * 100
				}
			}
		}
	}

	// 磁盘
	if info, err := os.Stat("/"); err == nil {
		if sys, ok := info.Sys().(*syscall.Statfs_t); ok {
			total := float64(sys.Blocks) * float64(sys.Bsize) / 1024 / 1024 / 1024 // Bytes to GB
			available := float64(sys.Bavail) * float64(sys.Bsize) / 1024 / 1024 / 1024
			stats.Disk = total - available
		}
	}

	return stats
}

// BackupHandler 备份
func BackupHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method != "POST" {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	// 执行备份脚本
	backupName := fmt.Sprintf("backup-%s", time.Now().Format("20060102-150405"))
	cmd := exec.Command("./scripts/backup.sh", backupName)
	output, err := cmd.CombinedOutput()

	if err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": err.Error(),
		})
		return
	}

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success":     true,
		"backup_name": backupName,
		"output":      string(output),
	})
}

// ListBackupsHandler 列出备份
func ListBackupsHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	backups := []BackupInfo{}

	// 读取备份目录
	backupDir := "data/backups"
	if entries, err := os.ReadDir(backupDir); err == nil {
		for _, entry := range entries {
			if entry.IsDir() {
				name := entry.Name()
				
				// 获取目录大小
				var size int64
				filepath.Walk(filepath.Join(backupDir, name), func(path string, info os.FileInfo, err error) error {
					if err == nil {
						size += info.Size()
					}
					return nil
				})

				sizeStr := formatSize(size)

				// 解析日期
				date := name
				if len(name) > 7 {
					date = name[7:] // 去掉 "backup-"
				}

				backups = append(backups, BackupInfo{
					Name: name,
					Size: sizeStr,
					Date: date,
				})
			}
		}
	}

	// 按日期排序
	sort.Slice(backups, func(i, j int) bool {
		return backups[i].Date > backups[j].Date
	})

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success":  true,
		"backups":  backups,
		"count":    len(backups),
	})
}

// RestoreHandler 恢复备份
func RestoreHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method != "POST" {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	var req struct {
		Backup string `json:"backup"`
	}

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "无效的请求",
		})
		return
	}

	if req.Backup == "" {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "未指定备份名称",
		})
		return
	}

	// 执行恢复脚本
	cmd := exec.Command("./scripts/restore.sh", req.Backup)
	output, err := cmd.CombinedOutput()

	if err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": err.Error(),
		})
		return
	}

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success": true,
		"output":  string(output),
	})
}

// ImportOpenClawHandler 导入 OpenClaw
func ImportOpenClawHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method != "POST" {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	var req struct {
		Type string `json:"type"`
		Path string `json:"path"`
	}

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "无效的请求",
		})
		return
	}

	if req.Path == "" {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "未指定导出文件路径",
		})
		return
	}

	// 执行导入脚本
	script := "./scripts/import-to-lobster.sh"
	args := []string{req.Path}

	cmd := exec.Command(script, args...)
	output, err := cmd.CombinedOutput()

	if err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": err.Error(),
		})
		return
	}

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success": true,
		"output":  string(output),
	})
}

// formatSize 格式化文件大小
func formatSize(bytes int64) string {
	const (
		KB = 1024
		MB = KB * 1024
		GB = MB * 1024
	)

	switch {
	case bytes >= GB:
		return fmt.Sprintf("%.1f GB", float64(bytes)/GB)
	case bytes >= MB:
		return fmt.Sprintf("%.1f MB", float64(bytes)/MB)
	case bytes >= KB:
		return fmt.Sprintf("%.1f KB", float64(bytes)/KB)
	default:
		return fmt.Sprintf("%d B", bytes)
	}
}
