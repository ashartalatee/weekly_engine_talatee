import os
import json
from datetime import datetime
import pandas as pd
from typing import List, Dict


def generate_duplicate_report(
    df: pd.DataFrame,
    near_duplicates: List[Dict],
    output_path: str
) -> Dict:

    total_records = len(df)

    exact_count = int((df["risk_label"] == "exact_duplicate").sum())
    near_high = int((df["risk_label"] == "near_duplicate_high").sum())
    near_medium = int((df["risk_label"] == "near_duplicate_medium").sum())

    report = {
        "summary": {
            "total_records": total_records,
            "exact_duplicates": exact_count,
            "near_duplicates_high": near_high,
            "near_duplicates_medium": near_medium
        },
        "samples": {
            "exact_duplicates": df[df["risk_label"] == "exact_duplicate"]
            .head(3)
            .to_dict(orient="records"),
            "near_duplicates": near_duplicates[:3]
        },
        "generated_at": datetime.utcnow().isoformat()
    }

    # INI KUNCI PRODUKSI
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    return report
