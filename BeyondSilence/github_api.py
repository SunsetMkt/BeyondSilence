import logging
import time

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s",
)


def get_recent_activities_of(user_name):
    query_url = f"https://api.github.com/users/{user_name}/events/public"  # Return latest 90 days activities
    req = None
    while req is None or req.status_code == 403 or req.status_code == 429:
        req = requests.get(query_url)
        if req.status_code == 403 or req.status_code == 429:
            # Wait for rate limit to reset
            reset_time = int(req.headers.get("x-ratelimit-reset"))
            logging.info(f"Rate limit reset time: {reset_time}")
            wait_time = reset_time - time.time() + 1
            time.sleep(wait_time)
    logging.info(f"Request status code: {req.status_code}")
    req.raise_for_status()
    logging.info(f"Request successful")
    return req.json()


def get_latest_activity_days_to_now(activities):
    # if activities is empty []
    if activities == []:
        logging.info(f"Activities is empty, returning 91")
        return 91
    latest_formatted_date = activities[0]["created_at"]  # YYYY-MM-DDTHH:MM:SSZ
    latest_date = time.strptime(latest_formatted_date, "%Y-%m-%dT%H:%M:%SZ")
    latest_timestamp = time.mktime(latest_date)
    now_timestamp = time.time()
    days = int((now_timestamp - latest_timestamp) / 86400)
    logging.info(f"Latest activity is {days} day(s) ago")
    return days


def get_days_of_inactivity(user_name):
    activities = get_recent_activities_of(user_name)
    days = get_latest_activity_days_to_now(activities)
    return days
