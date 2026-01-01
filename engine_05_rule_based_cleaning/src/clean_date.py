import pandas as pd

def clean_date_series(series: pd.Series, actions: list) -> pd.Series:
    s = series.copy()

    for step in actions:
        action = step["action"]

        if action == "parse_date":
            input_formats = step["params"]["input_formats"]
            output_format = step["params"]["output_format"]

            def parse_date(val):
                for fmt in input_formats:
                    try:
                        return pd.to_datetime(val, format=fmt).strftime(output_format)
                    except Exception:
                        continue
                raise ValueError(f"Invalid date: {val}")

            s = s.apply(parse_date)

        else:
            raise ValueError(f"Unsupported date action: {action}")

    return s
