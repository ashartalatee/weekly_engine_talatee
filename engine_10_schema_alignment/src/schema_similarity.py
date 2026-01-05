from difflib import SequenceMatcher
from typing import Dict, List, Tuple


def similarity_score(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def find_similar_columns(
    source_cols: List[str],
    target_cols: List[str],
    threshold: float = 0.7
) -> Dict[str, Tuple[str, float]]:
    """
    Return mapping:
    source_col -> (target_col, score)
    """
    matches = {}

    for src in source_cols:
        best_match = None
        best_score = 0.0

        for tgt in target_cols:
            score = similarity_score(src, tgt)
            if score > best_score:
                best_score = score
                best_match = tgt

        if best_score >= threshold:
            matches[src] = (best_match, round(best_score, 2))

    return matches
