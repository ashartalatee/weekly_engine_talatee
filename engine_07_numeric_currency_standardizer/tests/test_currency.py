# tests/test_currency.py

from src.normalize_currency import normalize_currency


def test_currency_idr():
    result = normalize_currency("Rp 1.250.000")
    assert result["value"] == 1250000
    assert result["currency"] == "IDR"


def test_currency_usd():
    result = normalize_currency("USD 1,200.50")
    assert result["value"] == 1200.50
    assert result["currency"] == "USD"
