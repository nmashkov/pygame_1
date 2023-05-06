import logging
import json


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


def setup_logger(name: str, log_file: str, level=logging.INFO):
    formatter = JSONFormatter()
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger
