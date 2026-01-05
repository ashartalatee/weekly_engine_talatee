from typing import Dict, List
from .schema_types import TableSchema


def diff_schema(
    source: TableSchema,
    target: TableSchema
) -> Dict[str, List[str]]:
    source_cols = {col.name for col in source.columns}
    target_cols = {col.name for col in target.columns}

    missing_in_source = list(target_cols - source_cols)
    extra_in_source = list(source_cols - target_cols)

    return {
        "source_file": source.source_file,
        "missing_columns": sorted(missing_in_source),
        "extra_columns": sorted(extra_in_source),
    }
