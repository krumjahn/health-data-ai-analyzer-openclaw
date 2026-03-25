---
name: health-analyzer-mac-local
description: Use the Health Data AI Analyzer Mac app to get a daily brief from one exact localhost endpoint, then return a concise summary and 3 practical suggestions. If direct fetch is unavailable, ask for one exact `!curl` command and continue from the JSON.
homepage: https://clawhub.ai/
user-invocable: true
command-dispatch: tool
command-tool: health_analyzer_local
command-arg-mode: raw
metadata: {"openclaw":{"requires":{"bins":["bash"]}}}
---

# Health Data AI Analyzer
This skill dispatches directly to the local `health_analyzer_local` tool.

Use it for:
- daily health briefs
- 3 practical non-medical suggestions
- simple recent step and sleep comparisons

The tool reads from the local Health Data AI Analyzer API on this Mac.
