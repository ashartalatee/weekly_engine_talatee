from collections import Counter
from typing import List, Dict

def detect_text_patterns(values: List[str]) -> Dict:
    patterns = []

    for v in values:
        if not isinstance(v, str) or not v.strip():
            patterns.append("EMPTY_OR_NON_STRING")
            continue

        value = v.strip()

        if value.isupper():
            patterns.append("ALL_UPPERCASE")
        elif value.islower():
            patterns.append("ALL_LOWERCASE")
        elif value.endswith("."):
            patterns.append("TRAILING_PUNCTUATION")
        elif "  " in value or value != value.strip():
            patterns.append("EXTRA_WHITESPACE")
        elif len(value.split()) > 1:
            patterns.append("MULTI_WORD")
        else:
            patterns.append("NORMAL")

    return {
        "total_values": len(values),
        "pattern_distribution": dict(Counter(patterns)),
        "samples": list(set(values))[:5]
    }