# BeyondSilence（超越寂静）

BeyondSilence recognizes prolonged user inactivity on GitHub (Max 89 days), offering a gentle acknowledgment by showing pre-set messages.

## Quick Start

### BEYONDSILENCE_CONFIG

```json
{
  "github_user_name": "MurataHimeko",
  "days_before": 15,
  "main_description": "这就是，最后一课了.....",
  "messages": [
    {
      "environ": "MESSAGE1",
      "description": "姬子温柔地注视着你，不再言语。",
      "content": ""
    },
    {
      "environ": "MESSAGE2",
      "description": "琪亚娜，我已经没有什么能教你的了。",
      "content": ""
    }
  ]
}
```

### BEYONDSILENCE_KEYS

```json
{
  "MESSAGE1": "姬子温柔地注视着你",
  "MESSAGE2": "我已经没有什么能教你的了"
}
```

Run `gen_env.py` to get env variable `BEYONDSILENCE_CONFIG` and `BEYONDSILENCE_KEYS`.

Set `BEYONDSILENCE_CONFIG` and `BEYONDSILENCE_KEYS` in GitHub Actions Repository secrets.

Enable GitHub Actions.
