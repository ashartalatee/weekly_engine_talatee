# src/parse_multiplier.py

import re

MULTIPLIERS = {
    "K": 1_000,
    "M": 1_000_000,
    "B": 1_000_000_000,
}


def parse_multiplier(value: str) -> float:
    match = re.match(r"([\d\.,]+)\s*([KMB])$", value, re.IGNORECASE)
    if not match:
        raise ValueError(f"No multiplier found in {value}")

    number_part = match.group(1)
    multiplier = MULTIPLIERS[match.group(2).upper()]

    number_part = number_part.replace(",", "")
    return float(number_part) * multiplier
