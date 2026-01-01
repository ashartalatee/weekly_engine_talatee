import yaml
from pathlib import Path


class RuleValidationError(Exception):
    pass


ALLOWED_COLUMN_TYPES = {"text", "numeric", "date"}
ALLOWED_ACTIONS = {
    "trim",
    "lowercase",
    "uppercase",
    "replace",
    "regex_replace",
    "remove_symbols",
    "to_float",
    "parse_date",
}


def load_rules(rule_path: str) -> dict:
    path = Path(rule_path)
    if not path.exists():
        raise RuleValidationError(f"Rule file not found: {rule_path}")

    with open(path, "r", encoding="utf-8") as f:
        rules = yaml.safe_load(f)

    validate_rules(rules)
    return rules


def validate_rules(rules: dict):
    if not isinstance(rules, dict):
        raise RuleValidationError("Rules must be a YAML mapping")

    _validate_dataset(rules)
    _validate_settings(rules)
    _validate_columns(rules)


def _validate_dataset(rules: dict):
    if "dataset" not in rules:
        raise RuleValidationError("Missing 'dataset' section")


def _validate_settings(rules: dict):
    if "settings" not in rules:
        raise RuleValidationError("Missing 'settings' section")


def _validate_columns(rules: dict):
    columns = rules.get("columns")
    if not isinstance(columns, dict) or not columns:
        raise RuleValidationError("'columns' must be a non-empty mapping")

    for col_name, col_def in columns.items():
        _validate_column(col_name, col_def)


def _validate_column(name: str, col_def: dict):
    if "type" not in col_def:
        raise RuleValidationError(f"Column '{name}' missing 'type'")

    col_type = col_def["type"]
    if col_type not in ALLOWED_COLUMN_TYPES:
        raise RuleValidationError(
            f"Column '{name}' has invalid type '{col_type}'"
        )

    actions = col_def.get("actions")
    if not isinstance(actions, list) or not actions:
        raise RuleValidationError(
            f"Column '{name}' must have non-empty 'actions' list"
        )

    for action in actions:
        _validate_action(name, action)


def _validate_action(column_name: str, action: dict):
    if "action" not in action:
        raise RuleValidationError(
            f"Action missing 'action' key in column '{column_name}'"
        )

    action_name = action["action"]
    if action_name not in ALLOWED_ACTIONS:
        raise RuleValidationError(
            f"Invalid action '{action_name}' in column '{column_name}'"
        )

    params = action.get("params")
    if params is not None and not isinstance(params, dict):
        raise RuleValidationError(
            f"'params' for action '{action_name}' in column '{column_name}' must be a dict"
        )
