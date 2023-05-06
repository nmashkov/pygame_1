import os
import logging
import json

from settings import (BASE_DIR, BASE_LOGS_DIR, SESSION_DIR)


# create JSON formatter
class JSONFormatter(logging.Formatter):
    def format(self, record):
        message = record.msg
        if isinstance(message, dict):
            message = json.dumps(message)
        else:
            message = str(message)
        record.msg = message
        record.args = ()
        record.levelname = ""
        return super().format(record)


def check_dirs():
    dir = f'{BASE_DIR}/{BASE_LOGS_DIR}/{SESSION_DIR}'
    if not os.path.exists(dir):
        os.makedirs(dir)


def check_file(log_file):
    if not os.path.exists(log_file):
        with open(log_file, 'w'):
            pass


def setup_logger(name: str, log_file: str, level=logging.INFO):

    check_dirs()

    dir = f'{BASE_DIR}/{BASE_LOGS_DIR}/{SESSION_DIR}/{log_file}'

    check_file(dir)

    formatter = JSONFormatter()
    file_handler = logging.FileHandler(dir)
    # file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger
