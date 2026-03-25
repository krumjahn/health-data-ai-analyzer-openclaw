# Troubleshooting

Use this when the skill cannot reach the local app data or when the user says the skill is not working.

## Quick diagnosis order

1. Confirm the Mac app `Health Data AI Analyzer` is open.
2. Confirm the user opened `🦞 OpenClaw / API` in the app.
3. Confirm `Local API for OpenClaw and scripts` is enabled.
4. Confirm a saved analysis is selected.
5. Run:

```bash
python3 {baseDir}/scripts/check_local_setup.py
```

6. If needed, run:

```bash
curl "http://127.0.0.1:8765/openclaw/status"
curl "http://127.0.0.1:8765/openclaw/daily-brief?date=2026-03-19"
```

## Common failure cases

### Local API unreachable

Likely causes:
- Mac app is not open
- Local API is disabled
- app is still starting the API

Suggested fix:
- open the app
- turn on local API
- wait a moment
- retry

### Status works, daily brief fails

Likely causes:
- no saved analysis selected
- requested date is not present in the selected analysis

Suggested fix:
- select a saved analysis in `🦞 OpenClaw / API`
- retry with today’s date or a known imported date

### Data looks incomplete

Likely causes:
- missing metrics in the selected export
- incomplete sleep or recovery data for that day

Suggested fix:
- say `insufficient data`
- do not invent missing values
- if needed, compare multiple recent days instead of a single date
