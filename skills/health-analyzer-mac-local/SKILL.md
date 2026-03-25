---
name: apple-health-daily-brief
description: |
  Read Apple Health data from the Health Data AI Analyzer Mac app.
  Use when the user wants a daily health brief, a short daily OpenClaw message,
  or a recent steps and sleep comparison based on data saved on their Mac.
metadata: {"openclaw":{"homepage":"https://github.com/krumjahn/health-data-ai-analyzer-openclaw","requires":{"bins":["bash","curl","python3"]}}}
---

# Apple Health Daily Brief

Use this skill with the macOS app `Health Data AI Analyzer`.

This skill is for users who want OpenClaw to read their latest saved Apple Health analysis and turn it into:

- a daily health brief
- a short daily OpenClaw message
- a 7-day steps and sleep comparison
- concise practical non-medical suggestions

This skill reads from the Mac app's local API on the same Mac. It does not connect directly to Apple HealthKit from OpenClaw.

## Resources

- `README.md` - high-level setup and example prompts
- `references/local-api.md` - endpoint reference for the local Mac app API
- `references/troubleshooting.md` - quick diagnosis and common failure states
- `references/heartbeat.md` - how to use this skill for a short daily OpenClaw health message
- `scripts/health-analyzer-brief.sh` - helper shell wrapper for local testing
- `scripts/health-analyzer-local.py` - helper script to fetch status, daily briefs, and 7-day step/sleep comparisons from the local API
- `scripts/check_local_setup.py` - verifies the local API is reachable and whether a saved analysis is loaded
- `scripts/create_daily_message.py` - turns the latest local brief into a short daily OpenClaw message
- `scripts/compare_recent_trends.py` - prints a 7-day steps and sleep comparison
- `scripts/create_weekly_summary.py` - prints a compact weekly summary with recent movement, sleep, and workout patterns

## Before you use this skill

Confirm all of these:

- the user has the macOS app `Health Data AI Analyzer` installed
- the user has already imported or synced Apple Health data into the app
- the user has selected a saved analysis in `🦞 OpenClaw / API`
- the user has enabled `Local API for OpenClaw and scripts` in the app

If any of those are missing, help the user fix that first.

## App-side setup flow

When the user says the skill is not working yet, walk them through this exact app flow:

1. Open `Health Data AI Analyzer`
2. Open the `🦞 OpenClaw / API` tab
3. If no analysis is selected:
   - click `Use Last Analysis`, or
   - click `Choose Health Data`
4. If Local API is off:
   - turn on `Local API for OpenClaw and scripts`
5. Wait for the app to show the current integration source
6. Only then retry local API requests

Do not skip the selected-analysis step. The local API depends on a saved analysis chosen in the app.

## First-run workflow

When a user installs this skill for the first time, follow this order:

1. verify the local app API is reachable
2. verify a saved analysis is loaded
3. if setup is incomplete, explain the exact missing step
4. once setup is complete, generate the requested brief or comparison

Recommended first command:

```bash
python3 {baseDir}/scripts/check_local_setup.py
```

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

For local shell testing outside the skill, this helper script may also exist:

```bash
/bin/bash "$HOME/Library/Containers/com.rumjahn.healthkitanalyzer/Data/Library/Application Support/Health Data AI Analyzer/bin/health-analyzer-brief" status
```

Use the helper only for manual troubleshooting. Prefer the direct local HTTP endpoints in normal skill use.

For a script-based local check, this bundled helper is available:

```bash
python3 {baseDir}/scripts/health-analyzer-local.py status
python3 {baseDir}/scripts/health-analyzer-local.py daily-brief 2026-03-19
python3 {baseDir}/scripts/health-analyzer-local.py compare-last-7-days
```

These additional scripts are available:

```bash
python3 {baseDir}/scripts/check_local_setup.py
python3 {baseDir}/scripts/create_daily_message.py
python3 {baseDir}/scripts/create_daily_message.py 2026-03-19
python3 {baseDir}/scripts/compare_recent_trends.py
python3 {baseDir}/scripts/create_weekly_summary.py
```

## Primary workflow

### 1. Check status first when setup may be incomplete

Use:

```bash
curl "http://127.0.0.1:8765/openclaw/status"
```

If the response says the dataset is not loaded, tell the user to open the Mac app and select health data in `🦞 OpenClaw / API`.

If the endpoint fails entirely:

