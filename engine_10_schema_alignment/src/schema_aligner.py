import pandas as pd
from typing import Dict, List


def align_dataframe(
    df: pd.DataFrame,
    target_columns: List[str],
    mapping_rules: Dict[str, str]
) -> pd.DataFrame:
    """
    Steps:
    1. Rename columns using mapping rules
    2. Add missing target columns as NA
    3. Drop non-target columns
    4. Reorder columns to match target schema
    """

    # 1. Rename
    df = df.rename(columns=mapping_rules)

    # 2. Add missing columns
    for col in target_columns:
        if col not in df.columns:
            df[col] = pd.NA

    # 3. Keep only target columns
    df = df[target_columns]

    return df
