import csv
import json
from pathlib import Path
from typing import List, Dict


class WriteError(Exception):
    pass


def write_output(
    data: List[Dict],
    output_cfg: dict
):
    """
    Write scraped data to CSV or JSON based on config.
    """
    output_format = output_cfg.get("format")
    output_path = output_cfg.get("path")

    if not output_format or not output_path:
        raise WriteError("Invalid output configuration")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    if output_format == "csv":
        _write_csv(data, output_path)
    elif output_format == "json":
        _write_json(data, output_path)
    else:
        raise WriteError(f"Unsupported output format: {output_format}")


def _write_csv(data: List[Dict], path: str):
    if not data:
        raise WriteError("No data to write")

    fieldnames = data[0].keys()

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def _write_json(data: List[Dict], path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
