from datetime import datetime
from typing import Optional, Dict

def parse_date(
    value: str,
    detected_format: Dict
) -> Optional[datetime]:
    if value is None or detected_format is None:
        return None

    try:
        return datetime.strptime(value, detected_format["pattern"])
    except Exception:
        return None
