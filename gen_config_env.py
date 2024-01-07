import base64
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

config_str = json.dumps(config)

config_str = base64.b64encode(config_str.encode("utf-8")).decode("utf-8")

print(f"BEYONDSILENCE_CONFIG={config_str}")
