package api

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"lobster-orchestrator/pkg/instance"
)

// Server API 服务器
type Server struct {
	manager *instance.Manager
	port    int
}

// StartServer 启动 API 服务器
func StartServer(port int, manager *instance.Manager) {
	s := &Server{
		manager: manager,
		port:    port,
	}

	http.HandleFunc("/", s.RootHandler)
	http.HandleFunc("/api/v1/instances", s.InstancesHandler)
	http.HandleFunc("/api/v1/instances/", s.InstanceHandler)
	http.HandleFunc("/api/v1/health", s.HealthHandler)
	http.HandleFunc("/api/v1/picoclaw/status", PicoClawStatusHandler)
	http.HandleFunc("/api/v1/picoclaw/install", PicoClawInstallHandler)
	http.HandleFunc("/api/v1/picoclaw/check", PicoClawCheckHandler)

	// 静态文件 (Dashboard)
	fs := http.FileServer(http.Dir("web"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	log.Printf("🌐 API 服务器监听端口 %d", port)
	if err := http.ListenAndServe(fmt.Sprintf(":%d", port), nil); err != nil {
		log.Fatalf("API 服务器失败：%v", err)
	}
}

// RootHandler 根路径
func (s *Server) RootHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path == "/" || r.URL.Path == "/index.html" {
		http.ServeFile(w, r, "web/dashboard.html")
		return
	}
	http.NotFound(w, r)
}

// InstancesHandler 获取所有实例
func (s *Server) InstancesHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	switch r.Method {
	case "GET":
		statuses := s.manager.GetAllStatus()
		json.NewEncoder(w).Encode(map[string]interface{}{
			"success":   true,
			"instances": statuses,
			"count":     len(statuses),
		})

	case "POST":
		// TODO: 创建新实例
		w.WriteHeader(http.StatusNotImplemented)
		json.NewEncoder(w).Encode(map[string]string{
			"error": "Not implemented",
		})

	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
	}
}

// InstanceHandler 单个实例操作
func (s *Server) InstanceHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	// 从路径提取实例 ID
	// /api/v1/instances/{id}
	path := r.URL.Path
	id := path[len("/api/v1/instances/"):]

	switch r.Method {
	case "GET":
		status, err := s.manager.GetStatus(id)
		if err != nil {
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(map[string]string{
				"error": err.Error(),
			})
			return
		}
		json.NewEncoder(w).Encode(map[string]interface{}{
			"success":  true,
			"instance": status,
		})

	case "POST":
		// 启动实例
		if err := s.manager.Start(id); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{
				"error": err.Error(),
			})
			return
		}
		json.NewEncoder(w).Encode(map[string]string{
			"success": "Instance started",
		})

	case "DELETE":
		// 停止实例
		if err := s.manager.Stop(id); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{
				"error": err.Error(),
			})
			return
		}
		json.NewEncoder(w).Encode(map[string]string{
			"success": "Instance stopped",
		})

	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
	}
}

// HealthHandler 健康检查
func (s *Server) HealthHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]interface{}{
		"status": "healthy",
		"service": "lobster-orchestrator",
	})
}
