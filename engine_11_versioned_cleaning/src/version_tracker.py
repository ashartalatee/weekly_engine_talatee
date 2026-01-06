import json
from pathlib import Path
from datetime import datetime

VERSIONS_FILE = Path("reports/versions.json")

def load_versions():
    if VERSIONS_FILE.exists():
        with open(VERSIONS_FILE, "r") as f:
            return json.load(f)
    return []

def get_next_version_id(versions: list) -> int:
    if not versions:
        return 1
    return max(v["version_id"] for v in versions) + 1

def register_new_version(snapshot: dict) -> dict:
    versions = load_versions()
    version_id = get_next_version_id(versions)

    version_entry = {
        "version_id": version_id,
        "created_at": datetime.utcnow().isoformat(),
        "snapshot": snapshot
    }

    versions.append(version_entry)
    VERSIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(VERSIONS_FILE, "w") as f:
        json.dump(versions, f, indent=2)

    return version_entry