- tell the user to verify the Local API is enabled
- tell the user to keep the Mac app open
- retry once after they confirm setup
- if still unavailable, fall back to troubleshooting steps below

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

If the user asks for:

- "today"
- "this morning"
- "my latest brief"

use today’s date unless they specify a different date.

When you want a lightweight daily message instead of a full brief, prefer:

```bash
python3 {baseDir}/scripts/create_daily_message.py
```

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

When a metric is missing on some days, call that out explicitly instead of flattening it away.

### 4. For daily OpenClaw health messages

Use the daily brief endpoint and compress the result into a short check-in.

Good format:

```text
Today’s health check-in
- One-sentence summary
- 1 to 2 specific things to focus on today
```

This is a strong use case for users who want OpenClaw to give them a daily message about how to improve movement, sleep routine, or recovery habits.

For more detail, read `references/heartbeat.md`.

## Good requests

Use this skill for requests like:

- "Give me my daily health brief for today"
- "Give me my daily health brief for 2026-03-19 and 3 suggestions"
- "Compare my steps and sleep over the last 7 days"
- "Summarize what changed in my health data this week"
- "Give me a short daily OpenClaw health message"
- "How am I doing today based on my Apple Health data?"

## Requests this skill should not overclaim

Do not imply:

- live medical monitoring
- diagnosis
- clinician-grade interpretation
- direct HealthKit access inside OpenClaw

This skill depends on the Mac app’s saved analysis, not raw HealthKit access from the agent.

## Output style

- Do not provide medical advice, diagnosis, or treatment.
- Do not invent missing values.
- If data is missing, say `insufficient data`.
- Prefer plain language over technical jargon.
- Keep daily messages short enough to feel useful as a check-in.
- When comparing recent trends, favor clarity over exhaustive detail.

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

## Example raw daily brief request

```bash
curl "http://127.0.0.1:8765/openclaw/daily-brief?date=2026-03-19"
```

Example shape:

```json
{
  "ok": true,
  "success": true,
  "summary": "Daily Apple Health brief from Health Data AI Analyzer.",
  "data": {
    "date": "2026-03-19",
    "steps": {"value": 2444},
    "sleep": {"hours": null},
    "workouts": {"count": 0, "total_minutes": 0}
  }
}
```

Use the returned values as the source of truth.

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

## Heartbeat / automation use case

This skill works well for users who want a recurring daily OpenClaw message.

Suggested pattern:

- run a daily OpenClaw heartbeat or automation
- read the latest daily brief from the Mac app
- return one short health check-in

Suggested heartbeat command:

```bash
python3 {baseDir}/scripts/create_daily_message.py
```

For a richer weekly check-in, use:

```bash
python3 {baseDir}/scripts/create_weekly_summary.py
```

Example heartbeat-style output:

```text
Today’s health check-in
- Your movement is below your recent baseline.
- Focus on one easy walk and one fixed movement anchor today.
```

If there is no saved analysis or the API is unavailable, do not invent data. Prefer a lightweight failure path like telling the user setup is incomplete.

## Troubleshooting

If the API is not responding:

1. Ask the user to open the Mac app.
2. Ask them to go to `🦞 OpenClaw / API`.
3. Confirm `Local API for OpenClaw and scripts` is enabled.
4. Confirm a saved analysis is selected.
5. Retry:

```bash
curl "http://127.0.0.1:8765/openclaw/status"
python3 {baseDir}/scripts/health-analyzer-local.py status
python3 {baseDir}/scripts/check_local_setup.py
```

If that still fails, ask the user to restart the Mac app and try again.

If the status endpoint works but the daily brief endpoint fails:

1. Confirm a saved analysis is selected
2. Confirm the requested date exists in the saved analysis
3. Try today’s date or the latest known analysis date

If the user wants to debug outside OpenClaw, suggest:

```bash
curl "http://127.0.0.1:8765/openclaw/status"
curl "http://127.0.0.1:8765/openclaw/daily-brief?date=2026-03-19"
```

For more troubleshooting detail, read `references/troubleshooting.md`.

## Notes for agents

- Prefer the exact local API endpoints above.
- For daily brief requests, use the OpenClaw-specific endpoint first.
- For trend questions, use the daily steps and sleep endpoints.
- If the user wants a recurring daily message, suggest using OpenClaw heartbeat or automation after the basic setup works.
- If the runtime cannot reach the local API, explain the setup gap plainly instead of pretending data was read.
