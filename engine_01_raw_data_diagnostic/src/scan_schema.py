import pandas as pd
def scan_schema(df: pd.DataFrame, expected_schema: list) -> dict:
    actual_cols = df.columns.tolist()
    missing_cols = [col for col in expected_schema if col not in actual_cols]
    extra_cols = [col for col in actual_cols if col not in expected_schema]

    return {
        "missing_columns": missing_cols,
        "extra_columns": extra_cols,
        "total_columns_expected": len(expected_schema),
        "total_columns_actual": len(actual_cols)
    }