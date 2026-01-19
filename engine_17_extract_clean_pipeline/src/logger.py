import logging
from pathlib import Path


def setup_logger(name="pipeline_logger", log_dir="logs"):
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(Path(log_dir) / "pipeline.log")
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

class DataExtractor:
    def __init__(self, config: dict):
        self.output_dir = Path(config.get("output_dir", "data/extracted"))
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def extract(self, source: Path) -> Path:
        if not source.exists():
            raise FileNotFoundError(f"Source not found: {source}")

        if source.stat().st_size == 0:
            raise ValueError("Source file is empty")

        target = self.output_dir / source.name
        source.replace(target)

        return target

