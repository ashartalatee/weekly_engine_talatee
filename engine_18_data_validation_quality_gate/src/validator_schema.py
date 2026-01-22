def validate_schema(df, rule: dict) -> dict:
    required_cols = set(rule.get("required_columns", []))
    allow_extra = rule.get("allow_extra_columns", True)
    severity = rule.get("severity", "fail")

    df_cols = set(df.columns)

    missing_cols = list(required_cols - df_cols)
    extra_cols = list(df_cols - required_cols)

    if missing_cols:
        status = "FAIL"
    elif extra_cols and not allow_extra:
        status = "FAIL"
    else:
        status = "PASS"

    return {
        "validator": "schema",
        "status": status,
        "severity": severity,
        "details": {
            "missing_columns": missing_cols,
            "extra_columns": extra_cols
        },
        "message": "Schema sesuai" if status == "PASS" else "Schema tidak sesuai"
    }
