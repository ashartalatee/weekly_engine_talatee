from pathlib import Path
from datetime import datetime, timezone
import pandas as pd


class ValidationResult:
    def __init__(self, passed: bool, metrics: dict, checked_at: str):
        self.passed = passed
        self.metrics = metrics
        self.checked_at = checked_at


class DataValidator:
    def __init__(self, config: dict):
        self.config = config

    def validate(self, input_file: Path) -> ValidationResult:
        raise NotImplementedError("Validator must implement validate()")


class SimpleDataValidator(DataValidator):
    def validate(self, input_file: Path) -> ValidationResult:
        # ---------- HARD GUARDS ----------
        if not input_file.exists():
            return ValidationResult(
                passed=False,
                metrics={"error": "file_not_found"},
                checked_at=datetime.now(timezone.utc).isoformat()
            )

        if input_file.stat().st_size == 0:
            return ValidationResult(
                passed=False,
                metrics={"error": "empty_file"},
                checked_at=datetime.now(timezone.utc).isoformat()
            )

        try:
            df = pd.read_csv(input_file)
        except Exception as e:
            return ValidationResult(
                passed=False,
                metrics={"error": "invalid_csv", "detail": str(e)},
                checked_at=datetime.now(timezone.utc).isoformat()
            )

        if df.empty:
            return ValidationResult(
                passed=False,
                metrics={"error": "empty_dataframe"},
                checked_at=datetime.now(timezone.utc).isoformat()
            )

        # ---------- METRICS ----------
        metrics = {}

        missing_ratio = df.isna().mean().mean()
        duplicate_ratio = df.duplicated().mean()

        metrics["missing_ratio"] = round(float(missing_ratio), 4)
        metrics["duplicate_ratio"] = round(float(duplicate_ratio), 4)
        metrics["row_count"] = int(len(df))
        metrics["column_count"] = int(len(df.columns))

        # ---------- THRESHOLDS ----------
        thresholds = self.config.get("thresholds", {})
        max_missing = thresholds.get("max_missing_ratio", 1.0)
        max_duplicate = thresholds.get("max_duplicate_ratio", 1.0)

        passed = (
            metrics["missing_ratio"] <= max_missing and
            metrics["duplicate_ratio"] <= max_duplicate
        )

        return ValidationResult(
            passed=passed,
            metrics=metrics,
            checked_at=datetime.now(timezone.utc).isoformat()
        )


# ---------- LOCAL TEST ----------
if __name__ == "__main__":
    config = {
        "thresholds": {
            "max_missing_ratio": 0.2,
            "max_duplicate_ratio": 0.1
        }
    }

    input_file = Path("data/cleaned/PUT_FILENAME_HERE.csv")
    validator = SimpleDataValidator(config)
    result = validator.validate(input_file)

    print("Passed:", result.passed)
    print("Metrics:", result.metrics)
    print("Checked at:", result.checked_at)
