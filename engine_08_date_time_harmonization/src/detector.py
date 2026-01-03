from datetime import datetime
from typing import Optional, Dict, List
import yaml

def load_formats(config_path: str) -> List[Dict]:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)["formats"]

def detect_date_format(
        value: str,
        formats: List[Dict]
) -> Optional[Dict]:
    if value is None or str(value).strip() == "":
        return None
    
    value = str(value).strip()

    for fmt in sorted(formats, key=lambda x: x["priority"]):
        try:
            datetime.strptime(value, fmt["pattern"])
            return {
                "format_name": fmt["name"],
                "pattern": fmt["pattern"],
                "confidence": round(1 / fmt["priority"], 2)
            }
        except ValueError:
            continue
    
    return None