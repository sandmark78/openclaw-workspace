package api

import (
	"encoding/json"
	"net/http"
	"os/exec"
)

// PicoClawStatus PicoClaw 状态
type PicoClawStatus struct {
	Installed   bool   `json:"installed"`
	Version     string `json:"version,omitempty"`
	Path        string `json:"path,omitempty"`
	CanInstall  bool   `json:"can_install"`
	InstallPath string `json:"install_path"`
}

// PicoClawInstallRequest 安装请求
type PicoClawInstallRequest struct {
	Version string `json:"version"`
}

// PicoClawStatusHandler 获取 PicoClaw 状态
func PicoClawStatusHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	status := getPicoClawStatus()
	json.NewEncoder(w).Encode(map[string]interface{}{
		"success": true,
		"status":  status,
	})
}

// getPicoClawStatus 获取 PicoClaw 状态
func getPicoClawStatus() PicoClawStatus {
	status := PicoClawStatus{
		Installed:   false,
		CanInstall:  true,
		InstallPath: "$HOME/bin/picoclaw",
	}

	// 检查是否已安装
	path, err := exec.LookPath("picoclaw")
	if err == nil {
		status.Installed = true
		status.Path = path

		// 获取版本
		cmd := exec.Command("picoclaw", "version")
		output, err := cmd.Output()
		if err == nil {
			status.Version = string(output)
		}
	}

	return status
}

// PicoClawInstallHandler 安装 PicoClaw
func PicoClawInstallHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method != "POST" {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	var req PicoClawInstallRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		json.NewEncoder(w).Encode(map[string]string{
			"error": "无效的请求",
		})
		return
	}

	// 执行安装脚本
	script := "./scripts/install-picoclaw.sh"
	args := []string{}
	if req.Version != "" {
		args = append(args, req.Version)
	}

	cmd := exec.Command(script, args...)
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
		"success": true,
		"output":  string(output),
	})
}

// PicoClawCheckHandler 检查 PicoClaw 是否需要安装
func PicoClawCheckHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	status := getPicoClawStatus()
	needsInstall := !status.Installed

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success":       true,
		"needs_install": needsInstall,
		"status":        status,
	})
}
