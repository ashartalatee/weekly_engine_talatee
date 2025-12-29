import pandas as pd
from datetime import datetime

def scan_format(df: pd.DataFrame, config: dict) -> dict:
    result = {}

    # Tanggal
    date_cols = [col for col in df.columns if "date" in col.lower()]
    for col in date_cols:
        anomalies = 0
        for val in df[col]:
            try:
                # Cek semua format yang diperlukan
                valid = any(
                    datetime.strptime(str(val), fmt)
                    for fmt in config.get("date_formats_allowed", [])
                )
            except Exception:
                valid = False

            if not valid:
                anomalies += 1
        result[col] = {"format_anomalies_count": anomalies}

    # Numeric (placeholder)
    numeric_cols = [col for col in df.columns if df[col].dtype in ["int64","float64"]]
    for col in numeric_cols:
        # cek misalnya ada karakter non-numeric
        non_nomeric = df[col].apply(lambda x: not str(x).replace(".","").replace(",","").isdigit())
        result[col+"_numeric_anomalies"] = int(non_nomeric.sum())

    return result