def diff_schema(old_snapshot: dict, new_snapshot: dict) -> dict:
    old_cols = set(old_snapshot["columns"])
    new_cols = set(new_snapshot["columns"])

    return {
        "added_columns": list(new_cols - old_cols),
        "removed_columns": list(old_cols - new_cols),
        "unchanged_columns": list(old_cols & new_cols)
    }


def diff_quality(old_snapshot: dict, new_snapshot: dict) -> dict:
    def diff_dict(old, new):
        return {
            key: new.get(key, 0) - old.get(key, 0)
            for key in set(old) | set(new)
        }

    return {
        "row_count_diff": new_snapshot["row_count"] - old_snapshot["row_count"],
        "missing_values_diff": diff_dict(
            old_snapshot["missing_values"],
            new_snapshot["missing_values"]
        ),
        "duplicate_rows_diff": (
            new_snapshot["duplicate_rows"] - old_snapshot["duplicate_rows"]
        )
    }


def generate_diff_report(old_version: dict, new_version: dict) -> dict:
    return {
        "from_version": old_version["version_id"],
        "to_version": new_version["version_id"],
        "schema_diff": diff_schema(
            old_version["snapshot"], new_version["snapshot"]
        ),
        "quality_diff": diff_quality(
            old_version["snapshot"], new_version["snapshot"]
        )
    }
