import requests
from typing import Optional
from retry import retry
from logger import setup_logger


logger = setup_logger()


class FetchError(Exception):
    pass


def fetch_html(
    url: str,
    timeout: int = 10,
    headers: Optional[dict] = None
) -> str:
    """
    Fetch HTML content from a static website with retry & logging.
    """

    default_headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    if headers:
        default_headers.update(headers)

    def _request():
        logger.info(f"Fetching URL: {url}")
        response = requests.get(
            url,
            headers=default_headers,
            timeout=timeout
        )
        response.raise_for_status()
        return response.text

    try:
        return retry(_request)
    except Exception as e:
        logger.error(f"Fetch failed for {url}: {e}")
        raise FetchError(str(e))
