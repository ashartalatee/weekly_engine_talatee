import os

VALID_ENGINES = [
    "engine_02_cleaning_rules",
    "engine_03_multi_file_cleaning"
]

def check_path_exists(path, create=False):
    if not os.path.exists(path):
        if create:
            os.makedirs(path)
        else:
            return False
    return True

def validate_engine(engine_name):
    return engine_name in VALID_ENGINES
