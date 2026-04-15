package api

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strings"
)

// InstanceBackupHandler 实例备份
func InstanceBackupHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method != "POST" {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	var req struct {
		InstanceID string `json:"instance_id"`
	}

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "无效的请求",
		})
		return
	}

	if req.InstanceID == "" {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "未指定实例 ID",
		})
		return
	}

	// 备份单个实例的工作区
	backupName := fmt.Sprintf("instance-%s-%s", req.InstanceID, getTimeStamp())
	backupDir := fmt.Sprintf("data/backups/instances/%s", backupName)

	cmd := exec.Command("mkdir", "-p", backupDir)
	if err := cmd.Run(); err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": err.Error(),
		})
		return
	}

	// 复制工作区
	workspace := fmt.Sprintf("data/workspaces/%s", req.InstanceID)
	cmd = exec.Command("cp", "-r", workspace, backupDir)
	output, err := cmd.CombinedOutput()

	if err != nil {
		json.NewEncoder(w).Encode(map[string]interface{}{
			"success": false,
			"error":   err.Error(),
			"output":  string(output),
		})
		return
	}

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success":     true,
		"backup_name": backupName,
	})
}

// InstanceRestoreHandler 实例还原
func InstanceRestoreHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method != "POST" {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	var req struct {
		InstanceID string `json:"instance_id"`
		BackupName string `json:"backup_name"`
	}

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "无效的请求",
		})
		return
	}

	if req.InstanceID == "" || req.BackupName == "" {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "未指定实例 ID 或备份名称",
		})
		return
	}

	// 设置 PicoClaw 路径
	picoclawPath := os.Getenv("PICOCLAW_PATH")
	if picoclawPath == "" {
		picoclawPath = "/usr/local/bin/picoclaw"
	}
	
	// 还原工作区
	backupDir := fmt.Sprintf("data/backups/instances/%s", req.BackupName)
	workspace := fmt.Sprintf("data/workspaces/%s", req.InstanceID)

	// 先备份当前状态
	cmd := exec.Command("mv", workspace, workspace+".old")
	cmd.Run()

	// 还原
	cmd = exec.Command("cp", "-r", backupDir, workspace)
	output, err := cmd.CombinedOutput()

	if err != nil {
		// 还原失败，恢复旧版本
		exec.Command("mv", workspace+".old", workspace).Run()
		json.NewEncoder(w).Encode(map[string]interface{}{
			"success": false,
			"error":   err.Error(),
			"output":  string(output),
		})
		return
	}

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success": true,
	})
}

// ListInstanceBackupsHandler 列出实例备份
func ListInstanceBackupsHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	instanceID := r.URL.Query().Get("instance_id")
	if instanceID == "" {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "未指定实例 ID",
		})
		return
	}

	backups := []BackupInfo{}

	// 读取实例备份目录
	backupDir := fmt.Sprintf("data/backups/instances")
	if entries, err := os.ReadDir(backupDir); err == nil {
		for _, entry := range entries {
			if entry.IsDir() {
				name := entry.Name()
				if strings.HasPrefix(name, fmt.Sprintf("instance-%s-", instanceID)) {
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
					date := strings.TrimPrefix(name, fmt.Sprintf("instance-%s-", instanceID))

					backups = append(backups, BackupInfo{
						Name: name,
						Size: sizeStr,
						Date: date,
					})
				}
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

func getTimeStamp() string {
	cmd := exec.Command("date", "+%Y%m%d-%H%M%S")
	output, _ := cmd.Output()
	return strings.TrimSpace(string(output))
}
