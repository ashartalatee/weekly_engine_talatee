from src.text_cleaner import normalize_text

def test_basic_text_normalization():
    rules = {
        "trim_whitespace": True,
        "collapse_spaces": True,
        "lowercase": True
    }
    result = normalize_text("  JOHN   DOE ", rules)
    assert result == "john doe"
