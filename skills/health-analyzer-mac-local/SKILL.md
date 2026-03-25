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

## Purpose

Use this skill when the user wants OpenClaw to work with Apple Health data that has already been analyzed by the macOS app `Health Data AI Analyzer`.

This skill is not a generic health chatbot. It is specifically for:
- reading the latest saved local health analysis
- summarizing what changed in movement, sleep, and workouts
- generating short practical suggestions from that data
- turning the latest analysis into a short daily OpenClaw message

Use it for:
- daily health briefs
- 3 practical non-medical suggestions
- simple recent step and sleep comparisons
- short daily OpenClaw messages based on the latest saved analysis

## Setup Requirements

Before this skill is useful, all of these must be true:

- the macOS app `Health Data AI Analyzer` is installed
- the app has opened or synced a health export and completed analysis
- the user has selected the saved analysis they want to expose in `🦞 OpenClaw / API`
- the app’s Local API is enabled
- the local OpenClaw plugin tool `health_analyzer_local` is installed

Requirements:
- the macOS app `Health Data AI Analyzer` is installed
- Local API is enabled in the app
- a saved analysis is selected in `🦞 OpenClaw / API`

The tool reads from the local Health Data AI Analyzer API on this Mac.

The underlying local API serves data from the Mac app at `http://127.0.0.1:8765`, but this skill should use the registered OpenClaw tool instead of manually telling the user to build URLs.

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

When the user asks for a daily message or check-in, prefer a concise format that feels like a daily health note rather than a long report.

## Good Requests

Use this skill when the user asks for things like:
- "Give me my daily health brief for today"
- "Give me my daily health brief for 2026-03-19 and 3 suggestions"
- "Compare my steps and sleep over the last 7 days"
- "Summarize what changed in my health data this week"
- "Give me a short daily OpenClaw health message"

Also use it for prompts like:
- "How am I doing today based on my Apple Health data?"
- "What should I focus on today based on my recent health data?"
- "Give me a one-paragraph health check-in from my latest analysis"

## What Not To Do

- Do not invent missing values when the local analysis does not contain them.
- Do not provide diagnosis, treatment, or medical claims.
- Do not claim to use live Apple HealthKit directly from OpenClaw. This skill depends on the Mac app’s saved local analysis.
- Do not ask the user to paste JSON unless the tool/runtime is truly unavailable.

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

## Example Weekly Comparison

```text
Comparison for the last 7 days

Steps
- 2026-03-13: 10,240 steps
- 2026-03-14: 9,870 steps
- 2026-03-15: 11,120 steps

Sleep
- 2026-03-13: 6.8 h
- 2026-03-14: 7.1 h
- 2026-03-15: insufficient data

Summary
- Steps have been relatively stable, but sleep data is incomplete and one low-activity day stands out.
```

## Output Style

- Be concise by default.
- Use plain language.
- Prefer "insufficient data" over vague wording.
- Keep suggestions practical, specific, and easy to act on.
- If the user asks for a daily message, keep it short enough to feel like a useful morning check-in.

## Notes

- Keep the tone concise and practical.
- Do not provide medical advice or diagnosis.
- If data is missing, say so plainly instead of inventing values.
