import pandas as pd
from datetime import datetime

def create_data_snapshot(df: pd.DataFrame, source_name:str) -> dict:
    snapshot = {
        "source": source_name,
        "created_at": datetime.utcnow().isoformat(),
        "row_count": len(df),
        "columns": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "sample_rows": df.head(5).to_dict(orient="records")
    }
    return snapshot