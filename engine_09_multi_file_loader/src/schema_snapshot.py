def extract_schema(load_result: dict):
    """
    Mengambil snapshot schema dari hasil loader.
    """
    if load_result["status"] != "success":
        return None

    df = load_result["data"]

    schema = {
        "file_name": load_result["file_name"],
        "total_rows": load_result["rows"],
        "total_columns": load_result["columns"],
        "columns": []
    }

    for col in df.columns:
        schema["columns"].append({
            "name": str(col),
            "dtype": str(df[col].dtype)
        })

    return schema
