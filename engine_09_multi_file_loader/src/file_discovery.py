from pathlib import Path

ALLOWED_EXTENSIONS = {".csv", ".xlsx", ".json"}


def discover_files(root_dir: str, recursive: bool = True):
    """
    Menemukan semua file data di folder.
    Jika recursive=True, akan scan subfolder.
    """
    root_path = Path(root_dir)

    if not root_path.exists():
        raise FileNotFoundError(f"Folder tidak ditemukan: {root_dir}")

    pattern = "**/*" if recursive else "*"
    files = []

    for path in root_path.glob(pattern):
        if path.is_file() and path.suffix.lower() in ALLOWED_EXTENSIONS:
            file_info = {
                "file_name": path.name,
                "file_path": str(path.resolve()),
                "extension": path.suffix.lower().replace(".", ""),
                "size_mb": round(path.stat().st_size / (1024 * 1024), 3)
            }
            files.append(file_info)

    return files
