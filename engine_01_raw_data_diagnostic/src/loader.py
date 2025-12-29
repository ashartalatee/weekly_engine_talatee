import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_csv(file_path: str) -> pd.DataFrame:
    file_path_obj = Path(file_path)  # gunain nama beda, bukan Path

    if not file_path_obj.exists():
        logging.error(f"File tidak ditemukan: {file_path}")
        raise FileNotFoundError(f"{file_path} tidak ada")

    try:
        df = pd.read_csv(file_path_obj)
        logging.info(
            f"Berhasil load data | rows={df.shape[0]} cols={df.shape[1]}"
        )
        return df

    except Exception as e:
        logging.exception("Gagal load CSV")
        raise e
