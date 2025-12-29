import json
import logging
from pathlib import Path
import yaml

# Import modul engine
from loader import load_csv
from scan_missing import scan_missing
from scan_duplicates import scan_duplicates
from scan_format import scan_format
from scan_schema import scan_schema

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_diagnostic(file_path: str, config_path: str, output_path: str):
    """Jalankan semua diagnostic modul dan simpan report JSON"""
    # Load config
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # Load data
    df = load_csv(file_path)

    logging.info("Mulai diagnostic")

    # Scan missing
    missing_report = scan_missing(df, config)

    # Scan duplicate
    duplicate_report = scan_duplicates(df)

    # Scan format
    format_report = scan_format(df, config)

    # Scan schema
    expected_schema = config.get("expected_schema", df.columns.tolist())
    schema_report = scan_schema(df, expected_schema)

    # Compile report
    report = {
        "missing": missing_report,
        "duplicates": duplicate_report,
        "format": format_report,
        "schema": schema_report
    }

    # Save JSON
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)

    logging.info(f"Diagnostic selesai, report: {output_path}")
    return report

if __name__ == "__main__":
    # Path folder engine ini
    BASE_DIR = Path(__file__).parent.parent  # folder engine_01_raw_data_diagnostic

    FILE_PATH = BASE_DIR / "data" / "sample_dirty.csv"
    CONFIG_PATH = BASE_DIR / "config" / "diagnostic_rules.yaml"
    OUTPUT_PATH = BASE_DIR / "reports" / "sample_report.json"

    run_diagnostic(
        file_path=str(FILE_PATH),
        config_path=str(CONFIG_PATH),
        output_path=str(OUTPUT_PATH)
    )
