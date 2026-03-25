---
name: apple-health-daily-brief
description: |
  Read Apple Health data from the Health Data AI Analyzer Mac app.
  Use when the user wants a daily health brief, a short daily OpenClaw message,
  or a recent steps and sleep comparison based on data saved on their Mac.
metadata: {"openclaw":{"homepage":"https://github.com/krumjahn/health-data-ai-analyzer-openclaw","requires":{"bins":["bash","curl"]}}}
---

# Apple Health Daily Brief

Use this skill with the macOS app `Health Data AI Analyzer`.

This skill is for users who want OpenClaw to read their latest saved Apple Health analysis and turn it into:

- a daily health brief
- a short daily OpenClaw message
- a 7-day steps and sleep comparison
- concise practical non-medical suggestions

This skill reads from the Mac app's local API on the same Mac. It does not connect directly to Apple HealthKit from OpenClaw.

## Before you use this skill

Confirm all of these:

- the user has the macOS app `Health Data AI Analyzer` installed
- the user has already imported or synced Apple Health data into the app
- the user has selected a saved analysis in `🦞 OpenClaw / API`
- the user has enabled `Local API for OpenClaw and scripts` in the app

If any of those are missing, help the user fix that first.

## Local API runtime

The Mac app serves its local API at:

```text
http://127.0.0.1:8765
```

The endpoints this skill should use are:

- `GET /openclaw/status`
- `GET /openclaw/daily-brief?date=YYYY-MM-DD`
- `GET /steps/daily?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `GET /sleep/summary?start=YYYY-MM-DD&end=YYYY-MM-DD`

## Primary workflow

### 1. Check status first when setup may be incomplete

Use:

```bash
curl "http://127.0.0.1:8765/openclaw/status"
```

If the response says the dataset is not loaded, tell the user to open the Mac app and select health data in `🦞 OpenClaw / API`.

### 2. For daily brief requests

Use:

```bash
curl "http://127.0.0.1:8765/openclaw/daily-brief?date=YYYY-MM-DD"
```

If the user does not specify a date, default to today.

Return:

- `Status`
- `What changed`
- `Suggestions`
- `Missing data`

Keep it concise and practical.

### 3. For 7-day steps and sleep comparisons

Use both:

```bash
curl "http://127.0.0.1:8765/steps/daily?start=YYYY-MM-DD&end=YYYY-MM-DD"
curl "http://127.0.0.1:8765/sleep/summary?start=YYYY-MM-DD&end=YYYY-MM-DD"
```

Return:

- recent daily values
- short comparison summary
- 2 or 3 practical suggestions only if the user asks for them

### 4. For daily OpenClaw health messages

Use the daily brief endpoint and compress the result into a short check-in.

Good format:

```text
Today’s health check-in
- One-sentence summary
- 1 to 2 specific things to focus on today
```

## Good requests

Use this skill for requests like:

- "Give me my daily health brief for today"
- "Give me my daily health brief for 2026-03-19 and 3 suggestions"
- "Compare my steps and sleep over the last 7 days"
- "Summarize what changed in my health data this week"
- "Give me a short daily OpenClaw health message"
- "How am I doing today based on my Apple Health data?"

## Output style

- Do not provide medical advice, diagnosis, or treatment.
- Do not invent missing values.
- If data is missing, say `insufficient data`.
- Prefer plain language over technical jargon.
- Keep daily messages short enough to feel useful as a check-in.

## Example daily brief

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

Missing data
- Sleep: insufficient data
```

## Example daily OpenClaw message

```text
Today’s health check-in
- Activity is below your recent baseline today.
- Focus on one easy walk and keep effort moderate.
```

## Example recent comparison

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

## Troubleshooting

If the API is not responding:

1. Ask the user to open the Mac app.
2. Ask them to go to `🦞 OpenClaw / API`.
3. Confirm `Local API for OpenClaw and scripts` is enabled.
4. Confirm a saved analysis is selected.
5. Retry:

```bash
curl "http://127.0.0.1:8765/openclaw/status"
```

If that still fails, ask the user to restart the Mac app and try again.

## Notes for agents

- Prefer the exact local API endpoints above.
- For daily brief requests, use the OpenClaw-specific endpoint first.
- For trend questions, use the daily steps and sleep endpoints.
- If the user wants a recurring daily message, suggest using OpenClaw heartbeat or automation after the basic setup works.
