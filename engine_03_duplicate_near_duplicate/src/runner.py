from .loader import load_csv
from .exact_duplicate import detect_exact_duplicates
from .near_duplicate import find_near_duplicates
from .scorer import score_records
from .reporter import generate_duplicate_report

def run_engine(
    input_path: str,
    text_column: str,
    report_path: str,
    similarity_threshold: float = 80.0
):
    # Load
    df = load_csv(input_path)

    # Exact duplicate
    df = detect_exact_duplicates(df)

    # Near duplicate
    pairs = find_near_duplicates(
        df,
        column=text_column,
        threshold=similarity_threshold
    )

    # Scoring
    df = score_records(df, pairs)

    # Report
    report = generate_duplicate_report(
        df,
        pairs,
        report_path
    )

    return report


if __name__ == "__main__":
    report = run_engine(
        input_path="data/sample_dirty.csv",
        text_column="name",
        report_path="../reports/duplicate_report.json"
    )

    print("Duplicate audit completed.")
    print(report["summary"])
