import json
from pathlib import Path

from file_discovery import discover_files
from file_loader import load_file
from schema_snapshot import extract_schema
from error_collector import ErrorCollector


def run_engine(
    data_dir: str,
    report_path: str,
    recursive: bool = True
):
    errors = ErrorCollector()

    files = discover_files(data_dir, recursive=recursive)

    loaded_files = 0
    schemas = []

    for file_info in files:
        result = load_file(file_info, error_collector=errors)

        if result["status"] == "success":
            loaded_files += 1
            schema = extract_schema(result)
            if schema:
                schemas.append(schema)

    report = {
        "engine": "engine_09_multi_file_loader",
        "data_directory": data_dir,
        "total_files_found": len(files),
        "files_loaded_successfully": loaded_files,
        "files_failed": len(files) - loaded_files,
        "schemas": schemas,
        "errors": errors.to_list(),
        "error_summary": errors.summary()
    }

    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return report


if __name__ == "__main__":
    run_engine(
        data_dir="data/raw_samples",
        report_path="reports/loader_report.json"
    )
