import pandas as pd
import re

def clean_text_series(series: pd.Series, actions: list) -> pd.Series:
    s = series.copy()

    for step in actions:
        action = step["action"]

        if action == "trim":
            s = s.astype(str).str.strip()

        elif action == "lowercase":
            s = s.astype(str).str.lower()

        elif action == "replace":
            mapping = step.get("params", {}).get("mapping", {})
            for k, v in mapping.items():
                s = s.str.replace(k, v, regex=False)

        elif action == "regex_replace":
            pattern = step["params"]["pattern"]
            replacement = step["params"]["replacement"]
            s = s.str.replace(pattern, replacement, regex=True)

        else:
            raise ValueError(f"Unsupported text action: {action}")

    return s
