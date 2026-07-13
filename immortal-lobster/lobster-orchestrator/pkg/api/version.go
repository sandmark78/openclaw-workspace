package api

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os/exec"
	"strings"
)

// VersionInfo 版本信息
type VersionInfo struct {
	Current   string `json:"current"`
	Latest    string `json:"latest"`
	NeedsUpdate bool   `json:"needs_update"`
	Changelog string `json:"changelog"`
}

// VersionHandler 版本检查
func VersionHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	info := getVersionInfo()
	json.NewEncoder(w).Encode(map[string]interface{}{
		"success": true,
		"version": info,
	})
}

// getVersionInfo 获取版本信息
func getVersionInfo() VersionInfo {
	info := VersionInfo{
		Current: "0.3.5",
		Latest:  "0.3.5",
		NeedsUpdate: false,
	}

	// 从 GitHub 获取最新版本
	cmd := exec.Command("curl", "-s", "https://api.github.com/repos/immortal-lobster/lobster-orchestrator/releases/latest")
	output, err := cmd.Output()
	if err == nil {
		var release struct {
			TagName string `json:"tag_name"`
			Body    string `json:"body"`
		}
		if err := json.Unmarshal(output, &release); err == nil {
			info.Latest = strings.TrimPrefix(release.TagName, "v")
			info.Changelog = release.Body
			
			// 比较版本
			if compareVersions(info.Current, info.Latest) < 0 {
				info.NeedsUpdate = true
			}
		}
	}

	return info
}

// UpdateHandler 执行升级
func UpdateHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method != "POST" {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	// 执行升级脚本
	cmd := exec.Command("./scripts/update.sh")
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

// compareVersions 比较版本号 (返回 -1/0/1)
func compareVersions(v1, v2 string) int {
	parts1 := strings.Split(v1, ".")
	parts2 := strings.Split(v2, ".")

	for i := 0; i < len(parts1) && i < len(parts2); i++ {
		var n1, n2 int
		fmt.Sscanf(parts1[i], "%d", &n1)
		fmt.Sscanf(parts2[i], "%d", &n2)

		if n1 < n2 {
			return -1
		} else if n1 > n2 {
			return 1
		}
	}

	if len(parts1) < len(parts2) {
		return -1
	} else if len(parts1) > len(parts2) {
		return 1
	}

	return 0
}
