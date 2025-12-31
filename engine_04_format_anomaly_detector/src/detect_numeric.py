import re
from collections import Counter
from typing import List, Dict


NUMERIC_PATTERNS = {
    "PLAIN_NUMBER": r"^\d+(\.\d+)?$",
    "COMMA_THOUSAND": r"^\d{1,3}(,\d{3})+$",
    "DOT_THOUSAND": r"^\d{1,3}(\.\d{3})+$",
    "CURRENCY_PREFIX": r"^(Rp|IDR)\s?\d+([.,]\d+)?$",
    "MIXED_SEPARATORS": r".*[.,].*[.,].*"
}


def detect_numeric_patterns(values: List[str]) -> Dict:
    patterns_found = []

    for v in values:
        if not isinstance(v, str) or not v.strip():
            patterns_found.append("EMPTY_OR_NON_STRING")
            continue

        matched = False
        value = v.strip()

        for name, pattern in NUMERIC_PATTERNS.items():
            if re.match(pattern, value):
                patterns_found.append(name)
                matched = True
                break

        if not matched:
            patterns_found.append("UNKNOWN_PATTERN")

    return {
        "total_values": len(values),
        "pattern_distribution": dict(Counter(patterns_found)),
        "samples": list(set(values))[:5]
    }
