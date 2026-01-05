import pandas as pd
import json
from pathlib import Path

from schema_mapper import load_mapping_rules
from schema_aligner import align_dataframe
from report_builder import build_alignment_report


TARGET_COLUMNS = [
    "order_id",
    "customer_name",
    "order_date",
    "total"
]


def run_alignment(
    raw_dir: Path,
    aligned_dir: Path,
    report_dir: Path,
    mapping_rules_path: Path
):
    aligned_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    mapping_rules = load_mapping_rules(mapping_rules_path)

    for csv_file in raw_dir.glob("*.csv"):
        try:
            df = pd.read_csv(csv_file)
            original_cols = list(df.columns)

            aligned_df = align_dataframe(
                df=df,
                target_columns=TARGET_COLUMNS,
                mapping_rules=mapping_rules
            )

            # Save aligned data
            aligned_path = aligned_dir / f"{csv_file.stem}_aligned.csv"
            aligned_df.to_csv(aligned_path, index=False)

            # Build report
            report = build_alignment_report(
                source_file=csv_file.name,
                original_columns=original_cols,
                aligned_df=aligned_df,
                mapping_rules=mapping_rules,
                target_columns=TARGET_COLUMNS,
            )

            report_path = report_dir / f"{csv_file.stem}_report.json"
            with open(report_path, "w") as f:
                json.dump(report, f, indent=2)

            print(f"✔ Processed {csv_file.name}")

        except Exception as e:
            error_report = {
                "source_file": csv_file.name,
                "error": str(e)
            }

            error_path = report_dir / f"{csv_file.stem}_error.json"
            with open(error_path, "w") as f:
                json.dump(error_report, f, indent=2)

            print(f"✖ Failed {csv_file.name}")


if __name__ == "__main__":
    run_alignment(
        raw_dir=Path("data/raw"),
        aligned_dir=Path("data/aligned"),
        report_dir=Path("reports"),
        mapping_rules_path=Path("config/column_mapping_rules.yaml")
    )
