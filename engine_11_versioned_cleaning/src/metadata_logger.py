from datetime import datetime
import json
from pathlib import Path

METADATA_LOG = Path("reports/metadata_log.json")

def log_execution(
    engine_name: str,
    engine_version: str,
    executed_by: str,
    source_version: int,
    config_used: dict
) -> dict:
    entry = {
        "engine_name": engine_name,
        "engine_version": engine_version,
        "executed_by": executed_by,
        "executed_at": datetime.utcnow().isoformat(),
        "source_version": source_version,
        "config_used": config_used
    }

    logs = []
    if METADATA_LOG.exists():
        with open(METADATA_LOG, "r") as f:
            logs = json.load(f)

    logs.append(entry)
    METADATA_LOG.parent.mkdir(parents=True, exist_ok=True)

    with open(METADATA_LOG, "w") as f:
        json.dump(logs, f, indent=2)

    return entry
