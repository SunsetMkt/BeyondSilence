import logging
import time

from . import env_utils as Env

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s",
)


def gen_regular_output():
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return f"Last update time: {now_time}, everything is OK"


def gen_triggered_output(config):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    output = f'GitHub user name: {config["github_user_name"]}' + "\n"
    output += (
        f'Last update time: {now_time}, triggered by inactivity of {config["days_before"]} days'
        + "\n"
    )
    output += f'Main description:\n{config["main_description"]}' + "\n"
    output += f"Messages:\n"
    for message in config["messages"]:
        output += f"{message['environ']}: {message['description']}\n"
        real_value = message["content"]
        if real_value:
            output += f"Value: {real_value}\n"
        else:
            output += "Value: [environ unset]\n"
        output += "\n"
    output += "End of output\n"
    return output
