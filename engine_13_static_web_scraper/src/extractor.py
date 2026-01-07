from fetcher import fetch_html
from parser import parse_html


def extract_data_from_config(config: dict):
    request_cfg = config.get("request")
    selector_cfg = config.get("selectors")

    if not request_cfg or not selector_cfg:
        raise ValueError("Invalid config structure")

    html = fetch_html(
        url=request_cfg["url"],
        timeout=request_cfg.get("timeout", 10),
        headers=request_cfg.get("headers")
    )

    data = parse_html(html, selector_cfg)
    return data
