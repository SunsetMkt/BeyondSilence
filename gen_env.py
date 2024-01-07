import base64
import json


def gen_env(envname, filename):
    with open(filename, "r", encoding="utf-8") as f:
        config = json.load(f)

    config_str = json.dumps(config)

    config_str = base64.b64encode(config_str.encode("utf-8")).decode("utf-8")

    print(f"{envname}={config_str}")
    print()


if __name__ == "__main__":
    gen_env("BEYONDSILENCE_CONFIG", "config.example.json")
    gen_env("BEYONDSILENCE_KEYS", "keys.example.json")
