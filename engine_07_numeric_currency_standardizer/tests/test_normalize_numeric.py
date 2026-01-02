# tests/test_normalize_numeric.py

import pytest
from src.normalize_numeric import normalize_numeric, NumericNormalizationError


def test_us_format():
    assert normalize_numeric("1,200.50") == 1200.50


def test_eu_format():
    assert normalize_numeric("1.200,50") == 1200.50


def test_accounting_negative():
    assert normalize_numeric("(2,000)") == -2000.0


def test_plain_number():
    assert normalize_numeric("1200") == 1200.0


def test_missing():
    assert normalize_numeric("") is None


def test_invalid_format():
    with pytest.raises(NumericNormalizationError):
        normalize_numeric("2.5M")
