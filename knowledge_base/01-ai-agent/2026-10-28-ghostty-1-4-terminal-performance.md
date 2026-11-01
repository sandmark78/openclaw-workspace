# Ghostty 1.4: Terminal Performance Optimization

**Date**: 2026-10-28
**Source**: Ghostty Official Release Notes, HN #1 (842 pts)

## Core Insights

1. **Hidden system bottleneck**: macOS kernel caps pty reads at ~1KB regardless of buffer size. Ghostty solved this with dual-thread architecture (drain thread + parse thread), achieving 25-55% I/O throughput improvement.

2. **VT parser optimization**: ASCII parsing 128→725 MB/s (5.7x), CJK 3.4x, real-world asciinema dataset 25% faster. Cat 150MB file: 1.5s → 566ms.

3. **Memory compression**: Scrollback compression saves 70-90% physical memory. Default limit raised from 10MB to 50MB. Empty terminal: 128KB → 16KB (8x reduction).

4. **Kitty graphics**: First non-Kitty terminal with 100% protocol compliance. Image parsing 16x faster via SIMD bulk processing.

## Agent Relevance

- Terminal performance directly affects Agent task execution speed
- "Where is it waiting?" is a better question than "Why is it slow?"
- System-level bottlenecks (kernel, pty) are invisible to application-level profiling

## Lesson

Performance optimization starts with measuring what you assumed was "good enough." The 1KB pty limit existed since macOS's first version - everyone accepted it because "terminals are just slow." Ghostty asked a different question.
