import redis
import logging
import os

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
REDIS_DB = os.environ.get("REDIS_DB", 0)
REDIS_MAX_CONNECTIONS = os.environ.get("REDIS_MAX_CONNECTION", 8)

pool = redis.ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    max_connections=REDIS_MAX_CONNECTIONS,
    decode_responses=True,
)
redis = redis.Redis(connection_pool=pool)


def redis_set(key, value):
    try:
        redis.set(key, value)
    except Exception as e:
        logging.error(e)
        return False
    return True


def redis_get(key):
    try:
        value = redis.get(key)
    except Exception as e:
        logging.error(e)
        return None
    return value


def redis_set_if_not_exist(key, value):
    try:
        answer = redis.setnx(key, value)
    except Exception as e:
        logging.error(e)
        return False
    if answer == 0:
        return False
    return True
