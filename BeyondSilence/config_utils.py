import base64
import hashlib
import json
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s",
)

from . import env_utils as Env

DEFAULT_CONFIG_ENV_NAME = "BEYONDSILENCE_CONFIG"
logging.info(f"DEFAULT_CONFIG_ENV_NAME: {DEFAULT_CONFIG_ENV_NAME}")

raw_config = None


def sha256_of(string):
    return hashlib.sha256(string.encode("utf-8")).hexdigest()


def load_config(raw_config):
    hash_of_raw_config = sha256_of(raw_config)
    logging.info(f"SHA256 of raw config: {hash_of_raw_config}")
    try:
        config = json.loads(raw_config)
        logging.info(f"Load config from json")
    except json.JSONDecodeError:
        try:
            decoded_config = base64.b64decode(raw_config).decode("utf-8")
            config = json.loads(decoded_config)
            logging.info(f"Load config from Base64")
        except (base64.binascii.Error, json.JSONDecodeError):
            # Handle error when unable to load config
            config = None
            logging.error("Unable to load config")
            raise Exception("Unable to load config")

    # Validate

    # github_user_name
    # Must be a string
    if not isinstance(config["github_user_name"], str):
        logging.error("github_user_name must be a string")
        raise Exception("github_user_name must be a string")

    # days_before
    # Must be a number between 1 and 90
    if not isinstance(config["days_before"], int):
        logging.error("days_before must be an integer")
        raise Exception("days_before must be an integer")
    if config["days_before"] > 90 or config["days_before"] < 1:
        logging.warning("days_before must be between 1 and 90, set to 89")
        config["days_before"] = 89

    # main_description
    # Must be a string
    if not isinstance(config["main_description"], str):
        logging.error("main_description must be a string")
        raise Exception("main_description must be a string")

    # messages
    # Must be a list
    if not isinstance(config["messages"], list):
        logging.error("messages must be a list")
        raise Exception("messages must be a list")
    # Every item of messages must be a dict, has environ and description and both strings
    # Validate messages
    for message in config["messages"]:
        if not isinstance(message, dict):
            logging.error("Each item of messages must be a dictionary")
            raise Exception("Each item of messages must be a dictionary")
        if "environ" not in message or "description" not in message:
            logging.error("Each message must have 'environ' and 'description' keys")
            raise Exception("Each message must have 'environ' and 'description' keys")
        if not isinstance(message["environ"], str) or not isinstance(
            message["description"], str
        ):
            logging.error("The values of 'environ' and 'description' must be strings")
            raise Exception("The values of 'environ' and 'description' must be strings")
        # There must be an ENV for the environ name
        if not Env.get_env_var(message["environ"]):
            logging.error(
                f"There is no environment variable set for {sha256_of(message['environ'])}"
            )
            raise Exception(
                f"There is no environment variable set for {sha256_of(message['environ'])}"
            )

    return config


if Env.get_env_var(DEFAULT_CONFIG_ENV_NAME):
    raw_config = Env.get_env_var(DEFAULT_CONFIG_ENV_NAME)
    logging.info(f"Using environment variable {DEFAULT_CONFIG_ENV_NAME}")
elif os.path.exists("config.json"):
    # read from config.json
    with open("config.json", "r", encoding="utf-8") as f:
        raw_config = f.read()
    logging.info("Using config.json")
elif os.path.exists("config.example.json"):
    # read from config.example.json
    with open("config.example.json", "r", encoding="utf-8") as f:
        raw_config = f.read()
    logging.info("Using config.example.json")
else:
    logging.error("No config file found")
    raise Exception("No config file found")

config = load_config(raw_config)
