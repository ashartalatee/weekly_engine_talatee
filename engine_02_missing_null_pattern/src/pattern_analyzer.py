import pandas as pd
from collections import Counter
from .null_detector import is_missing


def analyze_missing_patterns(df: pd.DataFrame, rules: dict) -> dict:
    """
    Analyze patterns of missing values.
    """
    row_missing_patterns = []
    problematic_rows = []

    for idx, row in df.iterrows():
        missing_cols = [
            col for col in df.columns
            if is_missing(row[col], rules, col)
        ]

        if missing_cols:
            row_missing_patterns.append(tuple(sorted(missing_cols)))
            problematic_rows.append({
                "row_index": idx,
                "missing_columns": missing_cols,
                "missing_count": len(missing_cols)
            })

    pattern_counter = Counter(row_missing_patterns)

    top_patterns = [
        {
            "missing_columns": list(pattern),
            "count": count
        }
        for pattern, count in pattern_counter.most_common(5)
    ]

    # Kolom yang sering muncul dalam pola missing
    column_frequency = Counter()
    for pattern in row_missing_patterns:
        for col in pattern:
            column_frequency[col] += 1

    most_problematic_columns = [
        {
            "column": col,
            "missing_occurrences": count
        }
        for col, count in column_frequency.most_common()
    ]

    return {
        "top_missing_patterns": top_patterns,
        "problematic_rows": problematic_rows,
        "most_problematic_columns": most_problematic_columns
    }
