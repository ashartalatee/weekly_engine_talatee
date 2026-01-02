# src/normalize_numeric.py

import re
from src.detect_format import detect_numeric_format


class NumericNormalizationError(Exception):
    pass


def normalize_numeric(value: str) -> float | None:
    if value is None:
        return None

    raw = str(value).strip()

    if raw == "" or raw.upper() in {"N/A", "NA", "NULL"}:
        return None

    fmt = detect_numeric_format(raw)

    is_negative = False

    # Accounting negative: (2,000)
    if fmt == "ACCOUNTING_NEGATIVE":
        is_negative = True
        raw = raw.strip("()")

    # Remove spaces
    raw = raw.replace(" ", "")

    # US format: 1,200.50
    if fmt == "US_FORMAT":
        raw = raw.replace(",", "")

    # EU format: 1.200,50
    elif fmt == "EU_FORMAT":
        raw = raw.replace(".", "").replace(",", ".")

    # Comma separator (ambiguous, assume thousands)
    elif fmt == "COMMA_SEPARATOR":
        raw = raw.replace(",", "")

    # Dot separator (ambiguous, assume decimal)
    elif fmt == "DOT_SEPARATOR":
        pass

    # Plain number
    elif fmt == "PLAIN_NUMBER":
        pass

    else:
        raise NumericNormalizationError(
            f"Unsupported numeric format: {fmt} | value={value}"
        )

    try:
        number = float(raw)
    except ValueError:
        raise NumericNormalizationError(f"Failed to parse numeric: {value}")

    return -number if is_negative else number
