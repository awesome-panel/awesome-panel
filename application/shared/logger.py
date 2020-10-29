"""Contains a method to get a logger"""
import logging

LEVEL = logging.INFO
LEVEL_NAME = "INFO"
# pylint: disable=implicit-str-concat
LOG_FORMAT = (
    "%(asctime)s :: %(levelname)s ::  %(filename)s :: %(funcName)s :: " "%(lineno)s :: %(message)s"
)

# file_handler = logging.FileHandler(filename='test.log', mode='w')
# file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
# CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
# CONSOLE_HANDLER.setFormatter(logging.Formatter(LOG_FORMAT))


def get_logger(name):
    """Returns a logger"""
    logger = logging.getLogger(name)
    # logger.addHandler(CONSOLE_HANDLER)
    logger.setLevel(logging.DEBUG)
    return logger


def _log_started():
    """Starts the logger"""
    _logger = get_logger(__name__)
    _logger.info("Session Started")
    _logger.info("Log Level %s", LEVEL_NAME)


_log_started()
