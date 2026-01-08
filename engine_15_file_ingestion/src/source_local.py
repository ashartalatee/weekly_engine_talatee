from pathlib import Path

def discover_files(base_path: str):
    """
    Menemukan semua file di folder (rekursif)
    """
    base = Path(base_path)

    if not base.exists():
        raise FileExistsError(f"Path tidak ditemukan: {base_path}")
    
    files = []
    for path in base.rglob("*"):
        if path.is_file():
            files.append(path)

    return files