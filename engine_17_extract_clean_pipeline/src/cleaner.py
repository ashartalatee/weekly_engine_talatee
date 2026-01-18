from pathlib import Path
import pandas as pd
from datetime import datetime, timezone


class CleaningResult:
    def __init__(self, output_path: Path, rows_before: int, rows_after: int):
        self.output_path = output_path
        self.rows_before = rows_before
        self.rows_after = rows_after
        self.cleaned_at = datetime.now(timezone.utc).isoformat()


class DataCleaner:
    def __init__(self, config: dict):
        self.config = config

    def clean(self, input_file: Path) -> CleaningResult:
        raise NotImplementedError("Cleaner must implement clean()")


class SimpleDataCleaner(DataCleaner):
    def clean(self, input_file: Path) -> CleaningResult:
        output_dir = Path("data/cleaned")
        output_dir.mkdir(parents=True, exist_ok=True)

        df = pd.read_csv(input_file)
        rows_before = len(df)

        rules = self.config.get("rules", {})

        # RULE 1 — Drop empty rows
        if rules.get("drop_empty_rows", False):
            df = df.dropna(how="all")

        # RULE 2 — Trim whitespace (SAFE & FUTURE-PROOF)
        if rules.get("trim_whitespace", False):
            for col in df.select_dtypes(include="object").columns:
                df[col] = df[col].map(
                    lambda x: x.strip() if isinstance(x, str) else x
                )

        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        output_file = output_dir / f"cleaned_{timestamp}.csv"
        df.to_csv(output_file, index=False)

        return CleaningResult(
            output_path=output_file,
            rows_before=rows_before,
            rows_after=len(df)
        )


if __name__ == "__main__":
    config = {
        "rules": {
            "drop_empty_rows": True,
            "trim_whitespace": True
        }
    }

    input_file = Path("data/raw/sample.csv")
    cleaner = SimpleDataCleaner(config)
    result = cleaner.clean(input_file)

    print("Cleaned file:", result.output_path)
    print("Rows before:", result.rows_before)
    print("Rows after:", result.rows_after)
