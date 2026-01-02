# tests/test_multiplier.py

from src.parse_multiplier import parse_multiplier


def test_multiplier_m():
    assert parse_multiplier("2.5M") == 2_500_000
