#!/usr/bin/env python3

import json
import urllib.request
from datetime import date, timedelta

BASE_URL = "http://127.0.0.1:8765"


def fetch_json(path: str):
    with urllib.request.urlopen(f"{BASE_URL}{path}", timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def date_string(days_ago: int) -> str:
    return (date.today() - timedelta(days=days_ago)).isoformat()


def main():
    start = date_string(6)
    end = date_string(0)
    steps = fetch_json(f"/steps/daily?start={start}&end={end}")
    sleep = fetch_json(f"/sleep/summary?start={start}&end={end}")

    step_days = ((steps.get("data") or {}).get("days") or [])
    sleep_days = ((sleep.get("data") or {}).get("days") or [])

    print("Comparison for the last 7 days")
    print("")
    print("Steps")
    for day in step_days:
        print(f"- {day.get('date', 'Unknown')}: {day.get('value', 'insufficient data')} steps")
    print("")
    print("Sleep")
    for day in sleep_days:
        value = day.get("hours")
        formatted = "insufficient data" if value is None else f"{float(value):.1f} h"
        print(f"- {day.get('date', 'Unknown')}: {formatted}")


if __name__ == "__main__":
    raise SystemExit(main())
