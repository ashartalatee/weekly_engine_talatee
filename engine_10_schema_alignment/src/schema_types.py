from dataclasses import dataclass
from typing import List


@dataclass
class ColumnSchema:
    name: str
    dtype: str
    index: int


@dataclass
class TableSchema:
    source_file: str
    columns: List[ColumnSchema]
