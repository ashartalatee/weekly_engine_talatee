from src.runner import run

run(
    input_csv="data/sample_dirty.csv",
    output_csv="data/sample_clean.csv",
    report_path="reports/standardization_report.json"
)
