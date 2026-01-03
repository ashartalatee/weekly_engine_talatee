from datetime import datetime
from typing import Optional

STANDARD_FORMAT = "%Y-%m-%d %H:%M:%S"

def normalize_datetime(dt: Optional[datetime]) -> Optional[str]:
    if dt is None:
        return None
    return dt.strftime(STANDARD_FORMAT)
