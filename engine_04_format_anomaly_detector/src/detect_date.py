import re
from collections import Counter
from typing import List, Dict


DATE_PATTERNS = {
    "YYYY-MM-DD": r"^\d{4}-\d{2}-\d{2}$",
    "DD/MM/YY": r"^\d{2}/\d{2}/\d{2}$",
    "Month D YYYY": r"^[A-Za-z]{3,9}\s\d{1,2}\s\d{4}$",
    "YYYY/MM/DD": r"^\d{4}/\d{2}/\d{2}$",
    "DD-MM-YYYY": r"^\d{2}-\d{2}-\d{4}$"
}


def detect_date_patterns(values: List[str]) -> Dict:
    """
    Mendeteksi pola format tanggal tanpa parsing ke datetime.
    """
    patterns_found = []

    for v in values:
        if not isinstance(v, str) or not v.strip():
            patterns_found.append("EMPTY_OR_NON_STRING")
            continue

        matched = False
        for name, pattern in DATE_PATTERNS.items():
            if re.match(pattern, v.strip()):
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
