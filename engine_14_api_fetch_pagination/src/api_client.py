# src/api_client.py

import requests
from typing import Dict, Any, Optional
from src.logger import setup_logger
from src.retry_handler import RetryHandler


class APIClient:
    def __init__(
        self,
        base_url: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 10,
        retry_handler: Optional[RetryHandler] = None
    ):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.timeout = timeout
        self.retry_handler = retry_handler or RetryHandler()
        self.logger = setup_logger()

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        url = f"{self.base_url}{endpoint}"

        def _request():
            self.logger.info(f"GET {url} | params={params}")
            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response

        return self.retry_handler.run(_request)