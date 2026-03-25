---
name: health-analyzer-mac-local
description: Use the Health Data AI Analyzer Mac app with OpenClaw to read your latest Apple Health daily brief, compare recent sleep and steps, and return concise non-medical suggestions from data stored on your Mac.
homepage: https://github.com/krumjahn/health-data-ai-analyzer-openclaw
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

Requirements:
- the macOS app `Health Data AI Analyzer` is installed
- Local API is enabled in the app
- a saved analysis is selected in `🦞 OpenClaw / API`

The tool reads from the local Health Data AI Analyzer API on this Mac.
