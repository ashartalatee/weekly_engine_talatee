from pathlib import Path
import pandas as pd
from datetime import datetime


# =========================
# RESULT OBJECT
# =========================
class ExtractionResult:
    def __init__(self, output_path: Path, rows: int):
        self.output_path = output_path
        self.rows = rows
        self.extracted_at = datetime.utcnow().isoformat()


# =========================
# BASE CONTRACT
# =========================
class BaseExtractor:
    def __init__(self, config: dict):
        self.config = config

    def extract(self, source: Path) -> ExtractionResult:
        raise NotImplementedError("Extractor must implement extract(source)")


# =========================
# CONCRETE IMPLEMENTATION
# =========================
class LocalCSVExtractor(BaseExtractor):
    def extract(self, source: Path) -> ExtractionResult:
        output_dir = Path("data/raw")
        output_dir.mkdir(parents=True, exist_ok=True)

        df = pd.read_csv(source)

        output_file = output_dir / f"extracted_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(output_file, index=False)

        return ExtractionResult(
            output_path=output_file,
            rows=len(df)
        )


# =========================
# FACADE (PIPELINE ENTRY)
# =========================
class DataExtractor(BaseExtractor):
    """
    Facade extractor.
    Pipeline hanya boleh kenal class ini.
    """

    def __init__(self, config: dict):
        super().__init__(config)

        extractor_type = config.get("type", "csv_local")

        if extractor_type == "csv_local":
            self.impl = LocalCSVExtractor(config)
        else:
            raise ValueError(f"Unsupported extractor type: {extractor_type}")

    def extract(self, source: Path) -> Path:
        result = self.impl.extract(source)
        return result.output_path


# =========================
# MANUAL TEST
# =========================
if __name__ == "__main__":
    config = {
        "type": "csv_local"
    }

    extractor = DataExtractor(config)
    output = extractor.extract(Path("data/raw/sample_input.csv"))

    print("Extracted file:", output)
