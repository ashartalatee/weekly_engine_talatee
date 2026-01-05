import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.schema_reader import read_schema

schema = read_schema(ROOT_DIR / "data/raw/sales_january.csv")
print(schema)
