import pandas as pd

def detect_exact_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["is_exact_duplicate"] = df.duplicated(keep=False)
    return df

if __name__ == "__main__":
    from loader import load_csv

    df = load_csv("../data/sample_dirty.csv")
    result = detect_exact_duplicates(df)
    print(result)
