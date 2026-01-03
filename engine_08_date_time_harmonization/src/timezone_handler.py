from datetime import datetime
from typing import Optional, Dict
import pytz

def apply_timezone(
    dt: Optional[datetime],
    raw_value: str,
    tz_rules: Dict
) -> Optional[datetime]:
    if dt is None:
        return None

    # Jika sudah timezone-aware
    if dt.tzinfo is not None:
        return dt.astimezone(pytz.timezone(tz_rules["output_timezone"]))

    # Deteksi timezone dari string mentah
    for key, tz_name in tz_rules["known_timezones"].items():
        if key in str(raw_value):
            tz = pytz.timezone(tz_name)
            localized = tz.localize(dt)
            return localized.astimezone(pytz.timezone(tz_rules["output_timezone"]))

    # Pakai default timezone
    default_tz = pytz.timezone(tz_rules["default_timezone"])
    localized = default_tz.localize(dt)
    return localized.astimezone(pytz.timezone(tz_rules["output_timezone"]))
