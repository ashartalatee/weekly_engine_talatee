from loader import load_data
from detect_date import detect_date_patterns
from detect_numeric import detect_numeric_patterns
from detect_text import detect_text_patterns
from pattern_grouper import group_anomaly_patterns
from reporter import generate_report


def main():
    df = load_data("../data/sample_dirty.csv")

    reports = {
        "order_date": detect_date_patterns(df["order_date"].astype(str).tolist()),
        "amount": detect_numeric_patterns(df["amount"].astype(str).tolist()),
        "city": detect_text_patterns(df["city"].astype(str).tolist()),
        "customer_name": detect_text_patterns(df["customer_name"].astype(str).tolist()),
    }

    summary = group_anomaly_patterns(reports)

    generate_report(
        summary=summary,
        output_path="../reports/format_anomaly_report.json"
    )

    print("FORMAT ANOMALY REPORT GENERATED")


if __name__ == "__main__":
    main()
