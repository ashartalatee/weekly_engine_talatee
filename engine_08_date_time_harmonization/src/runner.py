import pandas as pd
import yaml
from pathlib import Path

from detector import load_formats, detect_date_format
from parser import parse_date
from normalizer import normalize_datetime
from timezone_handler import apply_timezone
from validator import validate_datetime

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "raw_sample.csv"
OUTPUT_PATH = BASE_DIR / "data" / "cleaned_sample.csv"
REPORT_PATH = BASE_DIR / "reports" / "harmonization_report.json"

DATE_COLUMNS = ["created_at", "updated_at", "order_date"]

VALIDATION_RULES = {
    "min_year": 1900,
    "disallow_future": True
}

def main():
    df = pd.read_csv(DATA_PATH)

    formats = load_formats(BASE_DIR / "config" / "date_formats.yaml")
    with open(BASE_DIR / "config" / "timezone_rules.yaml") as f:
        tz_rules = yaml.safe_load(f)

    report = []

    for col in DATE_COLUMNS:
        cleaned_values = []

        for raw in df[col]:
            fmt = detect_date_format(raw, formats)
            parsed = parse_date(raw, fmt)
            tz_applied = apply_timezone(parsed, str(raw), tz_rules)
            validation = validate_datetime(tz_applied, VALIDATION_RULES)

            if validation["is_valid"]:
                cleaned = normalize_datetime(tz_applied)
            else:
                cleaned = None

            cleaned_values.append(cleaned)

            report.append({
                "column": col,
                "raw_value": raw,
                "detected_format": fmt["format_name"] if fmt else None,
                "is_valid": validation["is_valid"],
                "reason": validation["reason"]
            })

        df[col] = cleaned_values

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    REPORT_PATH.parent.mkdir(exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)

    with open(REPORT_PATH, "w") as f:
        yaml.safe_dump(report, f)

if __name__ == "__main__":
    main()
