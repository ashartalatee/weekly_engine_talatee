from pathlib import Path
from datetime import datetime, timezone

from extractor import DataExtractor
from cleaner import SimpleDataCleaner
from validator import SimpleDataValidator
from logger import setup_logger
from reporter import PipelineReporter


class PipelineResult:
    def __init__(self, status: str, detail: dict):
        self.status = status
        self.detail = detail


class DataPipeline:
    def __init__(self, config: dict):
        self.config = config

        self.logger = setup_logger()
        self.reporter = PipelineReporter()

        self.extractor = DataExtractor(config)
        self.cleaner = SimpleDataCleaner(config)
        self.validator = SimpleDataValidator(config)

    def run(self, source: Path) -> PipelineResult:
        self.logger.info(f"PIPELINE START | source={source}")

        try:
            # 1. Extract
            extracted_file = self.extractor.extract(source)
            self.logger.info(f"EXTRACT OK | file={extracted_file}")

            # 2. Clean
            cleaning_result = self.cleaner.clean(extracted_file)
            cleaned_file = cleaning_result.output_path
            self.logger.info(
                f"CLEAN OK | rows_before={cleaning_result.rows_before} "
                f"rows_after={cleaning_result.rows_after} "
                f"file={cleaned_file}"
            )

            # 3. Validate
            validation_result = self.validator.validate(cleaned_file)
            self.logger.info(
                f"VALIDATION | passed={validation_result.passed} "
                f"metrics={validation_result.metrics}"
            )

            if not validation_result.passed:
                result = PipelineResult(
                    status="FAILED_QUALITY",
                    detail={
                        "metrics": validation_result.metrics,
                        "checked_at": validation_result.checked_at
                    }
                )
            else:
                result = PipelineResult(
                    status="SUCCESS",
                    detail={
                        "cleaned_file": str(cleaned_file),
                        "metrics": validation_result.metrics
                    }
                )

        except Exception as e:
            self.logger.error(f"PIPELINE ERROR | {str(e)}")
            result = PipelineResult(
                status="ERROR",
                detail={
                    "message": str(e),
                    "time": datetime.now(timezone.utc).isoformat()
                }
            )

        report_path = self.reporter.generate(result)
        self.logger.info(f"REPORT GENERATED | {report_path}")
        self.logger.info(f"PIPELINE END | status={result.status}")

        return result


if __name__ == "__main__":
    config = {
        "rules": {
            "drop_empty_rows": True,
            "trim_whitespace": True
        },
        "thresholds": {
            "max_missing_ratio": 0.2,
            "max_duplicate_ratio": 0.1
        }
    }

    pipeline = DataPipeline(config)
    source_file = Path("data/raw/sample_input.csv")

    result = pipeline.run(source_file)
    print("STATUS:", result.status)
    print("DETAIL:", result.detail)
