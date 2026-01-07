import yaml
from pathlib import Path


class ConfigError(Exception):
    pass


def load_config(config_path: str) -> dict:
    """
    Load YAML configuration for scraper engine.
    """
    path = Path(config_path)

    if not path.exists():
        raise ConfigError(f"Config file not found: {config_path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise ConfigError(f"Failed to load config: {e}")
