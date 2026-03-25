# Local API Reference

This skill depends on the local API exposed by the macOS app `Health Data AI Analyzer`.

## Base URL

```text
http://127.0.0.1:8765
```

## Endpoints used by this skill

### `GET /openclaw/status`

Use this to confirm:

- the app is running
- the local API is enabled
- a saved analysis is selected

### `GET /openclaw/daily-brief?date=YYYY-MM-DD`

Use this for daily brief requests.

Typical fields returned:

- `date`
- `context_summary`
- `steps`
- `sleep`
- `workouts`
- `heart_rate`
- `hrv`
- `signals`

### `GET /steps/daily?start=YYYY-MM-DD&end=YYYY-MM-DD`

Use this when the user wants a recent steps comparison.

### `GET /sleep/summary?start=YYYY-MM-DD&end=YYYY-MM-DD`

Use this when the user wants a recent sleep comparison.

## Troubleshooting

If these endpoints do not respond:

1. Open the Mac app.
2. Go to `🦞 OpenClaw / API`.
3. Confirm that `Local API for OpenClaw and scripts` is enabled.
4. Confirm a saved analysis is selected.
5. Retry the request.
