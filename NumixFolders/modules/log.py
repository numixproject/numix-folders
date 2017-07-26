import logging
import sys


class Logger:
    """Logger class."""
    instance = None

    FORMAT = "[%(levelname)-s] %(asctime)s %(message)s"
    DATE = "%Y-%m-%d %H:%M:%S"
    APP = "org.Numix.Folders"

    @staticmethod
    def get_default():
        """Return default instance of Logger."""
        if Logger.instance is None:
            logger = logging.getLogger(Logger.APP)

            handler = logging.StreamHandler(sys.stdout)
            formater = logging.Formatter(Logger.FORMAT, Logger.DATE)
            handler.setFormatter(formater)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)

            Logger.instance = logging.getLogger(Logger.APP)
        return Logger.instance

    @staticmethod
    def warning(msg):
        """Log warning message."""
        Logger.get_default().warning(msg)

    @staticmethod
    def debug(msg):
        """Log debug message."""
        Logger.get_default().debug(msg)

    @staticmethod
    def info(msg):
        """Log info message."""
        Logger.get_default().info(msg)

    @staticmethod
    def error(msg):
        """Log error message."""
        Logger.get_default().error(msg)
