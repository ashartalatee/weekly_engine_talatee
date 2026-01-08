import time
from typing import Callable, Tuple, Type
from logger_setup import get_logger
from error_classifier import is_retryable_error

logger = get_logger("retry_policy")


class RetryExceededError(Exception):
    pass


def retry_with_backoff(
    func: Callable,
    exceptions: Tuple[Type[Exception], ...],
    max_attempts: int = 3,
    base_delay: int = 2,
    backoff_multiplier: int = 2,
    *args,
    **kwargs
):
    attempt = 1
    delay = base_delay

    while attempt <= max_attempts:
        try:
            logger.info(f"Attempt {attempt} executing function {func.__name__}")
            return func(*args, **kwargs)

        except exceptions as e:
            logger.warning(
                f"Retryable error on attempt {attempt}: {str(e)}"
            )

            if attempt == max_attempts:
                logger.error("Max retry attempts reached")
                raise RetryExceededError(str(e))

            logger.info(f"Sleeping for {delay} seconds before retry")
            time.sleep(delay)
            delay *= backoff_multiplier
            attempt += 1

            
        except Exception as e:
            if not is_retryable_error(e):
                logger.error(f"Non-retryable error: {str(e)}")
                raise

            logger.warning(
                f"Retryable error on attempt {attempt}: {str(e)}"
            )