import pandas as pd
from pathlib import Path
from .schema_types import ColumnSchema, TableSchema


def infer_dtype(series: pd.Series) -> str:
    if pd.api.types.is_integer_dtype(series):
        return "int"
    if pd.api.types.is_float_dtype(series):
        return "float"
    if pd.api.types.is_datetime64_any_dtype(series):
        return "datetime"
    return "string"


def read_schema(csv_path: Path) -> TableSchema:
    df = pd.read_csv(csv_path)

    columns = []
    for idx, col in enumerate(df.columns):
        dtype = infer_dtype(df[col])
        columns.append(
            ColumnSchema(
                name=col,
                dtype=dtype,
                index=idx
            )
        )

    return TableSchema(
        source_file=csv_path.name,
        columns=columns
    )
