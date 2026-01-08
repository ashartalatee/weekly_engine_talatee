# src/runner.py
import yaml
from pathlib import Path

from src.source_local import discover_files
from src.source_sftp import fetch_sftp_files
from src.detector import classify_files
from src.loader import load_file
from src.error_handler import handle_error


def load_config():
    with open("config/ingestion_rules.yaml") as f:
        return yaml.safe_load(f)


def run_ingestion():
    config = load_config()
    all_files = []

    # LOCAL SOURCE
    if config["sources"]["local"]["enabled"]:
        local_path = config["sources"]["local"]["path"]
        all_files.extend(discover_files(local_path))

    # SFTP SOURCE
    if config["sources"]["sftp"]["enabled"]:
        sftp_cfg = config["sources"]["sftp"]
        files, errors = fetch_sftp_files(
            host=sftp_cfg["host"],
            port=sftp_cfg["port"],
            username=sftp_cfg["username"],
            password=sftp_cfg["password"],
            remote_path=sftp_cfg["remote_path"],
        )
        all_files.extend(files)

        for fname, reason in errors:
            handle_error(Path(fname), reason)

    # DETECTION
    valid_files, rejected_files = classify_files(all_files)
    for file_path, reason in rejected_files:
        handle_error(file_path, reason)

    # LOADING
    for file_path in valid_files:
        data, error = load_file(file_path)
        if error:
            handle_error(file_path, error)
        else:
            # sementara hanya print (nanti diteruskan)
            print(f"Loaded: {file_path.name} | Rows: {len(data)}")


if __name__ == "__main__":
    run_ingestion()
