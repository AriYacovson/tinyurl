import redis
import logging

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
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