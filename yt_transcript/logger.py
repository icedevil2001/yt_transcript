from loguru import logger
import sys

def setup_logger(log_level="INFO"):
    """
    Set up the logger with a specific format and level.
    """
    logger.remove()  # Remove the default logger
    logger.add(
        sys.stderr,
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        level=log_level,
        colorize=True,
    )
    logger.info("Logger is set up.")

    

