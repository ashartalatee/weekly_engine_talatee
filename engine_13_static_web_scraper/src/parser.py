from bs4 import BeautifulSoup
from typing import List, Dict


class ParseError(Exception):
    pass


def parse_html(
    html: str,
    selectors: Dict
) -> List[Dict]:
    """
    Parse HTML into structured data based on selectors.

    selectors example:
    {
        "container": "div.item",
        "fields": {
            "name": "h2",
            "price": "span.price"
        }
    }
    """
    soup = BeautifulSoup(html, "html.parser")

    container_selector = selectors.get("container")
    field_selectors = selectors.get("fields")

    if not container_selector or not field_selectors:
        raise ParseError("Invalid selectors configuration")

    containers = soup.select(container_selector)

    results = []

    for idx, container in enumerate(containers):
        item = {}
        for field, selector in field_selectors.items():
            element = container.select_one(selector)
            item[field] = element.get_text(strip=True) if element else None
        results.append(item)

    return results
