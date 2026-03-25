#!/usr/bin/env python3

import json
import sys
import urllib.error
import urllib.request

BASE_URL = "http://127.0.0.1:8765"


def fetch_json(path: str):
    with urllib.request.urlopen(f"{BASE_URL}{path}", timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    try:
        payload = fetch_json("/openclaw/status")
        data = payload.get("data", {})
        dataset_loaded = bool(data.get("dataset_loaded"))

        result = {
            "ok": True,
            "base_url": BASE_URL,
            "dataset_loaded": dataset_loaded,
            "app": data.get("app"),
            "app_version": data.get("app_version"),
            "last_imported_at": data.get("last_imported_at"),
            "last_synced_at": data.get("last_synced_at"),
            "available_metrics": data.get("available_metrics", []),
        }
        print(json.dumps(result, indent=2))
        return 0 if dataset_loaded else 10
    except urllib.error.URLError as error:
        print(json.dumps({
            "ok": False,
            "error": "local_api_unreachable",
            "message": str(error),
            "base_url": BASE_URL,
        }, indent=2))
        return 2
    except Exception as error:
        print(json.dumps({
            "ok": False,
            "error": "unexpected_error",
            "message": str(error),
        }, indent=2))
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
