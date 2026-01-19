from pathlib import Path
import pandas as pd
from datetime import datetime, timezone


# =========================
# RESULT OBJECT (STABLE)
# =========================
class CleaningResult:
    def __init__(
        self,
        output_path: Path,
        rows_before: int,
        rows_after: int
    ):
        self.output_path = output_path
        self.rows_before = rows_before
        self.rows_after = rows_after
        self.cleaned_at = datetime.now(timezone.utc).isoformat()


# =========================
# BASE CLEANER CONTRACT
# =========================
class DataCleaner:
    def __init__(self, config: dict):
        self.config = config or {}

    def clean(self, input_file: Path) -> CleaningResult:
        raise NotImplementedError(
            "Cleaner must implement clean()"
        )


# =========================
# SIMPLE PRODUCTION CLEANER
# =========================
class SimpleDataCleaner(DataCleaner):
    def clean(self, input_file: Path) -> CleaningResult:
        # ---------
        # HARD GUARDS
        # ---------
        if not isinstance(input_file, Path):
            raise TypeError("input_file must be pathlib.Path")

        if not input_file.exists():
            raise FileNotFoundError(
                f"Input file not found: {input_file}"
            )

        if input_file.stat().st_size == 0:
            raise ValueError(
                f"Input file is empty: {input_file}"
            )

        # ---------
        # LOAD CSV SAFELY
        # ---------
        try:
            df = pd.read_csv(input_file)
        except Exception as e:
            raise ValueError(
                f"Failed to read CSV '{input_file}': {str(e)}"
            )

        if df.empty:
            raise ValueError(
                "CSV loaded successfully but contains no rows"
            )

        rows_before = len(df)

        # ---------
        # APPLY RULES
        # ---------
        rules = self.config.get("rules", {})

        # RULE 1 — Drop fully empty rows
        if rules.get("drop_empty_rows", False):
            df = df.dropna(how="all")

        # RULE 2 — Trim whitespace (safe for mixed types)
        if rules.get("trim_whitespace", False):
            for col in df.select_dtypes(include="object").columns:
                df[col] = df[col].map(
                    lambda x: x.strip()
                    if isinstance(x, str)
                    else x
                )

        # ---------
        # OUTPUT (SAFE & TRACEABLE)
        # ---------
        output_dir = Path(
            self.config.get("output_dir", "data/cleaned")
        )
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now(timezone.utc).strftime(
            "%Y%m%d_%H%M%S"
        )
        output_file = (
            output_dir / f"cleaned_{timestamp}.csv"
        )

        df.to_csv(output_file, index=False)

        return CleaningResult(
            output_path=output_file,
            rows_before=rows_before,
            rows_after=len(df)
        )


# =========================
# LOCAL DEBUG ENTRY
# =========================
if __name__ == "__main__":
    config = {
        "output_dir": "data/cleaned",
        "rules": {
            "drop_empty_rows": True,
            "trim_whitespace": True
        }
    }

    input_file = Path("data/raw/sample.csv")

    cleaner = SimpleDataCleaner(config)
    result = cleaner.clean(input_file)

    print("[OK] Cleaning finished")
    print("Output file :", result.output_path)
    print("Rows before:", result.rows_before)
    print("Rows after :", result.rows_after)
    print("Cleaned at :", result.cleaned_at)
