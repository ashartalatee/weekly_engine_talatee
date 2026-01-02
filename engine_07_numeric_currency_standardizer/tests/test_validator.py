# tests/test_validator.py

import pytest
from src.validator import validate_record, DataValidationError

def test_valid_record():
    record = {"value": 1000.0, "currency": "IDR"}
    result = validate_record(record)
    assert result["validated"] is True

def test_missing_value():
    with pytest.raises(DataValidationError):
        validate_record({"value": None, "currency": "IDR"})
