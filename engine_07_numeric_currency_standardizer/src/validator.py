# src/validator.py

import math

class DataValidationError(Exception):
    pass


def validate_record(record: dict) -> dict:
    value = record.get("value")
    currency = record.get("currency")

    if value is None:
        raise DataValidationError("Value is None")

    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        raise DataValidationError("Value is NaN or infinite")

    if currency is None:
        raise DataValidationError("Currency is missing")

    if value < -1_000_000_000 or value > 1_000_000_000_000:
        raise DataValidationError("Value out of reasonable range")

    record["validated"] = True
    return record
