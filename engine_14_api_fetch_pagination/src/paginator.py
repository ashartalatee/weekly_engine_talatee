# src/paginator.py

from typing import Dict, Any, List
from src.api_client import APIClient


class Paginator:
    def __init__(
        self,
        client: APIClient,
        endpoint: str,
        pagination_config: Dict[str, Any],
        base_params: Dict[str, Any] = None
    ):
        self.client = client
        self.endpoint = endpoint
        self.config = pagination_config
        self.base_params = base_params or {}

    def fetch_all(self) -> List[Dict[str, Any]]:
        results = []
        page = self.config.get("start_page", 1)

        while True:
            params = dict(self.base_params)
            params[self.config["page_param"]] = page
            params[self.config["limit_param"]] = self.config["limit"]

            response = self.client.get(self.endpoint, params=params)
            data = response.json()

            if not data and self.config["stop_condition"]["when_response_empty"]:
                break

            results.extend(data)
            page += 1

        return results
