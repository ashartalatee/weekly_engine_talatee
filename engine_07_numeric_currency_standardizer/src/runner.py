# src/runner.py

import csv
from src.normalize_currency import normalize_currency
from src.validator import validate_record, DataValidationError


def run(input_csv: str, output_csv: str, report_path: str):
    results = []
    errors = []

    with open(input_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for idx, row in enumerate(rows, start=1):
        try:
            normalized = normalize_currency(row.get("amount"))
            validated = validate_record(normalized)

            row["normalized_value"] = validated["value"]
            row["currency"] = validated["currency"]
            results.append(row)

        except Exception as e:
            errors.append({
                "row": idx,
                "raw_value": row.get("amount"),
                "error": str(e)
            })

    # Write cleaned CSV
    if results:
        fieldnames = results[0].keys()
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

    # Write report
    report = {
        "total_rows": len(rows),
        "success": len(results),
        "failed": len(errors),
        "errors": errors
    }

    with open(report_path, "w", encoding="utf-8") as f:
        import json
        json.dump(report, f, indent=2)

    return report
