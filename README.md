# BeyondSilence（超越寂静）

BeyondSilence recognizes prolonged user inactivity on GitHub (Max 89 days), offering a gentle acknowledgment by showing pre-set messages.

## Quick Start

```json
{
  "github_user_name": "your_github_user_name",
  "days_before": 30,
  "main_description": "This is main description",
  "messages": [
    {
      "environ": "MESSAGE1",
      "description": "This is message 1"
    },
    {
      "environ": "MESSAGE2",
      "description": "This is message 2"
    }
  ]
}
```

Run `gen_config_env.py` to get env variable `BEYONDSILENCE_CONFIG` with the config.

Set the env variable `BEYONDSILENCE_CONFIG` in GitHub Actions Secrets.
