from clean_text import clean_text_series
from clean_numeric import clean_numeric_series
from clean_date import clean_date_series

def dispatch_cleaning(series, col_type, actions):
    if col_type == "text":
        return clean_text_series(series, actions)

    elif col_type == "numeric":
        return clean_numeric_series(series, actions)

    elif col_type == "date":
        return clean_date_series(series, actions)

    else:
        raise ValueError(f"Unsupported column type: {col_type}")
