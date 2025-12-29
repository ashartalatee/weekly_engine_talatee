import pandas as pd

def scan_missing(df: pd.DataFrame, rules: dict) -> dict:
    result = {}

    total_rows = len(df)

    for col in df.columns:
        missing_count = df[col].isna().sum()
        missing_ratio = missing_count / total_rows if total_rows > 0 else 0

        severty = "ok"
        if missing_ratio >= rules["missing_threshold"]["critical"]:
            severty = "critical"
        elif missing_ratio >= rules["missing_threshold"]["warning"]:
            severty = "warning"

        result[col] = {
            "missing_count": int(missing_count),
            "missing_ratio": round(missing_ratio, 3),
            "severty": severty
        }

    return result