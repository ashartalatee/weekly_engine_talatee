import argparse
from pathlib import Path
import sys
import yaml

from pipeline import DataPipeline


# -----------------------------
# CLI CONTRACT
# -----------------------------
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
        help="Path ke file konfigurasi pipeline"
    )

    return parser


# -----------------------------
# CONFIG LOADER (HARDENED)
# -----------------------------
def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        print(f"[ERROR] Config file not found: {config_path}")
        sys.exit(10)

    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print(f"[ERROR] Failed to read config: {str(e)}")
        sys.exit(11)

    if not isinstance(config, dict):
        print("[ERROR] Invalid config format (must be YAML dict)")
        sys.exit(12)

    return config


# -----------------------------
# MAIN ENTRY
# -----------------------------
def main():
    parser = build_parser()
    args = parser.parse_args()

    source = Path(args.source)
    if not source.exists():
        print(f"[ERROR] Source file not found: {source}")
        sys.exit(20)

    try:
        config = load_config(Path(args.config))
        pipeline = DataPipeline(config)
        result = pipeline.run(source)

    except Exception as e:
        # FINAL SAFETY NET — USER NEVER SEES TRACEBACK
        print("[FATAL] Pipeline crashed")
        print("Reason:", str(e))
        sys.exit(99)

    # -----------------------------
    # RESULT HANDLING (USER CONTRACT)
    # -----------------------------
    if result.status == "SUCCESS":
        print("[OK] Pipeline finished successfully")
        print("Cleaned file:", result.detail.get("cleaned_file"))
        sys.exit(0)

    elif result.status == "FAILED_QUALITY":
        print("[FAILED] Data did not pass quality gate")
        print("Metrics:", result.detail.get("metrics"))
        sys.exit(2)

    else:
        print("[ERROR] Pipeline failed")
        print("Detail:", result.detail)
        sys.exit(3)


if __name__ == "__main__":
    main()
