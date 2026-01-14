from pathlib import Path
import pandas as pd
from datetime import datetime


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
        df = pd.read_csv(input_file)

        total_rows = len(df)
        metrics = {}

        # Missing ratio
        missing_ratio = df.isna().mean().mean()
        metrics["missing_ratio"] = round(missing_ratio, 4)

        # Duplicate ratio
        duplicate_ratio = df.duplicated().mean()
        metrics["duplicate_ratio"] = round(duplicate_ratio, 4)

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
            checked_at=datetime.utcnow().isoformat()
        )
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
