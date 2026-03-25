# Health Data AI Analyzer for OpenClaw

Local OpenClaw integration for the macOS app `Health Data AI Analyzer`.

Repo: `https://github.com/krumjahn/health-data-ai-analyzer-openclaw`

This repo contains:

- an OpenClaw skill at `skills/health-analyzer-mac-local/SKILL.md`
- a local OpenClaw plugin at `extensions/health-analyzer-local/openclaw.plugin.json`

## What It Does

After you install the Mac app and load a health analysis, OpenClaw can:

- read your daily brief from the local app API
- compare recent steps and sleep
- generate short, non-medical suggestions

## Requirements

- macOS app: `Health Data AI Analyzer`
- OpenClaw installed
- Local API enabled in the Mac app
- A saved analysis selected for OpenClaw / API

## Install Locally

1. Clone this repo.
2. Install the plugin from `extensions/health-analyzer-local`.
3. Install or publish the skill from `skills/health-analyzer-mac-local`.
4. Restart OpenClaw.

## Example Prompts

```text
/skill health-analyzer-mac-local Give me my daily health brief for today and 3 suggestions for that day.
```

```text
/skill health-analyzer-mac-local Give me my daily health brief for 2026-03-19 and 3 suggestions for that day.
```

```text
/skill health-analyzer-mac-local Compare my steps and sleep over the last 7 days.
```

## Heartbeat

An example heartbeat file is included at `HEARTBEAT.example.md`.

Do not put secrets in `HEARTBEAT.md`.
