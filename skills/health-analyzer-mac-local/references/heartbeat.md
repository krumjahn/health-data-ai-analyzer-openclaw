# Heartbeat Use Case

This skill works well for users who want OpenClaw to send one short daily health message.

## Goal

Read the latest saved Apple Health analysis from the Mac app and return one short message like:

```text
Today’s health check-in
- Your activity is below your recent baseline.
- Focus on one easy walk and keep effort moderate today.
```

## Suggested local command

```bash
python3 {baseDir}/scripts/create_daily_message.py
```

## Good heartbeat behavior

- keep the message short
- use the latest available local brief
- avoid medical language
- if local data is unavailable, fail lightly instead of inventing a message

## Good follow-up behavior

If the user asks for more detail after the short message:
- use the full daily brief
- or use the weekly summary script
