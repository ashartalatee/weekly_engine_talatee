from typing import Dict, List
import pandas as pd


def build_alignment_report(
    source_file: str,
    original_columns: List[str],
    aligned_df: pd.DataFrame,
    mapping_rules: Dict[str, str],
    target_columns: List[str],
) -> Dict:
    renamed = {
        src: tgt
        for src, tgt in mapping_rules.items()
        if src in original_columns
    }

    added = [
        col for col in target_columns
        if col not in original_columns
    ]

    dropped = [
        col for col in original_columns
        if col not in mapping_rules and col not in target_columns
    ]

    empty_required = [
        col for col in target_columns
        if col in aligned_df.columns and aligned_df[col].isna().all()
    ]

    return {
        "source_file": source_file,
        "summary": {
            "renamed_columns": renamed,
            "added_columns": added,
            "dropped_columns": dropped,
            "empty_columns": empty_required,
        },
        "notes": "Alignment dilakukan berdasarkan target schema dan aturan manual.",
    }
