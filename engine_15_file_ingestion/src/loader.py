import pandas as pd

def load_file(file_path):
    """
    Mencoba memuat file ke DataFrame.
    Return tuple: (data, error)
    """
    try:
        suffix = file_path.suffix.lower()

        if suffix == ".csv":
            data = pd.read_csv(file_path)
        elif suffix == ".xlsx":
            data = pd.read_excel(file_path)
        elif suffix == ".json":
            data = pd.read_json(file_path)
        else:
            return None, "unsupported_format"
        
        if data.empty:
            return None, "empty_dataframe"
        
        return data, None
    
    except Exception as e:
        return None, str(e)