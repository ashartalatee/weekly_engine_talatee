# src/runner.py

import yaml
from src.api_client import APIClient
from src.paginator import Paginator
from src.response_parser import ResponseParser


def run_engine(
    api_config_path: str,
    pagination_config_path: str,
    fields=None
):
    # Load configs
    with open(api_config_path) as f:
        api_config = yaml.safe_load(f)

    with open(pagination_config_path) as f:
        pagination_config = yaml.safe_load(f)

    # Setup client
    client = APIClient(
        base_url=api_config["base_url"],
        headers=api_config.get("headers"),
        timeout=api_config.get("timeout", 10)
    )

    # Pagination
    paginator = Paginator(
        client=client,
        endpoint=api_config["endpoint"],
        pagination_config=pagination_config,
        base_params=api_config.get("params")
    )

    raw_data = paginator.fetch_all()

    # Parsing
    parser = ResponseParser(fields=fields)
    parsed_data = parser.parse(raw_data)

    return parsed_data
