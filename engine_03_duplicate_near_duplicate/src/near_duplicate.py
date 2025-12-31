import pandas as pd
from typing import List, Dict
from .similarity import string_similarity


def find_near_duplicates(
    df: pd.DataFrame,
    column: str,
    threshold: float = 85.0
) -> List[Dict]:
    """
    Cari pasangan data yang mirip (near-duplicate)
    """
    results = []
    values = df[column].astype(str).tolist()

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            score = string_similarity(values[i], values[j])

            if score >= threshold:
                results.append({
                    "row_i": i,
                    "row_j": j,
                    "value_i": values[i],
                    "value_j": values[j],
                    "similarity_score": score
                })

    return results
