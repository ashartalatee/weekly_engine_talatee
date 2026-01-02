# tests/test_detect_format.py

from src.detect_format import detect_numeric_format

def test_detect_formats():
    assert detect_numeric_format("1,200.50") == "US_FORMAT"
    assert detect_numeric_format("1.200,50") == "EU_FORMAT"
    assert detect_numeric_format("(2,000)") == "ACCOUNTING_NEGATIVE"
    assert detect_numeric_format("2.5M") == "MULTIPLIER_FORMAT"
    assert detect_numeric_format("5%") == "PERCENTAGE"
    assert detect_numeric_format("Rp 1.250.000") == "CURRENCY_OR_TEXT"
    assert detect_numeric_format("") == "INVALID_OR_MISSING"
