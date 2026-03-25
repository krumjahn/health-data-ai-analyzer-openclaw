# Apple Health Daily Brief

Use OpenClaw with the macOS app `Health Data AI Analyzer` to read a saved Apple Health analysis and turn it into:

- a daily health brief
- a short daily health message
- a recent steps and sleep comparison
- concise practical non-medical suggestions

## Works best for

- users who already use the `Health Data AI Analyzer` Mac app
- users who want OpenClaw to summarize their local Apple Health data
- users who want a daily OpenClaw health check-in based on recent trends

## Setup

1. Install the Mac app `Health Data AI Analyzer`
2. Import or sync Apple Health data in the app
3. Open `🦞 OpenClaw / API`
4. Select the saved analysis to use
5. Turn on `Local API for OpenClaw and scripts`
6. Restart OpenClaw if needed

## Example prompts

- `Give me my daily health brief for today`
- `Give me my daily health brief for 2026-03-19 and 3 suggestions`
- `Compare my steps and sleep over the last 7 days`
- `Give me a short daily health check-in from my latest Apple Health analysis`

## Example output

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

## Local API

The skill uses the local app API on the same Mac:

- `http://127.0.0.1:8765/openclaw/status`
- `http://127.0.0.1:8765/openclaw/daily-brief?date=YYYY-MM-DD`
- `http://127.0.0.1:8765/steps/daily?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `http://127.0.0.1:8765/sleep/summary?start=YYYY-MM-DD&end=YYYY-MM-DD`

See `references/local-api.md` for more details.
