from pathlib import Path

from .loader import load_data
from .null_detector import load_null_rules, detect_missing
from .pattern_analyzer import analyze_missing_patterns
from .reporter import generate_markdown_report


def run_engine(
    data_path: str,
    rule_path: str,
    dataset_name: str = "Unknown Dataset"
):
    print(" Loading data...")
    df = load_data(data_path)

    print(" Loading missing rules...")
    rules = load_null_rules(rule_path)

    print(" Detecting missing values...")
    missing_summary = detect_missing(df, rules)

    print(" Analyzing missing patterns...")
    pattern_analysis = analyze_missing_patterns(df, rules)

    print(" Generating report...")
    report_path = generate_markdown_report(
        dataset_name=dataset_name,
        missing_summary=missing_summary,
        pattern_analysis=pattern_analysis,
        output_dir="reports"
    )

    print(" Engine finished successfully")
    print(f" Report generated at: {report_path}")


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent

    data_file = BASE_DIR / "data" / "sample_dirty.csv"
    rule_file = BASE_DIR / "config" / "null_rules.yaml"

    run_engine(
        data_path=str(data_file),
        rule_path=str(rule_file),
        dataset_name="Sample Dirty Dataset"
    )
