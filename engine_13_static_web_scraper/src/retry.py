import time
from typing import Callable
from logger import setup_logger

logger = setup_logger()


def retry(
    func: Callable,
    retries: int = 3,
    delay: int = 2,
    backoff: int = 2,
    exceptions: tuple = (Exception,)
):
    attempt = 1
    current_delay = delay

    while attempt <= retries:
        try:
            return func()
        except exceptions as e:
            logger.warning(
                f"Attempt {attempt} failed: {e}"
            )
            if attempt == retries:
                logger.error("Max retry reached. Giving up.")
                raise
            time.sleep(current_delay)
            current_delay *= backoff
            attempt += 1
