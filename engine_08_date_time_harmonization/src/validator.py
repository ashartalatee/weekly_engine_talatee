from datetime import datetime
from typing import Optional, Dict
import pytz

def validate_datetime(
    dt: Optional[datetime],
    rules: Dict
) -> Dict:
    if dt is None:
        return {
            "is_valid": False,
            "reason": "datetime_parse_failed"
        }

    now = datetime.now(pytz.UTC)

    if dt.year < rules["min_year"]:
        return {
            "is_valid": False,
            "reason": "year_too_old"
        }

    if rules["disallow_future"] and dt > now:
        return {
            "is_valid": False,
            "reason": "future_datetime"
        }

    return {
        "is_valid": True,
        "reason": None
    }
