ALLOWED_EXTENSIONS = {"csv", "xlsx", "json"}

def is_valid_extension(file_path):
    return file_path.suffix.replace(".", "").lower() in ALLOWED_EXTENSIONS

def is_empty_file(file_path):
    return file_path.stat().st_size == 0

def is_loadable(data, error):
    """
    Menentukan apakah file benar-benar layak lanjut
    """
    if error is not None:
        return False
    return True

def classify_files(file_paths):
    valid_files = []
    rejected_files = []

    for file_path in file_paths:
        if not is_valid_extension(file_path):
            rejected_files.append((file_path, "invalid_extension"))
            continue

        if is_empty_file(file_path):
            rejected_files.append((file_path, "empty_file"))
            continue

        valid_files.append(file_path)

    return valid_files, rejected_files