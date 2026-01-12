from pathlib import Path
import pandas as pd
from datetime import datetime


class CleaningResult:
    def __init__(self, output_path: Path, rows_before: int, rows_after: int):
        self.output_path = output_path
        self.rows_before = rows_before
        self.rows_after = rows_after
        self.cleaned_at = datetime.utcnow().isoformat()


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

        if rules.get("drop_empty_rows", False):
            df = df.dropna(how="all")

        if rules.get("trim_whitespace", False):
            df = df.applymap(
                lambda x: x.strip() if isinstance(x, str) else x
            )

        output_file = output_dir / f"cleaned_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
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

    input_file = Path("data/sample_input.csv")
    cleaner = SimpleDataCleaner(config)
    result = cleaner.clean(input_file)

    print("Cleaned file:", result.output_path)
    print("Rows before:", result.rows_before)
    print("Rows after:", result.rows_after)
