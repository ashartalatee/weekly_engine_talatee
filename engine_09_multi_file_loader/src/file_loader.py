import pandas as pd


def load_file(
    file_info: dict,
    encodings=None,
    error_collector=None
):
    """
    Memuat satu file data berdasarkan metadata.
    Error tidak melempar exception ke luar,
    tapi dicatat ke error_collector jika ada.
    """
    if encodings is None:
        encodings = ["utf-8", "latin1"]

    path = file_info["file_path"]
    ext = file_info["extension"]
    last_error = None

    for enc in encodings:
        try:
            if ext == "csv":
                df = pd.read_csv(path, encoding=enc)
            elif ext == "xlsx":
                df = pd.read_excel(path)
            elif ext == "json":
                df = pd.read_json(path)
            else:
                raise ValueError(f"Unsupported extension: {ext}")

            return {
                "status": "success",
                "file_name": file_info["file_name"],
                "rows": len(df),
                "columns": len(df.columns),
                "data": df,
                "error": None
            }

        except Exception as e:
            last_error = str(e)

    # semua encoding gagal → catat error
    if error_collector:
        error_collector.add(
            file_name=file_info["file_name"],
            file_path=file_info["file_path"],
            stage="load",
            error_message=last_error
        )

    return {
        "status": "failed",
        "file_name": file_info["file_name"],
        "data": None,
        "error": last_error
    }
