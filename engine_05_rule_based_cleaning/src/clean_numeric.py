import pandas as pd

def clean_numeric_series(series: pd.Series, actions: list) -> pd.Series:
    s = series.copy()

    for step in actions:
        action = step["action"]

        if action == "remove_symbols":
            symbols = step.get("params", {}).get("symbols", [])
            for sym in symbols:
                s = s.astype(str).str.replace(sym, "", regex=False)

        elif action == "to_float":
            s = s.astype(float)

        else:
            raise ValueError(f"Unsupported numeric action: {action}")

    return s
