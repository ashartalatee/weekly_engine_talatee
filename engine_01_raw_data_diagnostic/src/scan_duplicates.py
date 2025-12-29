import pandas as pd

def scan_duplicates(df: pd.DataFrame) -> dict:
    result = {}

    # Exact duplicate
    exact_dup = df.duplicated(keep=False)
    result["exact_duplicates_count"] = int(exact_dup.sum())

    # Near-duplicate: nama lowercase & strip
    if "name" in df.columns:
        names_clean = df["name"].astype(str).str.lower().str.strip()
        near_dup_count = names_clean.duplicated(keep=False).sum()
        result["near_duplicates_count"] = int(near_dup_count)
    else:
        result["near_duplicates_count"] = 0
    return result