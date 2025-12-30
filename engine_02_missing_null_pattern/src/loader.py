import pandas as pd
from pathlib import Path

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load dataset from csv or excel
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    elif path.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(path)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")