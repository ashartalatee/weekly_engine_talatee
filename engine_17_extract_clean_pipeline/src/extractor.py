from pathlib import Path
import pandas as pd
from datetime import datetime


class ExtractionResult:
    def __init__(self, output_path: Path, rows: int):
        self.output_path = output_path
        self.rows = rows
        self.extracted_at = datetime.utcnow().isoformat()


class BaseExtractor:
    def __init__(self, config: dict):
        self.config = config

    def extract(self) -> ExtractionResult:
        raise NotImplementedError("Extractor must implement extract()")


class LocalCSVExtractor(BaseExtractor):
    def extract(self) -> ExtractionResult:
        source_path = Path(self.config["options"]["path"])
        output_dir = Path("data/raw")
        output_dir.mkdir(parents=True, exist_ok=True)

        df = pd.read_csv(source_path)

        output_file = output_dir / f"extracted_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(output_file, index=False)

        return ExtractionResult(
            output_path=output_file,
            rows=len(df)
        )


if __name__ == "__main__":
    config = {
        "type": "csv_local",
        "options": {
            "path": "data/raw/sample_input.csv"
        }
    }

    extractor = LocalCSVExtractor(config)
    result = extractor.extract()

    print("Extracted file:", result.output_path)
    print("Rows:", result.rows)
