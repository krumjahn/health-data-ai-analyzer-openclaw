#!/usr/bin/env python3

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date

BASE_URL = "http://127.0.0.1:8765"


def fetch_json(path: str):
    with urllib.request.urlopen(f"{BASE_URL}{path}", timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def today_string() -> str:
    return date.today().isoformat()


def fmt_number(value):
    if value is None:
        return "insufficient data"
    if isinstance(value, float):
        return f"{value:.1f}"
    return str(value)


def main():
    target_date = sys.argv[1] if len(sys.argv) > 1 else today_string()
    try:
        payload = fetch_json(f"/openclaw/daily-brief?date={urllib.parse.quote(target_date)}")
        brief = payload.get("data", {})
        steps = (brief.get("steps") or {}).get("value")
        baseline = (brief.get("steps") or {}).get("baseline_7d")
        sleep_hours = (brief.get("sleep") or {}).get("hours")
        signals = brief.get("signals") or []

        lines = [
            "Today’s health check-in",
            f"- {brief.get('context_summary') or f'Daily brief for {target_date}'}",
        ]

        if "activity_below_baseline" in signals and steps is not None and baseline is not None:
            lines.append(f"- Steps are below baseline today: {fmt_number(steps)} vs {fmt_number(baseline)}.")
            lines.append("- Focus on one easy walk and one fixed movement anchor.")
        elif sleep_hours is not None:
            lines.append(f"- Sleep recorded: {fmt_number(sleep_hours)} hours.")
            lines.append("- Use that as context for today’s activity and recovery choices.")
        else:
            lines.append("- Keep today’s plan simple and moderate because some recovery data is missing.")

        print("\n".join(lines))
        return 0
    except urllib.error.URLError as error:
        print(f"local api request failed: {error}", file=sys.stderr)
        return 2
    except Exception as error:
        print(f"unexpected error: {error}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
