import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data tanpa mengubah nilai apapun.
    Ini adalah loader netral untuk kebutuhan audit.
    """
    df = pd.read_csv(file_path)

    return df