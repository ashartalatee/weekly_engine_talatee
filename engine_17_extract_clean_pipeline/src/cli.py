import argparse
from pathlib import Path
import sys

from pipeline import DataPipeline

def build_parser():
    parser = argparse.ArgumentParser(
        description="Engine 17 — Extract Clean Pipeline"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path ke file sumber (CSV)"
    )

    parser.add_argument(
        "--config",
        default="config/validate.yaml",
        help="Path ke file konfigurasi"
    )

    return parser

import yaml


def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        print(f"[ERROR] Config file not found: {config_path}")
        sys.exit(1)

    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def main():
    parser = build_parser()
    args = parser.parse_args()

    source = Path(args.source)
    if not source.exists():
        print(f"[ERROR] Source file not found: {source}")
        sys.exit(1)

    config_path = Path(args.config)
    config = load_config(config_path)

    pipeline = DataPipeline(config)
    result = pipeline.run(source)

    if result.status == "SUCCESS":
        print("[OK] Pipeline finished successfully")
        print("Cleaned file:", result.detail.get("cleaned_file"))
    elif result.status == "FAILED_QUALITY":
        print("[FAILED] Data did not pass quality gate")
        print("Metrics:", result.detail.get("metrics"))
        sys.exit(2)
    else:
        print("[ERROR] Pipeline failed")
        print(result.detail)
        sys.exit(3)
if __name__ == "__main__":
    main()
