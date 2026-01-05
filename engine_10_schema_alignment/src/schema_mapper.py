import yaml
from pathlib import Path
from typing import Dict


def load_mapping_rules(path: Path) -> Dict[str, str]:
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data.get("mappings", {})


def apply_mapping_rules(
    source_columns,
    mapping_rules: Dict[str, str]
) -> Dict[str, str]:
    """
    Return:
    source_col -> target_col
    """
    mappings = {}

    for col in source_columns:
        if col in mapping_rules:
            mappings[col] = mapping_rules[col]

    return mappings
