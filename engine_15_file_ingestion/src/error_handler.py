# src/error_handler.py
from src.logger import get_logger

logger = get_logger()

def handle_error(file_path, error_type):
    message = f"File '{file_path.name}' gagal diproses | Alasan: {error_type}"
    logger.error(message)
