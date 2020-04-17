import logging.config
from utils import config_util


def configure(log_file: str, logger_name: str) -> logging.Logger:
    logging.config.dictConfig(config_util.load_config(log_file))
    logging.getLogger('urllib3.connectionpool').setLevel(logging.WARNING)
    return logging.getLogger(logger_name)
