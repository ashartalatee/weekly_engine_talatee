import pandas as pd
from src.null_detector import detect_missing

def test_missing_detection():
    df = pd.DataFrame({
        "name": ["A", "", "C"],
        "email": ["a@mail.com", None, "NA"]
    })

    rules = {
        "missing_strings": ["", "NA"],
        "zero_as_missing": {"enabled": False},
        "column_specific_rules": {}
    }

    result = detect_missing(df, rules)

    assert result["missing_by_column"]["name"] == 1
    assert result["missing_by_column"]["email"] == 2