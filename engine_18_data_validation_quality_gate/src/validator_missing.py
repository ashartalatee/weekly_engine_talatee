import pandas as pd

def validate_missing(df: pd.DataFrame, rule: dict) -> dict:
    max_pct = rule.get("max_missing_percentage", 0)
    severity = rule.get("severity", "warning")

    missing_pct = df.isnull().mean().max() * 100

    if missing_pct > max_pct:
        status = "FAIL" if severity == "fail" else "WARN"
    else:
        status = "PASS"

    return {
        "validator": "missing_value",
        "status": status,
        "severity": severity,
        "details": {
            "max_missing_percentage": max_pct,
            "actual_missing_percentage": round(missing_pct, 2)
        },
        "message": f"Missing value tertinggi: {round(missing_pct,2)}%"
    }
