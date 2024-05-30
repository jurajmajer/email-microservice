import logging
import os

log = logging.getLogger()


def read_env_var(env_name, log_error=True, default_value=None):
    ret_val = os.getenv(env_name)
    if log_error and ret_val is None:
        log.error('Environment variable ' + env_name + ' is not set')
    if ret_val is None:
        ret_val = default_value
    return ret_val
