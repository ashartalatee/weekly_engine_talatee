import pandas as pd
import yaml
from pathlib import Path

def load_null_rules(rule_path: str) -> dict:
    with open(rule_path, "r") as f:
        return yaml.safe_load(f)

def is_missing(value, rules: dict, column_name: str = None) -> bool:
    # Pandas native missing
    if pd.isna(value):
        return True
    
    str_value = str(value).strip()

    # Column specific rules
    col_rules = rules.get("column_specific_rules", {}).get(column_name, {})
    if "missing_if" in col_rules:
        if str_value in col_rules["missing_if"]:
            return True
    
    # Global missing strings
    if str_value in rules.get("missing_strings", []):
        return True
    
    # Zero as missing (numeric)
    if rules.get("zero_as_missing", "").get("enabled", False):
        try:
            if float(value) == 0:
                return True
        except ValueError:
            pass

    return False

def detect_missing(df: pd.DataFrame, rules: dict) -> dict:
    missing_by_column = {}
    missing_by_row = []

    for col in df.columns:
        count = 0
        for val in df[col]:
            if is_missing(val, rules, col):
                count += 1
        missing_by_column[col] = count

    for idx, row in df.iterrows():
        row_missing = 0
        for col in df.columns:
            if is_missing(row[col], rules, col):
                row_missing += 1
        missing_by_row.append({
            "row_index": idx,
            "missing_count": row_missing
        })

    return {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_by_column": missing_by_column,
        "missing_by_row": missing_by_row
    }