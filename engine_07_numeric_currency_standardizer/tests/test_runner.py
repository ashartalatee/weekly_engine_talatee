# tests/test_runner.py

from src.runner import run

def test_runner(tmp_path):
    input_csv = "data/sample_dirty.csv"
    output_csv = tmp_path / "clean.csv"
    report_path = tmp_path / "report.json"

    report = run(input_csv, output_csv, report_path)

    assert report["total_rows"] > 0
    assert "success" in report
    assert "failed" in report
