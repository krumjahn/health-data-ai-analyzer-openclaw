---
name: health-analyzer-mac-local
description: Use the Health Data AI Analyzer Mac app with OpenClaw to read your Apple Health data, summarize what changed, and give short practical suggestions. Example: "Steps were 2,444 vs a 7-day baseline of 10,005. Add one easy walk today and keep effort moderate."
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
- short daily OpenClaw messages based on the latest saved analysis

Requirements:
- the macOS app `Health Data AI Analyzer` is installed
- Local API is enabled in the app
- a saved analysis is selected in `🦞 OpenClaw / API`

The tool reads from the local Health Data AI Analyzer API on this Mac.

## What It Returns

For daily brief requests, return:
- a short status summary
- what changed versus recent baseline when available
- 3 practical non-medical suggestions
- explicit missing-data notes when a metric is unavailable

For recent trend requests, return:
- a compact comparison of recent steps and sleep
- a short summary of the main pattern
- practical next-step suggestions when the user asks for them

## Good Requests

Use this skill when the user asks for things like:
- "Give me my daily health brief for today"
- "Give me my daily health brief for 2026-03-19 and 3 suggestions"
- "Compare my steps and sleep over the last 7 days"
- "Summarize what changed in my health data this week"
- "Give me a short daily OpenClaw health message"

## Example Output

```text
Status
- Today was a low-activity day relative to your recent baseline.

What changed
- Steps: 2,444 vs 7-day baseline 10,005
- Workouts: 0 minutes, 0 workouts
- Sleep: insufficient data

Suggestions
1. Add one easy walk today instead of trying to catch up with a hard workout.
2. Use one fixed movement anchor, like a walk after lunch.
3. Keep effort moderate when recovery data is missing.
```

## Notes

- Keep the tone concise and practical.
- Do not provide medical advice or diagnosis.
- If data is missing, say so plainly instead of inventing values.
