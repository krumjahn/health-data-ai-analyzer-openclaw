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


def average(values):
    numeric = [float(value) for value in values if value is not None]
    if not numeric:
        return None
    return sum(numeric) / len(numeric)


def fmt_hours(value):
    if value is None:
        return "insufficient data"
    return f"{float(value):.1f} h"


def fmt_number(value):
    if value is None:
        return "insufficient data"
    return str(int(round(float(value))))


def main():
    start = date_string(6)
    end = date_string(0)

    steps_payload = fetch_json(f"/steps/daily?start={start}&end={end}")
    sleep_payload = fetch_json(f"/sleep/summary?start={start}&end={end}")
    workouts_payload = fetch_json(f"/workouts/summary?start={start}&end={end}")

    step_days = ((steps_payload.get("data") or {}).get("days") or [])
    sleep_days = ((sleep_payload.get("data") or {}).get("days") or [])
    workout_summary = workouts_payload.get("data") or {}

    step_values = [day.get("value") for day in step_days]
    sleep_values = [day.get("hours") for day in sleep_days]

    avg_steps = average(step_values)
    avg_sleep = average(sleep_values)
    workout_count = workout_summary.get("count")
    workout_minutes = workout_summary.get("total_minutes")

    print("Weekly health summary")
    print("")
    print(f"Period: {start} to {end}")
    print("")
    print("Main patterns")
    print(f"- Average steps: {fmt_number(avg_steps)}")
    print(f"- Average sleep: {fmt_hours(avg_sleep)}")
    print(f"- Workouts: {workout_count if workout_count is not None else 'insufficient data'}")
    print(f"- Workout minutes: {workout_minutes if workout_minutes is not None else 'insufficient data'}")
    print("")
    print("Daily detail")
    for step_day in step_days:
        matching_sleep = next((item for item in sleep_days if item.get("date") == step_day.get("date")), {})
        print(
            f"- {step_day.get('date', 'Unknown')}: "
            f"{step_day.get('value', 'insufficient data')} steps, "
            f"{fmt_hours(matching_sleep.get('hours'))} sleep"
        )
    print("")
    print("Suggested next focus")
    if avg_steps is not None and avg_steps < 6000:
        print("- Add one reliable walking block each day next week.")
    else:
        print("- Keep movement consistent instead of chasing one very high-activity day.")
    if avg_sleep is None:
        print("- Fix missing sleep capture before drawing strong conclusions from recovery trends.")
    elif avg_sleep < 7:
        print("- Look for one concrete way to increase sleep opportunity this week.")
    else:
        print("- Keep sleep timing stable so recovery stays easier to interpret.")


if __name__ == "__main__":
    raise SystemExit(main())
