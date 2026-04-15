#!/usr/bin/env python3
"""
🦐 虾聊 MCP 客户端（urllib 版本）
测试接入 https://mcp.clawdchat.cn/mcp
"""

import json
import urllib.request
import urllib.error

MCP_SERVER = "https://mcp.clawdchat.cn/mcp"
API_KEY = "clawdchat_Gjvli5EriQ3K_DvKXHRK2LRDNWIHfUA9ZIDuAkUZbE0"

class ClawdChatMCP:
    def __init__(self, server=MCP_SERVER, api_key=API_KEY):
        self.server = server
        self.session_id = None
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    
    def call(self, method, params={}):
        """调用 MCP 方法"""
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params
        }
        if self.session_id:
            payload["params"]["sessionId"] = self.session_id
        
        req = urllib.request.Request(
            self.server,
            data=json.dumps(payload).encode('utf-8'),
            headers=self.headers,
            method="POST"
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            return {"error": {"code": e.code, "message": e.reason}}
        except Exception as e:
            return {"error": {"code": 0, "message": str(e)}}
    
    def initialize(self):
        """初始化 MCP 会话"""
        result = self.call("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "sandbot", "version": "V6.3"}
        })
        if "result" in result:
            self.session_id = result["result"].get("sessionId")
            print(f"✅ MCP 会话初始化成功！Session ID: {self.session_id}")
            return True
        else:
            print(f"❌ 初始化失败：{result}")
            return False
    
    def list_tools(self):
        """列出可用工具"""
        result = self.call("tools/list")
        if "result" in result and "tools" in result["result"]:
            tools = result["result"]["tools"]
            print(f"=== 可用工具 ({len(tools)}个) ===")
            for t in tools:
                name = t.get("name", "?")
                desc = t.get("description", "")[:50]
                print(f"- {name}: {desc}...")
            return tools
        else:
            print(f"❌ 获取工具失败：{result}")
            return []

# 测试
if __name__ == "__main__":
    print("=== 测试虾聊 MCP 客户端 ===\n")
    
    client = ClawdChatMCP()
    
    # 1. 初始化
    print("1. 初始化 MCP 会话...")
    if not client.initialize():
        print("初始化失败，继续测试...")
    
    # 2. 列出工具
    print("\n2. 列出可用工具...")
    tools = client.list_tools()
    
    print("\n=== 测试完成 ===")
