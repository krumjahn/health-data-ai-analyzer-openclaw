#!/usr/bin/env python3

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, timedelta

BASE_URL = "http://127.0.0.1:8765"


def fetch_json(path: str):
    url = f"{BASE_URL}{path}"
    with urllib.request.urlopen(url, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def today_string() -> str:
    return date.today().isoformat()


def days_ago_string(days: int) -> str:
    return (date.today() - timedelta(days=days)).isoformat()


def command_status():
    payload = fetch_json("/openclaw/status")
    print(json.dumps(payload, indent=2))


def command_daily_brief(target_date: str):
    quoted_date = urllib.parse.quote(target_date)
    payload = fetch_json(f"/openclaw/daily-brief?date={quoted_date}")
    print(json.dumps(payload, indent=2))


def command_compare_last_7_days():
    start = days_ago_string(6)
    end = today_string()
    steps = fetch_json(f"/steps/daily?start={start}&end={end}")
    sleep = fetch_json(f"/sleep/summary?start={start}&end={end}")
    print(json.dumps({"steps": steps, "sleep": sleep}, indent=2))


def main():
    if len(sys.argv) < 2:
        print("usage: health-analyzer-local.py status|daily-brief [YYYY-MM-DD]|compare-last-7-days", file=sys.stderr)
        return 1

    command = sys.argv[1]

    try:
        if command == "status":
            command_status()
            return 0
        if command == "daily-brief":
            target_date = sys.argv[2] if len(sys.argv) > 2 else today_string()
            command_daily_brief(target_date)
            return 0
        if command == "compare-last-7-days":
            command_compare_last_7_days()
            return 0
        print(f"unknown command: {command}", file=sys.stderr)
        return 1
    except urllib.error.URLError as error:
        print(f"local api request failed: {error}", file=sys.stderr)
        return 2
    except Exception as error:
        print(f"unexpected error: {error}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
