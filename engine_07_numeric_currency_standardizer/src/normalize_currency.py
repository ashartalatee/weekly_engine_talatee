# src/normalize_currency.py

import re
import yaml
from src.normalize_numeric import normalize_numeric
from src.parse_multiplier import parse_multiplier


def load_currency_rules(path="config/currency_rules.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def normalize_currency(value: str):
    rules = load_currency_rules()
    currencies = rules["currencies"]

    raw = str(value)

    # Multiplier (2.5M)
    if re.search(r"[KMB]$", raw, re.IGNORECASE):
        return {
            "value": parse_multiplier(raw),
            "currency": None,
            "source": value,
        }

    # Currency symbol
    for code, rule in currencies.items():
        for symbol in rule["symbols"]:
            if symbol in raw:
                cleaned = raw.replace(symbol, "").strip()
                return {
                    "value": normalize_numeric(cleaned),
                    "currency": code,
                    "source": value,
                }

    # No currency
    return {
        "value": normalize_numeric(raw),
        "currency": rules.get("default_currency"),
        "source": value,
    }
