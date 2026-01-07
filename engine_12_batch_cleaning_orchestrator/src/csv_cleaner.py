import pandas as pd
import os

def clean_csv_folder(input_path, output_path):
    os.makedirs(output_path, exist_ok=True)

    files = [f for f in os.listdir(input_path) if f.endswith(".csv")]
    if not files:
        raise Exception("Tidak ada file CSV ditemukan")

    for file in files:
        input_file = os.path.join(input_path, file)
        output_file = os.path.join(output_path, file)

        df = pd.read_csv(input_file)

        # cleaning minimal (FOUNDATION)
        df = df.drop_duplicates()
        df = df.dropna(how="all")

        df.to_csv(output_file, index=False)
