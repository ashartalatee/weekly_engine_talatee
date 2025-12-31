import pandas as pd
from typing import List, Dict

def score_records(
        df: pd.DataFrame,
        near_duplicates: List[Dict],
        high_threshold: float = 90.0,
        medium_threshold: float = 80.0
) -> pd.DataFrame:
    """
    Memberi label risiko pada setiap baris data.
    """
    df = df.copy()
    df["risk_label"] = "safe"

    # Exact duplicate = risiko tertinggi
    if "is_exact_duplicates" in df.columns:
        df.loc[df["is_exact_duplicate"] == True, "risk_label"] = "exact_duplicate"

    # Near duplicate scoring
    for pair in  near_duplicates:
        score = pair["similarity_score"]
        i = pair["row_i"]
        j = pair["row_j"]

        if score >= high_threshold:
            label = "near_duplicate_high"
        elif score >= medium_threshold:
            label = "near_duplicate_medium"
        else:
            continue

        # Jangan override exact duplicate
        if df.loc[i, "risk_label"] == "safe":
            df.loc[i, "risk_label"] = label
        if df.loc[j, "risk_label"] == "safe":
            df.loc[j, "risk_label"] = label

    return df