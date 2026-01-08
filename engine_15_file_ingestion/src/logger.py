# src/logger.py
import logging
from pathlib import Path

LOG_PATH = Path("logs/ingestion.log")

def get_logger():
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("ingestion_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(LOG_PATH)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
