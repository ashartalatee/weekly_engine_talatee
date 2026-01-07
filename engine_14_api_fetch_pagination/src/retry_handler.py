# src/retry_handler.py

import time
from typing import Callable
from requests.exceptions import RequestException


class RetryHandler:
    def __init__(self, max_retries: int = 3, backoff_seconds: int = 2):
        self.max_retries = max_retries
        self.backoff_seconds = backoff_seconds

    def run(self, func: Callable, *args, **kwargs):
        last_exception = None

        for attempt in range(1, self.max_retries + 1):
            try:
                return func(*args, **kwargs)
            except RequestException as e:
                last_exception = e
                time.sleep(self.backoff_seconds)

        raise last_exception
