import random
import os
import logging
import string

from app.services.redis_service import redis_set, redis_get

BASE_URL = os.environ.get("BASE_URL", "/")
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", 4))
TINY_LETTERS = int(os.environ.get("TINY_LENGTH", 6))


def new_tiny(long_url: str) -> str:
    try:
        tiny_url = generate_tiny_url()
        i = 0
        while not redis_set(tiny_url, long_url) and i < MAX_RETRIES:
            tiny_code = generate_tiny_url()
            i += 1
        if i == MAX_RETRIES:
            raise Exception("SPACE IS FULL.")
        return BASE_URL + tiny_url + "/"
    except Exception as e:
        logging.error({"error": str(e)})


def generate_tiny_url() -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(TINY_LETTERS))


def get_tiny(tiny_url: str) -> str:
    return redis_get(tiny_url)
