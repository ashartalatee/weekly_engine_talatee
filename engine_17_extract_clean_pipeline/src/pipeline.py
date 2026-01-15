from pathlib import Path
from datetime import datetime

from extractor import DataExtractor
from cleaner import DataCleaner
from validator import SimpleDataValidator


class PipelineResult:
    def __init__(self, status: str, detail: dict):
        self.status = status
        self.detail = detail


class DataPipeline:
    def __init__(self, config: dict):
        self.config = config

        self.extractor = DataExtractor(config)
        self.cleaner = DataCleaner(config)
        self.validator = SimpleDataValidator(config)

    def run(self, source: Path) -> PipelineResult:
        raise NotImplementedError("Pipeline must implement run()")
    
    def run(self, source: Path) -> PipelineResult:
        try:
            # 1. Extract
            extracted_file = self.extractor.extract(source)

            # 2. Clean
            cleaned_file = self.cleaner.clean(extracted_file)

            # 3. Validate
            validation_result = self.validator.validate(cleaned_file)

            if not validation_result.passed:
                return PipelineResult(
                    status="FAILED_QUALITY",
                    detail={
                        "metrics": validation_result.metrics,
                        "checked_at": validation_result.checked_at
                    }
                )

            return PipelineResult(
                status="SUCCESS",
                detail={
                    "cleaned_file": str(cleaned_file),
                    "metrics": validation_result.metrics
                }
            )

        except Exception as e:
            return PipelineResult(
                status="ERROR",
                detail={
                    "message": str(e),
                    "time": datetime.utcnow().isoformat()
                }
            )

if __name__ == "__main__":
    config = {
        "thresholds": {
            "max_missing_ratio": 0.2,
            "max_duplicate_ratio": 0.1
        }
    }

    pipeline = DataPipeline(config)
    source_file = Path("data/raw/sample.csv")

    result = pipeline.run(source_file)
    print("STATUS:", result.status)
    print("DETAIL:", result.detail)

