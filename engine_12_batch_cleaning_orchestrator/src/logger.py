import logging
import os

LOG_FILE = "../logs/batch_run.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def log_info(message):
    logging.info(message)
    print(message)

def log_error(message):
    logging.error(message)
    print(message)
