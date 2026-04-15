#!/usr/bin/env node
/**
 * session-boot-memory hook
 * 每次会话启动时自动读取记忆文件并注入上下文
 * 
 * 读取：
 * - MEMORY.md (长期记忆)
 * - memory/YYYY-MM-DD.md (今日记忆)
 * - memory/YYYY-MM-DD-1.md (昨日记忆)
 */

const fs = require('fs');
const path = require('path');

function getWorkspaceDir() {
  return process.env.OPENCLAW_WORKSPACE_DIR || '/home/node/.openclaw/workspace';
}

function readMemoryFiles() {
  const workspace = getWorkspaceDir();
  const today = new Date().toISOString().slice(0, 10);
  const yesterday = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
  
  const memories = [];
  
  // 1. MEMORY.md (长期记忆)
  const memoryMd = path.join(workspace, 'MEMORY.md');
  if (fs.existsSync(memoryMd)) {
    const content = fs.readFileSync(memoryMd, 'utf8').slice(0, 3000);
    memories.push(`## 长期记忆 (MEMORY.md)\n${content}`);
  }
  
  // 2. 今日记忆
  const todayFile = path.join(workspace, 'memory', `${today}.md`);
  if (fs.existsSync(todayFile)) {
    const content = fs.readFileSync(todayFile, 'utf8').slice(0, 2000);
    memories.push(`## 今日记忆 (${today}.md)\n${content}`);
  }
  
  // 3. 昨日记忆
  const yesterdayFile = path.join(workspace, 'memory', `${yesterday}.md`);
  if (fs.existsSync(yesterdayFile)) {
    const content = fs.readFileSync(yesterdayFile, 'utf8').slice(0, 2000);
    memories.push(`## 昨日记忆 (${yesterday}.md)\n${content}`);
  }
  
  return memories.join('\n\n---\n\n');
}

// Hook 入口
module.exports = {
  name: 'session-boot-memory',
  events: ['session:start'],
  handler: async (event, context) => {
    console.log('[session-boot-memory] 会话启动，读取记忆文件...');
    
    const memoryContent = readMemoryFiles();
    
    if (memoryContent) {
      // 注入到系统提示词
      context.appendSystemPrompt(`
<workspace-memory>
以下是从工作区记忆文件中读取的内容，请在回复时参考这些记忆：

${memoryContent}

</workspace-memory>
`);
      console.log('[session-boot-memory] 记忆文件已注入上下文');
    } else {
      console.log('[session-boot-memory] 未找到记忆文件');
    }
  }
};
